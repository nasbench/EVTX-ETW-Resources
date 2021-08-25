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
    pid = int(data['EventHeader']['ProcessId'])
    time = int(data['EventHeader']["TimeStamp"])
    time = datetime.utcfromtimestamp(time / (10*1000*1000)-11644473600).strftime('%Y-%m-%d %H:%M:%S')
    eid = int(data['EventHeader']['EventDescriptor']['Id'])
    tid = int(data['EventHeader']['ThreadId'])
    task = data['Task Name']
    org_process_name, org_process_name_cmdline = getProcess(pid)

    if eid == 2:
        Flags = data["Flags"]
        CallTimeMs = data["CallTimeMs"]
        CallResult = data["CallResult"]
        TargetThreadId = int(data["TargetThreadId"], 16)
        TargetProcessId = int(data["TargetProcessId"], 16)
        TargetMethod = int(data["TargetMethod"])
        TargetInterface = data["TargetInterface"]

        process_name, process_name_cmdline = getProcess(TargetProcessId)

        print(f"TimeStamp: {time}\nTask: {task}\nEID: {eid}\nProcessId: {pid}\nProcessName: {org_process_name}\nProcess Commandline: {org_process_name_cmdline}\nThreadId: {tid}\nEvent Description:")
            
        print(f"\tFlags: {Flags}")
        print(f"\tCallTimeMs: {CallTimeMs}")
        print(f"\tCallResult: {CallResult}")
        print(f"\tTargetProcessId: {TargetProcessId}")
        print(f"\tTargetProcessName: {process_name}")
        print(f"\tTargetProcess Commandline: {process_name_cmdline}")
        print(f"\tTargetThreadId: {TargetThreadId}")
        print(f"\tTargetMethod: {TargetMethod}")
        print(f"\tTargetInterface: {TargetInterface}\n\n")
            

def main():
    # "{BF406804-6AFA-46E7-8A48-6C357E1D6D61}" "Microsoft-Windows-COMRuntime"
    name = "Microsoft-Windows-COMRuntime"
    guid = "{BF406804-6AFA-46E7-8A48-6C357E1D6D61}"
    providers = [etw.ProviderInfo(name, etw.GUID(guid))]
    with etw.ETW(providers=providers, event_callback=lambda x: raw(x), event_id_filters=[2]):
        etw.run('etw')

if __name__ == '__main__':
    main()