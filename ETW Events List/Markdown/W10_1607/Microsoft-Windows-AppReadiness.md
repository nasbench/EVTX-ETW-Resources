Provider                        |  Level        |  Event ID  |  Version  |  Channel      |  Task                                     |  Opcode  |  Keyword        |  Message
--------------------------------|---------------|------------|-----------|---------------|-------------------------------------------|----------|-----------------|----------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-AppReadiness  |  Error        |  10        |  0        |  Admin        |  AppReadiness_Error                       |          |  Error          |  The Appx operation '{Operation}' on '{PackageId}' failed for user '{User}' - {Error}. (Error: {Result})
Microsoft-Windows-AppReadiness  |  Warning      |  11        |  0        |  Operational  |  AppReadiness_Error                       |          |  Error          |  A exception was caught: {Error}.
Microsoft-Windows-AppReadiness  |  Error        |  12        |  0        |  Admin        |  AppReadiness_Error                       |          |  Error          |  The Appx preview tile generation failed for user '{User}': {Error}. (Result: {Result})
Microsoft-Windows-AppReadiness  |  Information  |  100       |  0        |  Admin        |  AppReadiness_Service_Lifetime            |  Start   |  Service        |
Microsoft-Windows-AppReadiness  |  Information  |  101       |  0        |  Admin        |  AppReadiness_Service_Lifetime            |  Stop    |  Service        |
Microsoft-Windows-AppReadiness  |  Information  |  102       |  0        |  Operational  |  AppReadiness_Service_Thread              |  Start   |  Service        |
Microsoft-Windows-AppReadiness  |  Information  |  103       |  0        |  Operational  |  AppReadiness_Service_Thread              |  Stop    |  Service        |
Microsoft-Windows-AppReadiness  |  Information  |  104       |  0        |  Operational  |  AppReadiness_Service                     |          |  Service        |  App Readiness status changed to '{Status}' (ExitCode: {ExitCode})
Microsoft-Windows-AppReadiness  |  Information  |  105       |  0        |  Operational  |  AppReadiness_Service                     |          |  Service        |  Checking for service idle. (Result={IsIdle}, Reason={Reason})
Microsoft-Windows-AppReadiness  |  Information  |  106       |  0        |  Operational  |  AppReadiness_Service                     |          |  Service        |  '{User}' has logged on.
Microsoft-Windows-AppReadiness  |  Information  |  107       |  0        |  Operational  |  AppReadiness_Service                     |          |  Service        |  '{User}' has logged off.
Microsoft-Windows-AppReadiness  |  Information  |  108       |  0        |  Operational  |  AppReadiness_PackageChange               |  Start   |  Service        |
Microsoft-Windows-AppReadiness  |  Information  |  109       |  0        |  Admin        |  AppReadiness_PackageChange               |  Stop    |  Service        |  App Readiness service has been notified of new apps. (Source: {Source}, Error: {Result})
Microsoft-Windows-AppReadiness  |  Information  |  200       |  0        |  Operational  |  AppReadiness_User_ProcessTasks           |  Start   |  User           |  Started processing tasks for '{User}'.
Microsoft-Windows-AppReadiness  |  Information  |  201       |  0        |  Operational  |  AppReadiness_User_ProcessTasks           |  Stop    |  User           |  Finished processing tasks for '{User}'.
Microsoft-Windows-AppReadiness  |  Information  |  205       |  0        |  Operational  |  AppReadiness_User_ProcessTasks           |          |  User           |  Loaded queue for '{User}' with {NumPackages} items.
Microsoft-Windows-AppReadiness  |  Information  |  206       |  0        |  Operational  |  AppReadiness_User_ProcessTasks           |  Start   |  User           |  '{TaskId}' started for {User}. (Priority: {Priority})
Microsoft-Windows-AppReadiness  |  Information  |  207       |  0        |  Operational  |  AppReadiness_User_ProcessTasks           |  Stop    |  User           |  '{TaskId}' finished for {User}. (Result: {Result})
Microsoft-Windows-AppReadiness  |  Information  |  209       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |          |  User           |  For '{User}' has changed mode from '{From}' to '{To}'
Microsoft-Windows-AppReadiness  |  Information  |  210       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |          |  User           |  App Readiness service has found new tasks for {User}.
Microsoft-Windows-AppReadiness  |  Information  |  211       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |          |  User           |  App Readiness service has completed tasks for {User}.
Microsoft-Windows-AppReadiness  |  Information  |  212       |  0        |  Operational  |  AppReadiness_User_ProcessTasks           |          |  User           |  {NumPackages} pre-installed apps found for {SID}
Microsoft-Windows-AppReadiness  |  Information  |  213       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |          |  User           |  '{Package}' {Operation} succeeded for {Username}. ({Elapsed} seconds)
Microsoft-Windows-AppReadiness  |  Error        |  214       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |          |  User           |  '{Package}' {Operation} failed for {User}. Error: '{Error}' ({Elapsed} seconds)
Microsoft-Windows-AppReadiness  |  Error        |  215       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |          |  User           |  '{Task}' failed for {Username}. Error: '{Error}' ({Elapsed} seconds)
Microsoft-Windows-AppReadiness  |  Information  |  216       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |          |  User           |  Activity for '{User}' has been suspended and will resume at {ResumeAt}.
Microsoft-Windows-AppReadiness  |  Information  |  217       |  0        |  Operational  |  AppReadiness_User_ProcessTasks           |          |  User           |  Activity for '{User}' has resumed.
Microsoft-Windows-AppReadiness  |  Information  |  218       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |          |  User           |  '{Package}' {Operation} failed for {User} and will be attempted after {AttemptAfter}.
Microsoft-Windows-AppReadiness  |  Information  |  219       |  0        |  Operational  |  AppReadiness_User_ProcessTasks           |          |  User           |  {NumPackages} pre-installed apps found for {SID}
Microsoft-Windows-AppReadiness  |  Information  |  220       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |          |  User           |  '{Task}' succeeded for {Username}. ({Elapsed} seconds)
Microsoft-Windows-AppReadiness  |  Information  |  221       |  0        |  Operational  |  AppReadiness_User_ProcessTasks           |          |  User           |  Task '{Task}' created for {Username}.
Microsoft-Windows-AppReadiness  |  Information  |  222       |  0        |  Operational  |  AppReadiness_User_ProcessTasks           |          |  User           |  '{TaskId}' was removed (Canceled: {TaskCanceled}) for '{User}' due to new opposing task of type {OpposingOperation}.
Microsoft-Windows-AppReadiness  |  Information  |  223       |  0        |  Operational  |  AppReadiness_User_Shutdown               |  Start   |  User           |  Shutdown for '{User}' has started.
Microsoft-Windows-AppReadiness  |  Information  |  224       |  0        |  Operational  |  AppReadiness_User_Shutdown               |  Stop    |  User           |  Shutdown for '{User}' has completed.
Microsoft-Windows-AppReadiness  |  Warning      |  225       |  0        |  Admin        |  AppReadiness_User_Shutdown               |          |  User           |  Canceling '{Task}' for '{Username}' due to shutdown.
Microsoft-Windows-AppReadiness  |  Information  |  226       |  0        |  Operational  |  AppReadiness_User_Shutdown               |          |  User           |  During shutdown '{User}' is waiting for tasks to complete.
Microsoft-Windows-AppReadiness  |  Information  |  227       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |          |  User           |  '{TaskId}' was selected as the next task for {User}. (Priority={Priority})
Microsoft-Windows-AppReadiness  |  Information  |  228       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |          |  User           |  '{Task}' succeeded. ({Elapsed} seconds)
Microsoft-Windows-AppReadiness  |  Information  |  229       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |          |  User           |  '{TaskId}' was selected as the next task. (Priority={Priority})
Microsoft-Windows-AppReadiness  |  Information  |  230       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |          |  User           |
Microsoft-Windows-AppReadiness  |  Information  |  231       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |  Start   |  User           |
Microsoft-Windows-AppReadiness  |  Information  |  232       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |  Stop    |  User           |  FWOpenPolicyStore returns {ExitCode}.
Microsoft-Windows-AppReadiness  |  Information  |  233       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |  Start   |  User           |
Microsoft-Windows-AppReadiness  |  Information  |  234       |  0        |  Admin        |  AppReadiness_User_ProcessTasks           |  Stop    |  User           |  FWClosePolicyStore returns {ExitCode}.
Microsoft-Windows-AppReadiness  |  Information  |  300       |  0        |  Operational  |  AppReadiness_ExecuteTask                 |  Start   |  Tasks          |  Started '{TaskId}' for '{User}'
Microsoft-Windows-AppReadiness  |  Information  |  301       |  0        |  Operational  |  AppReadiness_ExecuteTask                 |  Stop    |  Tasks          |  Finished '{TaskId}' for '{User}' lasted {Duration} seconds. ({Result})
Microsoft-Windows-AppReadiness  |  Information  |  302       |  0        |  Operational  |  AppReadiness_ExecuteTask                 |  Start   |  Tasks          |  Started group '{GroupId}' for '{User}'
Microsoft-Windows-AppReadiness  |  Information  |  303       |  0        |  Operational  |  AppReadiness_ExecuteTask                 |  Stop    |  Tasks          |  Finished group '{GroupId}' for '{User}' lasted {Duration} seconds. ({Result})
Microsoft-Windows-AppReadiness  |  Warning      |  304       |  0        |  Operational  |  AppReadiness_ExecuteTask                 |          |  Tasks          |  During execution of '{GroupId}' for '{User}' task '{TaskId}' failed. (Error: {Result})
Microsoft-Windows-AppReadiness  |  Information  |  305       |  0        |  Admin        |  AppReadiness_ExecuteTask                 |          |  Tasks          |  Package '{PackageFamilyName}' was removed from '{User}' first login group. (Reason: {Reason})
Microsoft-Windows-AppReadiness  |  Information  |  306       |  0        |  Operational  |  AppReadiness_ExecuteTask                 |          |  Tasks          |  For '{User}' task '{TaskId}' was canceled.
Microsoft-Windows-AppReadiness  |  Information  |  307       |  0        |  Operational  |  AppReadiness_ExecuteTask                 |          |  Tasks          |  Finished activation of '{PackageFamilyName}' for '{User}'. (Result: {Reason})
Microsoft-Windows-AppReadiness  |  Warning      |  308       |  0        |  Admin        |  AppReadiness_ExecuteTask                 |          |  Tasks          |  Preview tile creation failed '{PackageFamilyName}' for {User}. (Source: {Source}, Error: {Result})
Microsoft-Windows-AppReadiness  |  Information  |  309       |  0        |  Operational  |  AppReadiness_ExecuteTask                 |  Start   |  Tasks          |  Starting registry flush for '{User}'.
Microsoft-Windows-AppReadiness  |  Information  |  310       |  0        |  Operational  |  AppReadiness_ExecuteTask                 |  Stop    |  Tasks          |  Finished registry flush for '{User}'.
Microsoft-Windows-AppReadiness  |  Error        |  311       |  0        |  Admin        |  AppReadiness_ExecuteTask                 |          |  Tasks          |  Failed to flush registry key '{Key}' for '{User}'. (Error: {Result})
Microsoft-Windows-AppReadiness  |  Information  |  312       |  0        |  Operational  |  AppReadiness_ExecuteTask                 |          |  Tasks          |  Successfully created {NumPackages} preview tiles for {User}. (Source: {Source})
Microsoft-Windows-AppReadiness  |  Warning      |  313       |  0        |  Operational  |  AppReadiness_ExecuteTask                 |          |  Tasks          |  '{Group}' is canceling '{Task}' for '{User}' as a result of cancel.
Microsoft-Windows-AppReadiness  |  Information  |  314       |  0        |  Operational  |  AppReadiness_ExecuteTask                 |          |  Tasks          |  '{Group}' has selected '{Task}' for '{User}' for the next task.
Microsoft-Windows-AppReadiness  |  Information  |  315       |  0        |  Operational  |  AppReadiness_ExecuteTask                 |          |  Tasks          |  '{PackageFamilyName}' was removed from '{User}' first login group. (Reason: {Reason})
Microsoft-Windows-AppReadiness  |  Warning      |  316       |  0        |  Admin        |  AppReadiness_ExecuteTask                 |          |  Tasks          |  Installing '{PackageFamilyName}' for '{User}' has hit the in-activity timeout
Microsoft-Windows-AppReadiness  |  Information  |  317       |  0        |  Operational  |  AppReadiness_PreRegister_Package         |  Start   |  Tasks          |  Starting pre-registration of '{PackageId}'
Microsoft-Windows-AppReadiness  |  Information  |  318       |  0        |  Operational  |  AppReadiness_PreRegister_Package         |  Stop    |  Tasks          |  Completed pre-registration of '{PackageId}'
Microsoft-Windows-AppReadiness  |  Error        |  319       |  0        |  Admin        |  AppReadiness_PreRegister_Package         |          |  Tasks          |  Pre-registration for '{PackageId}' failed. (Error: {Result})
Microsoft-Windows-AppReadiness  |  Error        |  320       |  0        |  Admin        |  AppReadiness_ExecuteTask                 |          |  Tasks          |  Failed to flush registry key '{Key}'. (Error: {Result})
Microsoft-Windows-AppReadiness  |  Information  |  1001      |  0        |  Operational  |  AppReadiness_Api_Install                 |  Start   |  Api            |  API Enter for '{User}' (Process: {ProcessId})
Microsoft-Windows-AppReadiness  |  Information  |  1002      |  0        |  Operational  |  AppReadiness_Api_Install                 |  Stop    |  Api            |  API Exit for '{User}' (Process: {ProcessId} Result: {Result})
Microsoft-Windows-AppReadiness  |  Information  |  1003      |  0        |  Operational  |  AppReadiness_Api_Remove                  |  Start   |  Api            |  API Enter for '{User}' (Process: {ProcessId})
Microsoft-Windows-AppReadiness  |  Information  |  1004      |  0        |  Operational  |  AppReadiness_Api_Remove                  |  Stop    |  Api            |  API Exit for '{User}' (Process: {ProcessId} Result: {Result})
Microsoft-Windows-AppReadiness  |  Information  |  1005      |  0        |  Operational  |  AppReadiness_Api_GetTask                 |  Start   |  Api            |  API Enter for '{User}' (Process: {ProcessId})
Microsoft-Windows-AppReadiness  |  Information  |  1006      |  0        |  Operational  |  AppReadiness_Api_GetTask                 |  Stop    |  Api            |  API Exit for '{User}' (Process: {ProcessId} Result: {Result})
Microsoft-Windows-AppReadiness  |  Information  |  1009      |  0        |  Operational  |  AppReadiness_Api_ProcessTasks            |  Start   |  Api            |  API Enter for '{User}' (Process: {ProcessId})
Microsoft-Windows-AppReadiness  |  Information  |  1010      |  0        |  Operational  |  AppReadiness_Api_ProcessTasks            |  Stop    |  Api            |  API Exit for '{User}' (Process: {ProcessId} Result: {Result})
Microsoft-Windows-AppReadiness  |  Information  |  1013      |  0        |  Operational  |  AppReadiness_Api_HandlePackageChange     |  Start   |  Api            |  API Enter for '{User}' (Process: {ProcessId})
Microsoft-Windows-AppReadiness  |  Information  |  1014      |  0        |  Operational  |  AppReadiness_Api_HandlePackageChange     |  Stop    |  Api            |  API Exit for '{User}' (Process: {ProcessId} Result: {Result})
Microsoft-Windows-AppReadiness  |  Information  |  1015      |  0        |  Operational  |  AppReadiness_Api_CreateTask              |  Start   |  Api            |  API Enter for '{User}' (Process: {ProcessId})
Microsoft-Windows-AppReadiness  |  Information  |  1016      |  0        |  Operational  |  AppReadiness_Api_CreateTask              |  Stop    |  Api            |  API Exit for '{User}' (Process: {ProcessId} Result: {Result})
Microsoft-Windows-AppReadiness  |  Information  |  1017      |  0        |  Operational  |  AppReadiness_Api_EnterLogonPhase         |  Start   |  Api            |  API Enter for '{User}' (Process: {ProcessId})
Microsoft-Windows-AppReadiness  |  Information  |  1018      |  0        |  Operational  |  AppReadiness_Api_EnterLogonPhase         |  Stop    |  Api            |  API Exit for '{User}' (Process: {ProcessId} Result: {Result})
Microsoft-Windows-AppReadiness  |  Information  |  1019      |  0        |  Operational  |  AppReadiness_Api_ResolveStoreCategories  |  Start   |  Api            |  API Enter for '{User}' (Process: {ProcessId})
Microsoft-Windows-AppReadiness  |  Information  |  1020      |  0        |  Operational  |  AppReadiness_Api_ResolveStoreCategories  |  Stop    |  Api            |  API Exit for '{User}' (Process: {ProcessId} Result: {Result})
Microsoft-Windows-AppReadiness  |  Information  |  1021      |  0        |  Admin        |  AppReadiness_Api_DisableInAuditMode      |          |  Api            |  DisableInAuditMode registry value set to block API calls while in audit mode (audit mode: {IsAuditMode}).
Microsoft-Windows-AppReadiness  |  Information  |  2000      |  0        |  Debug        |  AppReadiness_ScorePackage                |  Start   |  Scoring        |
Microsoft-Windows-AppReadiness  |  Information  |  2001      |  0        |  Debug        |  AppReadiness_ScorePackage                |  Stop    |  Scoring        |
Microsoft-Windows-AppReadiness  |  Information  |  2002      |  0        |  Debug        |  AppReadiness_ScorePackage                |          |  Scoring        |
Microsoft-Windows-AppReadiness  |  Information  |  2003      |  0        |  Debug        |  AppReadiness_ScorePackage                |          |  Scoring        |
Microsoft-Windows-AppReadiness  |  Information  |  2005      |  0        |  Debug        |  AppReadiness_ScorePackage                |          |  Scoring        |
Microsoft-Windows-AppReadiness  |  Information  |  2006      |  0        |  Debug        |  AppReadiness_ScorePackage                |          |  Scoring        |
Microsoft-Windows-AppReadiness  |  Information  |  2007      |  0        |  Debug        |  AppReadiness_ScorePackage                |          |  Scoring        |
Microsoft-Windows-AppReadiness  |  Information  |  2008      |  0        |  Debug        |  AppReadiness_ScorePackage                |          |  Scoring        |
Microsoft-Windows-AppReadiness  |  Information  |  2009      |  0        |  Debug        |  AppReadiness_ScorePackage                |          |  Scoring        |
Microsoft-Windows-AppReadiness  |  Information  |  2500      |  0        |  Debug        |  AppReadiness_BrokerSession               |  Start   |  BrokerSession  |
Microsoft-Windows-AppReadiness  |  Information  |  2501      |  0        |  Debug        |  AppReadiness_BrokerSession               |  Stop    |  BrokerSession  |
Microsoft-Windows-AppReadiness  |  Information  |  2502      |  0        |  Debug        |  AppReadiness_BrokerSession               |          |  BrokerSession  |
Microsoft-Windows-AppReadiness  |  Information  |  2503      |  0        |  Debug        |  AppReadiness_BrokerSession               |          |  BrokerSession  |
Microsoft-Windows-AppReadiness  |  Information  |  2504      |  0        |  Operational  |  AppReadiness_BrokerSession               |          |  BrokerSession  |
Microsoft-Windows-AppReadiness  |  Information  |  3000      |  0        |  Debug        |  AppReadiness_PerfTrack                   |  Start   |  Tasks          |
Microsoft-Windows-AppReadiness  |  Information  |  3001      |  0        |  Debug        |  AppReadiness_PerfTrack                   |  Stop    |  Tasks          |
Microsoft-Windows-AppReadiness  |  Information  |  4000      |  0        |  Operational  |  AppReadiness_TriggerTask_Run             |          |  Triggers       |
Microsoft-Windows-AppReadiness  |  Information  |  4001      |  0        |  Operational  |  AppReadiness_MaintenanceTask_Run         |          |  Triggers       |
Microsoft-Windows-AppReadiness  |  Information  |  5000      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5001      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5002      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5003      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5004      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5005      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5006      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5007      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5008      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5009      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5010      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5011      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5012      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5013      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5014      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5015      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5016      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5017      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5018      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5019      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5020      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5021      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5022      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5023      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5024      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5025      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5026      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5027      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5028      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5029      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5030      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5031      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5032      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5033      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5034      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5035      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5036      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5037      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5038      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5039      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5040      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5041      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5042      |  0        |  Debug        |  AppReadiness_Timeline                    |  Start   |  Timeline       |
Microsoft-Windows-AppReadiness  |  Information  |  5043      |  0        |  Debug        |  AppReadiness_Timeline                    |  Stop    |  Timeline       |