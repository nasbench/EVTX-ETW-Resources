Provider                         |  Event ID  |  Channel                                      |  Message
---------------------------------|------------|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-Diagnosis-PCW  |  1         |  Microsoft-Windows-Diagnosis-PCW/Operational  |  Provider {ProviderGuid} failed to register. Error: "{Error}"
Microsoft-Windows-Diagnosis-PCW  |  2         |  Microsoft-Windows-Diagnosis-PCW/Operational  |  Provider {ProviderGuid} failed to register counter set {CounterSetGuid}. Error: "{Error}"
Microsoft-Windows-Diagnosis-PCW  |  3         |  Microsoft-Windows-Diagnosis-PCW/Operational  |  Instance ({CounterSetGuid}, {InstanceName}, {InstanceId}) could not be created. Error: "{Error}"
Microsoft-Windows-Diagnosis-PCW  |  4         |  Microsoft-Windows-Diagnosis-PCW/Analytic     |  About to call provider {ProviderGuid} callback with arguments ({CallbackReason}, {MachineName}, {MachineNameSize}).
Microsoft-Windows-Diagnosis-PCW  |  5         |  Microsoft-Windows-Diagnosis-PCW/Analytic     |  Callback returned. Return value: "{Status}"
Microsoft-Windows-Diagnosis-PCW  |  6         |  Microsoft-Windows-Diagnosis-PCW/Debug        |  Provider {ProviderGuid} received an invalid notification with size {Size}.
Microsoft-Windows-Diagnosis-PCW  |  7         |  Microsoft-Windows-Diagnosis-PCW/Debug        |  Provider {ProviderGuid} received notification: {RequestCode}.
Microsoft-Windows-Diagnosis-PCW  |  8         |  Microsoft-Windows-Diagnosis-PCW/Debug        |  Provider {ProviderGuid} notification handler has replied with size {Size} and error code "{Status}".
Microsoft-Windows-Diagnosis-PCW  |  9         |  Microsoft-Windows-Diagnosis-PCW/Debug        |  Notification returning with status: "{Status}"
Microsoft-Windows-Diagnosis-PCW  |  13        |  Microsoft-Windows-Diagnosis-PCW/Analytic     |  Query of provider {ProviderGuid} with id {Id} had data collected.
Microsoft-Windows-Diagnosis-PCW  |  16        |  Microsoft-Windows-Diagnosis-PCW/Operational  |  Counter {CounterId} of instance ({CounterSetGuid}, {InstanceName}, {InstanceId}) could not be modified. Error: "{Error}"
Microsoft-Windows-Diagnosis-PCW  |  17        |  Microsoft-Windows-Diagnosis-PCW/Operational  |  Provider {ProviderGuid} failed to unregister. Error: "{Error}"
Microsoft-Windows-Diagnosis-PCW  |  18        |  Microsoft-Windows-Diagnosis-PCW/Operational  |  Instance ({CounterSetGuid}, {InstanceName}, {InstanceId}) could not be closed. Error: "{Error}"
Microsoft-Windows-Diagnosis-PCW  |  19        |  Microsoft-Windows-Diagnosis-PCW/Operational  |  Instance ({CounterSetGuid}, {InstanceName}, {InstanceId}) could not be queried. Error: "{Error}"
Microsoft-Windows-Diagnosis-PCW  |  20        |  Microsoft-Windows-Diagnosis-PCW/Operational  |  Unable to load pcw.sys, phase {Phase} failed. Error: "{ErrorCode}"
Microsoft-Windows-Diagnosis-PCW  |  21        |  Microsoft-Windows-Diagnosis-PCW/Operational  |  Kernel-mode provider failed to register counter set {CounterSetName}. Error: "{ErrorCode}"
Microsoft-Windows-Diagnosis-PCW  |  22        |  Microsoft-Windows-Diagnosis-PCW/Operational  |  Kernel-mode provider failed to create instance {InstanceName} of counter set {CounterSetName}. Error: "{ErrorCode}"
Microsoft-Windows-Diagnosis-PCW  |  23        |  Microsoft-Windows-Diagnosis-PCW/Operational  |  Kernel-mode provider failed to add instance {InstanceName} of counter set {CounterSetName}. Error: "{ErrorCode}"
Microsoft-Windows-Diagnosis-PCW  |  24        |  Microsoft-Windows-Diagnosis-PCW/Analytic     |  PCW driver failed when executing ioctl function {FunctionIndex}. Error: "{ErrorCode}"
Microsoft-Windows-Diagnosis-PCW  |  25        |  Microsoft-Windows-Diagnosis-PCW/Debug        |  PCW device missing during registration of counter set {CounterSetGuid} of provider {ProviderGuid}.