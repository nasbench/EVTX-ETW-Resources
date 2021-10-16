Provider                              |  Event ID  |  Channel                                          |  Message
--------------------------------------|------------|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-NDIS-PacketCapture  |  1001      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |  Packet Fragment ({FragmentSize} bytes), MiniportIfIndex {MiniportIfIndex}, LowerIfIndex {LowerIfIndex}
Microsoft-Windows-NDIS-PacketCapture  |  1002      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |  Packet Metadata ({MetadataSize} bytes)
Microsoft-Windows-NDIS-PacketCapture  |  1003      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |  VMSwitch Packet Fragment ({FragmentSize} bytes), MiniportIfIndex {MiniportIfIndex}, LowerIfIndex {LowerIfIndex}
Microsoft-Windows-NDIS-PacketCapture  |  1011      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |  Capture Rules Count={RulesCount}
Microsoft-Windows-NDIS-PacketCapture  |  1012      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |  Driver Loaded (FriendlyName={FriendlyName} UniqueName={UniqueName} ServiceName={ServiceName})
Microsoft-Windows-NDIS-PacketCapture  |  1013      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |  Driver Unloaded (FriendlyName={FriendlyName} UniqueName={UniqueName} ServiceName={ServiceName})
Microsoft-Windows-NDIS-PacketCapture  |  1014      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |  Attached to miniport interface {MiniportIfIndex} above layer interface {LowerIfIndex} with media type {MediaType} (context={ReferenceContext})
Microsoft-Windows-NDIS-PacketCapture  |  1015      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |  Detached from miniport interface {MiniportIfIndex} above layer interface {LowerIfIndex} with media type {MediaType} (context={ReferenceContext})
Microsoft-Windows-NDIS-PacketCapture  |  1016      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |  Capture Rule: Id={RuleId} Directive={Directive} ValueLength={Length} Value={Value}
Microsoft-Windows-NDIS-PacketCapture  |  2001      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |  Driver load failed with status={ErrorCode} at location {Location}
Microsoft-Windows-NDIS-PacketCapture  |  2002      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |  FilterAttach failed with status={ErrorCode} at location {Location} (context={Context})
Microsoft-Windows-NDIS-PacketCapture  |  2003      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |  Received Invalid Capture Rule: Id={RuleId} Directive={Directive} ValueLength={Length} Value={Value}
Microsoft-Windows-NDIS-PacketCapture  |  3001      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |  Entering state '{NextState}' from state '{PreviousState}' (location={Location}, context={Context})
Microsoft-Windows-NDIS-PacketCapture  |  3002      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |  Entering state '{NextState}' from state '{PreviousState}' (location={Location}, context={Context})
Microsoft-Windows-NDIS-PacketCapture  |  5000      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |
Microsoft-Windows-NDIS-PacketCapture  |  5001      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |
Microsoft-Windows-NDIS-PacketCapture  |  5002      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |
Microsoft-Windows-NDIS-PacketCapture  |  5003      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |
Microsoft-Windows-NDIS-PacketCapture  |  5100      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |  Rundown: {SourceId}: {RundownId} - {Param1}, {Param2}, {ParamStr}. {Description}.
Microsoft-Windows-NDIS-PacketCapture  |  5101      |  Microsoft-Windows-NDIS-PacketCapture/Diagnostic  |  Event source: {SourceId}: {SourceName}, IfIndex: {IfIndex}, LayerCount: {LayerCount}.