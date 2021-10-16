Provider                                        |  Event ID  |  Channel                                                  |  Message
------------------------------------------------|------------|-----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  1         |  System                                                   |  An operation has failed ({ErrorParam1}, {ErrorParam2}, {ErrorParam3}, {ErrorParam4}).{Context}HResult: {hr}
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  2         |  System                                                   |  An operation has failed ({ErrorParam1}, {ErrorParam2}, {ErrorParam3}, {ErrorParam4}).{Context}Win32Error: {Win32Err}
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  3         |  System                                                   |  An operation has failed ({ErrorParam1}, {ErrorParam2}, {ErrorParam3}, {ErrorParam4}).{Context}NTStatus: {NTStatus}
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  4         |  System                                                   |  Failed to allocate object.Object: {ObjectName}Size: {ObjectSize}
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  5         |  System                                                   |  Unexpected size.Object: {Context}Expected Size: {ExpectedSize}Actual Size: {ActualSize}
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  6         |  System                                                   |  Invalid data.Name: {Name}Value: {Value}
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  7         |  System                                                   |  Device responded with an error status.Status: {Name}
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  8         |  System                                                   |  Bad device.Device: {Name}Reason: {String}
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  9         |  System                                                   |  The function is not supported.Function: {Name}Context: {String}
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  10        |  System                                                   |  A TCG Command has returned an error.Desc: {Description}Param1: {Param1}Param2: {Param2}Param3: {Param3}Param4: {Param4}Status: {CmdStatus}
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  11        |  System                                                   |  A TCG Silo Command has returned an error.{Description}SiloCommand={SiloCommand}, SiloStatus={SiloStatus}InvokingID={TCGInvokingID}, MethodID={TCGMethodID}
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  12        |  System                                                   |  A TCG Silo has returned the capabilities value of {Capabilities}.
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  13        |  System                                                   |  The system has performed an authentication operation on an Enhanced Storage device.BandID={BandID}Authorize={Authorize}Status={Status}
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  100       |  System                                                   |  The following informational event has occurred ({Param1}, {Param2}, {Param3}, {Param4}).{Context}
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  101       |  System                                                   |  The following warning event has occurred ({Param1}, {Param2}, {Param3}, {Param4}).{Context}
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  102       |  System                                                   |  The following error event has occurred ({Param1}, {Param2}, {Param3}, {Param4}).{Context}
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  200       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Get silo capabilities (SiloCmd={Param1}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  201       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Get silo capabilities returned (SiloCmd={Param1}, Status={Param2}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  202       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Execute silo command (SiloCmd={SiloCmd}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  203       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Excute silo command returned (SiloCmd={SiloCmd}, Status={TcgCmd}).InvokingId = {Status}MethodId = {Param1}
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  204       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Silo reset (SiloCmd={Param1}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  205       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Silo reset returned (SiloCmd={Param1}, Status={Param2}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  206       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: QueryCapabilities
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  207       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: QueryCapabilities returned (Status={Param1}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  208       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: Activate
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  209       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: Activate returned (Status={Param1}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  210       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: Revert
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  211       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: Revert returned (Status={Param1}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  212       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: EnumBands
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  213       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: EnumBands returned (Status={Param1}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  214       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: CreateBand
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  215       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: CreateBand returned (Status={Param1}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  216       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: SetBandLocation
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  217       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: SetBandLocation returned (Status={Param1}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  218       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: SetBandSecurity
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  219       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: SetBandSecurity returned (Status={Param1}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  220       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: DeleteBand
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  221       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: DeleteBand returned (Status={Param1}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  222       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: EraseBand
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  223       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: EraseBand returned (Status={Param1}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  224       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: GetBandMetadata
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  225       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: GetBandMetadata returned (Status={Param1}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  226       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: SetBandMetadata
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  227       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: SetBandMetadata returned (Status={Param1}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  228       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: RelinquishSilo
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  229       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: RelinquishSilo returned (Status={Param1}).
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  230       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: SetSid
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  |  231       |  Microsoft-Windows-EnhancedStorage-EhStorTcgDrv/Analytic  |  Ioctl: SetSid returned (Status={Param1}).