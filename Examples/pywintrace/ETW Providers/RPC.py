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
    
    InterfaceUuid = data["InterfaceUuid"]
    ProcNum = int(data["ProcNum"], 16)
    Protocol = data["Protocol"]
    NetworkAddress = data["NetworkAddress"]
    Endpoint = data["Endpoint"]
    Options = data["Options"]
    AuthenticationLevel = data["AuthenticationLevel"]
    AuthenticationService = data["AuthenticationService"]
    ImpersonationLevel = data["ImpersonationLevel"]

    if eid == 5:
        #Server RPC Call Started
        Description = "Server RPC call started"
    elif eid == 6:
        #Client RPC Call Started
        Description = "Client RPC call started"

    print(f"TimeStamp: {time}\nTask: {task}\nEID: {eid}\nProcessId: {pid}\nProcessName: {org_process_name}\nProcess Commandline: {org_process_name_cmdline}\nThreadId: {tid}\nEvent Description:")

    print(f"\tInterfaceUuid: {InterfaceUuid}")
    print(f"\tProcNum: {ProcNum}")
    print(f"\tProtocol: {Protocol}")
    print(f"\tNetworkAddress: {NetworkAddress}")
    print(f"\tEndpoint: {Endpoint}")
    print(f"\tOptions: {Options}")
    print(f"\tAuthenticationLevel: {AuthenticationLevel}")
    print(f"\tAuthenticationService: {AuthenticationService}")
    print(f"\tImpersonationLevel: {ImpersonationLevel}")
    print(f"\tDescription: {Description}\n\n")

def main():
    # "{6AD52B32-D609-4BE9-AE07-CE8DAE937E39}" "Microsoft-Windows-RPC"
    name = "Microsoft-Windows-RPC"
    guid = "{6AD52B32-D609-4BE9-AE07-CE8DAE937E39}"
    providers = [etw.ProviderInfo(name, etw.GUID(guid))]
    
    with etw.ETW(providers=providers, event_callback=lambda x: raw(x), event_id_filters=[5,6]):
        etw.run('etw')

if __name__ == '__main__':
    main()