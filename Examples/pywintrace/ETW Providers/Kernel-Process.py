import etw
import psutil
from datetime import datetime

def getProcess(pid):
    process_name = ""
    process_name_cmdline = ""
    for proc in psutil.process_iter():
        if proc.pid == pid:
            process_name = proc.name()
            process_name_cmdline = " ".join(proc.cmdline())
    return process_name, process_name_cmdline

def raw(x):
    data = x[1]
    
    time = int(data['EventHeader']["TimeStamp"])
    time = datetime.utcfromtimestamp(time / (10*1000*1000)-11644473600).strftime('%Y-%m-%d %H:%M:%S')

    eid = int(data['EventHeader']['EventDescriptor']['Id'])
    tid = int(data['EventHeader']['ThreadId'])
    pid = int(data['EventHeader']['ProcessId'])
    task = data['Task Name']

    org_process_name, org_process_name_cmdline = getProcess(pid)
    
    if eid == 1:
        # Process Creation
        # process %1 started at time %3 by parent %4 running in session %6 with name %11.
        ProcessID = int(data["ProcessID"])
        CreateTime = data["CreateTime"]
        ParentProcessID = int(data["ParentProcessID"])
        SessionID = data["SessionID"]
        ImageName = data["ImageName"]
        ProcessTokenElevationType = data["ProcessTokenElevationType"]
        ProcessTokenIsElevated = data["ProcessTokenIsElevated"]
        MandatoryLabel = data["MandatoryLabel"]

        try:
            Flags = data["Flags"]
        except:
            Flags = ""
        
        try:
            ImageChecksum = data["ImageChecksum"]
        except:
            ImageChecksum = ""

        try:
            TimeDateStamp = data["TimeDateStamp"]
        except:
            TimeDateStamp = ""
        
        try:
            PackageFullName = data["PackageFullName"]
        except:
            PackageFullName = ""
        
        try:
            PackageRelativeAppId = data["PackageRelativeAppId"]
        except:
            PackageFullName = ""

        process_name, process_name_cmdline = getProcess(ProcessID)
        parent_process_name, parent_process_name_cmdline = getProcess(ParentProcessID)

        desc = data["Description"].replace("%1", f"{ProcessID} ({process_name})").replace("%3", CreateTime).replace("%4", f"{pid} ({org_process_name})").replace("%6", SessionID).replace("%11", ImageName)

        print(f"TimeStamp: {time}\nTask: {task}\nEID: {eid}\nProcessId: {pid}\nProcessName: {org_process_name}\nProcess Commandline: {org_process_name_cmdline}\nThreadId: {tid}\nEvent Description:")
        print(f"\tCreateTime: {CreateTime}")
        print(f"\tProcessID: {ProcessID}")
        print(f"\tProcessName: {process_name}")
        print(f"\tProcess Commandline: {process_name_cmdline}")
        print(f"\tImageName: {ImageName}")
        print(f"\tParent ProcessID: {ParentProcessID}")
        print(f"\tParent ProcessName: {parent_process_name}")
        print(f"\tParent Process Commandline: {parent_process_name_cmdline}")
        print(f"\tSessionID: {SessionID}")
        print(f"\tProcessTokenElevationType: {ProcessTokenElevationType}")
        print(f"\tProcessTokenIsElevated: {ProcessTokenIsElevated}")
        print(f"\tMandatoryLabel: {MandatoryLabel}")
        print(f"\tFlags: {Flags}")
        print(f"\tPackageFullName: {PackageFullName}")
        print(f"\tPackageRelativeAppId: {PackageRelativeAppId}")
        print(f"\tDescription: {desc}\n\n")
    
    elif eid == 3:
        # Thread Start
        # 'Thread %2 (in Process %1) started. '
        ProcessID = int(data["ProcessID"])
        ThreadID = data["ThreadID"]
        StackBase = data["StackBase"]
        StackLimit = data["StackLimit"]
        UserStackBase = data["UserStackBase"]
        UserStackLimit = data["UserStackLimit"]
        StartAddr = data["StartAddr"]
        Win32StartAddr = data["Win32StartAddr"]
        TebBase = data["TebBase"]
        SubProcessTag = data["SubProcessTag"]

        process_name, process_name_cmdline = getProcess(ProcessID)

        desc = data["Description"].replace("%1", f"{ProcessID} ({process_name})").replace("%2", ThreadID)

        print(f"TimeStamp: {time}\nTask: {task}\nEID: {eid}\nProcessId: {pid}\nProcessName: {org_process_name}\nProcess Commandline: {org_process_name_cmdline}\nThreadId: {tid}\nEvent Description:")
        print(f"\tProcessID: {ProcessID}")
        print(f"\tProcessName: {process_name}")
        print(f"\tProcess Commandline: {process_name_cmdline}")
        print(f"\tThreadID: {ThreadID}")
        print(f"\tStackBase: {StackBase}")
        print(f"\tStackLimit: {StackLimit}")
        print(f"\tUserStackBase: {UserStackBase}")
        print(f"\tUserStackLimit: {UserStackLimit}")
        print(f"\tStartAddr: {StartAddr}")
        print(f"\tWin32StartAddr: {Win32StartAddr}")
        print(f"\tTebBase: {TebBase}")
        print(f"\tSubProcessTag: {SubProcessTag}")
        print(f"\tDescription: {desc}\n\n")
        

    elif eid == 5:
        # Image Load
        ImageBase = data["ImageBase"]
        ImageSize = data["ImageSize"]
        ProcessID = int(data["ProcessID"])
        ImageCheckSum = data["ImageCheckSum"]
        TimeDateStamp = data["TimeDateStamp"]
        DefaultBase = data["DefaultBase"]
        ImageName = data["ImageName"]

        process_name, process_name_cmdline = getProcess(ProcessID)

        desc = data["Description"].replace("%3", f"{ProcessID} ({process_name})").replace("%7", ImageName)

        print(f"TimeStamp: {time}\nTask: {task}\nEID: {eid}\nProcessId: {pid}\nProcessName: {org_process_name}\nProcess Commandline: {org_process_name_cmdline}\nThreadId: {tid}\nEvent Description:")
        print(f"\tProcessID: {ProcessID}")
        print(f"\tProcessName: {process_name}")
        print(f"\tProcess Commandline: {process_name_cmdline}")
        print(f"\tImageName: {ImageName}")
        print(f"\tImageBase: {ImageBase}")
        print(f"\tImageSize: {ImageSize}")
        print(f"\tImageChecksum: {ImageCheckSum}")
        print(f"\tDefaultBase: {DefaultBase}")
        print(f"\tDescription: {desc}\n\n")
        

def main():

    name = "Microsoft-Windows-Kernel-Process"
    guid = "{22FB2CD6-0E7B-422B-A0C7-2FAD1FD0E716}"
    providers = [etw.ProviderInfo(name, etw.GUID(guid))]
        
    with etw.ETW(providers=providers, event_callback=lambda x: raw(x), event_id_filters= [1,3,5]):
        etw.run('etw')

if __name__ == '__main__':
    main()