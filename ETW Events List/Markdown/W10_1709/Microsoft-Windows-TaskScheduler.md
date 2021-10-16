Provider                         |  Event ID  |  Channel      |  Message
---------------------------------|------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-TaskScheduler  |  100       |  Operational  |  Task Scheduler started "{InstanceId}" instance of the "{TaskName}" task for user "{UserContext}".
Microsoft-Windows-TaskScheduler  |  101       |  Operational  |  Task Scheduler failed to start "{TaskName}" task for user "{UserContext}". Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  102       |  Operational  |  Task Scheduler successfully finished "{InstanceId}" instance of the "{TaskName}" task for user "{UserContext}".
Microsoft-Windows-TaskScheduler  |  103       |  Operational  |  Task Scheduler failed to start instance "{InstanceId}" of "{TaskName}"  task for user "{UserContext}" . Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  104       |  Operational  |  Task Scheduler failed to log on "{UserName}" . Failure occurred in "{ErrorDescription}" . User Action: Ensure the credentials for the task are correctly specified. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  105       |  Operational  |  Task Scheduler failed to impersonate "{Context}" . Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  106       |  Operational  |  User "{UserContext}"  registered Task Scheduler task "{TaskName}"
Microsoft-Windows-TaskScheduler  |  107       |  Operational  |  Task Scheduler launched "{InstanceId}"  instance of task "{TaskName}" due to a time trigger condition.
Microsoft-Windows-TaskScheduler  |  108       |  Operational  |  Task Scheduler launched "{InstanceId}"  instance of task "{TaskName}"  according to an event trigger.
Microsoft-Windows-TaskScheduler  |  109       |  Operational  |  Task Scheduler launched "{InstanceId}"  instance of task "{TaskName}"  according to a registration trigger.
Microsoft-Windows-TaskScheduler  |  110       |  Operational  |  Task Scheduler launched "{InstanceId}"  instance of task "{TaskName}"  for user "{UserContext}" .
Microsoft-Windows-TaskScheduler  |  111       |  Operational  |  Task Scheduler terminated "{InstanceId}"  instance of the "{TaskName}"  task.
Microsoft-Windows-TaskScheduler  |  112       |  Operational  |  Task Scheduler could not start task "{TaskName}"  because the network was unavailable. User Action: Ensure the computer is connected to the required network as specified in the task. If the task does not require network presence, remove the network condition from the task configuration.
Microsoft-Windows-TaskScheduler  |  113       |  Operational  |  Task registered task "{TaskName}" , but not all specified triggers will start the task. User Action: Ensure all the task triggers are valid as configured. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  114       |  Operational  |  Task Scheduler could not launch task "{TaskName}"  as scheduled. Instance "{InstanceId}"  is started now as required by the configuration option to start the task when available, if schedule is missed.
Microsoft-Windows-TaskScheduler  |  115       |  Operational  |  Task Scheduler failed to roll back a transaction when updating or deleting a task. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  116       |  Operational  |  Task Scheduler validated the configuration for task "{TaskName}" , but credentials could not be stored. User Action: Re-register the task ensuring the credentials are valid. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  117       |  Operational  |  Task Scheduler launched "{InstanceId}"  instance of task "{TaskName}"  due to an idle condition.
Microsoft-Windows-TaskScheduler  |  118       |  Operational  |  Task Scheduler launched "{InstanceId}"  instance of task "{TaskName}"  due to system startup.
Microsoft-Windows-TaskScheduler  |  119       |  Operational  |  Task Scheduler launched "{InstanceId}"  instance of task "{TaskName}" due to user "{UserName}"  logon.
Microsoft-Windows-TaskScheduler  |  120       |  Operational  |  Task Scheduler launched "{InstanceId}"  instance of task "{TaskName}"  due to user "{UserName}"  connecting to the console trigger.
Microsoft-Windows-TaskScheduler  |  121       |  Operational  |  Task Scheduler launched "{InstanceId}"  instance of task "{TaskName}"  due to user "{UserName}"  disconnecting from the console trigger.
Microsoft-Windows-TaskScheduler  |  122       |  Operational  |  Task Scheduler launched "{InstanceId}"  instance of task "{TaskName}"  due to user "{UserName}"  remotely connecting trigger.
Microsoft-Windows-TaskScheduler  |  123       |  Operational  |  Task Scheduler launched "{InstanceId}"  instance of task "{TaskName}"  due to user "{UserName}"  remotely disconnecting trigger.
Microsoft-Windows-TaskScheduler  |  124       |  Operational  |  Task Scheduler launched "{InstanceId}"  instance of task "{TaskName}"  due to user "{UserName}"  locking the computer trigger.
Microsoft-Windows-TaskScheduler  |  125       |  Operational  |  Task Scheduler launched "{InstanceId}"  instance of task "{TaskName}"  due to user "{UserName}"  unlocking the computer trigger.
Microsoft-Windows-TaskScheduler  |  126       |  Operational  |  Task Scheduler failed to execute task "{TaskName}" . Attempting to restart. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  127       |  Operational  |  Task Scheduler failed to execute task "{TaskName}"  due to a shutdown race condition. Attempting to restart.
Microsoft-Windows-TaskScheduler  |  128       |  Operational  |  Task Scheduler did not launch task "{TaskName}" , because current time exceeds the configured task end time. User Action: Extend the end time boundary for the task if required.
Microsoft-Windows-TaskScheduler  |  129       |  Operational  |  Task Scheduler launch task "{TaskName}" , instance "{Path}"  with process ID {ProcessID}.
Microsoft-Windows-TaskScheduler  |  130       |  Operational  |  Task Scheduler failed to start task "{TaskName}" due to the service being busy.
Microsoft-Windows-TaskScheduler  |  131       |  Operational  |  Task Scheduler failed to start task "{TaskName}" because the number of tasks in the task queue exceeding the quota currently configured to {CurrentQuota}. User Action: Reduce the number of running tasks or increase the configured queue quota.
Microsoft-Windows-TaskScheduler  |  132       |  Operational  |  Task Scheduler task launching queue quota is approaching its preset limit of tasks currently configured to {CurrentQuota}. User Action: Reduce the number of running tasks or increase the configured queue quota.
Microsoft-Windows-TaskScheduler  |  133       |  Operational  |  Task Scheduler failed to start task {TaskName}" in TaskEngine "{TaskEngineName}"  for user "{UserName}". User Action: Reduce the number of tasks running in the specified user context.
Microsoft-Windows-TaskScheduler  |  134       |  Operational  |  Task Engine "{TaskEngineName}"  for user "{UserName}" is approaching its preset limit of tasks. User Action: Reduce the number of tasks running in the specified user context.
Microsoft-Windows-TaskScheduler  |  135       |  Operational  |  Task Scheduler could not start task "{TaskName}"  because the machine was not idle.
Microsoft-Windows-TaskScheduler  |  140       |  Operational  |  User "{UserName}"  updated Task Scheduler task "{TaskName}"
Microsoft-Windows-TaskScheduler  |  141       |  Operational  |  User "{UserName}"  deleted Task Scheduler task "{TaskName}"
Microsoft-Windows-TaskScheduler  |  142       |  Operational  |  User "{UserName}"  disabled Task Scheduler task "{TaskName}"
Microsoft-Windows-TaskScheduler  |  145       |  Operational  |  Task Scheduler woke up the computer to run a task.
Microsoft-Windows-TaskScheduler  |  146       |  Operational  |  Task Scheduler failed to load task "{TaskName}" at service startup. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  147       |  Operational  |  Task Scheduler recovered sucessfully the image of task "{TaskName}" after a corruption occured during OS upgrade.
Microsoft-Windows-TaskScheduler  |  148       |  Operational  |  Task Scheduler failed to recover the image of task "{TaskName}" after a corruption occured during OS upgrade. Additional Data: Error Value: 0x{ResultCode}.
Microsoft-Windows-TaskScheduler  |  149       |  Operational  |  Task "{TaskName}" is using a combination of properties that is incompatible with the scheduling engine.
Microsoft-Windows-TaskScheduler  |  150       |  Operational  |  Task Scheduler failed to subscribe for the event trigger for task "{TaskName}". Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  151       |  Operational  |  Task instantiation failed "{TaskName}". Check point: {LogPoint}. Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  152       |  Operational  |  Task "{TaskName}" was re-directed to legacy scheduling engine.
Microsoft-Windows-TaskScheduler  |  153       |  Operational  |  Task Scheduler did not launch task "{TaskName}" as it missed its schedule. Consider using the configuration option to start the task when available, if schedule is missed.
Microsoft-Windows-TaskScheduler  |  155       |  Operational  |  Task Scheduler is currently waiting on completion of task "{TaskPath}".
Microsoft-Windows-TaskScheduler  |  200       |  Operational  |  Task Scheduler launched action "{ActionName}" in instance "{TaskInstanceId}" of task "{TaskName}".
Microsoft-Windows-TaskScheduler  |  200       |  Operational  |  Task Scheduler launched action "{ActionName}" in instance "{TaskInstanceId}" of task "{TaskName}".
Microsoft-Windows-TaskScheduler  |  201       |  Operational  |  Task Scheduler successfully completed task "{TaskName}" , instance "{TaskInstanceId}" , action "{ActionName}" .
Microsoft-Windows-TaskScheduler  |  201       |  Operational  |  Task Scheduler successfully completed task "{TaskName}" , instance "{TaskInstanceId}" , action "{ActionName}" with return code {ResultCode}.
Microsoft-Windows-TaskScheduler  |  201       |  Operational  |  Task Scheduler successfully completed task "{TaskName}" , instance "{TaskInstanceId}" , action "{ActionName}" with return code {ResultCode}.
Microsoft-Windows-TaskScheduler  |  202       |  Operational  |  Task Scheduler failed to complete task "{TaskName}" , instance "{TaskInstanceId}" , action "{ActionName}" . Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  202       |  Operational  |  Task Scheduler failed to complete task "{TaskName}" , instance "{TaskInstanceId}" , action "{ActionName}" . Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  203       |  Operational  |  Task Scheduler failed to launch action "{ActionName}" in instance "{TaskInstanceId}" of task "{TaskName}". Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  204       |  Operational  |  Task Scheduler failed to retrieve the event triggering values for task "{TaskName}" . The event will be ignored. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  205       |  Operational  |  Task Scheduler failed to match the pattern of events for task "{TaskName}" . The events will be ignored. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  300       |  Operational  |  Task Scheduler started Task Engine "{TaskEngineName}"  with process ID {ProcessID}.
Microsoft-Windows-TaskScheduler  |  301       |  Operational  |  Task Scheduler is shutting down Task Engine "{TaskEngineName}"
Microsoft-Windows-TaskScheduler  |  303       |  Operational  |  Task Scheduler is shutting down Task Engine "{TaskEngineName}"  due to an error in "{ErrorDescription}" .  Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  304       |  Operational  |  Task Scheduler sent "{TaskName}"  task to Task Engine "{TaskEngineName}" . The task instance Id is "{TaskInstanceId}" .
Microsoft-Windows-TaskScheduler  |  305       |  Operational  |  Task Scheduler did not send "{TaskName}"  task to Task Engine "{TaskEngineName}" . Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  306       |  Operational  |  For Task Scheduler Task Engine "{TaskEngineName}" , the thread pool failed to process the message. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  307       |  Operational  |  Task Scheduler service failed to connect to the Task Engine "{TaskEngineName}"  process. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  308       |  Operational  |  Task Scheduler connected to the Task Engine "{TaskEngineName}"  process.
Microsoft-Windows-TaskScheduler  |  309       |  Operational  |  Task Scheduler {TaskCount} tasks orphaned during Task Engine "{TaskEngineName}"  shutdown. User Action: Find the process run by this task in the Task Manager and kill it manually.
Microsoft-Windows-TaskScheduler  |  310       |  Operational  |  Task Scheduler started Task Engine "{TaskEngineName}"  process. Command="{Command}" , ProcessID={ProcessID}, ThreadID={ThreadID}
Microsoft-Windows-TaskScheduler  |  311       |  Operational  |  Task Scheduler failed to start Task Engine "{TaskEngineName}"  process due to an error occurring in "{ErrorDescription}" . Command="{Command}" . Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  312       |  Operational  |  Task Scheduler created the Win32 job object for Task Engine "{TaskEngineName}" .
Microsoft-Windows-TaskScheduler  |  313       |  Operational  |  Task Scheduler channel with Task Engine "{TaskEngineName}"  is ready to send and receive messages.
Microsoft-Windows-TaskScheduler  |  314       |  Operational  |  Task Scheduler has no tasks running for Task Engine "{TaskEngineName}" , and the idle timer has started.
Microsoft-Windows-TaskScheduler  |  315       |  Operational  |  Task Engine "{TaskEngineName}"  process failed to connect to the Task Scheduler service. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  316       |  Operational  |  Task Engine "{TaskEngineName}"  failed to send a message to the Task Scheduler service. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  317       |  Operational  |  Task Scheduler started Task Engine "{TaskEngineName}"  process.
Microsoft-Windows-TaskScheduler  |  318       |  Operational  |  Task Scheduler shutdown Task Engine "{TaskEngineName}"  process.
Microsoft-Windows-TaskScheduler  |  319       |  Operational  |  Task Engine "{TaskEngineName}"  received a message from Task Scheduler service requesting to launch task "{TaskName}" .
Microsoft-Windows-TaskScheduler  |  320       |  Operational  |  Task Engine "{TaskEngineName}"  received a message from Task Scheduler service requesting to stop task instance "{TaskInstanceId}" .
Microsoft-Windows-TaskScheduler  |  322       |  Operational  |  Task Scheduler did not launch task "{TaskName}"  because instance "{TaskInstanceId}"  of the same task is already running.
Microsoft-Windows-TaskScheduler  |  323       |  Operational  |  Task Scheduler stopped instance "{StoppedTaskInstanceId}"  of task "{TaskName}"  in order to launch new instance "{NewTaskInstanceId}" .
Microsoft-Windows-TaskScheduler  |  324       |  Operational  |  Task Scheduler queued instance "{QueuedTaskInstanceId}"  of task "{TaskName}"  and will launch it as soon as instance "{RunningTaskInstanceId}"  completes.
Microsoft-Windows-TaskScheduler  |  325       |  Operational  |  Task Scheduler queued instance "{QueuedTaskInstanceId}"  of task "{TaskName}".
Microsoft-Windows-TaskScheduler  |  326       |  Operational  |  Task Scheduler did not launch task "{TaskName}"  because computer is running on batteries. User Action: If launching the task on batteries is required, change the respective flag in the task configuration.
Microsoft-Windows-TaskScheduler  |  327       |  Operational  |  Task Scheduler stopped instance "{TaskInstanceId}"  of task "{TaskName}"  because the computer is switching to battery power.
Microsoft-Windows-TaskScheduler  |  328       |  Operational  |  Task Scheduler stopped instance "{TaskInstanceId}"  of task "{TaskName}"  because computer is no longer idle.
Microsoft-Windows-TaskScheduler  |  329       |  Operational  |  Task Scheduler terminated "{TaskInstanceId}"  instance of the "{TaskName}"  task due to exceeding the time allocated for execution, as configured in the task definition. User Action: Increase the configured task timeout or investigate external reasons for the delay.
Microsoft-Windows-TaskScheduler  |  330       |  Operational  |  Task Scheduler stopped instance "{TaskInstanceId}"  of task "{TaskName}"  as request by user "{UserContext}" .
Microsoft-Windows-TaskScheduler  |  331       |  Operational  |  Task Scheduler will continue to execute Instance "{TaskInstanceId}"  of task "{TaskName}"  even after the designated timeout, due to a failure to create the timeout mechanism. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  332       |  Operational  |  Task Scheduler did not launch task "{TaskName}"  because user "{UserName}" was not logged on when the launching conditions were met. User Action: Ensure user is logged on or change the task definition to allow launching when user is logged off.
Microsoft-Windows-TaskScheduler  |  333       |  Operational  |  Task Scheduler did not launch task "{TaskName}"  because target session is RemoteApp session. User Action: If launching the task on RemoteApp sessions is required, change the respective flag in the task configuration.
Microsoft-Windows-TaskScheduler  |  334       |  Operational  |  Task Scheduler did not launch task "{TaskName}"  because target session is a WORKER session.
Microsoft-Windows-TaskScheduler  |  400       |  Operational  |  Task Scheduler service has started.
Microsoft-Windows-TaskScheduler  |  401       |  System       |  Task Scheduler service failed to start due to an error in "{ErrorDescription}" . Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  402       |  Operational  |  Task Scheduler service is shutting down.
Microsoft-Windows-TaskScheduler  |  403       |  Operational  |  Task Scheduler service has encountered an error in "{ErrorDescription}" . Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  404       |  System       |  Task Scheduler service has encountered RPC initialization error in "{ErrorDescription}". Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  405       |  System       |  Task Scheduler service has failed to initialize COM. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  406       |  System       |  Task Scheduler service failed to initialize credentials store. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  407       |  System       |  Task Scheduler service failed to initialize LSA. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  408       |  System       |  Task Scheduler service failed to initialize idle state detection module. Idle tasks may not be started as required. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  409       |  System       |  Task Scheduler service failed to initialize time change notification. System time updates may not be picked by the service and task schedules may not be updated. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  410       |  Operational  |  Task Scheduler service failed to set a wakeup timer. As a result, some scheduled tasks may not run while the system is suspended. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  411       |  Operational  |  Task Scheduler service received a time system change notification.
Microsoft-Windows-TaskScheduler  |  412       |  System       |  Task Scheduler service failed to launch tasks triggered by computer startup. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  413       |  System       |  Task Scheduler service failed to load tasks at service startup. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  414       |  System       |  Task Scheduler service found a misconfiguration in the {TaskName} definition. Additional Data: Error Value: {Parameter}.
Microsoft-Windows-TaskScheduler  |  500       |  Diagnostic   |  Process ID {ProcessId} has registered idle task ID {IdleTaskId}.
Microsoft-Windows-TaskScheduler  |  501       |  Diagnostic   |  Process ID {ProcessId} has completed idle task ID {IdleTaskId}.
Microsoft-Windows-TaskScheduler  |  502       |  Diagnostic   |  Execution of idle task ID {IdleTaskId} has started.
Microsoft-Windows-TaskScheduler  |  503       |  Diagnostic   |  Execution of idle task ID {IdleTaskId} has ended.
Microsoft-Windows-TaskScheduler  |  504       |  Diagnostic   |  Idle task ID {IdleTaskId} has been notified that explicit processing has been requested.
Microsoft-Windows-TaskScheduler  |  505       |  Diagnostic   |  Idle task ID {IdleTaskId} has returned from its explicit processing notification.
Microsoft-Windows-TaskScheduler  |  506       |  Diagnostic   |
Microsoft-Windows-TaskScheduler  |  507       |  Diagnostic   |
Microsoft-Windows-TaskScheduler  |  508       |  Diagnostic   |
Microsoft-Windows-TaskScheduler  |  509       |  Diagnostic   |  Idle Task Power Notification Received: {NotificationType} ({State})
Microsoft-Windows-TaskScheduler  |  510       |  Diagnostic   |
Microsoft-Windows-TaskScheduler  |  511       |  Diagnostic   |
Microsoft-Windows-TaskScheduler  |  512       |  Diagnostic   |  Idle check point: State {DetectionResult}, Reason {Reason}.
Microsoft-Windows-TaskScheduler  |  700       |  Operational  |  Task Scheduler service started Task Compatibility module.
Microsoft-Windows-TaskScheduler  |  701       |  System       |  Task Scheduler service failed to start Task Compatibility module. Tasks may not be able to register on previous Window versions. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  702       |  System       |  Task Scheduler failed to initialize the RPC server for starting the Task Compatibility module. Tasks may not be able to register on previous Window versions. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  703       |  System       |  Task Scheduler failed to initialize Net Schedule API for starting the Task Compatibility module. Tasks may not be able to register on previous Window versions. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  704       |  System       |  Task Scheduler failed to initialize LSA for starting the Task Compatibility module. Tasks may not be able to register on previous Window versions. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  705       |  System       |  Task Scheduler failed to start directory monitoring for the Task Compatibility module. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  706       |  Operational  |  Task Compatibility module failed to update task "{TaskName}"  to the required status {TaskStatus}. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  707       |  Operational  |  Task Compatibility module failed to delete task "{TaskName}" . Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  708       |  Operational  |  Task Compatibility module failed to set security descriptor "{SecurityDescriptor}"  for task "{TaskName}" . Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  709       |  Operational  |  Task Compatibility module failed to update task "{TaskName}" . Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  710       |  Operational  |  Task Compatibility module failed to upgrade existing tasks. Upgrade will be attempted again next time 'Task Scheduler' service starts. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  711       |  Operational  |  Task Compatibility module failed to upgrade NetSchedule account "{Account}" . Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  712       |  Operational  |  Task Compatibility module failed to read  existing store to upgrade tasks. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  713       |  Operational  |  Task Compatibility module failed to load task  "{TaskName}" for upgrade. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  714       |  Operational  |  Task Compatibility module failed to register  task  "{TaskName}" for upgrade. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  715       |  Operational  |  Task Compatibility module failed to delete  LSA store for upgrade. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  716       |  System       |  Task Compatibility module failed to upgrade existing scheduled tasks. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  717       |  Operational  |  Task Compatibility module failed to determine if upgrade is needed. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  718       |  System       |  Task scheduler was unable to upgrade the credential store from the Beta 2 version.  You may need to re-register any tasks that require passwords. Additional Data: Error Value: {ResultCode}.
Microsoft-Windows-TaskScheduler  |  719       |  System       |  To help optimize for performance, Task Scheduler has automatically disabled logging. To re-enable logging, please use Event Viewer.
Microsoft-Windows-TaskScheduler  |  800       |  Maintenance  |  Maintenance state changed to {hc_stateid} (Last Run: {LastRunDateTime}).
Microsoft-Windows-TaskScheduler  |  801       |  Maintenance  |  Maintenance launch operation failed. Additional error info: {ErrorCode}.
Microsoft-Windows-TaskScheduler  |  802       |  Maintenance  |  Maintenance re-configuration failed. Additional error info: {ErrorCode}.
Microsoft-Windows-TaskScheduler  |  803       |  Maintenance  |  Maintenance Scheduler engine task "{Task}" cannot be accessed. Additional error info: {ErrorCode}.
Microsoft-Windows-TaskScheduler  |  804       |  Maintenance  |  Maintenance Scheduler has detected cyclic dependency for the following maintenance tasks: {Task}.
Microsoft-Windows-TaskScheduler  |  805       |  Maintenance  |  Maintenance Task "{Task}" is behind deadline.
Microsoft-Windows-TaskScheduler  |  806       |  Maintenance  |  Maintenance task "{Task}" processing error. Additional error info {InfoCode}.
Microsoft-Windows-TaskScheduler  |  807       |  Maintenance  |  Maintenance complete (launch type {LauncherId}).
Microsoft-Windows-TaskScheduler  |  808       |  Maintenance  |  Maintenance Task "{Task}" requests computer wakeup during next regular maintenance run.
Microsoft-Windows-TaskScheduler  |  998       |  Debug        |  DEBUG! ({File}:{Line}) "{Name}" failed. ({HRESULT}).
Microsoft-Windows-TaskScheduler  |  999       |  Debug        |  DEBUG! "{String}".