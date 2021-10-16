Provider                        |  Event ID  |  Channel      |  Message
--------------------------------|------------|---------------|----------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-AppReadiness  |  10        |  Admin        |  The Appx operation '{Operation}' on '{PackageId}' failed for user '{User}' - {Error}. (Error: {Result})
Microsoft-Windows-AppReadiness  |  11        |  Operational  |  A exception was caught: {Error}.
Microsoft-Windows-AppReadiness  |  100       |  Admin        |
Microsoft-Windows-AppReadiness  |  101       |  Admin        |
Microsoft-Windows-AppReadiness  |  102       |  Operational  |
Microsoft-Windows-AppReadiness  |  103       |  Operational  |
Microsoft-Windows-AppReadiness  |  104       |  Operational  |  App Readiness status changed to '{Status}' (ExitCode: {ExitCode})
Microsoft-Windows-AppReadiness  |  105       |  Operational  |  Checking for service idle. (Result={IsIdle}, Reason={Reason})
Microsoft-Windows-AppReadiness  |  106       |  Operational  |  '{User}' has logged on.
Microsoft-Windows-AppReadiness  |  107       |  Operational  |  '{User}' has logged off.
Microsoft-Windows-AppReadiness  |  108       |  Operational  |
Microsoft-Windows-AppReadiness  |  109       |  Admin        |  App Readiness service has been notified of new apps. (Source: {Source}, Error: {Result})
Microsoft-Windows-AppReadiness  |  200       |  Operational  |  Started processing tasks for '{User}'.
Microsoft-Windows-AppReadiness  |  201       |  Operational  |  Finished processing tasks for '{User}'.
Microsoft-Windows-AppReadiness  |  205       |  Operational  |  Loaded queue for '{User}' with {NumPackages} items.
Microsoft-Windows-AppReadiness  |  206       |  Operational  |  '{TaskId}' started for {User}. (Priority: {Priority})
Microsoft-Windows-AppReadiness  |  207       |  Operational  |  '{TaskId}' finished for {User}. (Result: {Result})
Microsoft-Windows-AppReadiness  |  209       |  Admin        |  For '{User}' has changed mode from '{From}' to '{To}'
Microsoft-Windows-AppReadiness  |  210       |  Admin        |  App Readiness service has found new tasks for {User}.
Microsoft-Windows-AppReadiness  |  211       |  Admin        |  App Readiness service has completed tasks for {User}.
Microsoft-Windows-AppReadiness  |  212       |  Operational  |  {NumPackages} pre-installed apps found for {SID}
Microsoft-Windows-AppReadiness  |  213       |  Admin        |  '{Package}' {Operation} succeeded for {Username}. ({Elapsed} seconds)
Microsoft-Windows-AppReadiness  |  214       |  Admin        |  '{Package}' {Operation} failed for {User}. Error: '{Error}' ({Elapsed} seconds)
Microsoft-Windows-AppReadiness  |  215       |  Admin        |  '{Task}' failed for {Username}. Error: '{Error}' ({Elapsed} seconds)
Microsoft-Windows-AppReadiness  |  216       |  Admin        |  Activity for '{User}' has been suspended and will resume at {ResumeAt}.
Microsoft-Windows-AppReadiness  |  217       |  Operational  |  Activity for '{User}' has resumed.
Microsoft-Windows-AppReadiness  |  218       |  Admin        |  '{Package}' {Operation} failed for {User} and will be attempted after {AttemptAfter}.
Microsoft-Windows-AppReadiness  |  219       |  Operational  |  {NumPackages} pre-installed apps found for {SID}
Microsoft-Windows-AppReadiness  |  220       |  Admin        |  '{Task}' succeeded for {Username}. ({Elapsed} seconds)
Microsoft-Windows-AppReadiness  |  221       |  Operational  |  Task '{Task}' created for {Username}.
Microsoft-Windows-AppReadiness  |  222       |  Operational  |  '{TaskId}' was removed (Canceled: {TaskCanceled}) for '{User}' due to new opposing task of type {OpposingOperation}.
Microsoft-Windows-AppReadiness  |  223       |  Operational  |  Shutdown for '{User}' has started.
Microsoft-Windows-AppReadiness  |  224       |  Operational  |  Shutdown for '{User}' has completed.
Microsoft-Windows-AppReadiness  |  225       |  Admin        |  Canceling '{Task}' for '{Username}' due to shutdown.
Microsoft-Windows-AppReadiness  |  226       |  Operational  |  During shutdown '{User}' is waiting for tasks to complete.
Microsoft-Windows-AppReadiness  |  227       |  Admin        |  '{TaskId}' was selected as the next task for {User}. (Priority={Priority})
Microsoft-Windows-AppReadiness  |  300       |  Operational  |  Started '{TaskId}' for '{User}'
Microsoft-Windows-AppReadiness  |  301       |  Operational  |  Finished '{TaskId}' for '{User}' lasted {Duration} seconds. ({Result})
Microsoft-Windows-AppReadiness  |  302       |  Operational  |  Started group '{GroupId}' for '{User}'
Microsoft-Windows-AppReadiness  |  303       |  Operational  |  Finished group '{GroupId}' for '{User}' lasted {Duration} seconds. ({Result})
Microsoft-Windows-AppReadiness  |  304       |  Operational  |  During execution of '{GroupId}' for '{User}' task '{TaskId}' failed. (Error: {Result})
Microsoft-Windows-AppReadiness  |  305       |  Admin        |  Package '{PackageFamilyName}' was removed from '{User}' first login group. (Reason: {Reason})
Microsoft-Windows-AppReadiness  |  306       |  Operational  |  For '{User}' task '{TaskId}' was canceled.
Microsoft-Windows-AppReadiness  |  307       |  Operational  |  Finished activation of '{PackageFamilyName}' for '{User}'. (Result: {Reason})
Microsoft-Windows-AppReadiness  |  308       |  Admin        |  Preview tile creation failed '{PackageFamilyName}' for {User}. (Source: {Source}, Error: {Result})
Microsoft-Windows-AppReadiness  |  309       |  Operational  |  Starting registry flush for '{User}'.
Microsoft-Windows-AppReadiness  |  310       |  Operational  |  Finished registry flush for '{User}'.
Microsoft-Windows-AppReadiness  |  311       |  Admin        |  Failed to flush registry key '{Key}' for '{User}'. (Error: {Result})
Microsoft-Windows-AppReadiness  |  312       |  Operational  |  Successfully created {NumPackages} preview tiles for {User}. (Source: {Source})
Microsoft-Windows-AppReadiness  |  313       |  Operational  |  '{Group}' is canceling '{Task}' for '{User}' as a result of cancel.
Microsoft-Windows-AppReadiness  |  314       |  Operational  |  '{Group}' has selected '{Task}' for '{User}' for the next task.
Microsoft-Windows-AppReadiness  |  315       |  Operational  |  '{PackageFamilyName}' was removed from '{User}' first login group. (Reason: {Reason})
Microsoft-Windows-AppReadiness  |  316       |  Admin        |  Installing '{PackageFamilyName}' for '{User}' has hit the in-activity timeout
Microsoft-Windows-AppReadiness  |  317       |  Operational  |  Starting pre-registration of '{PackageId}'
Microsoft-Windows-AppReadiness  |  318       |  Operational  |  Completed pre-registration of '{PackageId}'
Microsoft-Windows-AppReadiness  |  319       |  Admin        |  Pre-registration for '{PackageId}' failed. (Error: {Result})
Microsoft-Windows-AppReadiness  |  1001      |  Debug        |
Microsoft-Windows-AppReadiness  |  1002      |  Debug        |
Microsoft-Windows-AppReadiness  |  1003      |  Debug        |
Microsoft-Windows-AppReadiness  |  1004      |  Debug        |
Microsoft-Windows-AppReadiness  |  1005      |  Debug        |
Microsoft-Windows-AppReadiness  |  1006      |  Debug        |
Microsoft-Windows-AppReadiness  |  1009      |  Debug        |
Microsoft-Windows-AppReadiness  |  1010      |  Debug        |
Microsoft-Windows-AppReadiness  |  1013      |  Debug        |
Microsoft-Windows-AppReadiness  |  1014      |  Debug        |
Microsoft-Windows-AppReadiness  |  1015      |  Debug        |
Microsoft-Windows-AppReadiness  |  1016      |  Debug        |
Microsoft-Windows-AppReadiness  |  1017      |  Debug        |
Microsoft-Windows-AppReadiness  |  1018      |  Debug        |
Microsoft-Windows-AppReadiness  |  1019      |  Debug        |
Microsoft-Windows-AppReadiness  |  1020      |  Debug        |
Microsoft-Windows-AppReadiness  |  1021      |  Admin        |  DisableInAuditMode registry value set to block API calls while in audit mode (audit mode: {IsAuditMode}).
Microsoft-Windows-AppReadiness  |  2000      |  Debug        |
Microsoft-Windows-AppReadiness  |  2001      |  Debug        |
Microsoft-Windows-AppReadiness  |  2002      |  Debug        |
Microsoft-Windows-AppReadiness  |  2003      |  Debug        |
Microsoft-Windows-AppReadiness  |  2005      |  Debug        |
Microsoft-Windows-AppReadiness  |  2006      |  Debug        |
Microsoft-Windows-AppReadiness  |  2007      |  Debug        |
Microsoft-Windows-AppReadiness  |  2008      |  Debug        |
Microsoft-Windows-AppReadiness  |  2009      |  Debug        |
Microsoft-Windows-AppReadiness  |  2500      |  Debug        |
Microsoft-Windows-AppReadiness  |  2501      |  Debug        |
Microsoft-Windows-AppReadiness  |  2502      |  Debug        |
Microsoft-Windows-AppReadiness  |  2503      |  Debug        |
Microsoft-Windows-AppReadiness  |  2504      |  Operational  |
Microsoft-Windows-AppReadiness  |  3000      |  Debug        |
Microsoft-Windows-AppReadiness  |  3001      |  Debug        |
Microsoft-Windows-AppReadiness  |  4000      |  Operational  |
Microsoft-Windows-AppReadiness  |  4001      |  Operational  |
Microsoft-Windows-AppReadiness  |  5000      |  Debug        |
Microsoft-Windows-AppReadiness  |  5001      |  Debug        |
Microsoft-Windows-AppReadiness  |  5002      |  Debug        |
Microsoft-Windows-AppReadiness  |  5003      |  Debug        |
Microsoft-Windows-AppReadiness  |  5004      |  Debug        |
Microsoft-Windows-AppReadiness  |  5005      |  Debug        |
Microsoft-Windows-AppReadiness  |  5006      |  Debug        |
Microsoft-Windows-AppReadiness  |  5007      |  Debug        |
Microsoft-Windows-AppReadiness  |  5008      |  Debug        |
Microsoft-Windows-AppReadiness  |  5009      |  Debug        |
Microsoft-Windows-AppReadiness  |  5010      |  Debug        |
Microsoft-Windows-AppReadiness  |  5011      |  Debug        |
Microsoft-Windows-AppReadiness  |  5012      |  Debug        |
Microsoft-Windows-AppReadiness  |  5013      |  Debug        |
Microsoft-Windows-AppReadiness  |  5014      |  Debug        |
Microsoft-Windows-AppReadiness  |  5015      |  Debug        |
Microsoft-Windows-AppReadiness  |  5016      |  Debug        |
Microsoft-Windows-AppReadiness  |  5017      |  Debug        |
Microsoft-Windows-AppReadiness  |  5018      |  Debug        |
Microsoft-Windows-AppReadiness  |  5019      |  Debug        |
Microsoft-Windows-AppReadiness  |  5020      |  Debug        |
Microsoft-Windows-AppReadiness  |  5021      |  Debug        |
Microsoft-Windows-AppReadiness  |  5022      |  Debug        |
Microsoft-Windows-AppReadiness  |  5023      |  Debug        |
Microsoft-Windows-AppReadiness  |  5024      |  Debug        |
Microsoft-Windows-AppReadiness  |  5025      |  Debug        |
Microsoft-Windows-AppReadiness  |  5026      |  Debug        |
Microsoft-Windows-AppReadiness  |  5027      |  Debug        |
Microsoft-Windows-AppReadiness  |  5028      |  Debug        |
Microsoft-Windows-AppReadiness  |  5029      |  Debug        |
Microsoft-Windows-AppReadiness  |  5030      |  Debug        |
Microsoft-Windows-AppReadiness  |  5031      |  Debug        |
Microsoft-Windows-AppReadiness  |  5032      |  Debug        |
Microsoft-Windows-AppReadiness  |  5033      |  Debug        |
Microsoft-Windows-AppReadiness  |  5034      |  Debug        |
Microsoft-Windows-AppReadiness  |  5035      |  Debug        |
Microsoft-Windows-AppReadiness  |  5036      |  Debug        |
Microsoft-Windows-AppReadiness  |  5037      |  Debug        |