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

    ScopeOfSearch = data["ScopeOfSearch"]
    SearchFilter = data["SearchFilter"]
    DistinguishedName = data["DistinguishedName"]
    AttributeList = data["AttributeList"]
    ProcessId = int(data["ProcessId"], 16)

    process_name, process_name_cmdline = getProcess(ProcessId)

    print(f"TimeStamp: {time}\nTask: {task}\nEID: {eid}\nProcessId: {pid}\nProcessName: {org_process_name}\nProcess Commandline: {org_process_name_cmdline}\nThreadId: {tid}\nEvent Description:")

    print(f"\tProcessId: {ProcessId}")
    print(f"\tProcessName: {process_name}")
    print(f"\tProcess Commandline: {process_name_cmdline}")
    print(f"\tScopeOfSearch: {ScopeOfSearch}")
    print(f"\tSearchFilter: {SearchFilter}")
    print(f"\tDistinguishedName: {DistinguishedName}")
    print(f"\tAttributeList: {AttributeList}\n\n")
    
        

def main():
    # "{099614A5-5DD7-4788-8BC9-E29F43DB28FC}" "Microsoft-Windows-LDAP-Client"
    name = "Microsoft-Windows-LDAP-Client"
    guid = "{099614A5-5DD7-4788-8BC9-E29F43DB28FC}"
    providers = [etw.ProviderInfo(name, etw.GUID(guid))]
    #  event_id_filters=[30]
    with etw.ETW(providers=providers, event_callback=lambda x: raw(x)):
        etw.run('etw')

if __name__ == '__main__':
    main()