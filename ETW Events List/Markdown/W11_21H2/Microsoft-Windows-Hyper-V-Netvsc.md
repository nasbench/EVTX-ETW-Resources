Provider                          |  Event ID  |  Channel                                      |  Message
----------------------------------|------------|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-Hyper-V-Netvsc  |  1         |  System                                       |  The VM and host networking components successfully negotiated protocol version '{Version}'
Microsoft-Windows-Hyper-V-Netvsc  |  2         |  System                                       |  The VM and host networking components failed to negotiate protocol version '{Version}'
Microsoft-Windows-Hyper-V-Netvsc  |  3         |  System                                       |  The miniport '{MiniportName}' was successfully initialized
Microsoft-Windows-Hyper-V-Netvsc  |  4         |  System                                       |  Failed to initialize miniport '{MiniportName}', Status = '{Status}'
Microsoft-Windows-Hyper-V-Netvsc  |  5         |  System                                       |  Failed to set config parameters on miniport NIC '{MiniportName}', Status = '{Status}'
Microsoft-Windows-Hyper-V-Netvsc  |  6         |  System                                       |  Miniport NIC '{MiniportName}' is halting
Microsoft-Windows-Hyper-V-Netvsc  |  7         |  System                                       |  Miniport NIC '{MiniportName}' reset
Microsoft-Windows-Hyper-V-Netvsc  |  8         |  System                                       |  Miniport NIC '{MiniportName}' hung
Microsoft-Windows-Hyper-V-Netvsc  |  9         |  System                                       |  Miniport NIC '{MiniportName}' halted
Microsoft-Windows-Hyper-V-Netvsc  |  10        |  System                                       |  Miniport NIC '{MiniportName}' paused
Microsoft-Windows-Hyper-V-Netvsc  |  11        |  System                                       |  Miniport NIC '{MiniportName}' restarted
Microsoft-Windows-Hyper-V-Netvsc  |  12        |  System                                       |  Miniport NIC '{MiniportName}' connected
Microsoft-Windows-Hyper-V-Netvsc  |  13        |  System                                       |  Miniport NIC '{MiniportName}' disconnected
Microsoft-Windows-Hyper-V-Netvsc  |  14        |  System                                       |  Miniport NIC '{MiniportName}' network has changed
Microsoft-Windows-Hyper-V-Netvsc  |  15        |  System                                       |  Failed to initialize microport for miniport '{MiniportName}', Status = '{Status}'
Microsoft-Windows-Hyper-V-Netvsc  |  16        |  Microsoft-Windows-Hyper-V-NETVSC/Diagnostic  |  NBL {Operation} miniport NIC '{MiniportName}' is dropped. Reason: {DropReason}. Status - {Status}.
Microsoft-Windows-Hyper-V-Netvsc  |  17        |  Microsoft-Windows-Hyper-V-NETVSC/Diagnostic  |  Failed to send packet at the microport. Reason: {DropReason}. Status - {Status}.
Microsoft-Windows-Hyper-V-Netvsc  |  18        |  Microsoft-Windows-Hyper-V-NETVSC/Diagnostic  |  NBL {Pointer} CorrelationID {CorrelationId} on IfIndex {IfIndex} direction {Direction} dropped reason {DropReason} status {Status}
Microsoft-Windows-Hyper-V-Netvsc  |  19        |  Microsoft-Windows-Hyper-V-NETVSC/Diagnostic  |  NBL {Pointer} CorrelationID {CorrelationId} on IfIndex {IfIndex} direction {Direction} Synthetic
Microsoft-Windows-Hyper-V-Netvsc  |  20        |  Microsoft-Windows-Hyper-V-NETVSC/Diagnostic  |  NBL {Pointer} CorrelationID {CorrelationId} on IfIndex {IfIndex} direction {Direction} VF
Microsoft-Windows-Hyper-V-Netvsc  |  34        |  System                                       |  PD initialization succeeded.
Microsoft-Windows-Hyper-V-Netvsc  |  35        |  System                                       |  PD initialization failed.
Microsoft-Windows-Hyper-V-Netvsc  |  36        |  System                                       |  PD cleanup succeeded.
Microsoft-Windows-Hyper-V-Netvsc  |  37        |  System                                       |  Open NDK adapter failed on Miniport '{MiniportName}'. FailureReason: {failureReason} Status: {Status}.
Microsoft-Windows-Hyper-V-Netvsc  |  38        |  System                                       |  NDK PnP event failed. PnPEvent: {NetEvent} Miniport: '{MiniportName}' FailureReason: {failureReason} Status: {Status}.
Microsoft-Windows-Hyper-V-Netvsc  |  39        |  System                                       |  VF adapter bind failed. FailureReason: {failureReason} MsgStatus: {Status}.
Microsoft-Windows-Hyper-V-Netvsc  |  40        |  System                                       |  Task, {Task}, failed because of low memory. {MemoryRequired} bytes of memory was required
Microsoft-Windows-Hyper-V-Netvsc  |  41        |  System                                       |  Sending Interface Index (IfIndex {IfIndex})of RNDIS miniport '{MiniportName}' to VF adapter '{VfAdapterName}' succeeded.
Microsoft-Windows-Hyper-V-Netvsc  |  42        |  System                                       |  Sending Interface Index (IfIndex {IfIndex})of RNDIS miniport '{MiniportName}' to VF adapter '{VfAdapterName}' failed. Status = {Status}. RequestHandled = {RequestHandled}. RDMA cannot be enabled on the adapter
Microsoft-Windows-Hyper-V-Netvsc  |  43        |  System                                       |  NDK PnP event succeeded. PnPEvent: {NetEvent} Miniport: '{MiniportName}'
Microsoft-Windows-Hyper-V-Netvsc  |  44        |  System                                       |  Miniport '{MiniportName}' reported NDK capabilities. Operation NDK enabled - {NdkEnabled}.
Microsoft-Windows-Hyper-V-Netvsc  |  45        |  System                                       |  Miniport '{MiniportName}' failed to report NDK capabilities. Operation NDK enabled - {NdkEnabled}.
Microsoft-Windows-Hyper-V-Netvsc  |  46        |  System                                       |  VF adapter '{VfAdapterName}' did not report NDK capabilities.
Microsoft-Windows-Hyper-V-Netvsc  |  47        |  System                                       |  VF adapter '{VfAdapterName}' reported NDK capabilities in enabled operational state.
Microsoft-Windows-Hyper-V-Netvsc  |  48        |  System                                       |  VF adapter '{VfAdapterName}' reported NDK capabilities in disabled operational state.
Microsoft-Windows-Hyper-V-Netvsc  |  49        |  System                                       |  A VF connection failed due to isolated VM restriction. Status: {Status}