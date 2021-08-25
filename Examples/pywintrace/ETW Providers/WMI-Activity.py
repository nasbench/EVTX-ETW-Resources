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
    event_description = data["Description"]

    org_process_name, org_process_name_cmdline = getProcess(pid)

    if eid == 11:
        # 'CorrelationId = %1; GroupOperationId = %2; OperationId = %3; Operation = %4; ClientMachine = %5; User = %7; ClientProcessId = %8; NamespaceName = %9 '
        CorrelationId = data["CorrelationId"]
        GroupOperationId = data["GroupOperationId"]
        OperationId = data["OperationId"]
        Operation = data["Operation"]
        ClientMachine = data["ClientMachine"]
        ClientProcessId = int(data['ClientProcessId'])
        User = data["User"]
        NamespaceName = data["NamespaceName"]

        eDescription = [i.lstrip().strip() for i in event_description.replace("%1", CorrelationId).replace("%2", GroupOperationId).replace("%3", OperationId).replace("%4", Operation).replace("%5", ClientMachine).replace("%7", User).replace("%8", str(ClientProcessId)).replace("%9", NamespaceName).split(';')]

        print(f"TimeStamp: {time}\nEID: {eid}\nProcessId: {pid}\nProcessName: {org_process_name}\nProcess Commandline: {org_process_name_cmdline}\nThreadId: {tid}\nEvent Description:")
        for i in eDescription:
            print(f"\t{i}")
        
        print("\n")
    elif eid == 5857:
        # '%1 provider started with result code %2. HostProcess = %3; ProcessID = %4; ProviderPath = %5 '
        ProviderName = data["ProviderName"]
        Code = data["Code"]
        HostProcess = data["HostProcess"]
        ProcessID = data["ProcessID"]
        ProviderPath = data["ProviderPath"]

        eDescription = [i.lstrip().strip() for i in event_description.replace("%1", ProviderName).replace("%2", Code).replace("%3", HostProcess).replace("%4", ProcessID).replace("%5", ProviderPath).split(';')]

        print(f"TimeStamp: {time}\nEID: {eid}\nProcessId: {pid}\nProcessName: {org_process_name}\nProcess Commandline: {org_process_name_cmdline}\nThreadId: {tid}\nEvent Description:")
        for i in eDescription:
            print(f"\t{i}")
        
        print("\n")
    elif eid == 12:
        # 'ProviderInfo for GroupOperationId = %1; Operation = %2; HostID = %3; ProviderName = %4; ProviderGuid = %5; Path = %6 '
        GroupOperationId = data["GroupOperationId"]
        Operation = data["Operation"]
        HostID = data["HostId"]
        ProviderName = data["ProviderName"]
        ProviderGuid = data["ProviderGuid"]
        Path = data["Path"]

        eDescription = [i.lstrip().strip() for i in event_description.replace("%1", GroupOperationId).replace("%2", Operation).replace("%3", HostID).replace("%4", ProviderName).replace("%5", ProviderGuid).replace("%6", Path).split(';')]

        print(f"TimeStamp: {time}\nEID: {eid}\nProcessId: {pid}\nProcessName: {org_process_name}\nProcess Commandline: {org_process_name_cmdline}\nThreadId: {tid}\nEvent Description:")
        for i in eDescription:
            print(f"\t{i}")
        
        print("\n")

def main():
    name = "Microsoft-Windows-WMI-Activity"
    guid = "{1418EF04-B0B4-4623-BF7E-D74AB47BBDAA}"
    providers = [etw.ProviderInfo(name, etw.GUID(guid))]
    
    # event_id_filters=[11, 12, 5857]
    with etw.ETW(providers=providers, event_callback=lambda x: raw(x), event_id_filters=[11, 12, 5857]):
        etw.run('etw')

if __name__ == '__main__':
    main()