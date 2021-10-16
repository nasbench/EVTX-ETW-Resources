Provider                              |  Event ID  |  Channel  |  Message
--------------------------------------|------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-DeviceSetupManager  |  100       |           |  DSM service start, mode is {Prop_CoreServiceMode}, last session (or boot) was {Prop_Event_Window_Seconds} seconds ago
Microsoft-Windows-DeviceSetupManager  |  101       |           |  DSM Service shutting down. Service uptime was {Prop_UpTime_Seconds} seconds, active worktime was {Prop_WorkTime_MilliSeconds} MilliSeconds.
Microsoft-Windows-DeviceSetupManager  |  102       |           |
Microsoft-Windows-DeviceSetupManager  |  103       |           |
Microsoft-Windows-DeviceSetupManager  |  104       |           |  DSM Service failed to start, result={HRESULT}
Microsoft-Windows-DeviceSetupManager  |  105       |           |
Microsoft-Windows-DeviceSetupManager  |  106       |           |  DSM Service is leaving the retry state, there have been {Prop_RetryCycleCount} retry cycles in this session
Microsoft-Windows-DeviceSetupManager  |  108       |           |  The DSM service has entered service state '{Prop_CoreServiceState}'
Microsoft-Windows-DeviceSetupManager  |  109       |           |  The DSM service has entered service mode '{Prop_CoreServiceMode}'
Microsoft-Windows-DeviceSetupManager  |  110       |           |  Job ({Prop_JobId}) has started for device container '{Prop_ContainerId}', type={Prop_JobType}
Microsoft-Windows-DeviceSetupManager  |  111       |           |  Job ({Prop_JobId}) has completed for device container '{Prop_ContainerId}', status={Prop_JobStatus}
Microsoft-Windows-DeviceSetupManager  |  112       |           |  Device '{Prop_DeviceName}' ({Prop_ContainerId}) has been serviced, processed {Prop_TaskCount} tasks, wrote {Prop_PropertyCount} properties, active worktime was {Prop_WorkTime_MilliSeconds} milliseconds.
Microsoft-Windows-DeviceSetupManager  |  120       |           |  Driver update {Prop_PackageId} has been downloaded from Windows Update, download time was {Prop_MilliSeconds} milliseconds
Microsoft-Windows-DeviceSetupManager  |  121       |           |  Driver install failed, result={HRESULT} for devnode '{Prop_DevnodeId}'
Microsoft-Windows-DeviceSetupManager  |  122       |           |
Microsoft-Windows-DeviceSetupManager  |  123       |           |  The DSM service was delayed by {Prop_Seconds} seconds for a driver query/download/install on device '{Prop_DeviceId}'
Microsoft-Windows-DeviceSetupManager  |  124       |           |  Driver {Prop_PackageId} was installed on device {Prop_DeviceInstanceId}, install time was {Prop_MilliSeconds} milliseconds
Microsoft-Windows-DeviceSetupManager  |  125       |           |  Installation of a driver on device {Prop_DevnodeId} was blocked by PnP restriction policy
Microsoft-Windows-DeviceSetupManager  |  126       |           |  Device '{Prop_DeviceInstanceId}' matched driver update {Prop_PackageId}
Microsoft-Windows-DeviceSetupManager  |  130       |           |  Metadata package {Prop_MetadataPackageId} has been staged for container {Prop_ContainerId}, time was {Prop_StageTimeMilliSeconds} milliseconds
Microsoft-Windows-DeviceSetupManager  |  131       |           |  Metadata staging failed, result={HRESULT} for container '{Prop_ContainerId}'
Microsoft-Windows-DeviceSetupManager  |  150       |           |  The device '{Prop_DeviceName}' with container ID {Prop_ContainerId}, has been removed.
Microsoft-Windows-DeviceSetupManager  |  151       |           |  The device '{Prop_DeviceName}' with container ID {Prop_ContainerId}, failed to respond to a device remove request.
Microsoft-Windows-DeviceSetupManager  |  152       |           |  Removal of device node '{Prop_DevnodeId}' failed with error code {HRESULT}.
Microsoft-Windows-DeviceSetupManager  |  160       |           |  Software {Prop_SoftwareName} was installed for device {Prop_DeviceInstanceId}, install time was {Prop_InstallTime} milliseconds.
Microsoft-Windows-DeviceSetupManager  |  161       |           |  Software {Prop_SoftwareName} was not newer, Version: '{Prop_HiHighPartNew}.{Prop_LoHighPartNew}.{Prop_HiLowPartNew}.{Prop_LoLowPartNew}'.  Current Version: '{Prop_HiHighPartOld}.{Prop_LoHighPartOld}.{Prop_HiLowPartOld}.{Prop_LoLowPartOld}'.
Microsoft-Windows-DeviceSetupManager  |  162       |           |  Software {Prop_SoftwareName} failed installation with error {Error}.
Microsoft-Windows-DeviceSetupManager  |  163       |           |  Software {Prop_SoftwareName} failed installation with error {Error} and process exit code {ExitCode}.
Microsoft-Windows-DeviceSetupManager  |  164       |           |  Software {Prop_SoftwareName} had non-critical error {Error} during installation, will retry later.
Microsoft-Windows-DeviceSetupManager  |  165       |           |  Software {Prop_SoftwareName} is being launched with command line: '{Prop_CommandLine}'.
Microsoft-Windows-DeviceSetupManager  |  166       |           |  Device {Prop_DeviceInstanceId} is requesting the following link from the Store: '{Prop_SoftwareLinks}'.
Microsoft-Windows-DeviceSetupManager  |  167       |           |  Product for pfn {Prop_SoftwarePfn} located: ProductId: {Prop_ProductId}, IsFramework: {Prop_IsFramework}
Microsoft-Windows-DeviceSetupManager  |  168       |           |  Uninstalling existing pfn {Prop_SoftwarePfn} failed with error {ErrorCode}
Microsoft-Windows-DeviceSetupManager  |  169       |           |  ProductId {Prop_ProductId} is already installed and is being checked for updates
Microsoft-Windows-DeviceSetupManager  |  170       |           |  ProductId {Prop_ProductId} is being installed
Microsoft-Windows-DeviceSetupManager  |  171       |           |  ProductId {Prop_ProductId} done processing, install {Prop_InstallType} completed with error {ErrorCode}
Microsoft-Windows-DeviceSetupManager  |  180       |           |  Retrieving Store entitlement for pfn {Prop_ProductId} failed with error {ErrorCode}
Microsoft-Windows-DeviceSetupManager  |  200       |           |
Microsoft-Windows-DeviceSetupManager  |  201       |           |
Microsoft-Windows-DeviceSetupManager  |  202       |           |
Microsoft-Windows-DeviceSetupManager  |  203       |           |
Microsoft-Windows-DeviceSetupManager  |  220       |           |  Registered the handler {Prop_NotificationHandler} for the app {Prop_PackageId} to handle notifications from the device container {Prop_ContainerId}.
Microsoft-Windows-DeviceSetupManager  |  221       |           |  A handler for the app {Prop_PackageId} was already registered for the device container {Prop_ContainerId}.
Microsoft-Windows-DeviceSetupManager  |  222       |           |  The device container {Prop_ContainerId} and the app {Prop_PackageId} specify background task information, but we failed to register with error {HRESULT}.
Microsoft-Windows-DeviceSetupManager  |  223       |           |  Unregistered for the Print background task after uninstalling the app {Prop_PackageId}.
Microsoft-Windows-DeviceSetupManager  |  224       |           |  Unregistered for the Mobile Operator background task after uninstalling the app {Prop_PackageId}.
Microsoft-Windows-DeviceSetupManager  |  230       |           |  Made the request to the store to download the app {Prop_PackageId} for device {Prop_ContainerId}.
Microsoft-Windows-DeviceSetupManager  |  231       |           |  Successfully installed the app {Prop_PackageId} from the store for device {Prop_ContainerId}.
Microsoft-Windows-DeviceSetupManager  |  232       |           |  There was an error trying to install app {Prop_PackageId} from the store for device {Prop_ContainerId}.  This operation will be retried when the device is reconnected or the user logs on again.
Microsoft-Windows-DeviceSetupManager  |  233       |           |  There was an error trying to install app {Prop_PackageId} from the store for device {Prop_ContainerId}.
Microsoft-Windows-DeviceSetupManager  |  234       |           |  Device {Prop_DevnodeId} has had a driver update installed. Install time was {Prop_MilliSeconds} milliseconds
Microsoft-Windows-DeviceSetupManager  |  300       |           |  The device container '{Prop_ContainerId}' has entered the ready state
Microsoft-Windows-DeviceSetupManager  |  301       |           |  Device setup for container '{Prop_ContainerId}' has been completed.
Microsoft-Windows-DeviceSetupManager  |  302       |           |  Device metadata that contains an extension namespace has been parsed for container '{Prop_ContainerId}', ExtensionNamespace = '{Prop_ServiceInfoNamespace}', Culture = '{Prop_CultureCode}'
Microsoft-Windows-DeviceSetupManager  |  400       |           |
Microsoft-Windows-DeviceSetupManager  |  401       |           |
Microsoft-Windows-DeviceSetupManager  |  402       |           |
Microsoft-Windows-DeviceSetupManager  |  403       |           |
Microsoft-Windows-DeviceSetupManager  |  404       |           |
Microsoft-Windows-DeviceSetupManager  |  405       |           |
Microsoft-Windows-DeviceSetupManager  |  406       |           |
Microsoft-Windows-DeviceSetupManager  |  407       |           |
Microsoft-Windows-DeviceSetupManager  |  408       |           |
Microsoft-Windows-DeviceSetupManager  |  409       |           |
Microsoft-Windows-DeviceSetupManager  |  410       |           |
Microsoft-Windows-DeviceSetupManager  |  411       |           |
Microsoft-Windows-DeviceSetupManager  |  412       |           |
Microsoft-Windows-DeviceSetupManager  |  413       |           |
Microsoft-Windows-DeviceSetupManager  |  7710      |           |
Microsoft-Windows-DeviceSetupManager  |  7711      |           |
Microsoft-Windows-DeviceSetupManager  |  7712      |           |
Microsoft-Windows-DeviceSetupManager  |  7713      |           |
Microsoft-Windows-DeviceSetupManager  |  7714      |           |
Microsoft-Windows-DeviceSetupManager  |  7715      |           |