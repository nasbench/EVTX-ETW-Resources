import etw
import psutil
from datetime import datetime
import os

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
    pid = int(data['EventHeader']['ProcessId'])
    time = int(data['EventHeader']["TimeStamp"])
    time = datetime.utcfromtimestamp(time / (10*1000*1000)-11644473600).strftime('%Y-%m-%d %H:%M:%S')
    eid = int(data['EventHeader']['EventDescriptor']['Id'])
    tid = int(data['EventHeader']['ThreadId'])
    
    task = data['Task Name']

    org_process_name, org_process_name_cmdline = getProcess(pid)

    if eid == 1102 or eid == 1001:
        Name = data["Name"]
        Value = data["Value"]
        CustomLevel = data["CustomLevel"]
        Description = data["Description"].replace("%2", Value)

        print(f"TimeStamp: {time}\nTask: {task}\nEID: {eid}\nProcessId: {pid}\nProcessName: {org_process_name}\nProcess Commandline: {org_process_name_cmdline}\nThreadId: {tid}\nEvent Description:")
        
        print(f"\tName: {Name}")
        print(f"\tIP/Hostname: {Value}")
        print(f"\tCustomLevel: {CustomLevel}")
        print(f"\tDescription: {Description}\n\n")


def main():
    #"{28AA95BB-D444-4719-A36F-40462168127E}" "Microsoft-Windows-TerminalServices-ClientActiveXCore"
    name = "Microsoft-Windows-TerminalServices-ClientActiveXCore"
    guid = "{28AA95BB-D444-4719-A36F-40462168127E}"
    providers = [etw.ProviderInfo(name, etw.GUID(guid))]
    with etw.ETW(providers=providers, event_callback=lambda x: raw(x), event_id_filters=[1001,1102]):
        etw.run('etw')

if __name__ == '__main__':
    main()