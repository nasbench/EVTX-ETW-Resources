Provider                        |  Event ID  |  Channel                    |  Message
--------------------------------|------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-TunnelDriver  |  1000      |  Tunnel Driver Etw Channel  |  Tunnel Driver of type {TunnelType} successfully initialized with index {Index}.
Microsoft-Windows-TunnelDriver  |  1001      |  Tunnel Driver Etw Channel  |  Tunnel Driver of type {TunnelType} could not initialize. Windows Status Code {ErrorCode}, Tunnel Status Code {TunnelReasonCode}.
Microsoft-Windows-TunnelDriver  |  1002      |  Tunnel Driver Etw Channel  |  Tunnel Driver Load: {TunnelType}. Status {ErrorCode}
Microsoft-Windows-TunnelDriver  |  1003      |  Tunnel Driver Etw Channel  |  Tunnel Updated flag for Interface with index {Interface Index}, interface forwarding is{Forwarding}set, weakhostreceive is{WeakHostReceive}set.
Microsoft-Windows-TunnelDriver  |  1004      |  Tunnel Driver Etw Channel  |  Tunnel received packet with incomplete inner IP header
Microsoft-Windows-TunnelDriver  |  1005      |  Tunnel Driver Etw Channel  |  Could not find tunnel interface for packet.
Microsoft-Windows-TunnelDriver  |  1006      |  Tunnel Driver Etw Channel  |  Packet filter on tunnel interface {Interface Index} is off. Dropping Packet.
Microsoft-Windows-TunnelDriver  |  1007      |  Tunnel Driver Etw Channel  |  Packet failed integrity check on interface type {TunnelType} with index {Interface Index}.
Microsoft-Windows-TunnelDriver  |  1008      |  Tunnel Driver Etw Channel  |  Non IPv6 Packet received on interface {Interface Index}.
Microsoft-Windows-TunnelDriver  |  1009      |  Tunnel Driver Etw Channel  |  Could not find tunnel interface for truncated ICMP message.
Microsoft-Windows-TunnelDriver  |  1010      |  Tunnel Driver Etw Channel  |  Could not find the source of the ICMP message on tunnel interface {Interface Index}.
Microsoft-Windows-TunnelDriver  |  1011      |  Tunnel Driver Etw Channel  |  Failed to copy Buffer into MDL while generating ICMPv6 message on tunnel interface {Interface Index}.
Microsoft-Windows-TunnelDriver  |  1012      |  Tunnel Driver Etw Channel  |  Completing the pause for tunnel interface {Interface Index}.
Microsoft-Windows-TunnelDriver  |  1013      |  Tunnel Driver Etw Channel  |  Completing power notification for tunnel interface {Interface Index}.
Microsoft-Windows-TunnelDriver  |  1014      |  Tunnel Driver Etw Channel  |  Tunnel interface {Interface Index} has media status set to {Media Status}.
Microsoft-Windows-TunnelDriver  |  1015      |  Tunnel Driver Etw Channel  |  Tunnel interface {Interface Index} {ReadError} could not be read.NDIS returned status {ErrorCode}.
Microsoft-Windows-TunnelDriver  |  1016      |  Tunnel Driver Etw Channel  |  Tunnel interface {Index} has unknown type {TunnelType}.
Microsoft-Windows-TunnelDriver  |  1017      |  Tunnel Driver Etw Channel  |  Tunnel interface of type {TunnelType} with index {Index} has been {Interface Operation}.
Microsoft-Windows-TunnelDriver  |  1018      |  Tunnel Driver Etw Channel  |  Teredo Tunnel offload {Teredo Flow Tuple} flow entry freed.
Microsoft-Windows-TunnelDriver  |  1019      |  Tunnel Driver Etw Channel  |  Teredo WFP receive path worker has NULL clone list.
Microsoft-Windows-TunnelDriver  |  1020      |  Tunnel Driver Etw Channel  |  Skipped offload flow creation for non-Teredo address pair.Local {Local Ipv6 Address} Remote {Remote IPv6 Address}.
Microsoft-Windows-TunnelDriver  |  1021      |  Tunnel Driver Etw Channel  |  Teredo Wfp created IPv4 flow with following parameters.LocalV4:{Source IPv4 Address} RemoteV4:{Destination IPv4 Address} LocalPort:{Source Port} RemotePort:{Destination Port}.
Microsoft-Windows-TunnelDriver  |  1022      |  Tunnel Driver Etw Channel  |  Teredo Wfp registration occured with status {NT Status}.
Microsoft-Windows-TunnelDriver  |  1023      |  Tunnel Driver Etw Channel  |  Teredo Wfp created V6 flow with status {NT Status} following parameters.LocalV4:{Local IPv4 Address} RemoteV4:{Remote IPv4 Address} LocalV6:{Local IPv6} RemoteV6:{Remote IPv6}.
Microsoft-Windows-TunnelDriver  |  1024      |  Tunnel Driver Etw Channel  |  Tunnel type {TunnelType} with index {Tunnel Interface Index} has IPv4 address {IPv4 Address} now {Yes or No} associated with physical interface with index {Interface Index}.
Microsoft-Windows-TunnelDriver  |  1025      |  Tunnel Driver Etw Channel  |  Tunnel type {TunnelType} offloaded {Offloaded Nbl Count} NBLs, Could not offload {Returned Nbl Count} NBLs
Microsoft-Windows-TunnelDriver  |  1026      |  Tunnel Driver Etw Channel  |  Tunnel Type {TunnelType} with index {Interface Index} is in an invalid device state such as not opened or being closed.{Dropped Nbl Count} NBLs could not be sent.
Microsoft-Windows-TunnelDriver  |  1027      |  Tunnel Driver Etw Channel  |  Teredo tunnel callout wasn't allowed to modify a packet. PID: {Process ID}. FilterID: {Filter ID}. Flow handle {Flow Handle}.