Provider                  |  Event ID  |  Channel                               |  Message
--------------------------|------------|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-NlaSvc  |  4001      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Entered State: {CurrentOrNextState} Interface Guid: {InterfaceGuid}
Microsoft-Windows-NlaSvc  |  4002      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Transitioning to State: {CurrentOrNextState} Interface Guid: {InterfaceGuid}
Microsoft-Windows-NlaSvc  |  4101      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Received WMI Media Connect Notification for '{AdapterName}' {InterfaceGuid}
Microsoft-Windows-NlaSvc  |  4102      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Received WMI Media Disconnect Notification for '{AdapterName}' {InterfaceGuid}
Microsoft-Windows-NlaSvc  |  4103      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Route change has occurred for interface {InterfaceGuid} ({MibNotificationType})
Microsoft-Windows-NlaSvc  |  4104      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Address change has occurred for interface {InterfaceGuid} ({MibNotificationType})
Microsoft-Windows-NlaSvc  |  4105      |  Microsoft-Windows-NlaSvc/Diagnostic   |
Microsoft-Windows-NlaSvc  |  4106      |  Microsoft-Windows-NlaSvc/Diagnostic   |
Microsoft-Windows-NlaSvc  |  4201      |  Microsoft-Windows-NlaSvc/Diagnostic   |
Microsoft-Windows-NlaSvc  |  4202      |  Microsoft-Windows-NlaSvc/Diagnostic   |
Microsoft-Windows-NlaSvc  |  4203      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Start gateway resolution on interface {InterfaceGuid} for {GatewayIpAddress}
Microsoft-Windows-NlaSvc  |  4204      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Stop gateway resolution on interface {InterfaceGuid} for {GatewayIpAddress}. Error: {ErrorCode} NlnsState: {NlnsState} MAC: {MacAddr}
Microsoft-Windows-NlaSvc  |  4205      |  Microsoft-Windows-NlaSvc/Operational  |  Gateway resolution failed on interface {InterfaceGuid} for {GatewayIpAddress} with error: {ErrorCode}
Microsoft-Windows-NlaSvc  |  4251      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Plug-in data indicated from {PluginName} for entity {EntityName} ({IndicatedRowCount} rows){RowInterfaceGuid}
Microsoft-Windows-NlaSvc  |  4261      |  Microsoft-Windows-NlaSvc/Diagnostic   |  DHCP has stabilized for {InterfaceGuid} ({NlaState})
Microsoft-Windows-NlaSvc  |  4301      |  Microsoft-Windows-NlaSvc/Diagnostic   |
Microsoft-Windows-NlaSvc  |  4302      |  Microsoft-Windows-NlaSvc/Diagnostic   |
Microsoft-Windows-NlaSvc  |  4311      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Start DsGetDcName({DnsSuffix},{Flags}) for DnsSuffix
Microsoft-Windows-NlaSvc  |  4312      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Stop DsGetDcName({DnsSuffix},{Flags}) for DnsSuffix returned error {ErrorCode} (domain={RetrievedDomain}, forest={RetrievedForest})
Microsoft-Windows-NlaSvc  |  4313      |  Microsoft-Windows-NlaSvc/Diagnostic   |  DsGetDcName({DnsSuffix},{Flags}) for DnsSuffix failed with error {ErrorCode}
Microsoft-Windows-NlaSvc  |  4321      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Start DsGetDcName({Flags}) for DS info
Microsoft-Windows-NlaSvc  |  4322      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Stop DsGetDcName({Flags}) for DS info returned error {ErrorCode} (domain={RetrievedDomain}, forest={RetrievedForest})
Microsoft-Windows-NlaSvc  |  4323      |  Microsoft-Windows-NlaSvc/Diagnostic   |  DsGetDcName({Flags}) for DS info failed with error {ErrorCode}
Microsoft-Windows-NlaSvc  |  4331      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Start DsGetDcName({Flags}) for root domain GUID
Microsoft-Windows-NlaSvc  |  4332      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Stop DsGetDcName({Flags}) for root domain GUID returned error {ErrorCode} (domain={RetrievedDomain}, forest={RetrievedForest})
Microsoft-Windows-NlaSvc  |  4333      |  Microsoft-Windows-NlaSvc/Operational  |  DsGetDcName({Flags}) for root domain GUID failed with error {ErrorCode}
Microsoft-Windows-NlaSvc  |  4341      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Start LDAP authentication on interface {Interface Name} ({Addresses}) ({Try Count} tries)
Microsoft-Windows-NlaSvc  |  4342      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Stop LDAP authentication on interface {Interface Name} ({Addresses})
Microsoft-Windows-NlaSvc  |  4343      |  Microsoft-Windows-NlaSvc/Operational  |  LDAP authentication on interface {Interface Name} ({Addresses}) failed with error {ErrorCode}
Microsoft-Windows-NlaSvc  |  4351      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Start ldap_connect({Addresses}) for DC={DcName} ({Try Number} of {Try Count} tries)
Microsoft-Windows-NlaSvc  |  4352      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Stop ldap_connect({Addresses}) for DC={DcName} ({Try Number} of {Try Count} tries)
Microsoft-Windows-NlaSvc  |  4353      |  Microsoft-Windows-NlaSvc/Diagnostic   |  ldap_connect({Addresses}) for DC={DcName} ({Try Number} of {Try Count} tries) failed with {ErrorCode}
Microsoft-Windows-NlaSvc  |  4354      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Start ldap_bind({Addresses}) for DC={DcName} ({Try Number} of {Try Count} tries)
Microsoft-Windows-NlaSvc  |  4355      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Stop ldap_bind({Addresses}) for DC={DcName} ({Try Number} of {Try Count} tries)
Microsoft-Windows-NlaSvc  |  4356      |  Microsoft-Windows-NlaSvc/Diagnostic   |  ldap_bind({Addresses}) for DC={DcName} ({Try Number} of {Try Count} tries) failed with {ErrorCode}
Microsoft-Windows-NlaSvc  |  4401      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Inserting identifying signature for interface {InterfaceGuid} Source={SignatureSource} Signature={Signature}
Microsoft-Windows-NlaSvc  |  4402      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Inserting identified signature for interface {InterfaceGuid} Source={SignatureSource} Signature={Signature}
Microsoft-Windows-NlaSvc  |  4403      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Removing identified signature for interface {InterfaceGuid} Source={SignatureSource} Signature={Signature}
Microsoft-Windows-NlaSvc  |  4404      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Inserting identified signature for interface {InterfaceGuid} Source={SignatureSource} Signature={Signature}
Microsoft-Windows-NlaSvc  |  4405      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Inserting identified signature for interface {InterfaceGuid} Source={SignatureSource} Signature={Signature}
Microsoft-Windows-NlaSvc  |  4407      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Adding interface '{AdapterName}' {InterfaceGuid}
Microsoft-Windows-NlaSvc  |  4408      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Removing interface '{AdapterName}' {InterfaceGuid}
Microsoft-Windows-NlaSvc  |  4409      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Adding interface '{AdapterName}' {InterfaceGuid}
Microsoft-Windows-NlaSvc  |  4410      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Inserting identified signature for interface {InterfaceGuid} Source={SignatureSource} Signature={Signature}
Microsoft-Windows-NlaSvc  |  4411      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Inserting identified signature for interface {InterfaceGuid} Source={SignatureSource} Signature={Signature}
Microsoft-Windows-NlaSvc  |  4451      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Network on {InterfaceGuid} is unlikely to be authentication-capable; authentication will continue in the background. Reason: {AuthCapUnlikelyReason}
Microsoft-Windows-NlaSvc  |  5001      |  Microsoft-Windows-NlaSvc/Diagnostic   |
Microsoft-Windows-NlaSvc  |  5002      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Inserting identified signature for interface {InterfaceGuid} Source={SignatureSource} Characteristics={SignatureCharacteristics}
Microsoft-Windows-NlaSvc  |  6101      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Perftrack cancel event for interface '{AdapterName}' {InterfaceGuid}
Microsoft-Windows-NlaSvc  |  6102      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Perftrack cancel event for interface '{AdapterName}' {InterfaceGuid}
Microsoft-Windows-NlaSvc  |  6103      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Perftrack cancel event for interface '{AdapterName}' {InterfaceGuid}
Microsoft-Windows-NlaSvc  |  6104      |  Microsoft-Windows-NlaSvc/Diagnostic   |  Perftrack cancel event for interface '{AdapterName}' {InterfaceGuid}