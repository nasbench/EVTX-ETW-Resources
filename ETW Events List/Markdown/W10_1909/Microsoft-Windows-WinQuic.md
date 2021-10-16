Provider                   |  Event ID  |  Channel  |  Message
---------------------------|------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-WinQuic  |  1         |           |  [conn][{Connection}] Begin, IsServer={IsServer}
Microsoft-Windows-WinQuic  |  2         |           |  [conn][{Connection}] End
Microsoft-Windows-WinQuic  |  3         |           |  [conn][{Connection}] Handshake complete
Microsoft-Windows-WinQuic  |  4         |           |  [conn][{Connection}] Scheduling: {State}
Microsoft-Windows-WinQuic  |  5         |           |  [conn][{Connection}] Execute: {Type}
Microsoft-Windows-WinQuic  |  6         |           |  [conn][{Connection}] Execute: {Type}
Microsoft-Windows-WinQuic  |  7         |           |  [conn][{Connection}] Execute: {Type}
Microsoft-Windows-WinQuic  |  100       |           |  [strm][{Stream}] Begin, Conn={Connection} ID={ID}
Microsoft-Windows-WinQuic  |  101       |           |  [strm][{Stream}] End
Microsoft-Windows-WinQuic  |  1000      |           |  [conn][{Connection}] FS: BytesSent={BytesSent} InFlight={BytesInFlight} InFlightMax={BytesInFlightMax} CWnd={CongestionWindow} SSThresh={SlowStartThreshold} InRecov={IsInRecovery} ConnFC={ConnectionFlowControl} StreamFC={StreamFlowControl} ISB={Connection}0 PostedBytes={Connection}1 SRtt={Connection}2
Microsoft-Windows-WinQuic  |  1001      |           |  [conn][{Connection}] BLOCKED: {Reason}
Microsoft-Windows-WinQuic  |  1002      |           |  [conn][{Connection}] UNBLOCKED: {Reason}
Microsoft-Windows-WinQuic  |  1003      |           |  [strm][{Stream}] BLOCKED: {Reason}
Microsoft-Windows-WinQuic  |  1004      |           |  [strm][{Stream}] UNBLOCKED: {Reason}
Microsoft-Windows-WinQuic  |  1005      |           |  [conn][{Connection}] CUBIC: SlowStartThreshold={SlowStartThreshold} K={K} WindowMax={WindowMax} WindowLastMax={WindowLastMax}
Microsoft-Windows-WinQuic  |  1006      |           |  [conn][{Connection}] Congestion Event