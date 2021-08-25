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

    opcode = int(data["EventHeader"]["EventDescriptor"]["Opcode"])
    eid = int(data["EventHeader"]["EventDescriptor"]["Id"])
    pid = int(data["EventHeader"]["ProcessId"])
    tid = int(data["EventHeader"]["ThreadId"])
    task_name = data["Task Name"]
    serviceName = data["ServiceName"]

    org_process_name, org_process_name_cmdline = getProcess(pid)

    op = ""
    if opcode == 1:
        op = "Start"
    elif opcode == 2:
        op = "Stop"
    
    print(f"TimeStamp: {time}\nEID: {eid}\nOperation: {op}\nProcessId: {pid}\nProcessName: {org_process_name}\nProcess Commandline: {org_process_name_cmdline}\nThreadId: {tid}\nEvent Description:")
    print(f"\tTask Name: {task_name}\n\tService Name: {serviceName}\n\n")

def main():
    # Microsoft-Windows-Services-Svchost ({06184C97-5201-480E-92AF-3A3626C5B140})
    name = "Microsoft-Windows-Services-Svchost"
    guid = "{06184C97-5201-480E-92AF-3A3626C5B140}"
    providers = [etw.ProviderInfo(name, etw.GUID(guid))]
    
    with etw.ETW(providers=providers, event_callback=lambda x: raw(x)):
        etw.run('etw')

if __name__ == '__main__':
    main()