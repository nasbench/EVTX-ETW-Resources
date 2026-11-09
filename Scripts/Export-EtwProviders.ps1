<#
.SYNOPSIS
    Exports the ETW provider manifests of this machine in the format used by
    ETWProvidersManifests/ (one XML per provider plus All.xml, as written by
    WEPExplorer).

.DESCRIPTION
    Uses System.Diagnostics.Eventing.Reader.ProviderMetadata and wevtapi.dll, so
    it needs no GUI and no extra tool. The output folder is named after the
    repository convention:

        <OS>_<version>_<edition>_<release date>_<build>.<UBR>
        e.g. WindowsServer2025_24H2_Standard_20260113_26100.32230

    The release date cannot be read from the machine: it is the release date of
    the cumulative update that matches the build (see the Microsoft release
    health page), so it is a parameter.

    Run it from an elevated Windows PowerShell 5.1 or PowerShell 7 prompt.

.PARAMETER ReleaseDate
    Release date of the installed update, as yyyyMMdd.

.PARAMETER OutDir
    Folder in which the build folder is created. Defaults to the current folder.

.PARAMETER Edition
    Edition used in the folder name. Defaults to the one of the running OS
    (Standard, Datacenter, Pro, Enterprise, Home, ...).

.PARAMETER Provider
    Only export the providers matching these names (wildcards allowed).

.PARAMETER Zip
    Also create <build folder>.zip next to the folder.

.EXAMPLE
    .\Export-EtwProviders.ps1 -ReleaseDate 20260113 -OutDir C:\dumps
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)][ValidatePattern('^\d{8}$')][string]$ReleaseDate,
    [string]$OutDir = (Get-Location).Path,
    [string]$Edition,
    [string[]]$Provider,
    [switch]$Zip
)
$ErrorActionPreference = 'Continue'

# --- Identify the OS and build the folder name -------------------------------
$cv = Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
$build = "$($cv.CurrentBuild).$($cv.UBR)"
$version = if ($cv.DisplayVersion) { $cv.DisplayVersion } else { $cv.ReleaseId }
if (-not $Edition) {
    $Edition = switch -Regex ($cv.EditionID) {
        'Datacenter'   { 'Datacenter'; break }
        '^Server'      { 'Standard'; break }
        '^Professional' { 'Pro'; break }
        '^Enterprise'  { 'Enterprise'; break }
        '^Core'        { 'Home'; break }
        default        { $cv.EditionID }
    }
}
if ($cv.ProductName -match 'Server\s+(\d{4})') { $os = "WindowsServer$($Matches[1])" }
elseif ([int]$cv.CurrentBuild -ge 22000) { $os = 'W11' }
else { $os = 'W10' }
$name = "${os}_${version}_${Edition}_${ReleaseDate}_${build}"
# .NET file APIs resolve relative paths against the process working directory, which can differ from PowerShell's
$OutDir = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($OutDir)
$dir = Join-Path $OutDir $name
$xmlDir = Join-Path $dir 'WEPExplorer'
if (Test-Path $xmlDir) { throw "$xmlDir already exists" }
New-Item -ItemType Directory -Force $xmlDir | Out-Null
$log = Join-Path $dir 'export.log'
function Log($m) { "$((Get-Date).ToUniversalTime().ToString('o')) $m" | Add-Content $log }

Add-Type -TypeDefinition @'
using System; using System.Runtime.InteropServices; using System.Collections.Generic;
public static class Wep {
  [DllImport("wevtapi.dll", CharSet=CharSet.Unicode, SetLastError=true)] static extern IntPtr EvtOpenPublisherMetadata(IntPtr s, string p, string l, int loc, int f);
  [DllImport("wevtapi.dll", SetLastError=true)] static extern bool EvtGetPublisherMetadataProperty(IntPtr h, int id, int f, int sz, IntPtr buf, out int used);
  [DllImport("wevtapi.dll", SetLastError=true)] static extern bool EvtGetObjectArraySize(IntPtr a, out int n);
  [DllImport("wevtapi.dll", SetLastError=true)] static extern bool EvtGetObjectArrayProperty(IntPtr a, int id, int idx, int f, int sz, IntPtr buf, out int used);
  [DllImport("wevtapi.dll")] static extern bool EvtClose(IntPtr h);
  static object Var(IntPtr buf) {
    int t = Marshal.ReadInt32(buf, 12);
    if (t == 1) { IntPtr p = Marshal.ReadIntPtr(buf, 0); return p == IntPtr.Zero ? "" : Marshal.PtrToStringUni(p); }
    if (t == 8) return (uint)Marshal.ReadInt32(buf, 0);
    if (t == 32) return Marshal.ReadIntPtr(buf, 0);
    return null;
  }
  public static string[] Channels(string prov) {
    var res = new List<string>();
    IntPtr h = EvtOpenPublisherMetadata(IntPtr.Zero, prov, null, 0, 0);
    if (h == IntPtr.Zero) return res.ToArray();
    IntPtr buf = Marshal.AllocHGlobal(65536); int used;
    try {
      if (!EvtGetPublisherMetadataProperty(h, 6, 0, 65536, buf, out used)) return res.ToArray();
      IntPtr arr = Marshal.ReadIntPtr(buf, 0); int n;
      if (arr == IntPtr.Zero || !EvtGetObjectArraySize(arr, out n)) return res.ToArray();
      for (int i = 0; i < n; i++) {
        string path = ""; uint idx = 0, id = 0, fl = 0, mid = 0xFFFFFFFF; object o;
        if (EvtGetObjectArrayProperty(arr, 7, i, 0, 65536, buf, out used)) path = (Var(buf) as string) ?? "";
        if (EvtGetObjectArrayProperty(arr, 8, i, 0, 65536, buf, out used)) { o = Var(buf); if (o is uint) idx = (uint)o; }
        if (EvtGetObjectArrayProperty(arr, 9, i, 0, 65536, buf, out used)) { o = Var(buf); if (o is uint) id = (uint)o; }
        if (EvtGetObjectArrayProperty(arr, 10, i, 0, 65536, buf, out used)) { o = Var(buf); if (o is uint) fl = (uint)o; }
        if (EvtGetObjectArrayProperty(arr, 11, i, 0, 65536, buf, out used)) { o = Var(buf); if (o is uint) mid = (uint)o; }
        res.Add(path + "\t" + idx + "\t" + id + "\t" + ((fl & 1) != 0 ? "true" : "false") + "\t" + mid);
      }
      EvtClose(arr);
    } finally { Marshal.FreeHGlobal(buf); EvtClose(h); }
    return res.ToArray();
  }
  // Opcodes of a provider as "name<TAB>packed value": the opcode and the task it belongs to share one value
  public static string[] Opcodes(string prov) {
    var res = new List<string>();
    IntPtr h = EvtOpenPublisherMetadata(IntPtr.Zero, prov, null, 0, 0);
    if (h == IntPtr.Zero) return res.ToArray();
    IntPtr buf = Marshal.AllocHGlobal(65536); int used;
    try {
      if (!EvtGetPublisherMetadataProperty(h, 21, 0, 65536, buf, out used)) return res.ToArray();
      IntPtr arr = Marshal.ReadIntPtr(buf, 0); int n;
      if (arr == IntPtr.Zero || !EvtGetObjectArraySize(arr, out n)) return res.ToArray();
      for (int i = 0; i < n; i++) {
        string name = ""; uint val = 0; object o;
        if (EvtGetObjectArrayProperty(arr, 22, i, 0, 65536, buf, out used)) name = (Var(buf) as string) ?? "";
        if (EvtGetObjectArrayProperty(arr, 23, i, 0, 65536, buf, out used)) { o = Var(buf); if (o is uint) val = (uint)o; }
        res.Add(name + "\t" + val);
      }
      EvtClose(arr);
    } finally { Marshal.FreeHGlobal(buf); EvtClose(h); }
    return res.ToArray();
  }
}
'@

$nl = "`r`n"
function Clean([object]$s) { if ($null -eq $s) { return '' }; ([string]$s) -replace '[\x00-\x08\x0B\x0C\x0E-\x1F]', '' }
function X([object]$s) { (Clean $s).Replace('&', '&amp;').Replace('<', '&lt;').Replace('>', '&gt;') }
function Cdata([object]$s) { '<![CDATA[' + $nl + (Clean $s).Replace(']]>', ']]]]><![CDATA[>').Replace("`n", "`r`n") + ']]>' }
function Msg($o) { if ($null -eq $o) { return '' }; if ($o.DisplayName) { return [string]$o.DisplayName }; if ($o.Name) { return [string]$o.Name }; '' }
function U64([long]$v) { [BitConverter]::ToUInt64([BitConverter]::GetBytes($v), 0) }

function Build([string]$n) {
  $sb = New-Object Text.StringBuilder
  $pm = $null
  try { $pm = New-Object System.Diagnostics.Eventing.Reader.ProviderMetadata($n) } catch { Log "OPENFAIL $n : $($_.Exception.InnerException.Message)$($_.Exception.Message)" }
  $i4 = '    '; $i8 = $i4 * 2; $i12 = $i4 * 3; $i16 = $i4 * 4; $i20 = $i4 * 5
  [void]$sb.Append("$i4<Provider>$nl$i8<Name>$(X $n)</Name>$nl$i8<Metadata>$nl")
  $evCount = 0
  if ($pm) {
    $help = ''; try { if ($pm.HelpLink) { $help = $pm.HelpLink.OriginalString } } catch {}
    $pmsg = ''; try { $pmsg = $pm.DisplayName } catch {}
    [void]$sb.Append("$i12<Guid>$(($pm.Id.ToString('B')).ToUpper())</Guid>$nl")
    if ($pm.ResourceFilePath) { [void]$sb.Append("$i12<ResourceFilePath>$(X $pm.ResourceFilePath)</ResourceFilePath>$nl") }
    [void]$sb.Append("$i12<ParameterFilePath>$(X $pm.ParameterFilePath)</ParameterFilePath>$nl")
    [void]$sb.Append("$i12<MessageFilePath>$(X $pm.MessageFilePath)</MessageFilePath>$nl")
    [void]$sb.Append("$i12<HelpLink>$(X $help)</HelpLink>$nl")
    [void]$sb.Append("$i12<PublisherMessage>$(X $pmsg)</PublisherMessage>$nl")
    $links = @{}; try { foreach ($l in $pm.LogLinks) { $links[$l.LogName] = $l } } catch {}
    [void]$sb.Append("$i12<Channels>$nl")
    foreach ($row in [Wep]::Channels($n)) {
      $f = $row.Split("`t"); $dn = ''; if ($links.ContainsKey($f[0]) -and $f[4] -ne '4294967295') { $dn = $links[$f[0]].DisplayName }
      [void]$sb.Append("$i16<Channel>$nl$i20<Message>$(X $dn)</Message>$nl$i20<Path>$(X $f[0])</Path>$nl$i20<Index>$($f[1])</Index>$nl$i20<Id>$($f[2])</Id>$nl$i20<Imported>$($f[3])</Imported>$nl$i16</Channel>$nl")
    }
    [void]$sb.Append("$i12</Channels>$nl$i12<Levels>$nl")
    try { foreach ($x in $pm.Levels) { [void]$sb.Append("$i16<Level>$nl$i20<Message>$(X $x.DisplayName)</Message>$nl$i20<Name>$(X $x.Name)</Name>$nl$i20<Value>$($x.Value)</Value>$nl$i16</Level>$nl") } } catch { Log "LEVELS $n $($_.Exception.Message)" }
    [void]$sb.Append("$i12</Levels>$nl$i12<Tasks>$nl")
    try { foreach ($x in $pm.Tasks) { [void]$sb.Append("$i16<Task>$nl$i20<Message>$(X $x.DisplayName)</Message>$nl$i20<Name>$(X $x.Name)</Name>$nl$i20<Value>$($x.Value)</Value>$nl$i16</Task>$nl") } } catch { Log "TASKS $n $($_.Exception.Message)" }
    [void]$sb.Append("$i12</Tasks>$nl$i12<Opcodes>$nl")
    # The opcode and the task it belongs to are packed in one value (opcode in the high word, task in the low word)
    $ops = @(); $opMsg = @{}
    try { foreach ($x in $pm.Opcodes) { $opMsg[$x.Name] = $x.DisplayName } } catch {}
    foreach ($row in [Wep]::Opcodes($n)) { $f = $row.Split("`t"); $raw = [uint32]$f[1]; $ops += [pscustomobject]@{ Name = $f[0]; Opcode = [int]($raw -shr 16); Task = [int]($raw -band 0xFFFF) } }
    foreach ($x in $ops) { [void]$sb.Append("$i16<Opcode>$nl$i20<Message>$(X $opMsg[$x.Name])</Message>$nl$i20<Name>$(X $x.Name)</Name>$nl$i20<Value>$($x.Opcode)</Value>$nl$i20<Task>$($x.Task)</Task>$nl$i16</Opcode>$nl") }
    [void]$sb.Append("$i12</Opcodes>$nl$i12<Keywords>$nl")
    try { foreach ($x in $pm.Keywords) { [void]$sb.Append("$i16<Keyword>$nl$i20<Message>$(X $x.DisplayName)</Message>$nl$i20<Name>$(X $x.Name)</Name>$nl$i20<Value>$(U64 $x.Value)</Value>$nl$i16</Keyword>$nl") } } catch { Log "KEYWORDS $n $($_.Exception.Message)" }
    [void]$sb.Append("$i12</Keywords>$nl$i8</Metadata>$nl$i8<EventMetadata>$nl")
    try {
      foreach ($e in $pm.Events) {
        $evCount++
        $ch = ''; try { if ($e.LogLink) { $ch = $e.LogLink.LogName } } catch {}
        $kw = ''; try { $kw = (@($e.Keywords | ForEach-Object { Msg $_ }) | Where-Object { $_ }) -join ' ' } catch {}
        $desc = ''; try { $desc = $e.Description } catch {}
        $tpl = ''; try { $tpl = $e.Template } catch {}
        $opv = 0; try { if ($e.Opcode) { $opv = [int]$e.Opcode.Value } } catch {}
        $tkv = 0; try { $tkv = [int]$e.Task.Value } catch {}
        $opm = ''
        if ($opv -ne 0) {
            # .NET names the opcode by value only; several opcodes share a value and differ by task
            $hit = $ops | Where-Object { $_.Opcode -eq $opv -and $_.Task -eq $tkv } | Select-Object -First 1
            if (-not $hit) { $hit = $ops | Where-Object { $_.Opcode -eq $opv -and $_.Task -eq 0 } | Select-Object -First 1 }
            if ($hit) { if ($opMsg[$hit.Name]) { $opm = [string]$opMsg[$hit.Name] } else { $opm = $hit.Name } } else { $opm = Msg $e.Opcode }
        }
        $ev = "$i12<Event>$nl$i16<Id>$($e.Id)</Id>$nl$i16<Version>$($e.Version)</Version>$nl"
        if ($ch) { $ev += "$i16<Channel>$(X $ch)</Channel>$nl" }
        $lv = Msg $e.Level; if ($lv) { $ev += "$i16<Level>$(X $lv)</Level>$nl" }
        $tk = ''; if ($tkv -ne 0) { $tk = Msg $e.Task }; if ($tk) { $ev += "$i16<Task>$(X $tk)</Task>$nl" }
        if ($opm) { $ev += "$i16<Opcode>$(X $opm)</Opcode>$nl" }
        if ($kw) { $ev += "$i16<Keyword>$(X $kw)</Keyword>$nl" }
        if ($desc) { $ev += "$i16<Message>$(Cdata $desc)</Message>$nl" }
        $ev += "$i16<Template>$(Cdata $tpl)</Template>$nl"
        $ev += "$i12</Event>$nl"
        [void]$sb.Append($ev)
      }
    } catch { Log "EVENTS $n after $evCount : $($_.Exception.Message)" }
  } else {
    [void]$sb.Append("$i12<Guid>{00000000-0000-0000-0000-000000000000}</Guid>$nl$i12<ParameterFilePath></ParameterFilePath>$nl$i12<MessageFilePath></MessageFilePath>$nl$i12<HelpLink></HelpLink>$nl$i12<PublisherMessage></PublisherMessage>$nl$i12<Channels>$nl$i12</Channels>$nl$i12<Levels>$nl$i12</Levels>$nl$i12<Tasks>$nl$i12</Tasks>$nl$i12<Opcodes>$nl$i12</Opcodes>$nl$i12<Keywords>$nl$i12</Keywords>$nl$i8</Metadata>$nl$i8<EventMetadata>$nl")
  }
  [void]$sb.Append("$i8</EventMetadata>$nl$i4</Provider>$nl")
  [pscustomobject]@{ Xml = $sb.ToString(); Events = $evCount; Opened = [bool]$pm; Guid = $(if ($pm) { $pm.Id.ToString('B').ToUpper() } else { '' }); Msg = $(if ($pm) { $pm.MessageFilePath } else { '' }) }
}

$utf8 = New-Object Text.UTF8Encoding $false
$names = [System.Diagnostics.Eventing.Reader.EventLogSession]::GlobalSession.GetProviderNames() | Sort-Object
# powershell -File passes -Provider a,b as one string
$Provider = @($Provider | ForEach-Object { $_ -split ',' } | Where-Object { $_ })
if ($Provider) { $names = $names | Where-Object { $n = $_; $Provider | Where-Object { $n -like $_ } } }
Log "START $name providers=$(@($names).Count)"
$all = New-Object Text.StringBuilder; [void]$all.Append("<Providers>$nl")
$used = @{}
foreach ($n in $names) {
    try {
        $r = Build $n
        # "TCP/IP" cannot be a file name; keep names that differ only by case apart
        $fn = $n -replace '[\\/:*?"<>|]', '_'
        if ($used.ContainsKey($fn.ToLower())) { $used[$fn.ToLower()]++; $fn = "${fn}_$($used[$fn.ToLower()])" } else { $used[$fn.ToLower()] = 1 }
        [IO.File]::WriteAllText("$xmlDir\$fn.xml", "<Providers>$nl" + $r.Xml + "</Providers>$nl", $utf8)
        [void]$all.Append($r.Xml)
    } catch { Log "FAILED $n : $($_.Exception.Message)" }
}
[void]$all.Append("</Providers>$nl")
[IO.File]::WriteAllText("$xmlDir\All.xml", $all.ToString(), $utf8)
Log "DONE files=$((Get-ChildItem $xmlDir -Filter *.xml).Count)"
if ($Zip) { Compress-Archive -Path $dir -DestinationPath "$dir.zip" -Force }
Write-Host "Exported to $dir"
