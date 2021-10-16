Provider                       |  Event ID  |  Channel  |  Message
-------------------------------|------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-GroupPolicy  |  1002      |  System   |  The processing of Group Policy failed because of a system allocation failure. Please ensure the computer is not running low on resources (memory, available disk space). Group Policy processing will be attempted at the next refresh cycle.
Microsoft-Windows-GroupPolicy  |  1006      |  System   |  The processing of Group Policy failed. Windows could not authenticate to the Active Directory service on a domain controller. (LDAP Bind function call failed). Look in the details tab for error code and description.
Microsoft-Windows-GroupPolicy  |  1007      |  System   |  The processing of Group Policy failed. Windows could not determine the site associated for this computer, which is required for Group Policy processing.
Microsoft-Windows-GroupPolicy  |  1030      |  System   |  The processing of Group Policy failed. Windows attempted to retrieve new Group Policy settings for this user or computer. Look in the details tab for error code and description. Windows will automatically retry this operation at the next refresh cycle. Computers joined to the domain must have proper name resolution and network connectivity to a domain controller for discovery of new Group Policy objects and settings. An event will be logged when Group Policy is successful.
Microsoft-Windows-GroupPolicy  |  1052      |  System   |  The processing of Group Policy failed. Windows could not determine the role of this computer. Role information (Workgroup, Member Server or Domain Controller) is required to process Group Policy.
Microsoft-Windows-GroupPolicy  |  1053      |  System   |  The processing of Group Policy failed. Windows could not resolve the username. This could be caused by one of more of the following: a) Name Resolution failure on the current domain controller. b) Active Directory Replication Latency (an account created on another domain controller has not replicated to the current domain controller).
Microsoft-Windows-GroupPolicy  |  1054      |  System   |  The processing of Group Policy failed. Windows could not obtain the name of a domain controller. This could be caused by a name resolution failure. Verify your Domain Name System (DNS) is configured and working correctly.
Microsoft-Windows-GroupPolicy  |  1055      |  System   |  The processing of Group Policy failed. Windows could not resolve the computer name. This could be caused by one of more of the following: a) Name Resolution failure on the current domain controller. b) Active Directory Replication Latency (an account created on another domain controller has not replicated to the current domain controller).
Microsoft-Windows-GroupPolicy  |  1058      |  System   |  The processing of Group Policy failed. Windows attempted to read the file {FilePath} from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: a) Name Resolution/Network Connectivity to the current domain controller. b) File Replication Service Latency (a file created on another domain controller has not replicated to the current domain controller). c) The Distributed File System (DFS) client has been disabled.
Microsoft-Windows-GroupPolicy  |  1065      |  System   |  The processing of Group Policy failed. Windows could not evaluate the Windows Management Instrumentation (WMI) filter for the Group Policy object {GPOCNName}. This could be caused by RSOP being disabled or Windows Management Instrumentation (WMI) service being disabled, stopped or other WMI errors. Make sure the WMI service is started and the start-up type is set to automatic. New Group Policy objects or settings will not process until this event has been resolved.
Microsoft-Windows-GroupPolicy  |  1068      |  System   |  The processing of Group Policy was interrupted. Windows prematurely ended the discovery and enforcement of Group Policy settings because the computer was requested to shutdown or the user logged off. Group Policy processing will be attempted next refresh cycle, on the next computer reboot or the next user logon.
Microsoft-Windows-GroupPolicy  |  1079      |  System   |  The processing of Group Policy failed. Windows could not obtain the list of Group Policy objects applicable for this computer or user. View the event details for more information.
Microsoft-Windows-GroupPolicy  |  1080      |  System   |  The processing of Group Policy failed. Windows could not search the Active Directory organisation unit hierarchy. View the event details for more information.
Microsoft-Windows-GroupPolicy  |  1085      |  System   |  Windows failed to apply the {ExtensionName} settings. {ExtensionName} settings might have its own log file. Please click on the "More information" link.
Microsoft-Windows-GroupPolicy  |  1088      |  System   |  The processing of Group Policy failed. Windows attempted to query the list of Group Policy objects and exceeded the maximum limit (999).
Microsoft-Windows-GroupPolicy  |  1089      |  System   |  Windows failed to record Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. This could be caused by RSOP being disabled or Windows Management Instrumentation (WMI) service being disabled, stopped or other WMI errors. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.
Microsoft-Windows-GroupPolicy  |  1090      |  System   |  Windows failed to record Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. This could be caused by Windows Management Instrumentation (WMI) service being disabled, stopped or other WMI errors. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.
Microsoft-Windows-GroupPolicy  |  1091      |  System   |  Windows could not record the Resultant Set of Policy (RSoP) information for the Group Policy extension <{ExtensionName}>. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.
Microsoft-Windows-GroupPolicy  |  1095      |  System   |  Windows encountered an error while recording Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.
Microsoft-Windows-GroupPolicy  |  1096      |  System   |  The processing of Group Policy failed. Windows could not apply the registry-based policy settings for the Group Policy object {GPOCNName}. Group Policy settings will not be resolved until this event is resolved. View the event details for more information on the filename and path that caused the failure.
Microsoft-Windows-GroupPolicy  |  1097      |  System   |  The processing of Group Policy failed. Windows could not determine the computer account to enforce Group Policy settings. This may be transient. Group Policy settings, including computer configuration, will not be enforced for this computer.
Microsoft-Windows-GroupPolicy  |  1101      |  System   |  The processing of Group Policy failed. Windows could not locate the directory object {DSObjectName}. Group Policy settings will not be enforced until this event is resolved. View the event details for more information on this error.
Microsoft-Windows-GroupPolicy  |  1104      |  System   |  Windows was unable to read the Windows Management Instrumentation (WMI) filter information associated with the Group Policy object {GPOCNName}. This may be caused by a deleted WMI Filter defined in the domain that is still in use by Group Policy objects. Group Policy settings for this Group Policy object will not be enforced. Other Group Policy objects may still apply. Windows will attempt to retrieve this information at the next policy cycle. This specific problem may be resolved by identifying all GPOs that reference the WMI filter and removing the references. Contact an administrator if this event recurs for several hours.
Microsoft-Windows-GroupPolicy  |  1109      |  System   |  The user account is in a different forest than the computer account. The processing of Group Policy from another forest is not allowed. Group Policy will be processed using Loopback Replace mode. The scope of the user policy settings will be determined by the location of the computer object in Active Directory. The settings will be acquired from the User Configuration of these policies.
Microsoft-Windows-GroupPolicy  |  1110      |  System   |  The processing of Group Policy failed. Windows could not determine if the user and computer accounts are in the same forest. Ensure the user domain name matches the name of a trusted domain that resides in the same forest as the computer account.
Microsoft-Windows-GroupPolicy  |  1112      |  System   |  The Group Policy Client Side Extension {ExtensionName} was unable to apply one or more settings because the changes must be processed before system start-up or user logon. The system will wait for Group Policy processing to finish completely before the next start-up or logon for this user, and this may result in slow start-up and boot performance.
Microsoft-Windows-GroupPolicy  |  1125      |  System   |  The processing of Group Policy failed because of an internal system error. Please see the Group Policy operational log for the specific error message. An attempt will be made to process Group Policy again at the next refresh cycle.
Microsoft-Windows-GroupPolicy  |  1126      |  System   |  Windows was unable to determine whether new Group Policy settings defined by a network administrator should be enforced for this user or computer because this computer's clock is not synchronised with the clock of one of the domain controllers for the domain. Because of this issue, this computer system may not be in compliance with the network administrator’s requirements, and users of this system may not be able to use some functionality on the network. Windows will periodically attempt to retry this operation, and it is possible that either this system or the domain controller will correct the time settings without intervention by an administrator, so the problem will be corrected. If this issue persists for more than an hour, checking the local system's clock settings to ensure they are accurate and are synchronised with the clocks on the network's domain controllers is one way to resolve this problem. A network administrator may be required to resolve the issue if correcting the local time settings does not address the problem.
Microsoft-Windows-GroupPolicy  |  1127      |  System   |  The processing of Group Policy failed due to an internal error. Please look into the Group Policy operational log for the specific error message. An attempt will be made to process Group Policy again at the next refresh cycle.
Microsoft-Windows-GroupPolicy  |  1128      |  System   |  The Group Policy Client Side Extension {ExtensionName} may have caused the Group Policy Service to terminate unexpectedly. To prevent further failures in the Group Policy Service, this extension has been temporarily disabled until after the next system restart. Group Policy settings managed by this extension may no longer be enforced until the system is restarted. The vendor of this extension should be contacted if this issue recurs.
Microsoft-Windows-GroupPolicy  |  1129      |  System   |  The processing of Group Policy failed because of lack of network connectivity to a domain controller. This may be a transient condition. A success message would be generated once the machine gets connected to the domain controller and Group Policy has successfully processed. If you do not see a success message for several hours, then contact your administrator.
Microsoft-Windows-GroupPolicy  |  1130      |  System   |  {ScriptType} failed. 	GPO Name: {GPODisplayName}	GPO File System Path: {GPOFileSystemPath}	Script Name: {GPOScriptCommandString}
Microsoft-Windows-GroupPolicy  |  1500      |  System   |  The Group Policy settings for the computer were processed successfully. There were no changes detected since the last successful processing of Group Policy.
Microsoft-Windows-GroupPolicy  |  1501      |  System   |  The Group Policy settings for the user were processed successfully. There were no changes detected since the last successful processing of Group Policy.
Microsoft-Windows-GroupPolicy  |  1502      |  System   |  The Group Policy settings for the computer were processed successfully. New settings from {NumberOfGroupPolicyObjects} Group Policy objects were detected and applied.
Microsoft-Windows-GroupPolicy  |  1503      |  System   |  The Group Policy settings for the user were processed successfully. New settings from {NumberOfGroupPolicyObjects} Group Policy objects were detected and applied.
Microsoft-Windows-GroupPolicy  |  4000      |           |  Starting computer boot policy processing for {PrincipalSamName}. Activity id: {PolicyActivityId}
Microsoft-Windows-GroupPolicy  |  4000      |           |  Starting computer boot policy processing for {PrincipalSamName}. Activity id: {PolicyActivityId}
Microsoft-Windows-GroupPolicy  |  4001      |           |  Starting user logon Policy processing for {PrincipalSamName}. Activity id: {PolicyActivityId}
Microsoft-Windows-GroupPolicy  |  4001      |           |  Starting user logon Policy processing for {PrincipalSamName}. Activity id: {PolicyActivityId}
Microsoft-Windows-GroupPolicy  |  4002      |           |  Starting policy processing due to network state change for computer {PrincipalSamName}. Activity id: {PolicyActivityId}
Microsoft-Windows-GroupPolicy  |  4002      |           |  Starting policy processing due to network state change for computer {PrincipalSamName}. Activity id: {PolicyActivityId}
Microsoft-Windows-GroupPolicy  |  4003      |           |  Starting policy processing due to network state change for user {PrincipalSamName}. Activity id: {PolicyActivityId}
Microsoft-Windows-GroupPolicy  |  4003      |           |  Starting policy processing due to network state change for user {PrincipalSamName}. Activity id: {PolicyActivityId}
Microsoft-Windows-GroupPolicy  |  4004      |           |  Starting manual processing of policy for computer {PrincipalSamName}. Activity id: {PolicyActivityId}
Microsoft-Windows-GroupPolicy  |  4004      |           |  Starting manual processing of policy for computer {PrincipalSamName}. Activity id: {PolicyActivityId}
Microsoft-Windows-GroupPolicy  |  4005      |           |  Starting manual processing of policy for user {PrincipalSamName}. Activity id: {PolicyActivityId}
Microsoft-Windows-GroupPolicy  |  4005      |           |  Starting manual processing of policy for user {PrincipalSamName}. Activity id: {PolicyActivityId}
Microsoft-Windows-GroupPolicy  |  4006      |           |  Starting periodic policy processing for computer {PrincipalSamName}. Activity id: {PolicyActivityId}
Microsoft-Windows-GroupPolicy  |  4006      |           |  Starting periodic policy processing for computer {PrincipalSamName}. Activity id: {PolicyActivityId}
Microsoft-Windows-GroupPolicy  |  4007      |           |  Starting periodic policy processing for user {PrincipalSamName}. Activity id: {PolicyActivityId}
Microsoft-Windows-GroupPolicy  |  4007      |           |  Starting periodic policy processing for user {PrincipalSamName}. Activity id: {PolicyActivityId}
Microsoft-Windows-GroupPolicy  |  4016      |           |  Starting {CSEExtensionName} Extension Processing. List of applicable Group Policy objects: ({GPOListStatusString}){DescriptionString}
Microsoft-Windows-GroupPolicy  |  4017      |           |  {OperationDescription} {Parameter}
Microsoft-Windows-GroupPolicy  |  4018      |           |  Starting {ScriptType} for {PrincipalSamName}.
Microsoft-Windows-GroupPolicy  |  4019      |           |  Running script name {ScriptName}.
Microsoft-Windows-GroupPolicy  |  4115      |           |  Group Policy Service started.
Microsoft-Windows-GroupPolicy  |  4116      |           |
Microsoft-Windows-GroupPolicy  |  4117      |           |  Group Policy Service started.
Microsoft-Windows-GroupPolicy  |  4126      |           |  Group Policy receiving applicable GPOs from the domain controller.
Microsoft-Windows-GroupPolicy  |  4216      |           |  Starting to save policies to the local datastore.
Microsoft-Windows-GroupPolicy  |  4217      |           |  Starting to load policies from the local datastore.
Microsoft-Windows-GroupPolicy  |  4218      |           |  Starting the first WMI query for the policy.
Microsoft-Windows-GroupPolicy  |  4257      |           |  Starting to download policies.
Microsoft-Windows-GroupPolicy  |  4326      |           |
Microsoft-Windows-GroupPolicy  |  5016      |           |  Completed {CSEExtensionName} Extension Processing in {CSEElaspedTimeInMilliSeconds} milliseconds.
Microsoft-Windows-GroupPolicy  |  5017      |           |  {OperationDescription} {Parameter}The call completed in {OperationElaspedTimeInMilliSeconds} milliseconds.
Microsoft-Windows-GroupPolicy  |  5018      |           |  Completed {ScriptType} for {PrincipalSamName} in {ScriptElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  5019      |           |  Completed {ScriptName} in {ScriptElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  5115      |           |  Group Policy Service stopped.
Microsoft-Windows-GroupPolicy  |  5116      |           |  Successfully completed the Group Policy Service initialisation phase.
Microsoft-Windows-GroupPolicy  |  5117      |           |  Group policy session completed successfully.
Microsoft-Windows-GroupPolicy  |  5126      |           |  Group Policy successfully got applicable GPOs from the domain controller.
Microsoft-Windows-GroupPolicy  |  5216      |           |  Successfully saved policies to the local datastore.
Microsoft-Windows-GroupPolicy  |  5217      |           |  Successfully loaded policies from the local datastore.
Microsoft-Windows-GroupPolicy  |  5218      |           |  Successfully completed the first WMI query.
Microsoft-Windows-GroupPolicy  |  5257      |           |  Successfully completed downloading policies.
Microsoft-Windows-GroupPolicy  |  5308      |           |  Domain Controller details: 	Domain Controller Name: {DCName}	Domain Controller IP Address: {DCIPAddress}
Microsoft-Windows-GroupPolicy  |  5309      |           |  Computer details: 	Computer role: {MachineRole}	Network name: {NetworkName}
Microsoft-Windows-GroupPolicy  |  5310      |           |  Account details: 	Account Name: {PrincipalCNName}	Account Domain Name: {PrincipalDomainName}	DC Name: {DCName}	DC Domain Name: {DCDomainName}
Microsoft-Windows-GroupPolicy  |  5311      |           |  The loopback policy processing mode is {PolicyProcessingMode}.
Microsoft-Windows-GroupPolicy  |  5312      |           |  List of applicable Group Policy objects: {DescriptionString}
Microsoft-Windows-GroupPolicy  |  5313      |           |  The following Group Policy objects were not applicable because they were filtered out: {DescriptionString}
Microsoft-Windows-GroupPolicy  |  5314      |           |  A {LinkDescription} link was detected. The Estimated bandwidth is {BandwidthInkbps} kbps. The slow link threshold is {ThresholdInkbps} kbps.
Microsoft-Windows-GroupPolicy  |  5315      |           |  Next policy processing for {PrincipalSamName} will be attempted in {NextPolicyApplicationTime} {NextPolicyApplicationTimeUnit}.
Microsoft-Windows-GroupPolicy  |  5320      |           |  {InfoDescription}
Microsoft-Windows-GroupPolicy  |  5321      |           |  {InfoDescription} Parameter: {OperationParameter1}
Microsoft-Windows-GroupPolicy  |  5322      |           |  Group policy waited for {TimeWaitedAtStartup} milliseconds for the network subsystem at computer boot.
Microsoft-Windows-GroupPolicy  |  5323      |           |
Microsoft-Windows-GroupPolicy  |  5324      |           |  Group Policy received the notification {NotificationType} from Winlogon for session {SessionId}.
Microsoft-Windows-GroupPolicy  |  5325      |           |  Group Policy received {NotificationType} notification from Service Control Manager.
Microsoft-Windows-GroupPolicy  |  5326      |           |  Group Policy successfully discovered the Domain Controller in {DCDiscoveryTimeInMilliSeconds} milliseconds.
Microsoft-Windows-GroupPolicy  |  5327      |           |  Estimated network bandwidth on one of the connections: {NetworkBandwidthInKbps} kbps.
Microsoft-Windows-GroupPolicy  |  5331      |           |  Service configuration update to standalone was attempted due to the presence of Group Policy client extension {UpdateCauseExtensionName} that is not part of the operating system and completed with status {ErrorCode}.
Microsoft-Windows-GroupPolicy  |  5332      |           |  Group policy waited for {TimeWaitedAtStartup} milliseconds for the Direct Access CorpNet connectivity at computer boot.
Microsoft-Windows-GroupPolicy  |  5340      |           |  The Group Policy processing mode is {PolicyApplicationMode}.
Microsoft-Windows-GroupPolicy  |  5351      |           |  Group policy session returned to winlogon.
Microsoft-Windows-GroupPolicy  |  6000      |           |
Microsoft-Windows-GroupPolicy  |  6001      |           |
Microsoft-Windows-GroupPolicy  |  6002      |           |
Microsoft-Windows-GroupPolicy  |  6003      |           |
Microsoft-Windows-GroupPolicy  |  6004      |           |
Microsoft-Windows-GroupPolicy  |  6005      |           |
Microsoft-Windows-GroupPolicy  |  6006      |           |
Microsoft-Windows-GroupPolicy  |  6007      |           |
Microsoft-Windows-GroupPolicy  |  6016      |           |  Completed {CSEExtensionName} Extension Processing in {CSEElaspedTimeInMilliSeconds} milliseconds.
Microsoft-Windows-GroupPolicy  |  6017      |           |
Microsoft-Windows-GroupPolicy  |  6018      |           |
Microsoft-Windows-GroupPolicy  |  6019      |           |
Microsoft-Windows-GroupPolicy  |  6033      |           |  Skipped {CSEExtensionName} Extension based on Group Policy client-side processing rules. Refer to a Resultant Set of Policy report for more information.
Microsoft-Windows-GroupPolicy  |  6034      |           |
Microsoft-Windows-GroupPolicy  |  6035      |           |  {CSEExtensionName} Extension deferred processing until next synchronous foreground. Refer to a Resultant Set of Policy report for more information.
Microsoft-Windows-GroupPolicy  |  6226      |           |
Microsoft-Windows-GroupPolicy  |  6308      |           |
Microsoft-Windows-GroupPolicy  |  6309      |           |
Microsoft-Windows-GroupPolicy  |  6310      |           |
Microsoft-Windows-GroupPolicy  |  6311      |           |
Microsoft-Windows-GroupPolicy  |  6312      |           |
Microsoft-Windows-GroupPolicy  |  6313      |           |
Microsoft-Windows-GroupPolicy  |  6314      |           |  Group policy bandwidth estimation failed. Group policy processing will continue. Assuming {LinkDescription} link.
Microsoft-Windows-GroupPolicy  |  6315      |           |
Microsoft-Windows-GroupPolicy  |  6320      |           |  Warning: {WarningDescription} Warning code {WarningCode}.
Microsoft-Windows-GroupPolicy  |  6321      |           |  Warning: {WarningDescription} Parameter: {OperationParameter1} : Warning code {WarningCode}.
Microsoft-Windows-GroupPolicy  |  6322      |           |
Microsoft-Windows-GroupPolicy  |  6323      |           |  Group Policy dependency ({DisplayName}) did not start. As a result, network related features of Group Policy such as bandwidth estimation and response to network changes will not work.
Microsoft-Windows-GroupPolicy  |  6324      |           |
Microsoft-Windows-GroupPolicy  |  6325      |           |
Microsoft-Windows-GroupPolicy  |  6326      |           |
Microsoft-Windows-GroupPolicy  |  6327      |           |
Microsoft-Windows-GroupPolicy  |  6330      |           |  An unfinished invocation of the Group Policy Client Side Extension {InfoDescription} from a previous instance of the Group Policy Service has been detected. This may indicate that the extension caused the Group Policy Client Service to terminate unexpectedly.
Microsoft-Windows-GroupPolicy  |  6331      |           |  Invalid Error Message.
Microsoft-Windows-GroupPolicy  |  6332      |           |
Microsoft-Windows-GroupPolicy  |  6337      |           |
Microsoft-Windows-GroupPolicy  |  6338      |           |
Microsoft-Windows-GroupPolicy  |  6339      |           |
Microsoft-Windows-GroupPolicy  |  6341      |           |
Microsoft-Windows-GroupPolicy  |  6342      |           |
Microsoft-Windows-GroupPolicy  |  6344      |           |  Group Policy network status is slowlink during sync mode process.
Microsoft-Windows-GroupPolicy  |  6345      |           |  The contact to dc is time-out during group policy sync mode process.
Microsoft-Windows-GroupPolicy  |  6346      |           |  Group Policy switches sync mode process to async mode.
Microsoft-Windows-GroupPolicy  |  7000      |           |  Computer boot policy processing failed for {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7000      |           |  Computer boot policy processing failed for {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7001      |           |  User logon policy processing failed for {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7001      |           |  User logon policy processing failed for {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7002      |           |  Policy processing due to network state change failed for computer {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7002      |           |  Policy processing due to network state change failed for computer {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7003      |           |  Policy processing due to network state change failed for user {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7003      |           |  Policy processing due to network state change failed for user {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7004      |           |  Manual processing of policy failed for computer {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7004      |           |  Manual processing of policy failed for computer {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7005      |           |  Manual processing of policy failed for user {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7005      |           |  Manual processing of policy failed for user {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7006      |           |  Periodic policy processing failed for computer {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7006      |           |  Periodic policy processing failed for computer {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7007      |           |  Periodic policy processing failed for user {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7007      |           |  Periodic policy processing failed for user {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7016      |           |  Completed {CSEExtensionName} Extension Processing in {CSEElaspedTimeInMilliSeconds} milliseconds.
Microsoft-Windows-GroupPolicy  |  7017      |           |  {OperationDescription} {Parameter}The call failed after {OperationElaspedTimeInMilliSeconds} milliseconds.
Microsoft-Windows-GroupPolicy  |  7018      |           |  Script for {PrincipalSamName} failed in {ScriptElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  7019      |           |
Microsoft-Windows-GroupPolicy  |  7117      |           |  Group policy session completed with error.
Microsoft-Windows-GroupPolicy  |  7126      |           |  Group Policy could not get applicable GPOs from the domain controller.
Microsoft-Windows-GroupPolicy  |  7216      |           |  Saved policies to the local datastore with error.
Microsoft-Windows-GroupPolicy  |  7217      |           |  Loaded policies from the local datastore with error.
Microsoft-Windows-GroupPolicy  |  7257      |           |  Downloaded policies with error.
Microsoft-Windows-GroupPolicy  |  7308      |           |
Microsoft-Windows-GroupPolicy  |  7309      |           |
Microsoft-Windows-GroupPolicy  |  7310      |           |
Microsoft-Windows-GroupPolicy  |  7311      |           |
Microsoft-Windows-GroupPolicy  |  7312      |           |
Microsoft-Windows-GroupPolicy  |  7313      |           |
Microsoft-Windows-GroupPolicy  |  7314      |           |
Microsoft-Windows-GroupPolicy  |  7315      |           |
Microsoft-Windows-GroupPolicy  |  7320      |           |  Error: {ErrorDescription} Error code {ErrorCode}.
Microsoft-Windows-GroupPolicy  |  7321      |           |  Error: {ErrorDescription} Parameter: {OperationParameter1} : Error code {ErrorCode}.
Microsoft-Windows-GroupPolicy  |  7322      |           |
Microsoft-Windows-GroupPolicy  |  7323      |           |
Microsoft-Windows-GroupPolicy  |  7324      |           |
Microsoft-Windows-GroupPolicy  |  7325      |           |
Microsoft-Windows-GroupPolicy  |  7326      |           |  Group Policy failed to discover the Domain Controller details in {DCDiscoveryTimeInMilliSeconds} milliseconds.
Microsoft-Windows-GroupPolicy  |  7327      |           |
Microsoft-Windows-GroupPolicy  |  7331      |           |  Service configuration update to standalone was attempted due to the presence of Group Policy client extension {UpdateCauseExtensionName} that is not part of the operating system and completed with status {ErrorCode}.
Microsoft-Windows-GroupPolicy  |  7332      |           |
Microsoft-Windows-GroupPolicy  |  8000      |           |  Completed computer boot policy processing for {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  8000      |           |  Completed computer boot policy processing for {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  8001      |           |  Completed user logon policy processing for {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  8001      |           |  Completed user logon policy processing for {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  8002      |           |  Completed policy processing due to network state change for computer {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  8002      |           |  Completed policy processing due to network state change for computer {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  8003      |           |  Completed policy processing due to network state change for user {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  8003      |           |  Completed policy processing due to network state change for user {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  8004      |           |  Completed manual processing of policy for computer {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  8004      |           |  Completed manual processing of policy for computer {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  8005      |           |  Completed manual processing of policy for user {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  8005      |           |  Completed manual processing of policy for user {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  8006      |           |  Completed periodic policy processing for computer {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  8006      |           |  Completed periodic policy processing for computer {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  8007      |           |  Completed periodic policy processing for user {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  8007      |           |  Completed periodic policy processing for user {PrincipalSamName} in {PolicyElaspedTimeInSeconds} seconds.
Microsoft-Windows-GroupPolicy  |  8016      |           |  {CSEExtensionName} Extension ({CSEExtensionId}) requests a sync mode process.
Microsoft-Windows-GroupPolicy  |  9001      |           |  This machine is configured to retrieve Group Policy files from a file share in an insecure way.UNC Path: {UncPath}Mutual Authentication Enforced: {MutualAuthenticationEnforced}Integrity Enforced: {IntegrityEnforced}Guidance: The UNC path contains log-on scripts and/or files that control system security policies. Microsoft recommends configuring Windows to require both mutual authentication and integrity when accessing files on this UNC path.For details on configuring Windows machines to require additional security when accessing specific UNC paths, visit http://support.microsoft.com/kb/3000483.