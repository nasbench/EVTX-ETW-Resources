Provider                     |  Event ID  |  Channel                                 |  Message
-----------------------------|------------|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-QoS-Pacer  |  1         |  Microsoft-Windows-QoS-Pacer/Diagnostic  |  Create {FlowType} at {SendSpec.TokenRate} bytes/sec with status {Status}
Microsoft-Windows-QoS-Pacer  |  1         |  Microsoft-Windows-QoS-Pacer/Diagnostic  |  PACER: Flow created with status {Status} (type={FlowType}, rate={SendSpec.TokenRate}Bps, service={SendSpec.ServiceType}, dscp={Status}1, 802.1p={Status}2, system={Status}5)
Microsoft-Windows-QoS-Pacer  |  2         |  Microsoft-Windows-QoS-Pacer/Diagnostic  |  Update {FlowType} from {OldSendSpec.TokenRate} to {Status}1 with status {Status}
Microsoft-Windows-QoS-Pacer  |  2         |  Microsoft-Windows-QoS-Pacer/Diagnostic  |  PACER: Flow updated with status {Status} (rate={SendSpec.TokenRate}Bps, service={SendSpec.ServiceType}, dscp={Status}1, 802.1p={Status}2)
Microsoft-Windows-QoS-Pacer  |  3         |  Microsoft-Windows-QoS-Pacer/Diagnostic  |  Start Pacer on NetLuid={NetLuid} ({FriendlyName})
Microsoft-Windows-QoS-Pacer  |  3         |  Microsoft-Windows-QoS-Pacer/Diagnostic  |  PACER: Starting adapter {FriendlyName} (luid={NetLuid})
Microsoft-Windows-QoS-Pacer  |  4         |  Microsoft-Windows-QoS-Pacer/Diagnostic  |  Stop Pacer on NetLuid={NetLuid} ({FriendlyName})
Microsoft-Windows-QoS-Pacer  |  4         |  Microsoft-Windows-QoS-Pacer/Diagnostic  |  PACER: Stopping adapter {FriendlyName} (luid={NetLuid})
Microsoft-Windows-QoS-Pacer  |  5         |  Microsoft-Windows-QoS-Pacer/Diagnostic  |  Update {FlowType} from {OldSendSpec.TokenRate} to {FlowType}0
Microsoft-Windows-QoS-Pacer  |  6         |  Microsoft-Windows-QoS-Pacer/Diagnostic  |  PACER: Flow deleted (dropped={DroppedPackets}, scheduled={PacketsScheduled}/{BytesScheduled}, transmitted={PacketsTransmitted}/{BytesTransmitted}, nbl={NblComplete}/{NblSent})
Microsoft-Windows-QoS-Pacer  |  7         |  Microsoft-Windows-QoS-Pacer/Diagnostic  |  PACER: Packet dropped, reason={DropReason}
Microsoft-Windows-QoS-Pacer  |  8         |  Microsoft-Windows-QoS-Pacer/Diagnostic  |  PACER: Non-conformance marking, dscp={DsClass}, 802.1p={TrafficClass}, WMM={Wmm}
Microsoft-Windows-QoS-Pacer  |  9         |  Microsoft-Windows-QoS-Pacer/Diagnostic  |  PACER: Application-based DSCP marking policy state={Allow}
Microsoft-Windows-QoS-Pacer  |  10        |  Microsoft-Windows-QoS-Pacer/Diagnostic  |  PACER: Packet rescheduled (eligible={IneligibleCount}/{TotalCount}, first-delta={IneligibleFirstDelta}, last-delta={IneligibleLastDelta})