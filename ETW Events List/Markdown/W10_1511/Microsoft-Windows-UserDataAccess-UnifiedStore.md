Provider                                       |  Event ID  |  Channel  |  Message
-----------------------------------------------|------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-UserDataAccess-UnifiedStore  |  1         |           |  Error: {P1_HResult} Location: {P2_String} Line Number: {P3_UInt32}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  2         |           |  Error Propagated: {P1_HResult} Location: {P2_String} Line Number: {P3_UInt32}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  101       |           |  Error: {P1_HResult} Location: {P2_String} Line Number: {P3_UInt32}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  102       |           |  Error Propagated: {P1_HResult} Location: {P2_String} Line Number: {P3_UInt32}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  1000      |           |
Microsoft-Windows-UserDataAccess-UnifiedStore  |  2000      |           |  Tombstone cleanup completed: store [{Arg1}], iterations [{Arg2}], duration [{Arg3} s]
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3000      |           |
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3001      |           |  Unified store lock was held for {Prop_UInt64} seconds. ReleaseFunc = {Prop_Hex_UInt32}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3002      |           |  Unified store lock type {Arg1} was not released even after {Arg2} seconds. Lock Owner Process Id: {Arg3}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3003      |           |  CeSeekDatabaseEx failed, Handle: {Prop_Handle}, HR: {Prop_HRESULT} SeekType: {Prop_UINT}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3004      |           |  CeWriteRecordProps failed, Handle: {Prop_Handle}, HR: {Prop_HRESULT}, OIDRecord: {Prop_UINT}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3005      |           |  CeReadRecordPropsEx failed, Handle: {Prop_Handle}, HR: {Prop_HRESULT}, Flags: {Prop_UINT}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3006      |           |  Closed handle before refcount was 0, Handle: {Prop_Handle}, Outstanding refCount: {Prop_INT}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3007      |           |
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3009      |           |  Mutex acquire failed, WaitResult = {Prop_UInt32}, HR = {Prop_Hex_UInt32}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3010      |           |  Deserialize Knowledge failed, HR = {Prop_ErrorCode}, cbKnowledge = {Prop_FullKnowledgeSize}, cbKnowledgeLogged = {Prop_LoggedKnowledgeSize}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3011      |           |  Opening Table {Prop_UInt32} without any index.
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3012      |           |  Restriction Type = {Prop_UInt32}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3013      |           |  PropertyRestriction: Operation {Prop_Prop1}, Property id {Prop_Prop2}.
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3014      |           |  BitMaskRestriction: Operation {Prop_Prop1}, Property id {Prop_Prop2}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3015      |           |  Seeked and read {Prop_UInt32} rows before finding row with matching index
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3016      |           |  Count {Count}: Property ids: {Array}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3017      |           |  MountDeviceVolume Error: {P1_HResult}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3018      |           |  Remote notification dispatched, Event type: {Prop_Handle}, Object type: {Prop_HRESULT}, Object Id: {Prop_UINT}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3019      |           |  Remote notification published, Event type: {Prop_Handle}, Object type: {Prop_HRESULT}, Object Id: {Prop_UINT}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3020      |           |
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3021      |           |  UnifiedStore delete store id = {Prop_UInt32}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3022      |           |  UnifiedStore delete folder types = {Prop_Handle}, store = {Prop_HRESULT}, id = {Prop_UINT}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3023      |           |  Table: {Prop_Trace_UnicodeString}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3024      |           |  Failed to commit transaction, attempting rollback recovery (error {Prop_Prop1}, session {Prop_Prop2})
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3025      |           |  Failed to rollback transaction (error {Prop_Prop1}, session {Prop_Prop2})
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3026      |           |  Recovery complete (error {Prop_Prop1}, session {Prop_Prop2})
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3027      |           |
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3028      |           |  Unified Store RPC Call: {Function}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3029      |           |  Failed to set property ID {Prop_Prop1}, error {Prop_Prop2}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3030      |           |  Process {Prop_Prop1} underflowed its suspend/resume count, now is {Prop_Prop2}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3031      |           |  Process {Prop_Prop1} suspended its message queue, count {Prop_Prop2}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3032      |           |  Process {Prop_Prop1} resumed its message queue, count {Prop_Prop2}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3033      |           |  Process with rundown identifier {Prop_Prop1} aborted {Prop_Prop2} transactions
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3034      |           |  Client process {Prop_Prop} has lost events
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3035      |           |  Client process {Prop_Prop} has resumed fetching events
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3036      |           |  Property should be added in schema. table: {Prop_Prop1}, id: {Prop_Prop2}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3037      |           |  Advisee in service process (vtable {Function}) has lost events
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3038      |           |
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3039      |           |  Final transaction rollback attempt failed, Error: {P1_HResult}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3040      |           |  Closing active table id: {Prop_Prop}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3041      |           |
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3042      |           |
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3043      |           |  Unified store process identifier {Prop_Prop} created for process
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3044      |           |  Process exit callback for process with identifier {Prop_Prop}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3045      |           |  Unified store rundown for process {Prop_Prop1} with identifier {Prop_Prop2}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3046      |           |  Store id: {Prop_Prop1} Supported Types changed to: {Prop_Prop2}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3047      |           |  DBSession::_UpgradeDatabase Error: {P1_HResult}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3048      |           |  JetAttachDatabase Error: {P1_HResult}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3049      |           |  Upgrading database, lcidChanged: {Prop_Handle}, storeVersionChanged: {Prop_HRESULT}, isIndexCorrupt: {Prop_UINT}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3050      |           |  Creating Missing indexes, table ID: {Prop_Prop1}, count: {Prop_Prop2}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3051      |           |  Number of indexes changed unexpectedly, table ID: {Prop_Prop1}, numExistingIndex: {Prop_Prop2}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3070      |           |  Attempting to defragment scope knowledge. Partner id: {Arg1}, scope id: {Arg2}, exceptions: {Arg3} positive and {Arg4} negative, min vector size: {Arg5}, max vector size: {Arg6}, starting tick count: {Arg7}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3071      |           |  Defragmented scope knowledge. Partner id: {Arg1}, scope id: {Arg2}, original size: {Arg3}, defragmented size: {Arg4}, exceptions: {Arg5}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3072      |           |  Done defragmenting scope knowledge. Partner id: {Arg1}, scope id: {Arg2}, succeeded: {Arg3}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3073      |           |  Attempting to defragment partner knowledge. Partner id: {Arg1}, size: {Arg2}, defragmentation threshold: {Arg3}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3074      |           |  The knowldege for partner id {Arg1} has {Arg2} scopes, {Arg3} positive exceptions, {Arg4} negative exceptions, min vector size: {Arg5} and max vector size: {Arg6}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3075      |           |  Successfully defragmented {Arg2} scopes out of {Arg3} for partner id {Arg1}.
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3076      |           |  Defragmented partner knowledge. Partner id: {Arg1}, original size: {Arg2}, defragmented size: {Arg3}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3077      |           |  Done defragmenting partner knowledge. Partner id: {Arg1}, succeeded: {Arg2}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3078      |           |  Failed to reduce the knowledge size for partner id {Arg1} below {Arg2}%% of the maximum size (size: {Arg2}, maximum size: {Arg4}).
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3079      |           |  The knowledge size for partner id {Arg1} exceeds {Arg3}%% of the maximum size (size: {Arg2}, maximum size: {Arg4}). The synchronization may exhibit degraded performance
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3080      |           |  The knowledge size for partner id {Arg1} exceeds {Arg3}%% of the maximum size (size: {Arg2}, maximum size: {Arg4}). The synchronization may start failing if the knowledge size keeps increasing
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3081      |           |  The knowledge size for partner id {Arg1} exceeds the maximum size (size: {Arg2}, maximum size: {Arg3}). The synchronization will fail
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3100      |           |  Closing stale notify context {Handle} on behalf of rundown id {Rundown}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3101      |           |  Closing stale object {Handle} on behalf of rundown id {Rundown}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3110      |           |  [store upgrade] The current store version is {Prop_Prop}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3112      |           |  [store upgrade] Performing upgrade task {TaskType}
Microsoft-Windows-UserDataAccess-UnifiedStore  |  3113      |           |  [store upgrade] {Prop_Prop} appointments updated
Microsoft-Windows-UserDataAccess-UnifiedStore  |  4001      |           |
Microsoft-Windows-UserDataAccess-UnifiedStore  |  4002      |           |