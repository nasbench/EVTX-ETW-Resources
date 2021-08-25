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

    # 10 + 11 + 12 + 15
    PID = int(data["PID"])
    Size = data["size"]
    daddr = data["daddr"]
    saddr = data["saddr"]
    dport = data["dport"]
    sport = data["sport"]
    seqnum = data["seqnum"]
    connid = data["connid"]

    if eid == 10:
        startime = data["startime"]
        endtime = data["endtime"]

    elif eid == 15 or eid == 12:
        mss = data["mss"]
        sackopt = data["sackopt"]
        tsopt = data["tsopt"]
        wsopt = data["wsopt"]
        rcvwin = data["rcvwin"]
        rcvwinscale = data["rcvwinscale"]
        sndwinscale = data["sndwinscale"]
    
    #EID 10 : 'TCPv4: %2 bytes transmitted from %4:%6 to %3:%5. '
    #EID 11 : 'TCPv4: %2 bytes received from %4:%6 to %3:%5. '
    #EID 12 : 'TCPv4: Connection attempted between %4:%6 and %3:%5. '
    #EID 15 : 'TCPv4: Connection established between %4:%6 and %3:%5. '
    Description = data["Description"].replace("%2", Size).replace("%4", saddr).replace("%6", sport).replace("%3", daddr).replace("%5", dport)

    process_name, process_name_cmdline = getProcess(PID)

    print(f"TimeStamp: {time}\nTask: {task}\nEID: {eid}\nProcessId: {pid}\nProcessName: {org_process_name}\nProcess Commandline: {org_process_name_cmdline}\nThreadId: {tid}\nEvent Description:")

    print(f"\tPID: {PID}")
    print(f"\tProcessName: {process_name}")
    print(f"\tPorcess Commandline: {process_name_cmdline}")
    print(f"\tSize: {Size}")
    print(f"\tDestination address (daddr): {daddr}")
    print(f"\tDestination port (dport): {dport}")
    print(f"\tSource address (saddr): {saddr}")
    print(f"\tSource port (sport): {sport}")
    print(f"\tSequence number (seqnum): {seqnum}")
    print(f"\tConnection ID (connid): {connid}")
    
    if eid == 10:
        #print(f"\tStart time: {startime}")
        #print(f"\tEnd time: {endtime}")
        pass
    elif eid == 15 or eid == 12:
        print(f"\tmss: {mss}")
        print(f"\tsackopt: {sackopt}")
        print(f"\ttsopt: {tsopt}")
        print(f"\twsopt: {wsopt}")
        print(f"\trcvwin: {rcvwin}")
        print(f"\trcvwinscale: {rcvwinscale}")
        print(f"\tsndwinscale: {sndwinscale}")
    
    print(f"\tDescription: {Description}\n\n")

        

def main():
    # "{7DD42A49-5329-4832-8DFD-43D979153A88}" "Microsoft-Windows-Kernel-Network"
    name = "Microsoft-Windows-Kernel-Network"
    guid = "{7DD42A49-5329-4832-8DFD-43D979153A88}"
    providers = [etw.ProviderInfo(name, etw.GUID(guid))]
    
    with etw.ETW(providers=providers, event_callback=lambda x: raw(x), event_id_filters=[10,11,12,15]):
        etw.run('etw')

if __name__ == '__main__':
    main()