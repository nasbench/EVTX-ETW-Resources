Provider                |  Event ID  |  Channel                             |  Message
------------------------|------------|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-OneX  |  1         |  Microsoft-Windows-OneX/Diagnostic   |  OneXDestroySupplicantPort
Microsoft-Windows-OneX  |  2         |  Microsoft-Windows-OneX/Diagnostic   |  OneXStartAuthentication
Microsoft-Windows-OneX  |  3         |  Microsoft-Windows-OneX/Diagnostic   |  OneXStopAuthentication
Microsoft-Windows-OneX  |  4         |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): EAP error WinError={WinError}, ReasonCode={ReasonCode}, EapMethod(Type={EAPMethodType}), RootCause is {RootCauseString}
Microsoft-Windows-OneX  |  5         |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Account is disabled and user is non-domain joined. Authentication will be tried with alternate credentials profile.
Microsoft-Windows-OneX  |  6         |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): EAP failure indication with error code {WinError} and reason code {ReasonCode}
Microsoft-Windows-OneX  |  7         |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Saving updated user data of size ({UserDataSize})
Microsoft-Windows-OneX  |  8         |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Saving updated connection data of size ({UserDataSize})
Microsoft-Windows-OneX  |  9         |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Successfully received UI Response
Microsoft-Windows-OneX  |  10        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): EapProcessPacketValidityAndGetResult returned action {Response}
Microsoft-Windows-OneX  |  11        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): EAP requested authentication restart
Microsoft-Windows-OneX  |  12        |  Microsoft-Windows-OneX/Diagnostic   |  Port({Context}): EapHostPeerInitialize failed, error {ErrorCode}
Microsoft-Windows-OneX  |  13        |  Microsoft-Windows-OneX/Diagnostic   |  Port({Context}): EapHostPeerEndSession failed, error {ErrorCode}
Microsoft-Windows-OneX  |  14        |  Microsoft-Windows-OneX/Diagnostic   |  Port({Context}): OneXGeneratePacketEvent failed, error {ErrorCode}
Microsoft-Windows-OneX  |  15        |  Microsoft-Windows-OneX/Diagnostic   |  Port({Context}): OneXGeneratePeerAuthRestartedEvent failed, error {ErrorCode}
Microsoft-Windows-OneX  |  16        |  Microsoft-Windows-OneX/Diagnostic   |  Port({Context}): EapHostPeerGetAuthStatus failed, error {ErrorCode}
Microsoft-Windows-OneX  |  17        |  Microsoft-Windows-OneX/Diagnostic   |  Port({Context}): MSMUIRequest failed, error {ErrorCode}
Microsoft-Windows-OneX  |  18        |  Microsoft-Windows-OneX/Diagnostic   |  Port({Context}): CompareSessionUserWithOwner failed, error {ErrorCode}
Microsoft-Windows-OneX  |  19        |  Microsoft-Windows-OneX/Diagnostic   |  Port({Context}): ProcessEapHostTLV failed, error {ErrorCode}
Microsoft-Windows-OneX  |  20        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Cannot send UI Request (code={UIRequestCode}) to MSM since UI is disabled for the port
Microsoft-Windows-OneX  |  21        |  Microsoft-Windows-OneX/Diagnostic   |  Port({Context}): Error {ErrorCode} in calling WTSQueryUserToken. Proposing machine authentication.
Microsoft-Windows-OneX  |  22        |  Microsoft-Windows-OneX/Diagnostic   |  Port({Context}): SupplicantGetUserTokenFromRuntimeState failed, error {ErrorCode}
Microsoft-Windows-OneX  |  23        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): The auth mode is User only but an appropriate user can't be found
Microsoft-Windows-OneX  |  24        |  Microsoft-Windows-OneX/Diagnostic   |  Port({Context}): CompareOneXCredentials failed, error {ErrorCode}
Microsoft-Windows-OneX  |  25        |  Microsoft-Windows-OneX/Diagnostic   |  Port({Context}): Failed to conditionally send Eapol start packet. Ignoring error {WarningCode}
Microsoft-Windows-OneX  |  26        |  Microsoft-Windows-OneX/Diagnostic   |  Port({Context}): OneXGenerateForceAuthenticatedEvent failed, error {ErrorCode}
Microsoft-Windows-OneX  |  27        |  Microsoft-Windows-OneX/Diagnostic   |  OneXValidateProfile failed, error {ErrorCode}, reason code {Context}
Microsoft-Windows-OneX  |  28        |  Microsoft-Windows-OneX/Diagnostic   |  EAP dll requested to show UI, but the UI for the port is not allowed with current credentials
Microsoft-Windows-OneX  |  29        |  Microsoft-Windows-OneX/Diagnostic   |  The EAP method does not support key derivation and will not be used for discovery
Microsoft-Windows-OneX  |  30        |  Microsoft-Windows-OneX/Diagnostic   |  The EAP method does not support mutual authentication and will not be used for discovery
Microsoft-Windows-OneX  |  31        |  Microsoft-Windows-OneX/Diagnostic   |  Done with creating discovery profiles. Created {ProfilesCount} profiles
Microsoft-Windows-OneX  |  32        |  Microsoft-Windows-OneX/Diagnostic   |  Created a 1X profile for discovery with eapType={EAPMethodType} and AuthMode={AuthMode}
Microsoft-Windows-OneX  |  33        |  Microsoft-Windows-OneX/Diagnostic   |  The EAP method {EAPMethodType} is not allowed for media type {MediaType} and will not be used for discovery
Microsoft-Windows-OneX  |  34        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Successfully sent UI Request (code={UIRequestCode}) to MSM
Microsoft-Windows-OneX  |  35        |  Microsoft-Windows-OneX/Diagnostic   |  Received a session change event ({ChangeType})
Microsoft-Windows-OneX  |  36        |  Microsoft-Windows-OneX/Diagnostic   |  Finished initializing a new port with id={PortId} and friendly name={FriendlyName}
Microsoft-Windows-OneX  |  37        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): MPPE-Send/Recv-Keys have been derived by supplicant
Microsoft-Windows-OneX  |  38        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Sending UI Request (code={UIRequestCode}) to MSM
Microsoft-Windows-OneX  |  39        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Asking MSM to delete user data for user token
Microsoft-Windows-OneX  |  40        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Received an EAP packet length={PacketLength}, type={PacketType}, identifier={Identifier}, eapType={EapMethodType}
Microsoft-Windows-OneX  |  41        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Sent an Eapol start packet
Microsoft-Windows-OneX  |  42        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): The supplicant is configured to not send an Eapol start packet
Microsoft-Windows-OneX  |  43        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Restarting authentication due to reason = {Reason}
Microsoft-Windows-OneX  |  44        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Authentication Starting
Microsoft-Windows-OneX  |  45        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Authentication Completed
Microsoft-Windows-OneX  |  46        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Time taken for this authentication = {TimeTaken} ms
Microsoft-Windows-OneX  |  47        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): 802.1X user identified. auth identity = {AuthIdentity}, sessionId = {SessionId}, username={Username}, domain={Domain}
Microsoft-Windows-OneX  |  48        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Stopping the current 802.1X authentication
Microsoft-Windows-OneX  |  49        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Starting a new 802.1X authentication ({Reason})
Microsoft-Windows-OneX  |  50        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Alternate credentials will be used for this profile
Microsoft-Windows-OneX  |  51        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): This is a discovery profile being attempted
Microsoft-Windows-OneX  |  52        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Trying timely configuration
Microsoft-Windows-OneX  |  53        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Completed the 802.1X authentication successfully
Microsoft-Windows-OneX  |  54        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Completed the 802.1X authentication because no authenticator was found
Microsoft-Windows-OneX  |  55        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): The session id ({SessionId}) received with the UI response is different than the session id for which the request was sent ({UIRequestSessionId}). Discarding this response
Microsoft-Windows-OneX  |  56        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): A pending UI request exists size={Size}, sessionId={SessionId}
Microsoft-Windows-OneX  |  57        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): User auth proposed for sessionId={SessionId} ({Reason})
Microsoft-Windows-OneX  |  58        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): The machine is in app server mode. Proposing machine auth
Microsoft-Windows-OneX  |  59        |  Microsoft-Windows-OneX/Diagnostic   |  EapHostPeerInvokeInteractiveUI failed, Error = {WinError} Reason = {ReasonCode}
Microsoft-Windows-OneX  |  60        |  Microsoft-Windows-OneX/Diagnostic   |  No EAP Cred fields to display
Microsoft-Windows-OneX  |  61        |  Microsoft-Windows-OneX/Diagnostic   |  Creds conversion failed (error={ErrorCode})
Microsoft-Windows-OneX  |  62        |  Microsoft-Windows-OneX/Diagnostic   |  EapHostPeerQueryInteractiveUIInputFields failed (error={ErrorCode})
Microsoft-Windows-OneX  |  63        |  Microsoft-Windows-OneX/Diagnostic   |  Displaying the change password dialog - {Result}
Microsoft-Windows-OneX  |  64        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Sending an EAP packet length={PacketLength}, type={PacketType}, identifier={Identifier}, eapType={EapMethodType}
Microsoft-Windows-OneX  |  65        |  Microsoft-Windows-OneX/Diagnostic   |  Port({PortId}): Identity being sent in the ResponseId packet is {Identity}
Microsoft-Windows-OneX  |  66        |  Microsoft-Windows-OneX/Operational  |  Port:({PortId}): Saving/Updating master copy of user dataSupplicantIsUsingExplicitCreds:({ExplicitCredentials})
Microsoft-Windows-OneX  |  68        |  Microsoft-Windows-OneX/Operational  |  Port({PortId}): Flushing User Data from Persistent StoreSupplicantIsUsingExplicitCreds:({ExplicitCredentials})
Microsoft-Windows-OneX  |  70        |  Microsoft-Windows-OneX/Operational  |  Port({PortId}):OneX Auth Timeout
Microsoft-Windows-OneX  |  60001     |  Microsoft-Windows-OneX/Diagnostic   |  Error: {ErrorCode} Location: {Location} Context: {Context}
Microsoft-Windows-OneX  |  60002     |  Microsoft-Windows-OneX/Diagnostic   |  Warning: {WarningCode} Location: {Location} Context: {Context}
Microsoft-Windows-OneX  |  60003     |  Microsoft-Windows-OneX/Diagnostic   |  Transitioned to State: {NextState} Context: {Context}
Microsoft-Windows-OneX  |  60004     |  Microsoft-Windows-OneX/Diagnostic   |  Updated Context: {Context} Update Reason: {UpdateReasonCode}
Microsoft-Windows-OneX  |  60101     |  Microsoft-Windows-OneX/Diagnostic   |  SourceAddress: {SourceAddress} SourcePort: {SourcePort} DestinationAddress: {DestinationAddress} DestinationPort: {DestinationPort} Protocol: {Protocol} ReferenceContext: {ReferenceContext}
Microsoft-Windows-OneX  |  60102     |  Microsoft-Windows-OneX/Diagnostic   |  SourceAddress: {SourceAddress} SourcePort: {SourcePort} DestinationAddress: {DestinationAddress} DestinationPort: {DestinationPort} Protocol: {Protocol} ReferenceContext: {ReferenceContext}
Microsoft-Windows-OneX  |  60103     |  Microsoft-Windows-OneX/Diagnostic   |  Interface Guid: {IfGuid} IfIndex: {IfIndex} Interface Luid: {IfLuid} ReferenceContext: {ReferenceContext}