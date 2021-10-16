Provider                           |  Event ID  |  Channel                                        |  Message
-----------------------------------|------------|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-WLAN-AutoConfig  |  4000      |  System                                         |  WLAN AutoConfig service has successfully started.
Microsoft-Windows-WLAN-AutoConfig  |  4001      |  System                                         |  WLAN AutoConfig service has successfully stopped.
Microsoft-Windows-WLAN-AutoConfig  |  4002      |  System                                         |  WLAN AutoConfig service has failed to start.Error Code: {ErrorCode}
Microsoft-Windows-WLAN-AutoConfig  |  4003      |  System                                         |  WLAN AutoConfig detected limited connectivity, attempting automatic recovery.Recovery Type: {Event}Error Code: {ErrorCode}Trigger Reason: {ChangeReason}IP Family: {IpFamily}
Microsoft-Windows-WLAN-AutoConfig  |  8000      |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  WLAN AutoConfig service started a connection to a wireless network.Network Adapter: {InterfaceDescription}Interface GUID: {InterfaceGuid}Connection Mode: {ConnectionMode}Profile Name: {ProfileName}SSID: {SSID}BSS Type: {BSSType}
Microsoft-Windows-WLAN-AutoConfig  |  8001      |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  WLAN AutoConfig service has successfully connected to a wireless network.Network Adapter: {InterfaceDescription}Interface GUID: {InterfaceGuid}Connection Mode: {ConnectionMode}Profile Name: {ProfileName}SSID: {SSID}BSS Type: {BSSType}PHY Type: {PHYType}Authentication: {AuthenticationAlgorithm}Encryption: {CipherAlgorithm}802.1x Enabled: {InterfaceGuid}0Hidden: {InterfaceGuid}2
Microsoft-Windows-WLAN-AutoConfig  |  8002      |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  WLAN AutoConfig service failed to connect to a wireless network.Network Adapter: {InterfaceDescription}Interface GUID: {InterfaceGuid}Connection Mode: {ConnectionMode}Profile Name: {ProfileName}SSID: {SSID}BSS Type: {BSSType}Failure Reason:{FailureReason}RSSI: {InterfaceGuid}0
Microsoft-Windows-WLAN-AutoConfig  |  8003      |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  WLAN AutoConfig service has successfully disconnected from a wireless network.Network Adapter: {InterfaceDescription}Interface GUID: {InterfaceGuid}Connection Mode: {ConnectionMode}Profile Name: {ProfileName}SSID: {SSID}BSS Type: {BSSType}Reason: {Reason}
Microsoft-Windows-WLAN-AutoConfig  |  8004      |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Wireless network is blocked due to connection failure.Network Adapter: {InterfaceDescription}Interface GUID: {InterfaceGuid}Connection Mode: {ConnectionMode}Profile Name: {ProfileName}SSID(s): {SSID(s)}BSS Type: {BSSType}Failure Reason:{FailureReason}Length of block timer (minutes): {BlockTime}
Microsoft-Windows-WLAN-AutoConfig  |  8005      |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  WLAN AutoConfig service has begun starting the hosted network.Interface GUID: {InterfaceGuid}SSID: {SSID}
Microsoft-Windows-WLAN-AutoConfig  |  8006      |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  WLAN AutoConfig service has finished starting the hosted network.Interface GUID: {InterfaceGuid}SSID: {SSID}
Microsoft-Windows-WLAN-AutoConfig  |  8007      |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  WLAN AutoConfig service has failed to start the hosted network.Error Code: {ErrorCode}Error Message: {ErrorMsg}Interface GUID: {InterfaceGuid}SSID: {SSID}
Microsoft-Windows-WLAN-AutoConfig  |  8008      |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  AutoConfig service has begun to stop the hosted network.Interface GUID: {InterfaceGuid}SSID: {SSID}
Microsoft-Windows-WLAN-AutoConfig  |  8009      |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  WLAN AutoConfig service has finished stopping the hosted network.Interface GUID: {InterfaceGuid}SSID: {SSID}
Microsoft-Windows-WLAN-AutoConfig  |  8010      |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  WLAN AutoConfig service has failed to stop the hosted network.Error Code: {ErrorCode}Error Message: {ErrorMsg}Interface GUID: {InterfaceGuid}SSID: {SSID}
Microsoft-Windows-WLAN-AutoConfig  |  8011      |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Connect to last good network Network Adapter: {InterfaceDescription}Interface GUID: {InterfaceGuid} Profile Name: {ProfileName}SSID: {SSID}BSS type: {BSSType}
Microsoft-Windows-WLAN-AutoConfig  |  8012      |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  NLO discovery Network Adapter: Interface GUID: {InterfaceGuid} {InterfaceDescription}
Microsoft-Windows-WLAN-AutoConfig  |  10000     |  System                                         |  WLAN Extensibility Module has failed to start.Module Path: {ExtensibleModulePath}Error Code: {ErrorCode}
Microsoft-Windows-WLAN-AutoConfig  |  10001     |  System                                         |  WLAN Extensibility Module has successfully started.Module Path: {ExtensibleModulePath}
Microsoft-Windows-WLAN-AutoConfig  |  10002     |  System                                         |  WLAN Extensibility Module has stopped.Module Path: {ExtensibleModulePath}
Microsoft-Windows-WLAN-AutoConfig  |  10003     |  System                                         |  WLAN Extensibility Module has stopped unexpectedly.Module Path: {ExtensibleModulePath}
Microsoft-Windows-WLAN-AutoConfig  |  10004     |  System                                         |  WLAN Extensibility Module has timed out.Module Path: {ExtensibleModulePath}
Microsoft-Windows-WLAN-AutoConfig  |  11000     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Wireless network association started.Network Adapter: {Adapter}Interface GUID: {DeviceGuid}Local MAC Address: {LocalMac}Network SSID: {SSID}BSS Type: {BSSType}Authentication: {Auth}Encryption: {Cipher}802.1X Enabled: {OnexEnabled}
Microsoft-Windows-WLAN-AutoConfig  |  11001     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Wireless network association succeeded.Network Adapter: {Adapter}Interface GUID: {DeviceGuid}Local MAC Address: {LocalMac}Network SSID: {SSID}BSS Type: {BSSType}Management Frame Protection Enabled: {ConnectionId}
Microsoft-Windows-WLAN-AutoConfig  |  11002     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Wireless network association failed.Network Adapter: {Adapter}Interface GUID: {DeviceGuid}Local MAC Address: {LocalMac}Network SSID: {SSID}BSS Type: {BSSType}Failure Reason: {FailureReason}Dot11 Status Code: {Dot11StatusCode}RSSI: {Adapter}0
Microsoft-Windows-WLAN-AutoConfig  |  11003     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Wireless security started.Network Adapter: {Adapter}Interface GUID: {DeviceGuid}Local MAC Address: {LocalMac}Network SSID: {SSID}BSS Type: {BSSType}Authentication: {Auth}Encryption: {Cipher}802.1x Enabled: {Adapter}0
Microsoft-Windows-WLAN-AutoConfig  |  11004     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Wireless security stopped.Network Adapter: {Adapter}Interface GUID: {DeviceGuid}Local MAC Address: {LocalMac}Network SSID: {SSID}BSS Type: {BSSType}Security Hint: {SecurityHint}
Microsoft-Windows-WLAN-AutoConfig  |  11005     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Wireless security succeeded.Network Adapter: {Adapter}Interface GUID: {DeviceGuid}Local MAC Address: {LocalMac}Network SSID: {SSID}BSS Type: {BSSType}
Microsoft-Windows-WLAN-AutoConfig  |  11006     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Wireless security failed.Network Adapter: {Adapter}Interface GUID: {DeviceGuid}Local MAC Address: {LocalMac}Network SSID: {SSID}BSS Type: {BSSType}Peer MAC Address: {PeerMac}Reason: {ReasonText}Error: {ErrorCode}
Microsoft-Windows-WLAN-AutoConfig  |  11007     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Wireless IHV security started.Network Adapter: {Adapter}Interface GUID: {DeviceGuid}Local MAC Address: {LocalMac}Network SSID: {SSID}BSS Type: {BSSType}
Microsoft-Windows-WLAN-AutoConfig  |  11008     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Wireless IHV security succeeded.Network Adapter: {Adapter}Interface GUID: {DeviceGuid}Local MAC Address: {LocalMac}Network SSID: {SSID}BSS Type: {BSSType}
Microsoft-Windows-WLAN-AutoConfig  |  11009     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Wireless IHV security failed.Network Adapter: {Adapter}Interface GUID: {DeviceGuid}Local MAC Address: {LocalMac}Network SSID: {SSID}BSS Type: {BSSType}Peer MAC Address: {PeerMac}Reason: {IhvReasonCode}Additional Data Length: {IhvDataLength}
Microsoft-Windows-WLAN-AutoConfig  |  11010     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Wireless security started.Network Adapter: {Adapter}Interface GUID: {DeviceGuid}Local MAC Address: {LocalMac}Network SSID: {SSID}BSS Type: {BSSType}Authentication: {Auth}Encryption: {Cipher}FIPS Mode: {Adapter}0802.1x Enabled: {Adapter}1
Microsoft-Windows-WLAN-AutoConfig  |  12011     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Wireless 802.1x authentication started.Network Adapter: {Adapter}Interface GUID: {DeviceGuid}Local MAC Address: {LocalMac}Network SSID: {SSID}BSS Type: {BSSType}Eap Information: Type {EapType}, Vendor ID {VendorID}, Vendor Type {VendorType}, Author ID {AuthorID}
Microsoft-Windows-WLAN-AutoConfig  |  12012     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Wireless 802.1x authentication succeeded.Network Adapter: {Adapter}Interface GUID: {DeviceGuid}Local MAC Address: {LocalMac}Network SSID: {SSID}BSS Type: {BSSType}Identity: {Identity}User: {Domain}Domain: {Domain}
Microsoft-Windows-WLAN-AutoConfig  |  12013     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Wireless 802.1x authentication failed.Network Adapter: {Adapter}Interface GUID: {DeviceGuid}Local MAC Address: {LocalMac}Network SSID: {SSID}BSS Type: {BSSType}Peer MAC Address: {PeerMac}Identity: {Identity}User: {User}Domain: {Domain}Reason: {Adapter}0Error: {Adapter}2EAP Reason: {Adapter}3EAP Root cause String: {Adapter}4EAP Error: {Adapter}5
Microsoft-Windows-WLAN-AutoConfig  |  12014     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Wireless 802.1x authentication was restarted.Network Adapter: {Adapter}Interface GUID: {DeviceGuid}Local MAC Address: {LocalMac}Network SSID: {SSID}BSS Type: {BSSType}Eap Information: Type {EapType}, Vendor ID {VendorID}, Vendor Type {VendorType}, Author ID {AuthorID}Restart Reason: {Adapter}0
Microsoft-Windows-WLAN-AutoConfig  |  13001     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  A pre-logon connection was not attempted.Result: {Result}Reason: {Reason}
Microsoft-Windows-WLAN-AutoConfig  |  13002     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  A pre-logon connection was attempted.Result: {Result}Interface GUID: {InterfaceGuid}Profile Name: {ProfileName}Requested Fields: {RequestedFields}
Microsoft-Windows-WLAN-AutoConfig  |  13011     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  A post-logon connection was not attempted.Result: {Result}Reason: {Reason}
Microsoft-Windows-WLAN-AutoConfig  |  13012     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  A post-logon connection was attempted.Result: {Result}Interface GUID: {InterfaceGuid}Profile Name: {ProfileName}
Microsoft-Windows-WLAN-AutoConfig  |  13013     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  The post-logon connection attempt is complete.Network connection attempt result: {Result}Reason: {Reason}Interface GUID: {InterfaceGuid}Profile Name: {ProfileName}
Microsoft-Windows-WLAN-AutoConfig  |  13014     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  A post-logon connection was attempted.Result: {Result}Interface GUID: {InterfaceGuid}Profile Name: {ProfileName}
Microsoft-Windows-WLAN-AutoConfig  |  13100     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  {CostSource} Cost is changed to {CostValue} for profile {ProfileName} on interface {InterfaceGuid}
Microsoft-Windows-WLAN-AutoConfig  |  13101     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Group Policy Cost is changed to {CostValue}
Microsoft-Windows-WLAN-AutoConfig  |  13102     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  {CostSource} Cost is cleared for profile {ProfileName} on interface {InterfaceGuid}
Microsoft-Windows-WLAN-AutoConfig  |  13103     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Group Policy Cost is cleared
Microsoft-Windows-WLAN-AutoConfig  |  14000     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Media notification received. Interface = {InterfaceDescription}, Connected = {Connected}.
Microsoft-Windows-WLAN-AutoConfig  |  14001     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Peer notification received. Interface = {InterfaceDescription}, Joined = {Joined}.
Microsoft-Windows-WLAN-AutoConfig  |  14002     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Enable AutoConfig. Interface = {InterfaceDescription}, Enabled = {Enabled}.
Microsoft-Windows-WLAN-AutoConfig  |  14003     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Set media streaming mode. Interface = {InterfaceDescription}, Enable = {Enabled}, Result = {Result}.
Microsoft-Windows-WLAN-AutoConfig  |  14004     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Set BSS type. Interface = {InterfaceDescription}, BSS type = {BSSType}.
Microsoft-Windows-WLAN-AutoConfig  |  14005     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Set radio state. Interface = {InterfaceDescription}, PHY = {PHY}, State = {RadioState}, Result = {Result}.
Microsoft-Windows-WLAN-AutoConfig  |  14006     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Start auto config. Interface = {InterfaceDescription}.
Microsoft-Windows-WLAN-AutoConfig  |  14007     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Stop auto config. Interface = {InterfaceDescription}.
Microsoft-Windows-WLAN-AutoConfig  |  14008     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Power setting = {PowerSetting}. Interface = {InterfaceDescription}.
Microsoft-Windows-WLAN-AutoConfig  |  14009     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Change session to {ConnectionId}. Interface = {InterfaceDescription}.
Microsoft-Windows-WLAN-AutoConfig  |  14010     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Radio is off. Interface = {InterfaceDescription}.
Microsoft-Windows-WLAN-AutoConfig  |  14011     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Change radio state for interface = {InterfaceDescription} :  PHY = {PHY}, software state = {SoftwareState}, hardware state = {HardwareState})
Microsoft-Windows-WLAN-AutoConfig  |  14012     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  The connection is not healthy. Pending profile update is ignored. Interface = {InterfaceDescription}
Microsoft-Windows-WLAN-AutoConfig  |  14013     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Profile {Profile} is updated. Interface = {InterfaceDescription}
Microsoft-Windows-WLAN-AutoConfig  |  14014     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  {ConnectionResetReason}, need to disconnect. Interface = {InterfaceDescription}
Microsoft-Windows-WLAN-AutoConfig  |  14015     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Set current operation mode. Interface = {InterfaceDescription}, OpMode = {OpMode}, Result = {Result}.
Microsoft-Windows-WLAN-AutoConfig  |  14016     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Got connection request, mode = {ConnectionMode}, flags = {Flags}, profile name = {Profile}, session = {ConnectionId}. Interface = {InterfaceDescription}
Microsoft-Windows-WLAN-AutoConfig  |  14017     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection cancelled by user. Interface = {InterfaceDescription}.
Microsoft-Windows-WLAN-AutoConfig  |  14018     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection failed. Interface = {InterfaceDescription}, Reason code = {ErrorCode}.
Microsoft-Windows-WLAN-AutoConfig  |  14019     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Stop all connection attempts for interface {InterfaceDescription}.
Microsoft-Windows-WLAN-AutoConfig  |  14020     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection succeeded on interface {InterfaceDescription}.
Microsoft-Windows-WLAN-AutoConfig  |  14021     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection complete on interface {InterfaceDescription}, session = {ConnectionId}, status = {Status}, ad hoc network formed = {Adhoc}
Microsoft-Windows-WLAN-AutoConfig  |  14022     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Got disconnect request. Interface = {InterfaceDescription}.
Microsoft-Windows-WLAN-AutoConfig  |  14023     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Set profile {Profile} to manual temporarily.
Microsoft-Windows-WLAN-AutoConfig  |  14024     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Disconnecting. Interface = {InterfaceDescription}.
Microsoft-Windows-WLAN-AutoConfig  |  14025     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Interface {InterfaceDescription} state is set to {State}.
Microsoft-Windows-WLAN-AutoConfig  |  14026     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  UI request for interface {InterfaceDescription} result = {Result}.
Microsoft-Windows-WLAN-AutoConfig  |  14027     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Profile {Profile} {HealthCheckResult}.
Microsoft-Windows-WLAN-AutoConfig  |  14028     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Profile name change. Interface = {InterfaceDescription}, old profile name = {OldProfileName}, new profile name = {NewProfileName}
Microsoft-Windows-WLAN-AutoConfig  |  14029     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Interface {InterfaceGuid} ({InterfaceDescription}) is successfully initialized.
Microsoft-Windows-WLAN-AutoConfig  |  14030     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  The current operation mode for interface {InterfaceDescription} is {OpMode}.
Microsoft-Windows-WLAN-AutoConfig  |  14031     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Interface {InterfaceGuid} type = {Type}.
Microsoft-Windows-WLAN-AutoConfig  |  14032     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Interface {InterfaceGuid} cannot be queried, error {ErrorCode}.
Microsoft-Windows-WLAN-AutoConfig  |  14033     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Failed to query physical medium for interface {InterfaceGuid}, because the device is not ready. Need to retry.
Microsoft-Windows-WLAN-AutoConfig  |  14034     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Found name {FriendlyName} for interface {DeviceGuid}
Microsoft-Windows-WLAN-AutoConfig  |  14035     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Network {SSID} is not permitted.
Microsoft-Windows-WLAN-AutoConfig  |  14036     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Power setting = {Setting}.
Microsoft-Windows-WLAN-AutoConfig  |  14037     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Disconnect the temporary connection {Profile} for interface {InterfaceDescription}, Reason = {Reason}.
Microsoft-Windows-WLAN-AutoConfig  |  14038     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Clear runtime state because the user who initiated the manual connection logged off.
Microsoft-Windows-WLAN-AutoConfig  |  14039     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  WTS session change. Type = {Type}, session id = {ConnectionId}.
Microsoft-Windows-WLAN-AutoConfig  |  14040     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Scan for networks. Interface = {InterfaceDescription}, scan type = {ScanType}, flush BSS list = {FlushBSSList}
Microsoft-Windows-WLAN-AutoConfig  |  14041     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Scan request is ignored because radio is off. Interface = {InterfaceDescription}.
Microsoft-Windows-WLAN-AutoConfig  |  14042     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Scan results are not queried because raido is off. Interface = {InterfaceDescription}.
Microsoft-Windows-WLAN-AutoConfig  |  14043     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  The scan state machine is stopped.
Microsoft-Windows-WLAN-AutoConfig  |  14044     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  No auto switch for the current connection ({Profile}).
Microsoft-Windows-WLAN-AutoConfig  |  14045     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection (auto = {Auto}) to {SSID} (multiple={Multiple}) using profile {ProfileName}.
Microsoft-Windows-WLAN-AutoConfig  |  14046     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  The session id={ConnectionId}, active={Active}, console={Console} is added.
Microsoft-Windows-WLAN-AutoConfig  |  14047     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  The state of session id={ConnectionId} is refreshed to active={Active}, console={Console}.
Microsoft-Windows-WLAN-AutoConfig  |  14048     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Active Console User state = {ActiveConsole}
Microsoft-Windows-WLAN-AutoConfig  |  14049     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  The session id={ConnectionId} is removed.
Microsoft-Windows-WLAN-AutoConfig  |  14050     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Discovery module has taken care of the UI request.
Microsoft-Windows-WLAN-AutoConfig  |  14051     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  UI request not sent because the network is suppressed and the UI request is notification type.
Microsoft-Windows-WLAN-AutoConfig  |  14052     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  IntfCompleteTimely failed, error {ErrorCode}
Microsoft-Windows-WLAN-AutoConfig  |  14053     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Session {ConnectionId}, Network suppressed status for {Network} is {Suppressed}.
Microsoft-Windows-WLAN-AutoConfig  |  14054     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Enable AutoConfig background scan. Interface = {InterfaceDescription}, Enabled = {Enabled}.
Microsoft-Windows-WLAN-AutoConfig  |  14055     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Discard this round of background scan because a connection process is in progress. Interface = {InterfaceDescription}
Microsoft-Windows-WLAN-AutoConfig  |  14056     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Discard this round of background scan because the current connection does not allow auto switch. Interface = {InterfaceDescription}
Microsoft-Windows-WLAN-AutoConfig  |  14057     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Discard this round of background scan because the current connection is the most preferred auto connection. Interface = {InterfaceDescription}
Microsoft-Windows-WLAN-AutoConfig  |  14058     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connect to {SSID} with profile {ProfileName}
Microsoft-Windows-WLAN-AutoConfig  |  14059     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Set operational state. Interface = {InterfaceDescription}, Enabled = {Enabled}.
Microsoft-Windows-WLAN-AutoConfig  |  14060     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Profile State changed. Profile: {Profile} Blocked for {BlockTimeMs} milliseconds (Single SSID: {SingleSSID})
Microsoft-Windows-WLAN-AutoConfig  |  14061     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Profile State changed. Profile: {Profile} Update State: {Update} (Single SSID: {SingleSSID})
Microsoft-Windows-WLAN-AutoConfig  |  14062     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  RpcCall {WlanRpcCallType} from client {ClientProcessId}
Microsoft-Windows-WLAN-AutoConfig  |  14063     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  SetAutoConfigParameterRpcCall for {OpCode} from process {ClientProcessId}
Microsoft-Windows-WLAN-AutoConfig  |  14064     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  SetInterfaceRpcCall for {OpCode} from process {ClientProcessId}
Microsoft-Windows-WLAN-AutoConfig  |  14065     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  PrivateSetInterfaceRpcCall for {OpCode} from process {ClientProcessId} on Interface {InterfaceGuid}
Microsoft-Windows-WLAN-AutoConfig  |  14066     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  InternalPrivateQuerySetInterfaceCall for {OpCode} on Interface {InterfaceGuid}
Microsoft-Windows-WLAN-AutoConfig  |  14067     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Screen Power State changed. Screen ON = {IsOn}
Microsoft-Windows-WLAN-AutoConfig  |  14068     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Low Power State changed. Low Power = {IsEnabled}
Microsoft-Windows-WLAN-AutoConfig  |  14069     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Adding WLAN Interface {InterfaceGuid} for {InterfaceDescription}
Microsoft-Windows-WLAN-AutoConfig  |  14070     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Removing WLAN Interface Interface {InterfaceGuid}
Microsoft-Windows-WLAN-AutoConfig  |  14071     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Expedited scan triggered on {InterfaceGuid} because {ExpeditedScanTrigger}
Microsoft-Windows-WLAN-AutoConfig  |  14072     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Disconnect triggered on {InterfaceGuid} Reason: {DisconnectTrigger}
Microsoft-Windows-WLAN-AutoConfig  |  14073     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Limited Connectivity Recovery Type: {RecoveryType} Event: {EventType} Data: {EventData}
Microsoft-Windows-WLAN-AutoConfig  |  14074     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Gateway Reachability State changed. Interface GUID: {InterfaceGuid} Reachable: {IsReachable}
Microsoft-Windows-WLAN-AutoConfig  |  14075     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Update allowed connectivity token - AutoConnect=[Enabled: {IsAutoConnectEnabled}, Count: {AutoConnectProfileCount}, FilterControl: {AutoConnectFilterControl}], ManualConnect=[Enabled: {IsManualConnectEnabled}, Count: {ManualConnectProfileCount}, FilterControl: {ManualConnectFilterControl}], Interface: {InterfaceDescription}
Microsoft-Windows-WLAN-AutoConfig  |  20000     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Begin Connect API
Microsoft-Windows-WLAN-AutoConfig  |  20001     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Begin Disconnect API
Microsoft-Windows-WLAN-AutoConfig  |  20002     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Calling MSMSecPerformPreAssociateSecurity
Microsoft-Windows-WLAN-AutoConfig  |  20003     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Calling MSMSecStopSecurity
Microsoft-Windows-WLAN-AutoConfig  |  20004     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connect completion reason {Reason}, session {Session}, adhoc formed {AdHocFormed}
Microsoft-Windows-WLAN-AutoConfig  |  20005     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Received CONNECT COMPLETION, status {Status}, assocStatus {AssocStatus}
Microsoft-Windows-WLAN-AutoConfig  |  20006     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  FSM Current state {CurrState}, event {EventId}
Microsoft-Windows-WLAN-AutoConfig  |  20007     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  FSM Transition from State: {CurrState} to State: {NewState}
Microsoft-Windows-WLAN-AutoConfig  |  20008     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Phy Type not compatible
Microsoft-Windows-WLAN-AutoConfig  |  20009     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Link Quality: {Quality}
Microsoft-Windows-WLAN-AutoConfig  |  20010     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Received IHV PORT DOWN, peer {BSSID}
Microsoft-Windows-WLAN-AutoConfig  |  20011     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Received IHV PORT UP, peer {BSSID}
Microsoft-Windows-WLAN-AutoConfig  |  20012     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Post Connect Security has Completed Successfully
Microsoft-Windows-WLAN-AutoConfig  |  20013     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Post Connect Security has FAILED with reason code: {ErrorCode}
Microsoft-Windows-WLAN-AutoConfig  |  20014     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Received Security Packet: {PacketType}
Microsoft-Windows-WLAN-AutoConfig  |  20015     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Security PreConnect Completion, security reason: {Reason}, error {Error}
Microsoft-Windows-WLAN-AutoConfig  |  20016     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Send Security Packet Length = {Length} and Completion Handle = {Handle}
Microsoft-Windows-WLAN-AutoConfig  |  20017     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Send Security Packet Length = {Length} and Completion Handle = {Handle}
Microsoft-Windows-WLAN-AutoConfig  |  20018     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  SSID = {SSID} BSSIDCount = {BSSIDCount}
Microsoft-Windows-WLAN-AutoConfig  |  20019     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  A client has associated with the hosted network. Interface GUID: {InterfaceGuid}Interface description:{InterfaceDescription}Network SSID: {SSID}Local MAC address: {LocalMAC}Peer MAC address: {PeerMAC}
Microsoft-Windows-WLAN-AutoConfig  |  20020     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  A client has successfully authenticated with the hosted network. Interface GUID: {InterfaceGuid}Interface description:{InterfaceDescription}Network SSID: {SSID}Local MAC address: {LocalMAC}Peer MAC address: {PeerMAC}
Microsoft-Windows-WLAN-AutoConfig  |  20021     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  A client has failed to authenticate with the hosted network. Error code: {ErrorCode}Error Message: {ErrorMsg}Interface GUID: {InterfaceGuid}Interface description:{InterfaceDescription}Network SSID: {SSID}Local MAC address: {LocalMAC}
Microsoft-Windows-WLAN-AutoConfig  |  20022     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Begin Scan
Microsoft-Windows-WLAN-AutoConfig  |  20023     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Scan completion Status {Status}
Microsoft-Windows-WLAN-AutoConfig  |  20024     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Number of Unique Wlan Networks {Count}
Microsoft-Windows-WLAN-AutoConfig  |  20025     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Visible Network: {Ssid}, {BssidCount} BSSIDS, {AuthAlgoId}/{CipherAlgoId}, {Rssi} RSSI
Microsoft-Windows-WLAN-AutoConfig  |  21001     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Adapter({InterfaceGuid}) New Adapter {FriendlyName} ({PKMIDs})
Microsoft-Windows-WLAN-AutoConfig  |  21002     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Adapter({InterfaceGuid}) IntfSecState Transition {OldState} --> {NewState}
Microsoft-Windows-WLAN-AutoConfig  |  21003     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Adapter({InterfaceGuid}) Received StopSecurity
Microsoft-Windows-WLAN-AutoConfig  |  21004     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Pre-Associate Failure Auth {AuthAlgoId}, Cipher {CipherAlgoId}, OneX Enabled({OneXEnabled}), UICancelled({UICancelled})
Microsoft-Windows-WLAN-AutoConfig  |  21005     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Received MSMSec UI Response, but already have key material!
Microsoft-Windows-WLAN-AutoConfig  |  21006     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Received UI response {ResponseType}
Microsoft-Windows-WLAN-AutoConfig  |  21007     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  TIMING OUT 802.1x Authentication
Microsoft-Windows-WLAN-AutoConfig  |  21008     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  NOT TIMING OUT 802.1x authentication, next timer in {Context} msec
Microsoft-Windows-WLAN-AutoConfig  |  21009     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  802.1x veto-ed FAST ROAMING (Error {ErrorCode}), performing full authentication
Microsoft-Windows-WLAN-AutoConfig  |  21010     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Port ({PortId}) Peer {PeerAddr} AuthMgr Transition {OldState} --> {NewState}
Microsoft-Windows-WLAN-AutoConfig  |  21011     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Sending UI response to 802.1x
Microsoft-Windows-WLAN-AutoConfig  |  21012     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  KeyExt Transition {OldState} --> {NewState}
Microsoft-Windows-WLAN-AutoConfig  |  21013     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Explicit failure from 802.1x, (Reason {Reason}, Error {Error})
Microsoft-Windows-WLAN-AutoConfig  |  21014     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  802.1x success
Microsoft-Windows-WLAN-AutoConfig  |  21015     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Port({PortId}) Peer {PeerAddr} KeyMgr transition {OldState} --> {NewState}
Microsoft-Windows-WLAN-AutoConfig  |  21016     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Auth sent M1({PortId}), self {LocalAddr}, peer {PeerAddr}
Microsoft-Windows-WLAN-AutoConfig  |  21017     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Auth sent M3({PortId}), self {LocalAddr}, peer {PeerAddr}
Microsoft-Windows-WLAN-AutoConfig  |  21018     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Auth sent G1({PortId}), self {LocalAddr}, peer {PeerAddr}
Microsoft-Windows-WLAN-AutoConfig  |  21019     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Port({PortId}) Peer {PeerAddr} KeyMgrAuth Transition {OldState} --> {NewState}
Microsoft-Windows-WLAN-AutoConfig  |  21020     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  CONNECTION SECURED by OFFLOADED key exchange
Microsoft-Windows-WLAN-AutoConfig  |  21021     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Port({PortId}) Notify Key Exchange Status: Authenticator({Authenticator}) reason {Reason} , self {LocalAddr}, peer {PeerAddr}
Microsoft-Windows-WLAN-AutoConfig  |  21022     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Default Key: Idx {Index}, Algo {CipherAlgoId}, Direction= {Direction}, Len {Len}
Microsoft-Windows-WLAN-AutoConfig  |  21023     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Pairwise Key ({Addr}): Algo {CipherAlgoId}, Direction= {Direction}, Len {Len}
Microsoft-Windows-WLAN-AutoConfig  |  21024     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Adapter({AdapterId}) Connect Completion, Reason {Reason}, Error {Error}
Microsoft-Windows-WLAN-AutoConfig  |  21025     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Port({PortId}) Indicate Security Result, Peer {PeerAddr}, Reason {Reason} Error {Error}
Microsoft-Windows-WLAN-AutoConfig  |  21026     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Adapter({Context}) Tx to {PeerAddr}, Ethertype {EtherType}, size {Size}
Microsoft-Windows-WLAN-AutoConfig  |  21027     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Sending UI request to MSM ({SessionId})
Microsoft-Windows-WLAN-AutoConfig  |  21028     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Adapter({InterfaceGuid}) MSM Connect notification, Network "{SSID}"
Microsoft-Windows-WLAN-AutoConfig  |  21029     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Adapter({InterfaceGuid}) MSM Disconnect notification
Microsoft-Windows-WLAN-AutoConfig  |  21030     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Adapter({InterfaceGuid}) Port up for peer {PeerAddr}
Microsoft-Windows-WLAN-AutoConfig  |  21031     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Adapter({InterfaceGuid}) Port down for peer {PeerAddr}
Microsoft-Windows-WLAN-AutoConfig  |  21032     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Adapter({InterfaceGuid}) Rx from {PeerAddr}, Ethertype {EtherType}, size {Size}
Microsoft-Windows-WLAN-AutoConfig  |  21033     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Adapter({InterfaceGuid}) UI Response, request type {RequestType}, response type {ResponseType}, cancelled = {Cancelled}
Microsoft-Windows-WLAN-AutoConfig  |  21034     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Adapter({InterfaceGuid}) Create discovery profiles, SSID {SSID}, BSS type {BSSType}, secure {Secure}
Microsoft-Windows-WLAN-AutoConfig  |  21035     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Tx pkt completion, pkt {Context}
Microsoft-Windows-WLAN-AutoConfig  |  21036     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Adapter({InterfaceGuid}) MSM Redo security request
Microsoft-Windows-WLAN-AutoConfig  |  21037     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection health status is {AdapterId} ({InterfaceGuid}), HealthyHint {Healthy}
Microsoft-Windows-WLAN-AutoConfig  |  21038     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Transition network suspected
Microsoft-Windows-WLAN-AutoConfig  |  21039     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  UI Response - Valid = {Valid}, Cancelled = {Cancelled}
Microsoft-Windows-WLAN-AutoConfig  |  21040     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Port({Context}) MSMSendPacket failed, Error {ErrorCode}
Microsoft-Windows-WLAN-AutoConfig  |  21041     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |
Microsoft-Windows-WLAN-AutoConfig  |  21042     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  PreAuthMgr Transition {OldState} --> {NewState}
Microsoft-Windows-WLAN-AutoConfig  |  21043     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  PreAuth: 802.1X Success, Received keys by Pre-Authentication for {PeerAddr}
Microsoft-Windows-WLAN-AutoConfig  |  21044     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  PreAuth: Explicit failure from 802.1x, (Reason {Reason}, Error {Error})
Microsoft-Windows-WLAN-AutoConfig  |  21045     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  PreAuth: 802.1x success
Microsoft-Windows-WLAN-AutoConfig  |  21046     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Received unicast key material in EAPOL-Key (Rapid rekey {RapidRekey})
Microsoft-Windows-WLAN-AutoConfig  |  21047     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  CONNECTION SECURED by RC4 key exchange
Microsoft-Windows-WLAN-AutoConfig  |  21048     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  CONNECTION SECURED by RSN key exchange
Microsoft-Windows-WLAN-AutoConfig  |  21049     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  RSN Key Receive: Key Message M1
Microsoft-Windows-WLAN-AutoConfig  |  21050     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  RSN Key Receive: Key Message M3
Microsoft-Windows-WLAN-AutoConfig  |  21051     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  RSN Key Receive: Key Message M2
Microsoft-Windows-WLAN-AutoConfig  |  21052     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  RSN Key Receive: Key Message M4
Microsoft-Windows-WLAN-AutoConfig  |  21053     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  RSN Key Receive: Key Message G1
Microsoft-Windows-WLAN-AutoConfig  |  21054     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  RSN Key Receive: Key Message G2
Microsoft-Windows-WLAN-AutoConfig  |  21055     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  FAST ROAMING is {AdapterId}
Microsoft-Windows-WLAN-AutoConfig  |  21056     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Unknown transition into Failure, EventType {Context}
Microsoft-Windows-WLAN-AutoConfig  |  21057     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Port({PortId}) Peer {PeerAddr} SecMgr Transition {OldState} --> {NewState}
Microsoft-Windows-WLAN-AutoConfig  |  21058     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  CONNECTION SECURED by WPA key exchange
Microsoft-Windows-WLAN-AutoConfig  |  21059     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  WPA Key Receive: Key Message M1
Microsoft-Windows-WLAN-AutoConfig  |  21060     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  WPA Key Receive: Key Message M3
Microsoft-Windows-WLAN-AutoConfig  |  21061     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  WPA Key Receive: Key Message G1
Microsoft-Windows-WLAN-AutoConfig  |  21062     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Eapol Key packet cache OVERFLOW
Microsoft-Windows-WLAN-AutoConfig  |  21063     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  PMK Cache overflowed, current {Current}, limit {Max}
Microsoft-Windows-WLAN-AutoConfig  |  21064     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  WLAN Security Settings: BSS Type {BSSType}, Authentication {AuthAlgoId}, Encryption {CipherAlgoId}, OneX Enabled {OnexEnabled}, Eap Information - Type {EapType}, Vendor ID {VendorID}, Vendor Type {VendorType}, Author ID {AuthorID}
Microsoft-Windows-WLAN-AutoConfig  |  21065     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Received multicast key material in EAPOL-Key (Rapid rekey {RapidRekey})
Microsoft-Windows-WLAN-AutoConfig  |  21066     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Default Key ID set to Index {Index}
Microsoft-Windows-WLAN-AutoConfig  |  30000     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection started 1
Microsoft-Windows-WLAN-AutoConfig  |  30001     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection timeout threshold reached 1
Microsoft-Windows-WLAN-AutoConfig  |  30002     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection succeeded
Microsoft-Windows-WLAN-AutoConfig  |  30003     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection started 2
Microsoft-Windows-WLAN-AutoConfig  |  30004     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection timeout threshold reached 2
Microsoft-Windows-WLAN-AutoConfig  |  30005     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection started 3
Microsoft-Windows-WLAN-AutoConfig  |  30006     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection timeout threshold reached 3
Microsoft-Windows-WLAN-AutoConfig  |  30007     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Manual connect initiated, end running reconnect scenarios
Microsoft-Windows-WLAN-AutoConfig  |  30008     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Manual connect initiated, end running reconnect scenarios
Microsoft-Windows-WLAN-AutoConfig  |  30009     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Manual connect initiated, end running reconnect scenarios
Microsoft-Windows-WLAN-AutoConfig  |  30010     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  UI interaction requested 1
Microsoft-Windows-WLAN-AutoConfig  |  30011     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  UI interaction requested 2
Microsoft-Windows-WLAN-AutoConfig  |  30012     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  UI interaction requested 3
Microsoft-Windows-WLAN-AutoConfig  |  30013     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection succeeded - Hidden network 1
Microsoft-Windows-WLAN-AutoConfig  |  30014     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection succeeded - Hidden network 2
Microsoft-Windows-WLAN-AutoConfig  |  30015     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection succeeded - Hidden network 3
Microsoft-Windows-WLAN-AutoConfig  |  30016     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Selection list exhausted 1
Microsoft-Windows-WLAN-AutoConfig  |  30017     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Selection list exhausted 2
Microsoft-Windows-WLAN-AutoConfig  |  30018     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Selection list exhausted 3
Microsoft-Windows-WLAN-AutoConfig  |  30019     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connection succeeded to previous network - expected roaming
Microsoft-Windows-WLAN-AutoConfig  |  30020     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |
Microsoft-Windows-WLAN-AutoConfig  |  30021     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |
Microsoft-Windows-WLAN-AutoConfig  |  30022     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |
Microsoft-Windows-WLAN-AutoConfig  |  30100     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |
Microsoft-Windows-WLAN-AutoConfig  |  30101     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |
Microsoft-Windows-WLAN-AutoConfig  |  30102     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |
Microsoft-Windows-WLAN-AutoConfig  |  30103     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |
Microsoft-Windows-WLAN-AutoConfig  |  30104     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Cancel WLAN Resume-Reconnect Interface GUID: {InterfaceGuid}
Microsoft-Windows-WLAN-AutoConfig  |  30105     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |
Microsoft-Windows-WLAN-AutoConfig  |  40001     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Connect Diagnostic InformationInterface GUID: {InterfaceGuid}Network Adapter: {InterfaceDescription}Connection Mode: {ConnectionMode}SSID: {SSID}BSS Type: {BSSType}Authentication: {AuthAlgo}Encryption: {CipherAlgo}802.1X Enabled: {OnexEnabled}IHV Bitmap: {IHVBitmap}Hidden: {InterfaceGuid}0Peer MAC: {InterfaceGuid}1WLAN Status Code: {InterfaceGuid}2Dot11 Status Code: {InterfaceGuid}3Assoc Time: {InterfaceGuid}4Assoc Restart Count: {InterfaceGuid}5Auth Time: {InterfaceGuid}6Auth Restart Count: {InterfaceGuid}7Device ID: {InterfaceGuid}8Device Manufacturer: {ConnectionMode}8Driver Service: {InterfaceDescription}0Driver Version: {InterfaceGuid}9Driver Date: {SSID}2RSSI: {InterfaceDescription}1Signal Quality: {InterfaceDescription}2%%Channel: {InterfaceDescription}3Interfering AP Count: {InterfaceDescription}4Total Visible AP Count: {InterfaceDescription}5Max AP Phy Type: {InterfaceDescription}6Max AP Channel Width: {InterfaceDescription}7AP Description: {InterfaceDescription}8AP Manufacturer: {InterfaceDescription}9AP Model Name: {ConnectionMode}0AP Model Number: {ConnectionMode}1Detailed Status On Roam: {ConnectionMode}2Rx Rate:{ConnectionMode}3Tx Rate: {ConnectionMode}4EAP Type: {ConnectionMode}5802.1x Auth Mode: {ConnectionMode}6HotSpot 2.0: {ConnectionMode}7Profile Type {ConnectionMode}9System MAC Randomization: {SSID}0Profile MAC Randomization: {SSID}1
Microsoft-Windows-WLAN-AutoConfig  |  40002     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Limited Recovery Diagnostic StatisticsInterface GUID: {InterfaceGuid}Disconnect Extensions: {DisconnectExtensions}Roam Extensions: {RoamExtensions}Suspect Duration: {SuspectDurationMs} msBssid Changed: {BssidChanged}Detection Link Quality: {DetectionLinkQuality}Current Link Quality: {CurrentLinkQuality}MacTxUnicastCount: {MacTxUnicastCount}MacRxUnicastCount: {MacRxUnicastCount}MacRxMulticastCount: {InterfaceGuid}0MacRxUnicastDecryptSuccess: {InterfaceGuid}1MacRxUnicastDecryptFailure: {InterfaceGuid}2PhyTxFailedCount: {InterfaceGuid}3PhyTxFrameCount: {InterfaceGuid}4PhyTxRetryCount: {InterfaceGuid}5PhyRxFrameCount: {InterfaceGuid}6PhyRxFcsErrorCount: {InterfaceGuid}7Current Tx Rate: {InterfaceGuid}8Current Rx Rate:{InterfaceGuid}9
Microsoft-Windows-WLAN-AutoConfig  |  40003     |  Microsoft-Windows-WLAN-AutoConfig/Diagnostic   |  Diagnostic Statistics DifferenceInterface GUID: {InterfaceGuid}Event: {DiagnosticStatsDifferenceTrigger}MacTxUnicastCount: {MacTxUnicastCount}MacRxUnicastCount: {MacRxUnicastCount}MacRxMulticastCount: {MacRxMulticastCount}MacRxUnicastDecryptSuccess: {MacRxUnicastDecryptSuccess}MacRxUnicastDecryptFailure: {MacRxUnicastDecryptFailure}PhyTxFailedCount: {PhyTxFailedCount}PhyTxFrameCount: {PhyTxFrameCount}PhyTxRetryCount: {InterfaceGuid}0PhyRxFrameCount: {InterfaceGuid}1PhyRxFcsErrorCount: {InterfaceGuid}2TimeDiffMs: {InterfaceGuid}3
Microsoft-Windows-WLAN-AutoConfig  |  60001     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Error: {ErrorCode} Location: {Location} Context: {Context}
Microsoft-Windows-WLAN-AutoConfig  |  60002     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Warning: {WarningCode} Location: {Location} Context: {Context}
Microsoft-Windows-WLAN-AutoConfig  |  60003     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Transitioned to State: {NextState} Context: {Context}
Microsoft-Windows-WLAN-AutoConfig  |  60004     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Updated Context: {Context} Update Reason: {UpdateReasonCode}
Microsoft-Windows-WLAN-AutoConfig  |  60101     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  SourceAddress: {SourceAddress} SourcePort: {SourcePort} DestinationAddress: {DestinationAddress} DestinationPort: {DestinationPort} Protocol: {Protocol} ReferenceContext: {ReferenceContext}
Microsoft-Windows-WLAN-AutoConfig  |  60102     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  SourceAddress: {SourceAddress} SourcePort: {SourcePort} DestinationAddress: {DestinationAddress} DestinationPort: {DestinationPort} Protocol: {Protocol} ReferenceContext: {ReferenceContext}
Microsoft-Windows-WLAN-AutoConfig  |  60103     |  Microsoft-Windows-WLAN-AutoConfig/Operational  |  Interface Guid: {IfGuid} IfIndex: {IfIndex} Interface Luid: {IfLuid} ReferenceContext: {ReferenceContext}