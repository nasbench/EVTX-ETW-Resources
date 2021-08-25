import etw
import psutil
from datetime import datetime

def raw(x):
    data = x[1]
    time = int(data['EventHeader']["TimeStamp"])
    time = datetime.utcfromtimestamp(time / (10*1000*1000)-11644473600).strftime('%Y-%m-%d %H:%M:%S')

    eid = int(data['EventHeader']['EventDescriptor']['Id'])
    tid = int(data['EventHeader']['ThreadId'])
    pid = int(data['EventHeader']['ProcessId'])
    task_name = data['Task Name']

    org_process_name = ""
    org_process_name_cmdline = ""

    for proc in psutil.process_iter():
        if proc.pid == pid:
            org_process_name = proc.name()
            org_process_name_cmdline = " ".join(proc.cmdline())

    status = 0
    desc = ""
    if eid == 6105:
        desc = f"UNLOCK Started"
    elif eid == 6106:
        desc = f"UNLOCK Successful (Reason : {status})"
    elif eid == 6107:
        status = data["Status"]
        desc = f"UNLOCK Failed (Reason : {status})"
    elif eid == 6108:
        desc = f"LOGON Started"
    elif eid == 6109:
        status = data["Status"]
        desc = f"LOGON Failed (Reason: {status})"
    elif eid == 6110:
        desc = f"LOGON Sucessful (Reason: {status})"
    elif eid == 6113:
        desc = f"LOCK Started"

    print(f"TimeStamp: {time}\nEID: {eid}\nOperation: {task_name}\nProcessId: {pid}\nProcessName: {org_process_name}\nProcess Commandline: {org_process_name_cmdline}\nThreadId: {tid}\nEvent Description: {desc}\n\n")


def main():
    # Microsoft-Windows-Winlogon ({DBE9B383-7CF3-4331-91CC-A3CB16A3B538})
    name = "Microsoft-Windows-Winlogon"
    guid = "{DBE9B383-7CF3-4331-91CC-A3CB16A3B538}"
    providers = [etw.ProviderInfo(name, etw.GUID(guid))]
        
    with etw.ETW(providers=providers, event_callback=lambda x: raw(x), event_id_filters=[6113,6112,6111,6110,6109,6108,6107,6106,6105]):
        etw.run('etw')

if __name__ == '__main__':
    main()