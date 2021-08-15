import etw
import psutil


def myHnadler(data):
    event = data[1]

    pid = int(event["ProcessID"])
    ppid = int(event["EventHeader"]["ProcessId"])

    process_name = ""
    parent_process_name = ""

    for process in psutil.process_iter():
        if process.pid == pid:
            process_name = process.name()
        if process.pid == ppid:
            parent_process_name = process.name()

    print(f"\"{parent_process_name}\" (PPID: {ppid}) Created : \"{process_name}\" (PID : {pid})")

def main():

    # This example uses the "Microsoft-Windows-Kernel-Process" provider and filter on EID 1 (Process Creation)

    name = "Microsoft-Windows-Kernel-Process"
    GUID = "{22FB2CD6-0E7B-422B-A0C7-2FAD1FD0E716}"
    providers = [etw.ProviderInfo(name, etw.GUID(GUID))]

    # Monitor only Event ID : 1 (ProcessStart)
    with etw.ETW(providers=providers, event_callback=lambda d: myHnadler(d), event_id_filters=[1]):
        etw.run('etw')

if __name__ == '__main__':
    main()