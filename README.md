# EVTX/ETW Resources

This is a repository that contains a bunch of resources to learn and understand EVTX/ETW (Event Tracing for Windows)

## A Quick Rundown

Here's what you can expect from each of the main subfolders within this repo. Please take a minute to educate yourself!

### ETWProvidersManifests

[ETWProvidersManifests](https://github.com/nasbench/EVTX-ETW-Resources/tree/main/ETWProvidersManifests) will contain raw XMLs for each Event Log Provider for each respective version of Windows. At minimum, there should be 800 of these for each system. An example can be seen below:

![](https://github.com/nasbench/EVTX-ETW-Resources/blob/main/Media/ETWProvidersManifests.gif?raw=true)

### ETWProvidersCSVs

[ETWProvidersCSVs](https://github.com/nasbench/EVTX-ETW-Resources/tree/main/ETWProvidersCSVs) will contain a CSV for each Provider and all the possible event IDs, event messages, etc contained within that Provider. An example can be seen below:

![](https://github.com/nasbench/EVTX-ETW-Resources/blob/main/Media/ETWProvidersCSVs.gif?raw=true)

Within the ETWProvidersCSVs subfolder, there are two other subfolders that separate Windows-native and Third-Party Event Log Providers.

#### Internal

Any Event Log Provider that exists upon a clean install of Windows will be included here. 

#### ThirdParty

Any Event Log Provider that doesn't ship with Windows will be included here. Some examples can include, but are not limited to: Third-Party Antivirus, Sysmon, Microsoft Office (technically doesn't ship with Windows), or Remote Admin Tools like Splashtop.

### ETWEventsList

[ETWEventsList](https://github.com/nasbench/EVTX-ETW-Resources/tree/main/ETWEventsList) will provide a CSV for each respective version of Windows that contains ALL of the possible event IDs, event messages, etc for that version of Windows. This is offered in a combined CSV for ALL Providers as well as each Provider separated out into their own CSV for that specific version of Windows. An example can be seen below:

![](https://github.com/nasbench/EVTX-ETW-Resources/blob/main/Media/ETWEventsList.gif?raw=true)

### Examples

[Examples](https://github.com/nasbench/ETW-Resources/tree/main/Examples) will contain example scripts to collect ETW events using different libraries.

## Content

- [EVTX/ETW Resources](#evtxetw-resources)
  - [Content](#content)
  - [Structure](#structure)
  - [Blogs / Research (<https://nasbench.medium.com/>)](#blogs--research-httpsnasbenchmediumcom)
  - [Tools](#tools)
    - [Interacting w/ ETW](#interacting-w-etw)
    - [Dumping ETW Providers Manifest](#dumping-etw-providers-manifest)
    - [Scripting w/ ETW (Detection, Digital Forensics)](#scripting-w-etw-detection-digital-forensics)
  - [Online Resources](#online-resources)
    - [Architecture](#architecture)
    - [Research](#research)
    - [Talks](#talks)
    - [Books](#books)
    - [Other Github Projects w/ ETW Content](#other-github-projects-w-etw-content)
  - [Contributing](#contributing)

## Blogs / Research (<https://nasbench.medium.com/>)

- [A Primer On Event Tracing For Windows (ETW)](https://nasbench.medium.com/a-primer-on-event-tracing-for-windows-etw-997725c082bf)
- [Finding Detection and Forensic Goodness In ETW Providers](https://nasbench.medium.com/finding-detection-and-forensic-goodness-in-etw-providers-7c7a2b5b5f4f)
- [Windows 11 “New” ETW Providers — Overview](https://nasbench.medium.com/windows-11-new-etw-providers-overview-a2a5fbc85775)

## Tools

The following is a list of tools that can let us interact with the different ETW providers available. The examples directory contains example scripts and commands on how to use these tools

### Interacting w/ ETW

- [**Logman**](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/logman)
- [**Microsoft.Diagnostics.Tracing.TraceEvent**](nuget.org/packages/Microsoft.Diagnostics.Tracing.TraceEvent/)
- [**Message Analyzer**](https://github.com/riverar/messageanalyzer-archive)

### Dumping ETW Providers Manifest

- [**ETW Explorer**](https://github.com/zodiacon/EtwExplorer/)
- [**WEPExplorer**](https://github.com/lallousx86/WinTools/tree/master/WEPExplorer)
- [**PerfView**](https://github.com/microsoft/perfview)

### Scripting w/ ETW (Detection, Digital Forensics)

- [**PSalander**](https://github.com/matthastings/PSalander)
- [**Sealighter**](https://github.com/pathtofile/Sealighter)
- [**PyWintrace**](https://github.com/fireeye/pywintrace)
- [**SilkETW**](https://github.com/fireeye/SilkETW)
- [**KrabsETW**](https://github.com/microsoft/krabsetw/)

## Online Resources

The following are blogs and articles published by the wider security community discussing various aspects of ETW

### Architecture

- [Event Tracing: Improve Debugging And Performance Tuning With ETW by Microsoft](https://docs.microsoft.com/en-us/archive/msdn-magazine/2007/april/event-tracing-improve-debugging-and-performance-tuning-with-etw)
- [About Event Tracing by Microsoft](https://docs.microsoft.com/en-us/windows/desktop/etw/about-event-tracing)
- [Part 1 - ETW Introduction and Overview by Microsoft](https://web.archive.org/web/20200725154736/https://docs.microsoft.com/en-us/archive/blogs/ntdebugging/part-1-etw-introduction-and-overview)
- [Part 2 - Exploring and Decoding ETW Providers using Event Log Channels by Microsoft](https://web.archive.org/web/20200816023246/https://docs.microsoft.com/en-us/archive/blogs/ntdebugging/part-2-exploring-and-decoding-etw-providers-using-event-log-channels)
- [Part 3 - ETW Methods of Tracing by Microsoft](https://web.archive.org/web/20200731060805/https://docs.microsoft.com/en-us/archive/blogs/ntdebugging/part-3-etw-methods-of-tracing)
- [ETW: Event Tracing for Windows 101](https://www.ired.team/miscellaneous-reversing-forensics/windows-kernel-internals/etw-event-tracing-for-windows-101)
- [ETW: Event Tracing for Windows, Part 1: Intro by Mozilla](https://blog.mozilla.org/sfink/2010/11/01/etw-part-1-intro/)
- [ETW: Event Tracing for Windows, part 2: field reporting by Mozilla](https://blog.mozilla.org/sfink/2010/11/01/etw-part-2-field-reporting/)
- [ETW: Event Tracing for Windows, part 3: architecture by Mozilla](https://blog.mozilla.org/sfink/2010/11/02/etw-part-3-architecture/)
- [ETW: Event Tracing for Windows, part 4: collection by Mozilla](https://blog.mozilla.org/sfink/2010/11/03/etw-part-4-collection/)
- [ETW Security by Geoff Chappell](https://www.geoffchappell.com/studies/windows/km/ntoskrnl/api/etw/secure/index.htm)
- [Writing an Instrumentation Manifest](https://docs.microsoft.com/en-us/windows/win32/wes/writing-an-instrumentation-manifest)

### Research

- [Tampering with Windows Event Tracing: Background, Offense, and Defense by Palantir](https://blog.palantir.com/tampering-with-windows-event-tracing-background-offense-and-defense-4be7ac62ac63)
- [Introduction to Threat Intelligence ETW](https://undev.ninja/introduction-to-threat-intelligence-etw/)
- [Detecting process injection with ETW](https://blog.redbluepurple.io/windows-security-research/kernel-tracing-injection-detection)
- [Experimenting with Protected Processes and Threat-Intelligence](https://blog.tofile.dev/2020/12/16/elam.html)
- [Bypassing the Microsoft-Windows-Threat-Intelligence Kernel APC Injection Sensor](https://medium.com/@philiptsukerman/bypassing-the-microsoft-windows-threat-intelligence-kernel-apc-injection-sensor-92266433e0b0)
- [Data Source Analysis and Dynamic Windows RE using WPP and TraceLogging](https://posts.specterops.io/data-source-analysis-and-dynamic-windows-re-using-wpp-and-tracelogging-e465f8b653f7)
- [Detecting Parent PID Spoofing](https://blog.f-secure.com/detecting-parent-pid-spoofing/)
- [Veni, No Vidi, No Vici: Attacks on ETW Blind EDR Sensors](https://www.blackhat.com/eu-21/briefings/schedule/index.html#veni-no-vidi-no-vici-attacks-on-etw-blind-edr-sensors-24842)

### Talks

- [T208 Hidden Treasure Detecting Intrusions with ETW Zac Brown - Derbycon 7](https://www.youtube.com/watch?v=VABMu05mYww&ab_channel=AdrianCrenshaw)
- [T208 Hidden Treasure Detecting Intrusions with ETW Zac Brown - GrrCON 2017](https://www.youtube.com/watch?v=ppGmRUhQO80&ab_channel=AdrianCrenshaw)
- [RECON 2019 - Using WPP and TraceLogging Tracing (Matt Graeber)](https://www.youtube.com/watch?v=l2co6ZCQCXU)
- [S25 Tracing Adversaries Detecting Attacks with ETW Matt Hastings Dave Hull - Derbycon 7](https://www.youtube.com/watch?v=3RwADlGX40o)
- [The Good, the Bad and the ETW (Grzegorz Tworek)](https://www.youtube.com/watch?v=0XTdCxq7kCY)

### Books

- [Windows Internals, Part 2, 7th Edition](https://www.microsoftpressstore.com/store/windows-internals-part-2-9780135462331)
- [Windows 10 System Programming, Part 2](https://leanpub.com/windows10systemprogrammingpart2)

### Other Github Projects w/ ETW Content

- [OSSEM Data Dictionaries](https://github.com/OTRF/OSSEM-DD) by [OTRF](https://github.com/OTRF)
- [ETW Providers Docs](https://github.com/repnz/etw-providers-docs) by [repnz](https://github.com/repnz)
- [Windows 10 ETW Events](https://github.com/jdu2600/Windows10EtwEvents) by [jdu2600](https://github.com/jdu2600)

## Contributing

If you want to contribute to this project simply follow these steps:

1. Download the latest version of [WEPExplorer](https://github.com/lallousx86/WinTools/tree/master/WEPExplorer)
2. Download the latest version of [Auto Keyboard Presser](https://www.autosofted.com/auto_keyboard_presser/)
3. Follow the steps in the GIF below

![MUCHGIF](https://user-images.githubusercontent.com/8741929/138963332-9d59bbfa-09b4-43c4-8958-4c4f98b1a2ca.gif)

4. Fork the repo and upload your files
5. Make a PR and receive our eternal thanks
