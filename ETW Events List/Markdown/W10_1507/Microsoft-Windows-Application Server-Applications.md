Provider                                           |  Event ID  |  Channel      |  Message
---------------------------------------------------|------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-Application Server-Applications  |  100       |  Analytic     |  TrackRecord= WorkflowInstanceRecord, InstanceID = {InstanceId}, RecordNumber = {RecordNumber}, EventTime = {EventTime}, ActivityDefinitionId = {ActivityDefinitionId}, State = {State}, Annotations = {Annotations}, ProfileName = {ProfileName}
Microsoft-Windows-Application Server-Applications  |  101       |  Analytic     |  TrackRecord = WorkflowInstanceUnhandledExceptionRecord, InstanceID = {InstanceId}, RecordNumber = {RecordNumber}, EventTime = {EventTime}, ActivityDefinitionId = {ActivityDefinitionId}, SourceName = {SourceName}, SourceId = {SourceId}, SourceInstanceId = {SourceInstanceId}, SourceTypeName={SourceTypeName}, Exception={Exception}, Annotations= {InstanceId}0, ProfileName = {InstanceId}1
Microsoft-Windows-Application Server-Applications  |  102       |  Analytic     |  TrackRecord = WorkflowInstanceAbortedRecord, InstanceID = {InstanceId}, RecordNumber = {RecordNumber}, EventTime = {EventTime}, ActivityDefinitionId = {ActivityDefinitionId}, Reason = {Reason}, Annotations = {Annotations}, ProfileName = {ProfileName}
Microsoft-Windows-Application Server-Applications  |  103       |  Analytic     |  TrackRecord = ActivityStateRecord, InstanceID = {InstanceId}, RecordNumber={RecordNumber}, EventTime={EventTime}, State = {State}, Name={Name}, ActivityId={ActivityId}, ActivityInstanceId={ActivityInstanceId}, ActivityTypeName={ActivityTypeName}, Arguments={Arguments}, Variables={InstanceId}0, Annotations={InstanceId}1, ProfileName = {InstanceId}2
Microsoft-Windows-Application Server-Applications  |  104       |  Analytic     |  TrackRecord = ActivityScheduledRecord, InstanceID = {InstanceId},  RecordNumber = {RecordNumber}, EventTime = {EventTime}, Name = {Name}, ActivityId = {ActivityId}, ActivityInstanceId = {ActivityInstanceId}, ActivityTypeName = {ActivityTypeName}, ChildActivityName = {ChildActivityName}, ChildActivityId = {ChildActivityId}, ChildActivityInstanceId = {InstanceId}0, ChildActivityTypeName ={InstanceId}1, Annotations={InstanceId}2, ProfileName = {InstanceId}3
Microsoft-Windows-Application Server-Applications  |  105       |  Analytic     |  TrackRecord = FaultPropagationRecord, InstanceID={InstanceId}, RecordNumber={RecordNumber}, EventTime={EventTime}, FaultSourceActivityName={FaultSourceActivityName}, FaultSourceActivityId={FaultSourceActivityId}, FaultSourceActivityInstanceId={FaultSourceActivityInstanceId}, FaultSourceActivityTypeName={FaultSourceActivityTypeName}, FaultHandlerActivityName={FaultHandlerActivityName},  FaultHandlerActivityId = {FaultHandlerActivityId}, FaultHandlerActivityInstanceId ={InstanceId}0, FaultHandlerActivityTypeName={InstanceId}1, Fault={InstanceId}2, IsFaultSource={InstanceId}3, Annotations={InstanceId}4, ProfileName = {InstanceId}5
Microsoft-Windows-Application Server-Applications  |  106       |  Analytic     |  TrackRecord = CancelRequestedRecord, InstanceID={InstanceId}, RecordNumber={RecordNumber}, EventTime={EventTime}, Name={Name}, ActivityId={ActivityId}, ActivityInstanceId={ActivityInstanceId}, ActivityTypeName = {ActivityTypeName}, ChildActivityName = {ChildActivityName}, ChildActivityId = {ChildActivityId}, ChildActivityInstanceId = {InstanceId}0, ChildActivityTypeName ={InstanceId}1, Annotations={InstanceId}2, ProfileName = {InstanceId}3
Microsoft-Windows-Application Server-Applications  |  107       |  Analytic     |  TrackRecord = BookmarkResumptionRecord, InstanceID={InstanceId}, RecordNumber={RecordNumber},EventTime={EventTime}, Name={Name}, SubInstanceID={SubInstanceID},  OwnerActivityName={OwnerActivityName}, OwnerActivityId ={OwnerActivityId}, OwnerActivityInstanceId={OwnerActivityInstanceId}, OwnerActivityTypeName={OwnerActivityTypeName}, Annotations={InstanceId}0, ProfileName = {InstanceId}1
Microsoft-Windows-Application Server-Applications  |  108       |  Analytic     |  TrackRecord = CustomTrackingRecord, InstanceID = {InstanceId}, RecordNumber={RecordNumber}, EventTime={EventTime},  Name={Name}, ActivityName={ActivityName}, ActivityId={ActivityId}, ActivityInstanceId={ActivityInstanceId}, ActivityTypeName={ActivityTypeName}, Data={Data}, Annotations={InstanceId}0, ProfileName = {InstanceId}1
Microsoft-Windows-Application Server-Applications  |  110       |  Analytic     |  TrackRecord = CustomTrackingRecord, InstanceID = {InstanceId}, RecordNumber={RecordNumber}, EventTime={EventTime}, Name={Name}, ActivityName={ActivityName}, ActivityId={ActivityId}, ActivityInstanceId={ActivityInstanceId}, ActivityTypeName={ActivityTypeName}, Data={Data}, Annotations={InstanceId}0, ProfileName = {InstanceId}1
Microsoft-Windows-Application Server-Applications  |  111       |  Analytic     |  TrackRecord = CustomTrackingRecord, InstanceID = {InstanceId}, RecordNumber={RecordNumber}, EventTime={EventTime}, Name={Name}, ActivityName={ActivityName}, ActivityId={ActivityId}, ActivityInstanceId={ActivityInstanceId}, ActivityTypeName={ActivityTypeName}, Data={Data}, Annotations={InstanceId}0, ProfileName = {InstanceId}1
Microsoft-Windows-Application Server-Applications  |  112       |  Analytic     |  TrackRecord = WorkflowInstanceSuspendedRecord, InstanceID = {InstanceId}, RecordNumber = {RecordNumber}, EventTime = {EventTime}, ActivityDefinitionId = {ActivityDefinitionId}, Reason = {Reason}, Annotations = {Annotations}, ProfileName = {ProfileName}
Microsoft-Windows-Application Server-Applications  |  113       |  Analytic     |  TrackRecord = WorkflowInstanceTerminatedRecord, InstanceID = {InstanceId}, RecordNumber = {RecordNumber}, EventTime = {EventTime}, ActivityDefinitionId = {ActivityDefinitionId}, Reason = {Reason}, Annotations = {Annotations}, ProfileName = {ProfileName}
Microsoft-Windows-Application Server-Applications  |  114       |  Analytic     |  TrackRecord= WorkflowInstanceRecord, InstanceID = {InstanceId}, RecordNumber = {RecordNumber}, EventTime = {EventTime}, ActivityDefinitionId = {ActivityDefinitionId}, State = {State}, Annotations = {Annotations}, ProfileName = {ProfileName}, WorkflowDefinitionIdentity = {WorkflowDefinitionIdentity}
Microsoft-Windows-Application Server-Applications  |  115       |  Analytic     |  TrackRecord = WorkflowInstanceAbortedRecord, InstanceID = {InstanceId}, RecordNumber = {RecordNumber}, EventTime = {EventTime}, ActivityDefinitionId = {ActivityDefinitionId}, Reason = {Reason},  Annotations = {Annotations}, ProfileName = {ProfileName}, WorkflowDefinitionIdentity = {WorkflowDefinitionIdentity}
Microsoft-Windows-Application Server-Applications  |  116       |  Analytic     |  TrackRecord = WorkflowInstanceSuspendedRecord, InstanceID = {InstanceId}, RecordNumber = {RecordNumber}, EventTime = {EventTime}, ActivityDefinitionId = {ActivityDefinitionId}, Reason = {Reason}, Annotations = {Annotations}, ProfileName = {ProfileName}, WorkflowDefinitionIdentity = {WorkflowDefinitionIdentity}
Microsoft-Windows-Application Server-Applications  |  117       |  Analytic     |  TrackRecord = WorkflowInstanceTerminatedRecord, InstanceID = {InstanceId}, RecordNumber = {RecordNumber}, EventTime = {EventTime}, ActivityDefinitionId = {ActivityDefinitionId}, Reason = {Reason},  Annotations = {Annotations}, ProfileName = {ProfileName}, WorkflowDefinitionIdentity = {WorkflowDefinitionIdentity}
Microsoft-Windows-Application Server-Applications  |  118       |  Analytic     |  TrackRecord = WorkflowInstanceUnhandledExceptionRecord, InstanceID = {InstanceId}, RecordNumber = {RecordNumber}, EventTime = {EventTime}, ActivityDefinitionId = {ActivityDefinitionId}, SourceName = {SourceName}, SourceId = {SourceId}, SourceInstanceId = {SourceInstanceId}, SourceTypeName={SourceTypeName}, Exception={Exception},  Annotations= {InstanceId}0, ProfileName = {InstanceId}1, WorkflowDefinitionIdentity = {InstanceId}2
Microsoft-Windows-Application Server-Applications  |  119       |  Analytic     |  TrackRecord= WorkflowInstanceUpdatedRecord, InstanceID = {InstanceId}, RecordNumber = {RecordNumber}, EventTime = {EventTime}, ActivityDefinitionId = {ActivityDefinitionId}, State = {State}, OriginalDefinitionIdentity = {OriginalDefinitionIdentity}, UpdatedDefinitionIdentity = {UpdatedDefinitionIdentity}, Annotations = {Annotations}, ProfileName = {ProfileName}
Microsoft-Windows-Application Server-Applications  |  131       |  Debug        |  Pool allocating {Size} Bytes.
Microsoft-Windows-Application Server-Applications  |  132       |  Debug        |  BufferPool of size {PoolSize}, changing quota by {Delta}.
Microsoft-Windows-Application Server-Applications  |  133       |  Debug        |  IO Thread scheduler callback invoked.
Microsoft-Windows-Application Server-Applications  |  134       |  Debug        |  IO Thread scheduler callback invoked.
Microsoft-Windows-Application Server-Applications  |  201       |  Debug        |  The Dispatcher invoked 'AfterReceiveReply' on a ClientMessageInspector of type '{TypeName}'.
Microsoft-Windows-Application Server-Applications  |  202       |  Analytic     |  The Dispatcher invoked 'BeforeSendRequest' on a ClientMessageInspector of type  '{TypeName}'.
Microsoft-Windows-Application Server-Applications  |  203       |  Analytic     |  The Dispatcher invoked 'AfterCall' on a ClientParameterInspector of type '{TypeName}'.
Microsoft-Windows-Application Server-Applications  |  204       |  Analytic     |  The Dispatcher invoked 'BeforeCall' on a ClientParameterInspector of type '{TypeName}'.
Microsoft-Windows-Application Server-Applications  |  205       |  Analytic     |  An OperationInvoker invoked the '{MethodName}' method. Caller information: '{CallerInfo}'.
Microsoft-Windows-Application Server-Applications  |  206       |  Analytic     |  The Dispatcher invoked an ErrorHandler of type  '{TypeName}' with an exception of type '{ExceptionTypeName}'.  ErrorHandled == '{Handled}'.
Microsoft-Windows-Application Server-Applications  |  207       |  Analytic     |  The Dispatcher invoked a FaultProvider of type '{TypeName}' with an exception of type '{ExceptionTypeName}'.
Microsoft-Windows-Application Server-Applications  |  208       |  Analytic     |  The Dispatcher invoked 'AfterReceiveReply' on a MessageInspector of type '{TypeName}'.
Microsoft-Windows-Application Server-Applications  |  209       |  Analytic     |  The Dispatcher invoked 'BeforeSendRequest' on a MessageInspector of type '{TypeName}'.
Microsoft-Windows-Application Server-Applications  |  210       |  Analytic     |  The '{ThrottleName}' throttle limit of '{Limit}' was hit.
Microsoft-Windows-Application Server-Applications  |  211       |  Analytic     |  The Dispatcher invoked 'AfterCall' on a ParameterInspector of type '{TypeName}'.
Microsoft-Windows-Application Server-Applications  |  212       |  Analytic     |  The Dispatcher invoked 'BeforeCall' on a ParameterInspector of type '{TypeName}'.
Microsoft-Windows-Application Server-Applications  |  213       |  Analytic     |  ServiceHost started: '{ServiceTypeName}'.
Microsoft-Windows-Application Server-Applications  |  214       |  Analytic     |  An OperationInvoker completed the call to the '{MethodName}' method.  The method call duration was '{Duration}' ms.
Microsoft-Windows-Application Server-Applications  |  215       |  Analytic     |  The transport received a message from '{ListenAddress}'.
Microsoft-Windows-Application Server-Applications  |  216       |  Analytic     |  The transport sent a message to '{DestinationAddress}'.
Microsoft-Windows-Application Server-Applications  |  217       |  Debug        |  The Client is executing Action '{Action}' associated with the '{ContractName}' contract. The message will be sent to '{Destination}'.
Microsoft-Windows-Application Server-Applications  |  218       |  Analytic     |  The Client completed executing Action '{Action}' associated with the '{ContractName}' contract. The message was sent to '{Destination}'.
Microsoft-Windows-Application Server-Applications  |  219       |  Analytic     |  There was an unhandled exception of type '{ExceptionTypeName}' during message processing.  Full Exception Details: {ExceptionToString}.
Microsoft-Windows-Application Server-Applications  |  220       |  Analytic     |  The Dispatcher sent a message to the transport. Correlation ID == '{CorrelationId}'.
Microsoft-Windows-Application Server-Applications  |  221       |  Analytic     |  The Dispatcher received a message from the transport. Correlation ID == '{CorrelationId}'.
Microsoft-Windows-Application Server-Applications  |  222       |  Analytic     |  The '{MethodName}' method threw an unhandled exception when invoked by the OperationInvoker. The method call duration was '{Duration}' ms.
Microsoft-Windows-Application Server-Applications  |  223       |  Analytic     |  The '{MethodName}' method threw a FaultException when invoked by the OperationInvoker. The method call duration was '{Duration}' ms.
Microsoft-Windows-Application Server-Applications  |  224       |  Analytic     |  The '{ThrottleName}' throttle limit of '{Limit}' is at 70%%.
Microsoft-Windows-Application Server-Applications  |  225       |  Analytic     |  Calculated correlation key '{InstanceKey}' using values '{Values}' in parent scope '{ParentScope}'.
Microsoft-Windows-Application Server-Applications  |  226       |  Analytic     |  {ClosedCount} idle services out of total {TotalCount} activated services closed.
Microsoft-Windows-Application Server-Applications  |  301       |  Analytic     |  Name:'{Name}', Reference:'{HostReference}', Payload:{Payload}
Microsoft-Windows-Application Server-Applications  |  302       |  Analytic     |  Name:'{Name}', Reference:'{HostReference}', Payload:{Payload}
Microsoft-Windows-Application Server-Applications  |  303       |  Analytic     |  Name:'{Name}', Reference:'{HostReference}', Payload:{Payload}
Microsoft-Windows-Application Server-Applications  |  401       |  Analytic     |  Activity boundary.
Microsoft-Windows-Application Server-Applications  |  402       |  Analytic     |  Activity boundary.
Microsoft-Windows-Application Server-Applications  |  403       |  Analytic     |  Activity boundary.
Microsoft-Windows-Application Server-Applications  |  404       |  Analytic     |  Activity boundary.
Microsoft-Windows-Application Server-Applications  |  440       |  Analytic     |  Activity boundary.
Microsoft-Windows-Application Server-Applications  |  441       |  Analytic     |  Activity boundary.
Microsoft-Windows-Application Server-Applications  |  451       |  Analytic     |  {data1}
Microsoft-Windows-Application Server-Applications  |  452       |  Analytic     |  {data1}
Microsoft-Windows-Application Server-Applications  |  499       |  Analytic     |  Transfer event emitted.
Microsoft-Windows-Application Server-Applications  |  501       |  Debug        |  Begin compilation
Microsoft-Windows-Application Server-Applications  |  502       |  Debug        |  End compilation
Microsoft-Windows-Application Server-Applications  |  503       |  Debug        |  ServiceHostFactory begin creation
Microsoft-Windows-Application Server-Applications  |  504       |  Debug        |  ServiceHostFactory end creation
Microsoft-Windows-Application Server-Applications  |  505       |  Debug        |  Begin CreateServiceHost
Microsoft-Windows-Application Server-Applications  |  506       |  Debug        |  End CreateServiceHost
Microsoft-Windows-Application Server-Applications  |  507       |  Debug        |  HostedTransportConfigurationManager begin configuration initialization
Microsoft-Windows-Application Server-Applications  |  508       |  Debug        |  HostedTransportConfigurationManager end configuration initialization
Microsoft-Windows-Application Server-Applications  |  509       |  Analytic     |  ServiceHost Open started.
Microsoft-Windows-Application Server-Applications  |  510       |  Analytic     |  ServiceHost Open completed.
Microsoft-Windows-Application Server-Applications  |  513       |  Debug        |  Received request with virtual path '{VirtualPath}' from the AppDomain '{AppDomainFriendlyName}'.
Microsoft-Windows-Application Server-Applications  |  514       |  Debug        |  WebHostRequest stop.
Microsoft-Windows-Application Server-Applications  |  601       |  Debug        |  Processed ServiceActivation Element Relative Address:'{RelativeAddress}', Normalized Relative Address '{NormalizedAddress}' .
Microsoft-Windows-Application Server-Applications  |  602       |  Debug        |  Incoming request matches a ServiceActivation element with address '{IncomingAddress}'.
Microsoft-Windows-Application Server-Applications  |  603       |  Debug        |  Incoming request matches a WCF Service defined in Asp.Net route with address {IncomingAddress}.
Microsoft-Windows-Application Server-Applications  |  604       |  Debug        |  A new Asp.Net route '{AspNetRoutePrefix}' with serviceType '{ServiceType}' and serviceHostFactoryType '{ServiceHostFactoryType}' is added.
Microsoft-Windows-Application Server-Applications  |  605       |  Debug        |  IncrementBusyCount called. Source : {Data}
Microsoft-Windows-Application Server-Applications  |  606       |  Debug        |  DecrementBusyCount called. Source : {Data}
Microsoft-Windows-Application Server-Applications  |  701       |  Analytic     |  ServiceChannelOpen started.
Microsoft-Windows-Application Server-Applications  |  702       |  Analytic     |  ServiceChannelOpen completed.
Microsoft-Windows-Application Server-Applications  |  703       |  Analytic     |  ServiceChannelCall started.
Microsoft-Windows-Application Server-Applications  |  704       |  Analytic     |  ServiceChannel asynchronous calls started.
Microsoft-Windows-Application Server-Applications  |  706       |  Debug        |  Http Send Request Start.
Microsoft-Windows-Application Server-Applications  |  707       |  Debug        |  Http Send Request Stop.
Microsoft-Windows-Application Server-Applications  |  708       |  Analytic     |  Message received from http transport.
Microsoft-Windows-Application Server-Applications  |  709       |  Analytic     |  Message dispatching started.
Microsoft-Windows-Application Server-Applications  |  710       |  Analytic     |  Start authentication for message dispatching
Microsoft-Windows-Application Server-Applications  |  711       |  Analytic     |  Start authorization for message dispatching
Microsoft-Windows-Application Server-Applications  |  712       |  Analytic     |  Message dispatching completed
Microsoft-Windows-Application Server-Applications  |  715       |  Analytic     |  ServiceChannel Open Start.
Microsoft-Windows-Application Server-Applications  |  716       |  Analytic     |  ServiceChannel Open Stop.
Microsoft-Windows-Application Server-Applications  |  717       |  Analytic     |  Http Send streamed message started.
Microsoft-Windows-Application Server-Applications  |  1001      |  Debug        |  WorkflowInstance Id: '{data1}' has completed in the Closed state.
Microsoft-Windows-Application Server-Applications  |  1002      |  Debug        |  WorkflowApplication Id: '{data1}' was terminated. It has completed in the Faulted state with an exception.
Microsoft-Windows-Application Server-Applications  |  1003      |  Debug        |  WorkflowInstance Id: '{data1}' has completed in the Canceled state.
Microsoft-Windows-Application Server-Applications  |  1004      |  Debug        |  WorkflowInstance Id: '{data1}' was aborted with an exception.
Microsoft-Windows-Application Server-Applications  |  1005      |  Debug        |  WorkflowApplication Id: '{data1}' went idle.
Microsoft-Windows-Application Server-Applications  |  1006      |  Debug        |  WorkflowInstance Id: '{data1}' has encountered an unhandled exception.  The exception originated from Activity '{data2}', DisplayName: '{data3}'.  The following action will be taken: {data4}.
Microsoft-Windows-Application Server-Applications  |  1007      |  Debug        |  WorkflowApplication Id: '{data1}' was Persisted.
Microsoft-Windows-Application Server-Applications  |  1008      |  Debug        |  WorkflowInstance Id: '{data1}' was Unloaded.
Microsoft-Windows-Application Server-Applications  |  1009      |  Debug        |  Parent Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}' scheduled child Activity '{data4}', DisplayName: '{data5}', InstanceId: '{data6}'.
Microsoft-Windows-Application Server-Applications  |  1010      |  Debug        |  Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}' has completed in the '{data4}' state.
Microsoft-Windows-Application Server-Applications  |  1011      |  Debug        |  An ExecuteActivityWorkItem has been scheduled for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.
Microsoft-Windows-Application Server-Applications  |  1012      |  Debug        |  Starting execution of an ExecuteActivityWorkItem for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.
Microsoft-Windows-Application Server-Applications  |  1013      |  Debug        |  An ExecuteActivityWorkItem has completed for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.
Microsoft-Windows-Application Server-Applications  |  1014      |  Debug        |  A CompletionWorkItem has been scheduled for parent Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.  Completed Activity '{data4}', DisplayName: '{data5}', InstanceId: '{data6}'.
Microsoft-Windows-Application Server-Applications  |  1015      |  Debug        |  Starting execution of a CompletionWorkItem for parent Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'. Completed Activity '{data4}', DisplayName: '{data5}', InstanceId: '{data6}'.
Microsoft-Windows-Application Server-Applications  |  1016      |  Debug        |  A CompletionWorkItem has completed for parent Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'. Completed Activity '{data4}', DisplayName: '{data5}', InstanceId: '{data6}'.
Microsoft-Windows-Application Server-Applications  |  1017      |  Debug        |  A CancelActivityWorkItem has been scheduled for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.
Microsoft-Windows-Application Server-Applications  |  1018      |  Debug        |  Starting execution of a CancelActivityWorkItem for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.
Microsoft-Windows-Application Server-Applications  |  1019      |  Debug        |  A CancelActivityWorkItem has completed for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.
Microsoft-Windows-Application Server-Applications  |  1020      |  Debug        |  A Bookmark has been created for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.  BookmarkName: {data4}, BookmarkScope: {data5}.
Microsoft-Windows-Application Server-Applications  |  1021      |  Debug        |  A BookmarkWorkItem has been scheduled for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.  BookmarkName: {data4}, BookmarkScope: {data5}.
Microsoft-Windows-Application Server-Applications  |  1022      |  Debug        |  Starting execution of a BookmarkWorkItem for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.  BookmarkName: {data4}, BookmarkScope: {data5}.
Microsoft-Windows-Application Server-Applications  |  1023      |  Debug        |  A BookmarkWorkItem has completed for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'. BookmarkName: {data4}, BookmarkScope: {data5}.
Microsoft-Windows-Application Server-Applications  |  1024      |  Debug        |  A BookmarkScope has been created: {data1}.
Microsoft-Windows-Application Server-Applications  |  1025      |  Debug        |  The BookmarkScope that had TemporaryId: '{data1}' has been initialized with Id: '{data2}'.
Microsoft-Windows-Application Server-Applications  |  1026      |  Debug        |  A TransactionContextWorkItem has been scheduled for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.
Microsoft-Windows-Application Server-Applications  |  1027      |  Debug        |  Starting execution of a TransactionContextWorkItem for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.
Microsoft-Windows-Application Server-Applications  |  1028      |  Debug        |  A TransactionContextWorkItem has completed for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.
Microsoft-Windows-Application Server-Applications  |  1029      |  Debug        |  A FaultWorkItem has been scheduled for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.  The exception was propagated from Activity '{data4}', DisplayName: '{data5}', InstanceId: '{data6}'.
Microsoft-Windows-Application Server-Applications  |  1030      |  Debug        |  Starting execution of a FaultWorkItem for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.  The exception was propagated from Activity '{data4}', DisplayName: '{data5}', InstanceId: '{data6}'.
Microsoft-Windows-Application Server-Applications  |  1031      |  Debug        |  A FaultWorkItem has completed for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'. The exception was propagated from Activity '{data4}', DisplayName: '{data5}', InstanceId: '{data6}'.
Microsoft-Windows-Application Server-Applications  |  1032      |  Debug        |  A runtime work item has been scheduled for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.
Microsoft-Windows-Application Server-Applications  |  1033      |  Debug        |  Starting execution of a runtime work item for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.
Microsoft-Windows-Application Server-Applications  |  1034      |  Debug        |  A runtime work item has completed for Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.
Microsoft-Windows-Application Server-Applications  |  1035      |  Debug        |  The runtime transaction has been set by Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}'.  Execution isolated to Activity '{data4}', DisplayName: '{data5}', InstanceId: '{data6}'.
Microsoft-Windows-Application Server-Applications  |  1036      |  Debug        |  Activity '{data1}', DisplayName: '{data2}', InstanceId: '{data3}' has scheduled completion of the runtime transaction.
Microsoft-Windows-Application Server-Applications  |  1037      |  Debug        |  The runtime transaction has completed with the state '{data1}'.
Microsoft-Windows-Application Server-Applications  |  1038      |  Debug        |  Entering a no persist block.
Microsoft-Windows-Application Server-Applications  |  1039      |  Debug        |  Exiting a no persist block.
Microsoft-Windows-Application Server-Applications  |  1040      |  Debug        |  In argument '{data1}' on Activity '{data2}', DisplayName: '{data3}', InstanceId: '{data4}' has been bound with value: {data5}.
Microsoft-Windows-Application Server-Applications  |  1041      |  Debug        |  WorkflowApplication Id: '{data1}' is idle and persistable.  The following action will be taken: {data2}.
Microsoft-Windows-Application Server-Applications  |  1101      |  Debug        |  WorkflowInstance Id: '{Id}' E2E Activity
Microsoft-Windows-Application Server-Applications  |  1102      |  Debug        |  WorkflowInstance Id: '{Id}' E2E Activity
Microsoft-Windows-Application Server-Applications  |  1103      |  Debug        |  WorkflowInstance Id: '{Id}' E2E Activity
Microsoft-Windows-Application Server-Applications  |  1104      |  Debug        |  WorkflowInstance Id: '{Id}' E2E Activity
Microsoft-Windows-Application Server-Applications  |  1124      |  Debug        |  InvokeMethod '{data1}' - method is Static.
Microsoft-Windows-Application Server-Applications  |  1125      |  Debug        |  InvokeMethod '{data1}' - method is not Static.
Microsoft-Windows-Application Server-Applications  |  1126      |  Debug        |  An exception was thrown in the method called by the activity '{data1}'. {data2}
Microsoft-Windows-Application Server-Applications  |  1131      |  Debug        |  InvokeMethod '{data1}' - method uses asynchronous pattern of '{data2}' and '{data3}'.
Microsoft-Windows-Application Server-Applications  |  1132      |  Debug        |  InvokeMethod '{data1}' - method does not use asynchronous pattern.
Microsoft-Windows-Application Server-Applications  |  1140      |  Debug        |  Flowchart '{data1}' - Start has been scheduled.
Microsoft-Windows-Application Server-Applications  |  1141      |  Debug        |  Flowchart '{data1}' - was executed with no Nodes.
Microsoft-Windows-Application Server-Applications  |  1143      |  Debug        |  Flowchart '{data1}'/FlowStep - Next node is null. Flowchart execution will end.
Microsoft-Windows-Application Server-Applications  |  1146      |  Debug        |  Flowchart '{data1}'/FlowSwitch - Case '{data2}' was selected.
Microsoft-Windows-Application Server-Applications  |  1147      |  Debug        |  Flowchart '{data1}'/FlowSwitch - Default Case was selected.
Microsoft-Windows-Application Server-Applications  |  1148      |  Debug        |  Flowchart '{data1}'/FlowSwitch - could find neither a Case activity nor a Default Case matching the Expression result. Flowchart execution will end.
Microsoft-Windows-Application Server-Applications  |  1150      |  Debug        |  CompensableActivity '{data1}' is in the '{data2}' state.
Microsoft-Windows-Application Server-Applications  |  1223      |  Debug        |  The Switch activity '{data1}' could not find a Case activity matching the Expression result.
Microsoft-Windows-Application Server-Applications  |  1400      |  Analytic     |  {data1}
Microsoft-Windows-Application Server-Applications  |  1401      |  Analytic     |  {data1}
Microsoft-Windows-Application Server-Applications  |  1402      |  Analytic     |  {msg} Connection pool key: {key}
Microsoft-Windows-Application Server-Applications  |  1403      |  Analytic     |  {msg} Connection pool key: {key}
Microsoft-Windows-Application Server-Applications  |  1405      |  Analytic     |  {data1}
Microsoft-Windows-Application Server-Applications  |  1406      |  Analytic     |  {data1}
Microsoft-Windows-Application Server-Applications  |  1407      |  Analytic     |  {data1}
Microsoft-Windows-Application Server-Applications  |  1409      |  Analytic     |  {data1}
Microsoft-Windows-Application Server-Applications  |  1416      |  Analytic     |  {data1}
Microsoft-Windows-Application Server-Applications  |  1417      |  Analytic     |  {data1}
Microsoft-Windows-Application Server-Applications  |  1418      |  Debug        |  {data1}
Microsoft-Windows-Application Server-Applications  |  1419      |  Debug        |  {data1}
Microsoft-Windows-Application Server-Applications  |  1420      |  Analytic     |  {data1}
Microsoft-Windows-Application Server-Applications  |  1422      |  Analytic     |  {msg}
Microsoft-Windows-Application Server-Applications  |  1423      |  Debug        |  Negotiate token authenticator state cache ratio: {cur}/{max}
Microsoft-Windows-Application Server-Applications  |  1424      |  Debug        |  Security session ratio: {cur}/{max}
Microsoft-Windows-Application Server-Applications  |  1430      |  Analytic     |  Pending connections ratio: {cur}/{max}
Microsoft-Windows-Application Server-Applications  |  1431      |  Analytic     |  Concurrent calls ratio: {cur}/{max}
Microsoft-Windows-Application Server-Applications  |  1432      |  Analytic     |  Concurrent sessions ratio: {cur}/{max}
Microsoft-Windows-Application Server-Applications  |  1433      |  Analytic     |  Outbound connections per endpoint ratio: {cur}/{max}
Microsoft-Windows-Application Server-Applications  |  1436      |  Analytic     |  Pending messages per channel ratio: {cur}/{max}
Microsoft-Windows-Application Server-Applications  |  1438      |  Analytic     |  Concurrent instances ratio: {cur}/{max}
Microsoft-Windows-Application Server-Applications  |  1439      |  Debug        |  Zero pending accepts left
Microsoft-Windows-Application Server-Applications  |  1441      |  Analytic     |  {data1}
Microsoft-Windows-Application Server-Applications  |  1442      |  Analytic     |  Receive retry count reached on MSMQ message with id '{data1}'
Microsoft-Windows-Application Server-Applications  |  1443      |  Analytic     |  Max retry cycles exceeded on MSMQ message with id '{data1}'
Microsoft-Windows-Application Server-Applications  |  1445      |  Analytic     |  Created new '{itemTypeName}'
Microsoft-Windows-Application Server-Applications  |  1446      |  Analytic     |  Created new '{itemTypeName}'
Microsoft-Windows-Application Server-Applications  |  1449      |  Debug        |  Message received by workflow
Microsoft-Windows-Application Server-Applications  |  1450      |  Debug        |  Message sent from workflow
Microsoft-Windows-Application Server-Applications  |  1451      |  Analytic     |  {data1}
Microsoft-Windows-Application Server-Applications  |  2021      |  Debug        |  Execute work item start
Microsoft-Windows-Application Server-Applications  |  2022      |  Debug        |  Execute work item stop
Microsoft-Windows-Application Server-Applications  |  2023      |  Debug        |  SendMessageChannelCache miss
Microsoft-Windows-Application Server-Applications  |  2024      |  Debug        |  InternalCacheMetadata started on activity '{id}'.
Microsoft-Windows-Application Server-Applications  |  2025      |  Debug        |  InternalCacheMetadata stopped on activity '{id}'.
Microsoft-Windows-Application Server-Applications  |  2026      |  Debug        |  Compiling VB expression '{expr}'
Microsoft-Windows-Application Server-Applications  |  2027      |  Debug        |  CacheRootMetadata started on activity '{activityName}'
Microsoft-Windows-Application Server-Applications  |  2028      |  Debug        |  CacheRootMetadata stopped on activity {activityName}.
Microsoft-Windows-Application Server-Applications  |  2029      |  Debug        |  Finished compiling VB expression.
Microsoft-Windows-Application Server-Applications  |  2576      |  Debug        |  The TryCatch activity '{data1}' has caught an exception of type '{data2}'.
Microsoft-Windows-Application Server-Applications  |  2577      |  Debug        |  A child activity of the TryCatch activity '{data1}' has thrown an exception during cancelation.
Microsoft-Windows-Application Server-Applications  |  2578      |  Debug        |  A Catch or Finally activity that is associated with the TryCatch activity '{data1}' has thrown an exception.
Microsoft-Windows-Application Server-Applications  |  3300      |  Analytic     |  Failed to Complete {TypeName}.
Microsoft-Windows-Application Server-Applications  |  3301      |  Debug        |  Failed to Abandon {TypeName}.
Microsoft-Windows-Application Server-Applications  |  3302      |  Analytic     |  Receive Context faulted.
Microsoft-Windows-Application Server-Applications  |  3303      |  Debug        |  {TypeName} was Abandoned with exception {ExceptionToString}.
Microsoft-Windows-Application Server-Applications  |  3305      |  Debug        |  Number of cached channel factories is: '{Count}'.  At most '{MaxNum}' channel factories can be cached.
Microsoft-Windows-Application Server-Applications  |  3306      |  Debug        |  A channel factory has been aged out of the cache because the cache has reached its limit of '{Count}'.
Microsoft-Windows-Application Server-Applications  |  3307      |  Debug        |  Used matching channel factory found in cache.
Microsoft-Windows-Application Server-Applications  |  3308      |  Debug        |  Not using channel factory from cache, i.e. caching disabled for instance.
Microsoft-Windows-Application Server-Applications  |  3309      |  Debug        |  Query composition using '{TypeName}' was executed on the Request Uri: '{Uri}'.
Microsoft-Windows-Application Server-Applications  |  3310      |  Analytic     |  The '{OperationName}' operation was dispatched with errors.
Microsoft-Windows-Application Server-Applications  |  3311      |  Analytic     |  The '{OperationName}' operation was dispatched successfully.
Microsoft-Windows-Application Server-Applications  |  3312      |  Debug        |  A message with size '{Size}' bytes was read by the encoder.
Microsoft-Windows-Application Server-Applications  |  3313      |  Debug        |  A message with size '{Size}' bytes was written by the encoder.
Microsoft-Windows-Application Server-Applications  |  3314      |  Analytic     |  Session aborting for idle channel to uri:'{RemoteAddress}'.
Microsoft-Windows-Application Server-Applications  |  3319      |  Debug        |  Connection accept started.
Microsoft-Windows-Application Server-Applications  |  3320      |  Debug        |  ListenerId:{ListenerHashCode} accepted SocketId:{SocketHashCode}.
Microsoft-Windows-Application Server-Applications  |  3321      |  Debug        |  Pool for {PoolKey} has no available connection and {busy} busy connections.
Microsoft-Windows-Application Server-Applications  |  3322      |  Debug        |  Dispatcher started deserialization the request message.
Microsoft-Windows-Application Server-Applications  |  3323      |  Debug        |  Dispatcher completed deserialization the request message.
Microsoft-Windows-Application Server-Applications  |  3324      |  Debug        |  Dispatcher started serialization of the reply message.
Microsoft-Windows-Application Server-Applications  |  3325      |  Debug        |  Dispatcher completed serialization of the reply message.
Microsoft-Windows-Application Server-Applications  |  3326      |  Debug        |  Client request serialization started.
Microsoft-Windows-Application Server-Applications  |  3327      |  Debug        |  Client completed serialization of the request message.
Microsoft-Windows-Application Server-Applications  |  3328      |  Debug        |  Client started deserializing the reply message.
Microsoft-Windows-Application Server-Applications  |  3329      |  Debug        |  Client completed deserializing the reply message.
Microsoft-Windows-Application Server-Applications  |  3330      |  Debug        |  Security negotiation started.
Microsoft-Windows-Application Server-Applications  |  3331      |  Debug        |  Security negotiation completed.
Microsoft-Windows-Application Server-Applications  |  3332      |  Debug        |  SecurityTokenProvider opening completed.
Microsoft-Windows-Application Server-Applications  |  3333      |  Debug        |  Outgoing message has been secured.
Microsoft-Windows-Application Server-Applications  |  3334      |  Debug        |  Incoming message has been verified.
Microsoft-Windows-Application Server-Applications  |  3335      |  Debug        |  Service instance retrieval started.
Microsoft-Windows-Application Server-Applications  |  3336      |  Debug        |  Service instance retrieved.
Microsoft-Windows-Application Server-Applications  |  3337      |  Debug        |  ChannelHandlerId:{ChannelId} - Message receive loop started.
Microsoft-Windows-Application Server-Applications  |  3338      |  Debug        |  ChannelHandlerId:{ChannelId} - Message receive loop stopped.
Microsoft-Windows-Application Server-Applications  |  3339      |  Debug        |  ChannelFactory created .
Microsoft-Windows-Application Server-Applications  |  3340      |  Debug        |  Pipe connection accept started on {uri} .
Microsoft-Windows-Application Server-Applications  |  3341      |  Debug        |  Pipe connection accepted.
Microsoft-Windows-Application Server-Applications  |  3342      |  Debug        |  Connection establishment started for {Key}.
Microsoft-Windows-Application Server-Applications  |  3343      |  Debug        |  Connection established.
Microsoft-Windows-Application Server-Applications  |  3345      |  Debug        |  Session preamble for '{Via}' understood.
Microsoft-Windows-Application Server-Applications  |  3346      |  Debug        |  Connection reader sending fault '{FaultString}'.
Microsoft-Windows-Application Server-Applications  |  3347      |  Debug        |  Socket accept closed.
Microsoft-Windows-Application Server-Applications  |  3348      |  Analytic     |  Service host faulted.
Microsoft-Windows-Application Server-Applications  |  3349      |  Debug        |  Listener opening for '{Uri}'.
Microsoft-Windows-Application Server-Applications  |  3350      |  Debug        |  Listener open completed.
Microsoft-Windows-Application Server-Applications  |  3351      |  Analytic     |  Server max pooled connections quota reached.
Microsoft-Windows-Application Server-Applications  |  3352      |  Analytic     |  SocketId:{SocketId} to remote address {Uri} timed out.
Microsoft-Windows-Application Server-Applications  |  3353      |  Analytic     |  SocketId:{SocketId} to remote address {Uri} had a connection reset error.
Microsoft-Windows-Application Server-Applications  |  3354      |  Debug        |  Service security negotiation completed.
Microsoft-Windows-Application Server-Applications  |  3355      |  Analytic     |  Security negotiation processing failed.
Microsoft-Windows-Application Server-Applications  |  3356      |  Debug        |  Security verification succeeded.
Microsoft-Windows-Application Server-Applications  |  3357      |  Analytic     |  Security verification failed.
Microsoft-Windows-Application Server-Applications  |  3358      |  Debug        |  Socket duplicated for {Uri}.
Microsoft-Windows-Application Server-Applications  |  3359      |  Debug        |  Security impersonation succeeded.
Microsoft-Windows-Application Server-Applications  |  3360      |  Analytic     |  Security impersonation failed.
Microsoft-Windows-Application Server-Applications  |  3361      |  Analytic     |  Http channel request aborted.
Microsoft-Windows-Application Server-Applications  |  3362      |  Analytic     |  Http channel response aborted.
Microsoft-Windows-Application Server-Applications  |  3363      |  Analytic     |  Http authentication failed.
Microsoft-Windows-Application Server-Applications  |  3364      |  Analytic     |  SharedListenerProxy registration started for uri '{Uri}'.
Microsoft-Windows-Application Server-Applications  |  3365      |  Analytic     |  SharedListenerProxy Register Stop.
Microsoft-Windows-Application Server-Applications  |  3366      |  Analytic     |  SharedListenerProxy register failed with status '{Status}'.
Microsoft-Windows-Application Server-Applications  |  3367      |  Analytic     |  ConnectionPoolPreambleFailed.
Microsoft-Windows-Application Server-Applications  |  3368      |  Analytic     |  SslOnAcceptUpgradeStart
Microsoft-Windows-Application Server-Applications  |  3369      |  Analytic     |  SslOnAcceptUpgradeStop
Microsoft-Windows-Application Server-Applications  |  3370      |  Debug        |  BinaryMessageEncoder started encoding the message.
Microsoft-Windows-Application Server-Applications  |  3371      |  Debug        |  MtomMessageEncoder started encoding the message.
Microsoft-Windows-Application Server-Applications  |  3372      |  Debug        |  TextMessageEncoder started encoding the message.
Microsoft-Windows-Application Server-Applications  |  3373      |  Debug        |  BinaryMessageEncoder started decoding the message.
Microsoft-Windows-Application Server-Applications  |  3374      |  Debug        |  MtomMessageEncoder started decoding  the message.
Microsoft-Windows-Application Server-Applications  |  3375      |  Debug        |  TextMessageEncoder started decoding the message.
Microsoft-Windows-Application Server-Applications  |  3376      |  Debug        |  Http transport started receiving a message.
Microsoft-Windows-Application Server-Applications  |  3377      |  Debug        |  SocketId:{SocketId} read '{Size}' bytes read from '{Endpoint}'.
Microsoft-Windows-Application Server-Applications  |  3378      |  Debug        |  SocketId:{SocketId} read '{Size}' bytes read from '{Endpoint}'.
Microsoft-Windows-Application Server-Applications  |  3379      |  Debug        |  SocketId:{SocketId} writing '{Size}' bytes to '{Endpoint}'.
Microsoft-Windows-Application Server-Applications  |  3380      |  Debug        |  SocketId:{SocketId} writing '{Size}' bytes to '{Endpoint}'.
Microsoft-Windows-Application Server-Applications  |  3381      |  Debug        |  SessionId:{SessionId} acknowledgement sent.
Microsoft-Windows-Application Server-Applications  |  3382      |  Debug        |  SessionId:{SessionId} reconnecting.
Microsoft-Windows-Application Server-Applications  |  3383      |  Debug        |  SessionId:{SessionId} faulted.
Microsoft-Windows-Application Server-Applications  |  3384      |  Analytic     |  WindowsStreamSecurity initiating security upgrade.
Microsoft-Windows-Application Server-Applications  |  3385      |  Analytic     |  Windows streaming security on accepting upgrade.
Microsoft-Windows-Application Server-Applications  |  3386      |  Analytic     |  SocketId:{SocketId} is aborting.
Microsoft-Windows-Application Server-Applications  |  3388      |  Analytic     |  HttpGetContext start.
Microsoft-Windows-Application Server-Applications  |  3389      |  Debug        |  Client sending preamble start.
Microsoft-Windows-Application Server-Applications  |  3390      |  Debug        |  Client sending preamble stop.
Microsoft-Windows-Application Server-Applications  |  3391      |  Analytic     |  Http Message receive failed.
Microsoft-Windows-Application Server-Applications  |  3392      |  Debug        |  TransactionScope is being created with LocalIdentifier:'{LocalId}' and DistributedIdentifier:'{Distributed}'.
Microsoft-Windows-Application Server-Applications  |  3393      |  Debug        |  A streamed message was read by the encoder.
Microsoft-Windows-Application Server-Applications  |  3394      |  Debug        |  A streamed message was written by the encoder.
Microsoft-Windows-Application Server-Applications  |  3395      |  Debug        |  A message was written asynchronously by the encoder.
Microsoft-Windows-Application Server-Applications  |  3396      |  Debug        |  BufferId:{BufferId} completed writing '{Size}' bytes to underlying stream.
Microsoft-Windows-Application Server-Applications  |  3397      |  Debug        |  A message was written asynchronously by the encoder.
Microsoft-Windows-Application Server-Applications  |  3398      |  Debug        |  Pipe shared memory created at '{sharedMemoryName}' .
Microsoft-Windows-Application Server-Applications  |  3399      |  Debug        |  NamedPipe '{pipeName}' created.
Microsoft-Windows-Application Server-Applications  |  3401      |  Debug        |  Signature verification started.
Microsoft-Windows-Application Server-Applications  |  3402      |  Debug        |  Signature verification succeeded
Microsoft-Windows-Application Server-Applications  |  3403      |  Debug        |  Wrapped key decryption started.
Microsoft-Windows-Application Server-Applications  |  3404      |  Debug        |  Wrapped key decryption succeeded.
Microsoft-Windows-Application Server-Applications  |  3405      |  Debug        |  Encrypted data processing started.
Microsoft-Windows-Application Server-Applications  |  3406      |  Debug        |  Encrypted data processing succeeded.
Microsoft-Windows-Application Server-Applications  |  3407      |  Debug        |  Http message handler started processing the inbound request.
Microsoft-Windows-Application Server-Applications  |  3408      |  Debug        |  Http message handler started processing the inbound request asynchronously.
Microsoft-Windows-Application Server-Applications  |  3409      |  Debug        |  Http message handler completed processing an inbound request.
Microsoft-Windows-Application Server-Applications  |  3410      |  Analytic     |  Http message handler is faulted.
Microsoft-Windows-Application Server-Applications  |  3411      |  Analytic     |  WebSocket connection timed out.
Microsoft-Windows-Application Server-Applications  |  3412      |  Debug        |  Http message handler started processing the response.
Microsoft-Windows-Application Server-Applications  |  3413      |  Debug        |  Http message handler started processing the response asynchronously.
Microsoft-Windows-Application Server-Applications  |  3414      |  Debug        |  Http message handler completed processing the response.
Microsoft-Windows-Application Server-Applications  |  3415      |  Debug        |  WebSocket connection request to '{remoteAddress}' send start.
Microsoft-Windows-Application Server-Applications  |  3416      |  Debug        |  WebSocketId:{websocketId} connection request sent.
Microsoft-Windows-Application Server-Applications  |  3417      |  Debug        |  WebSocket connection accept start.
Microsoft-Windows-Application Server-Applications  |  3418      |  Debug        |  WebSocketId:{websocketId} connection accepted.
Microsoft-Windows-Application Server-Applications  |  3419      |  Analytic     |  WebSocket connection declined with status code '{errorMessage}'
Microsoft-Windows-Application Server-Applications  |  3420      |  Analytic     |  WebSocket connection request failed: '{errorMessage}'
Microsoft-Windows-Application Server-Applications  |  3421      |  Analytic     |  WebSocketId:{websocketId} connection is aborted.
Microsoft-Windows-Application Server-Applications  |  3422      |  Debug        |  WebSocketId:{websocketId} writing '{byteCount}' bytes to '{remoteAddress}'.
Microsoft-Windows-Application Server-Applications  |  3423      |  Debug        |  WebSocketId:{websocketId} asynchronous write stop.
Microsoft-Windows-Application Server-Applications  |  3424      |  Debug        |  WebSocketId:{websocketId} read start.
Microsoft-Windows-Application Server-Applications  |  3425      |  Debug        |  WebSocketId:{websocketId} read '{byteCount}' bytes from '{remoteAddress}'.
Microsoft-Windows-Application Server-Applications  |  3426      |  Debug        |  WebSocketId:{websocketId} sending close message to '{remoteAddress}' with close status '{closeStatus}'.
Microsoft-Windows-Application Server-Applications  |  3427      |  Debug        |  WebSocketId:{websocketId} sending close output message to '{remoteAddress}' with close status '{closeStatus}'.
Microsoft-Windows-Application Server-Applications  |  3428      |  Debug        |  WebSocketId:{websocketId} connection closed.
Microsoft-Windows-Application Server-Applications  |  3429      |  Debug        |  WebSocketId:{websocketId} connection close message received with status '{closeStatus}'.
Microsoft-Windows-Application Server-Applications  |  3430      |  Debug        |  Using the WebSocketVersion from a client WebSocket factory of type '{clientWebSocketFactoryType}'.
Microsoft-Windows-Application Server-Applications  |  3431      |  Debug        |  Creating the client WebSocket with a factory of type '{clientWebSocketFactoryType}'.
Microsoft-Windows-Application Server-Applications  |  3501      |  Analytic     |  ContractDescription with Name='{data1}' and Namespace='{data2}' has been inferred from WorkflowService.
Microsoft-Windows-Application Server-Applications  |  3502      |  Analytic     |  OperationDescription with Name='{data1}' in contract '{data2}' has been inferred from WorkflowService. IsOneWay={data3}.
Microsoft-Windows-Application Server-Applications  |  3503      |  Analytic     |  A duplicate CorrelationQuery was found with Where='{data1}'. This duplicate query will not be used when calculating correlation.
Microsoft-Windows-Application Server-Applications  |  3507      |  Analytic     |  A service endpoint has been added for address '{data1}', binding '{data2}', and contract '{data3}'.
Microsoft-Windows-Application Server-Applications  |  3508      |  Analytic     |  TrackingProfile '{TrackingProfile}' for the ActivityDefinitionId '{ActivityDefinitionId}' not found. Either the TrackingProfile is not found in the config file or the ActivityDefinitionId does not match.
Microsoft-Windows-Application Server-Applications  |  3550      |  Analytic     |  Operation '{data1}' cannot be performed at this time. Another attempt will be made when the service instance is ready to process this particular operation.
Microsoft-Windows-Application Server-Applications  |  3551      |  Analytic     |  Operation '{data2}' on service instance '{data1}' cannot be performed at this time. Another attempt will be made when the service instance is ready to process this particular operation.
Microsoft-Windows-Application Server-Applications  |  3552      |  Analytic     |  The throttle 'MaxPendingMessagesPerChannel' limit of  '{limit}' was hit. To increase this limit, adjust the MaxPendingMessagesPerChannel property on BufferedReceiveServiceBehavior.
Microsoft-Windows-Application Server-Applications  |  3553      |  Debug        |  XamlServicesLoad start
Microsoft-Windows-Application Server-Applications  |  3554      |  Debug        |  XamlServicesLoad Stop
Microsoft-Windows-Application Server-Applications  |  3555      |  Debug        |  CreateWorkflowServiceHost start
Microsoft-Windows-Application Server-Applications  |  3556      |  Debug        |  CreateWorkflowServiceHost Stop
Microsoft-Windows-Application Server-Applications  |  3557      |  Analytic     |  The call to EndCommit on the CommittableTransaction with id = '{data1}' threw a TransactionException with the following message: '{data2}'.
Microsoft-Windows-Application Server-Applications  |  3558      |  Analytic     |  Service activation start
Microsoft-Windows-Application Server-Applications  |  3559      |  Analytic     |  Service activation Stop
Microsoft-Windows-Application Server-Applications  |  3560      |  Analytic     |  Available memory (bytes): {availableMemoryBytes}
Microsoft-Windows-Application Server-Applications  |  3561      |  Operational  |  The service could not be activated. Exception details: {data1}
Microsoft-Windows-Application Server-Applications  |  3800      |  Debug        |  The Routing Service is closing client '{data1}'.
Microsoft-Windows-Application Server-Applications  |  3801      |  Debug        |  Routing Service client '{data1}' has faulted.
Microsoft-Windows-Application Server-Applications  |  3802      |  Debug        |  A Routing Service one way message is completing.
Microsoft-Windows-Application Server-Applications  |  3803      |  Debug        |  The Routing Service failed while processing a message on the endpoint with address '{data1}'.
Microsoft-Windows-Application Server-Applications  |  3804      |  Debug        |  The Routing Service is creating a client for endpoint: '{data1}'.
Microsoft-Windows-Application Server-Applications  |  3805      |  Debug        |  The Routing Service is configured with RouteOnHeadersOnly: {data1}, SoapProcessingEnabled: {data2}, EnsureOrderedDispatch: {data3}.
Microsoft-Windows-Application Server-Applications  |  3807      |  Debug        |  A Routing Service request reply message is completing.
Microsoft-Windows-Application Server-Applications  |  3809      |  Debug        |  The Routing Service routed message with ID: '{data1}' to {data2} endpoint lists.
Microsoft-Windows-Application Server-Applications  |  3810      |  Debug        |  A new RoutingConfiguration has been applied to the Routing Service.
Microsoft-Windows-Application Server-Applications  |  3815      |  Debug        |  The Routing Service is processing a message with ID: '{data1}', Action: '{data2}', Inbound URL: '{data3}' Received in Transaction: {data4}.
Microsoft-Windows-Application Server-Applications  |  3816      |  Debug        |  The Routing Service is transmitting the message with ID: '{data1}' [operation {data2}] to '{data3}'.
Microsoft-Windows-Application Server-Applications  |  3817      |  Debug        |  The Routing Service is committing a transaction with id: '{data1}'.
Microsoft-Windows-Application Server-Applications  |  3818      |  Debug        |  Routing Service component {data1} encountered a duplex callback exception.
Microsoft-Windows-Application Server-Applications  |  3819      |  Debug        |  Routing Service message with ID: '{data1}' [operation {data2}] moved to backup endpoint '{data3}'.
Microsoft-Windows-Application Server-Applications  |  3820      |  Debug        |  The Routing Service created a new Transaction with id '{data1}' for processing message(s).
Microsoft-Windows-Application Server-Applications  |  3821      |  Debug        |  The Routing Service failed while closing outbound client '{data1}'.
Microsoft-Windows-Application Server-Applications  |  3822      |  Debug        |  The Routing Service is sending back a response message with Action '{data1}'.
Microsoft-Windows-Application Server-Applications  |  3823      |  Debug        |  The Routing Service is sending back a Fault response message with Action '{data1}'.
Microsoft-Windows-Application Server-Applications  |  3824      |  Debug        |  The Routing Service is calling ReceiveContext.Complete for Message with ID: '{data1}'.
Microsoft-Windows-Application Server-Applications  |  3825      |  Debug        |  The Routing Service is calling ReceiveContext.Abandon for Message with ID: '{data1}'.
Microsoft-Windows-Application Server-Applications  |  3826      |  Debug        |  The Routing Service will send messages using existing transaction '{data1}'.
Microsoft-Windows-Application Server-Applications  |  3827      |  Debug        |  The Routing Service failed while sending to '{data1}'.
Microsoft-Windows-Application Server-Applications  |  3828      |  Analytic     |  Routing Service MessageFilterTable Match Start.
Microsoft-Windows-Application Server-Applications  |  3829      |  Analytic     |  Routing Service MessageFilterTable Match Stop.
Microsoft-Windows-Application Server-Applications  |  3830      |  Debug        |  The Routing Service is calling abort on channel: '{data1}'.
Microsoft-Windows-Application Server-Applications  |  3831      |  Debug        |  The Routing Service has handled an exception.
Microsoft-Windows-Application Server-Applications  |  3832      |  Debug        |  The Routing Service successfully transmitted Message with ID: '{data1} [operation {data2}] to '{data3}'.
Microsoft-Windows-Application Server-Applications  |  4001      |  Analytic     |  Transport listener session received with via '{via}'
Microsoft-Windows-Application Server-Applications  |  4002      |  Analytic     |  FailFastException.
Microsoft-Windows-Application Server-Applications  |  4003      |  Analytic     |  Service start pipe error.
Microsoft-Windows-Application Server-Applications  |  4008      |  Analytic     |  Session dispatch started.
Microsoft-Windows-Application Server-Applications  |  4010      |  Analytic     |  Session dispatch for '{Uri}' failed since pending session queue is full with '{count}' pending items.
Microsoft-Windows-Application Server-Applications  |  4011      |  Analytic     |  Message queue register start.
Microsoft-Windows-Application Server-Applications  |  4012      |  Analytic     |  Message queue registration aborted with status:'{Status}' for uri:'{Uri}'.
Microsoft-Windows-Application Server-Applications  |  4013      |  Analytic     |  Message queue unregister succeeded for uri:'{Uri}'.
Microsoft-Windows-Application Server-Applications  |  4014      |  Analytic     |  Message queue registration for uri:'{Uri}' failed with status:'{Status}'.
Microsoft-Windows-Application Server-Applications  |  4015      |  Analytic     |  Message queue registration completed for uri '{Uri}'.
Microsoft-Windows-Application Server-Applications  |  4016      |  Analytic     |  Message queue failed duplicating socket.
Microsoft-Windows-Application Server-Applications  |  4019      |  Analytic     |  MessageQueueDuplicatedSocketComplete
Microsoft-Windows-Application Server-Applications  |  4020      |  Analytic     |  Tcp transport listener starting to listen on uri:'{Uri}'.
Microsoft-Windows-Application Server-Applications  |  4021      |  Analytic     |  Tcp transport listener listening.
Microsoft-Windows-Application Server-Applications  |  4022      |  Analytic     |  Error Code:{hresult}
Microsoft-Windows-Application Server-Applications  |  4023      |  Analytic     |  Was closing all listener channel instances completed.
Microsoft-Windows-Application Server-Applications  |  4024      |  Analytic     |  Error Code:{hresult}
Microsoft-Windows-Application Server-Applications  |  4025      |  Analytic     |  Error Code:{hresult}
Microsoft-Windows-Application Server-Applications  |  4026      |  Analytic     |  WAS Connected.
Microsoft-Windows-Application Server-Applications  |  4027      |  Analytic     |  WAS Disconnected.
Microsoft-Windows-Application Server-Applications  |  4028      |  Analytic     |  Pipe transport listener listening start on uri:{Uri}.
Microsoft-Windows-Application Server-Applications  |  4029      |  Analytic     |  Pipe transport listener listening stop.
Microsoft-Windows-Application Server-Applications  |  4030      |  Analytic     |  Session dispatch succeeded.
Microsoft-Windows-Application Server-Applications  |  4031      |  Analytic     |  Session dispatch failed.
Microsoft-Windows-Application Server-Applications  |  4032      |  Analytic     |  WAS connection timed out.
Microsoft-Windows-Application Server-Applications  |  4033      |  Debug        |  Routing table lookup started.
Microsoft-Windows-Application Server-Applications  |  4034      |  Debug        |  Routing table lookup completed.
Microsoft-Windows-Application Server-Applications  |  4035      |  Debug        |  Pending session queue ratio: {curr}/{max}
Microsoft-Windows-Application Server-Applications  |  4201      |  Debug        |  End SQL command execution: {data1}
Microsoft-Windows-Application Server-Applications  |  4202      |  Debug        |  Starting SQL command execution: {data1}
Microsoft-Windows-Application Server-Applications  |  4203      |  Debug        |  Failed to extend lock expiration, lock expiration already passed or the lock owner was deleted. Aborting SqlWorkflowInstanceStore.
Microsoft-Windows-Application Server-Applications  |  4205      |  Debug        |  Command failed: {data1}
Microsoft-Windows-Application Server-Applications  |  4206      |  Debug        |  Encountered exception {data1} while attempting to unlock instance.
Microsoft-Windows-Application Server-Applications  |  4207      |  Debug        |  Giving up retrying a SQL command as the maximum number of retries have been performed.
Microsoft-Windows-Application Server-Applications  |  4208      |  Debug        |  Retrying a SQL command due to SQL error number {data1}.
Microsoft-Windows-Application Server-Applications  |  4209      |  Debug        |  Timeout trying to open a SQL connection. The operation did not complete within the allotted timeout of {data1}. The time allotted to this operation may have been a portion of a longer timeout.
Microsoft-Windows-Application Server-Applications  |  4210      |  Debug        |  Caught SQL Exception number {data1} message {data2}.
Microsoft-Windows-Application Server-Applications  |  4211      |  Debug        |  Queuing SQL retry with delay {data1} milliseconds.
Microsoft-Windows-Application Server-Applications  |  4212      |  Debug        |  Timeout trying to acquire the instance lock.  The operation did not complete within the allotted timeout of {data1}. The time allotted to this operation may have been a portion of a longer timeout.
Microsoft-Windows-Application Server-Applications  |  4213      |  Debug        |  Detection of runnable instances failed due to the following exception
Microsoft-Windows-Application Server-Applications  |  4214      |  Debug        |  Recovering instance locks failed due to the following exception
Microsoft-Windows-Application Server-Applications  |  4600      |  Debug        |  Message could not be logged as it exceeds the ETW event size
Microsoft-Windows-Application Server-Applications  |  4801      |  Debug        |  The DiscoveryClient created inside DiscoveryClientChannel failed to close and hence has been aborted.
Microsoft-Windows-Application Server-Applications  |  4802      |  Debug        |  A ProtocolException was suppressed while closing the DiscoveryClient. This could be because a DiscoveryService is still trying to send response to the DiscoveryClient.
Microsoft-Windows-Application Server-Applications  |  4803      |  Debug        |  The DiscoveryClient received a multicast suppression message from a DiscoveryProxy.
Microsoft-Windows-Application Server-Applications  |  4804      |  Debug        |  A {discoveryMessageName} message with messageId='{messageId}' was dropped by the DiscoveryClient because the corresponding {discoveryOperationName} operation was completed.
Microsoft-Windows-Application Server-Applications  |  4805      |  Debug        |  A {messageType} message with messageId='{messageId}' was dropped because it had invalid content.
Microsoft-Windows-Application Server-Applications  |  4806      |  Debug        |  A {discoveryMessageName} message with messageId='{messageId}' and relatesTo='{relatesTo}' was dropped by the DiscoveryClient because either the corresponding {discoveryOperationName} operation was completed or the relatesTo value is invalid.
Microsoft-Windows-Application Server-Applications  |  4807      |  Debug        |  A discovery request message with messageId='{messageId}' was dropped because it had an invalid ReplyTo address.
Microsoft-Windows-Application Server-Applications  |  4808      |  Debug        |  A {messageType} message was dropped because it did not have any content.
Microsoft-Windows-Application Server-Applications  |  4809      |  Debug        |  A {messageType} message was dropped because the message header did not contain the required MessageId property.
Microsoft-Windows-Application Server-Applications  |  4810      |  Debug        |  A {discoveryMessageName} message with messageId='{messageId}' was dropped by the DiscoveryClient because it did not have the DiscoveryMessageSequence property.
Microsoft-Windows-Application Server-Applications  |  4811      |  Debug        |  A {discoveryMessageName} message with messageId='{messageId}' was dropped by the DiscoveryClient because the message header did not contain the required RelatesTo property.
Microsoft-Windows-Application Server-Applications  |  4812      |  Debug        |  A discovery request message with messageId='{messageId}' was dropped because it did not have a ReplyTo address.
Microsoft-Windows-Application Server-Applications  |  4813      |  Debug        |  A {messageType} message with messageId='{messageId}' was dropped because it was a duplicate.
Microsoft-Windows-Application Server-Applications  |  4814      |  Debug        |  The discoverability of endpoint with EndpointAddress='{endpointAddress}' and ListenUri='{listenUri}' has been disabled.
Microsoft-Windows-Application Server-Applications  |  4815      |  Debug        |  The discoverability of endpoint with EndpointAddress='{endpointAddress}' and ListenUri='{listenUri}' has been enabled.
Microsoft-Windows-Application Server-Applications  |  4816      |  Debug        |  A Find operation was initiated in the DiscoveryClientChannel to discover endpoint(s).
Microsoft-Windows-Application Server-Applications  |  4817      |  Debug        |  The DiscoveryClientChannel failed to create the channel with a discovered endpoint with EndpointAddress='{endpointAddress}' and Via='{via}'. The DiscoveryClientChannel will now attempt to use the next available discovered endpoint.
Microsoft-Windows-Application Server-Applications  |  4818      |  Debug        |  The DiscoveryClientChannel failed to open the channel with a discovered endpoint with EndpointAddress='{endpointAddress}' and Via='{via}'. The DiscoveryClientChannel will now attempt to use the next available discovered endpoint.
Microsoft-Windows-Application Server-Applications  |  4819      |  Debug        |  The DiscoveryClientChannel successfully discovered an endpoint and opened the channel using it. The client is connected to a service using EndpointAddress='{endpointAddress}' and Via='{via}'.
Microsoft-Windows-Application Server-Applications  |  4820      |  Debug        |  The SynchronizationContext has been reset to its original value of {synchronizationContextType} by DiscoveryClientChannel.
Microsoft-Windows-Application Server-Applications  |  4821      |  Debug        |  The SynchronizationContext has been set to null by DiscoveryClientChannel before initiating the Find operation.
Microsoft-Windows-Application Server-Applications  |  5001      |  Debug        |  DataContract serialize {SurrogateType} with surrogates start.
Microsoft-Windows-Application Server-Applications  |  5002      |  Debug        |  DataContract serialize with surrogates stop.
Microsoft-Windows-Application Server-Applications  |  5003      |  Debug        |  DataContract deserialize {SurrogateType} with surrogates start.
Microsoft-Windows-Application Server-Applications  |  5004      |  Debug        |  DataContract deserialize with surrogates stop.
Microsoft-Windows-Application Server-Applications  |  5005      |  Debug        |  ImportKnownTypes start.
Microsoft-Windows-Application Server-Applications  |  5006      |  Debug        |  ImportKnownTypes stop.
Microsoft-Windows-Application Server-Applications  |  5007      |  Debug        |  DataContract resolver resolving {TypeName} start.
Microsoft-Windows-Application Server-Applications  |  5008      |  Debug        |  DataContract generate {Kind} writer for {TypeName} start.
Microsoft-Windows-Application Server-Applications  |  5009      |  Debug        |  DataContract generate writer stop.
Microsoft-Windows-Application Server-Applications  |  5010      |  Debug        |  DataContract generate {Kind} reader for {TypeName} start.
Microsoft-Windows-Application Server-Applications  |  5011      |  Debug        |  DataContract generation stop.
Microsoft-Windows-Application Server-Applications  |  5012      |  Debug        |  Json generate {Kind} reader for {TypeName} start.
Microsoft-Windows-Application Server-Applications  |  5013      |  Debug        |  Json reader generation stop.
Microsoft-Windows-Application Server-Applications  |  5014      |  Debug        |  Json generate {Kind} writer for {TypeName} start.
Microsoft-Windows-Application Server-Applications  |  5015      |  Debug        |  Json generate writer stop.
Microsoft-Windows-Application Server-Applications  |  5016      |  Debug        |  Generate Xml serializable for '{DCType}' start.
Microsoft-Windows-Application Server-Applications  |  5017      |  Debug        |  Generate Xml serializable stop.
Microsoft-Windows-Application Server-Applications  |  5203      |  Debug        |  JsonMessageEncoder started decoding the message.
Microsoft-Windows-Application Server-Applications  |  5204      |  Debug        |  JsonMessageEncoder started encoding the message.
Microsoft-Windows-Application Server-Applications  |  5402      |  Debug        |  SecurityToken (type '{tokenType}' and id '{tokenID}') validation started.
Microsoft-Windows-Application Server-Applications  |  5403      |  Debug        |  SecurityToken (type '{tokenType}' and id '{tokenID}') validation succeeded.
Microsoft-Windows-Application Server-Applications  |  5404      |  Debug        |  SecurityToken (type '{tokenType}' and id '{tokenID}') validation failed. {errorMessage}
Microsoft-Windows-Application Server-Applications  |  5405      |  Debug        |  Retrieval of issuer name:{issuerName} from tokenId:{tokenID} succeeded.
Microsoft-Windows-Application Server-Applications  |  5406      |  Debug        |  Retrieval of issuer name from tokenId:{tokenID} failed.
Microsoft-Windows-Application Server-Applications  |  5600      |  Debug        |  Federation message processing started.
Microsoft-Windows-Application Server-Applications  |  5601      |  Debug        |  Federation message processing succeeded.
Microsoft-Windows-Application Server-Applications  |  5602      |  Debug        |  Creating federation message from form post started.
Microsoft-Windows-Application Server-Applications  |  5603      |  Debug        |  Creating federation message from form post succeeded.
Microsoft-Windows-Application Server-Applications  |  5604      |  Debug        |  Reading session token from session cookie started.
Microsoft-Windows-Application Server-Applications  |  5605      |  Debug        |  Reading session token from session cookie succeeded.
Microsoft-Windows-Application Server-Applications  |  5606      |  Debug        |  Principal setting from session token started.
Microsoft-Windows-Application Server-Applications  |  5607      |  Debug        |  Principal setting from session token succeeded.
Microsoft-Windows-Application Server-Applications  |  39456     |  Debug        |  Size of tracking record {RecordNumber} exceeds maximum allowed by the ETW session for provider {ProviderId}
Microsoft-Windows-Application Server-Applications  |  39457     |  Debug        |  Tracking Record {data1} raised to {data2}.
Microsoft-Windows-Application Server-Applications  |  39458     |  Debug        |  Truncated tracking record {RecordNumber} written to ETW session with provider {ProviderId}. Variables/annotations/user data have been removed
Microsoft-Windows-Application Server-Applications  |  39459     |  Debug        |  Tracking data {Data} extracted in activity {Activity}.
Microsoft-Windows-Application Server-Applications  |  39460     |  Debug        |  The extracted argument/variable '{name}' is not serializable.
Microsoft-Windows-Application Server-Applications  |  57393     |  Debug        |  AppDomain unloading. AppDomain.FriendlyName {appdomainName}, ProcessName {processName}, ProcessId {processId}.
Microsoft-Windows-Application Server-Applications  |  57394     |  Analytic     |  Handling an exception.  Exception details: {data1}
Microsoft-Windows-Application Server-Applications  |  57395     |  Analytic     |  An unexpected failure occurred. Applications should not attempt to handle this error. For diagnostic purposes, this English message is associated with the failure: {data1}.
Microsoft-Windows-Application Server-Applications  |  57396     |  Analytic     |  Throwing an exception. Source: {data1}. Exception details: {data2}
Microsoft-Windows-Application Server-Applications  |  57397     |  Operational  |  Unhandled exception.  Exception details: {data1}
Microsoft-Windows-Application Server-Applications  |  57398     |  Analytic     |  The system hit the limit set for throttle 'MaxConcurrentInstances'. Limit for this throttle was set to {limit}. Throttle value can be changed by modifying attribute 'maxConcurrentInstances' in serviceThrottle element or by modifying 'MaxConcurrentInstances' property on behavior ServiceThrottlingBehavior.
Microsoft-Windows-Application Server-Applications  |  57399     |  Debug        |  Wrote to the EventLog.
Microsoft-Windows-Application Server-Applications  |  57400     |  Debug        |  Wrote to the EventLog.
Microsoft-Windows-Application Server-Applications  |  57401     |  Debug        |  Wrote to the EventLog.
Microsoft-Windows-Application Server-Applications  |  57402     |  Debug        |  Wrote to the EventLog.
Microsoft-Windows-Application Server-Applications  |  57403     |  Debug        |  Wrote to the EventLog.
Microsoft-Windows-Application Server-Applications  |  57404     |  Analytic     |  Handling an exception. Exception details: {data1}
Microsoft-Windows-Application Server-Applications  |  57405     |  Operational  |  Handling an exception. Exception details: {data1}
Microsoft-Windows-Application Server-Applications  |  57406     |  Analytic     |  Handling an exception  Exception details: {data1}
Microsoft-Windows-Application Server-Applications  |  57407     |  Analytic     |  Throwing an exception. Source: {data1}. Exception details: {data2}
Microsoft-Windows-Application Server-Applications  |  57408     |  Operational  |  Unhandled exception. Exception details: {data1}
Microsoft-Windows-Application Server-Applications  |  57409     |  Analytic     |  Throwing an exception. Source: {data1}. Exception details: {data2}
Microsoft-Windows-Application Server-Applications  |  57410     |  Analytic     |  Throwing an exception. Source: {data1}. Exception details: {data2}
Microsoft-Windows-Application Server-Applications  |  62326     |  Debug        |  The url '{data1}' hosts XAML document with root element type '{data2}'. The HTTP handler type '{data3}' is picked to serve all the requests made to this url.