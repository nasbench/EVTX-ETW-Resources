Provider                 |  Event ID  |  Channel                                  |  Message
-------------------------|------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-Audio  |  0         |  Microsoft-Windows-Audio/Operational      |  Windows Audio encountered an error while processing a device event.                    Event ID     : 0x{Event} ({EventName})                     Failure Code : 0x{hr}
Microsoft-Windows-Audio  |  1         |  Microsoft-Windows-Audio/Operational      |  Windows Audio encountered an error while processing a device event.                    DeviceEventType : 0x{DeviceEventType} ({DeviceEventTypeName})                     Failure Code    : 0x{hr}
Microsoft-Windows-Audio  |  2         |  Application                              |  Windows Audio failed during a call to SetServiceStatus.                    Service Type               : 0x{dwServiceType}                     Current State              : 0x{dwCurrentState}                     Controls Accepted          : 0x{dwControlsAccepted}                     Win32 Exit Code            : 0x{dwWin32ExitCode}                     Service Specific Exit Code : 0x{dwServiceSpecificExitCode}                     Check Point                : 0x{dwCheckPoint}                     Wait Hint                  : 0x{dwWaitHint}
Microsoft-Windows-Audio  |  3         |  Microsoft-Windows-Audio/Operational      |  Windows Audio failed to start the {szSubsystemName} subsystem.                    Subsystem Failure Code     : 0x{dwSubsystemFailureCode}
Microsoft-Windows-Audio  |  4         |  Microsoft-Windows-Audio/Operational      |  The Windows Audio Device Graph Isolation process (audiodg.exe) has terminated unexpectedly.                    Process Exit Code     : 0x{dwAudioDgTerminationCode}
Microsoft-Windows-Audio  |  5         |  Microsoft-Windows-Audio/Operational      |  The Windows Audio Device Graph Isolation process (audiodg.exe) could not be started.                    Error Code     : 0x{dwAudioDgStartupFailureCode}
Microsoft-Windows-Audio  |  10        |  Microsoft-Windows-Audio/CaptureMonitor   |  The Capture Monitor has failed to restart the capture monitor between {szInputEndpointName} and {szOutputEndpointName}  {dwRestartCount} times.                   The capture monitor will no longer attempt to start this monitor.
Microsoft-Windows-Audio  |  11        |  Microsoft-Windows-Audio/Operational      |  StreamFlags {dwAudioSrvStreamFlags}
Microsoft-Windows-Audio  |  12        |  Performance                              |
Microsoft-Windows-Audio  |  13        |  Performance                              |
Microsoft-Windows-Audio  |  14        |  Performance                              |
Microsoft-Windows-Audio  |  15        |  Performance                              |
Microsoft-Windows-Audio  |  16        |  Performance                              |
Microsoft-Windows-Audio  |  17        |  Performance                              |
Microsoft-Windows-Audio  |  18        |  Microsoft-Windows-Audio/Operational      |  Windows Audio Device Graph glitch threshold count exceeded                               Count   : 0x{dwAudioDgTerminationCode}
Microsoft-Windows-Audio  |  19        |  Performance                              |  Windows Audio Device Graph glitch threshold count exceeded                               Count   : 0x{dwGlitchCount}
Microsoft-Windows-Audio  |  20        |  Microsoft-Windows-Audio/PlaybackManager  |  Format: {Format}Sampling rate: {SamplingRate}HzOffloaded: {bAudioSrvStreamResourceType}
Microsoft-Windows-Audio  |  21        |  Microsoft-Windows-Audio/PlaybackManager  |  Sound level for application [{AppId}] changed to [{SoundLevel}]
Microsoft-Windows-Audio  |  22        |  Microsoft-Windows-Audio/PlaybackManager  |  Suspended: {bIsSuspended}
Microsoft-Windows-Audio  |  23        |  Microsoft-Windows-Audio/PlaybackManager  |  Released exclusive mode resource {bExclusiveModeStream}Released offload mode resource {bOffloadStream}
Microsoft-Windows-Audio  |  24        |  Microsoft-Windows-Audio/PlaybackManager  |  Stream started.App Id: {AppId}PID: {PID}Audio Stream Category: {Category}
Microsoft-Windows-Audio  |  25        |  Microsoft-Windows-Audio/PlaybackManager  |  Stream stopped.App Id: {AppId}PID: {PID}Audio Stream Category: {Category}
Microsoft-Windows-Audio  |  26        |  Microsoft-Windows-Audio/GlitchDetection  |  Capture Monitor Render Glitch: pCMonitor=[{pCMonitor}], DevicePosition=[{DevicePosition}], QPCPosition=[{QPCPosition}]
Microsoft-Windows-Audio  |  27        |  Microsoft-Windows-Audio/GlitchDetection  |  Capture Monitor Capture Glitch: pCMonitor=[{pCMonitor}], DevicePosition=[{DevicePosition}], QPCPosition=[{QPCPosition}]
Microsoft-Windows-Audio  |  28        |  Microsoft-Windows-Audio/GlitchDetection  |  APO Glitch: Format Converter INF detected: pCAudioFormatConvert=[{pCAudioFormatConvert}], [{ConverstionType}]
Microsoft-Windows-Audio  |  29        |  Microsoft-Windows-Audio/GlitchDetection  |  Engine Glitch: CP Client Input Endpoint - pCCrossProcessClientInputEndpoint=[{pCCrossProcessClientInputEndpoint}] No Messages in queue
Microsoft-Windows-Audio  |  30        |  Microsoft-Windows-Audio/GlitchDetection  |  Engine Glitch: CP Client Input Endpoint - pCCrossProcessClientInputEndpoint=[{pCCrossProcessClientInputEndpoint}] Queue item does not match requested size
Microsoft-Windows-Audio  |  31        |  Microsoft-Windows-Audio/GlitchDetection  |  Engine Glitch: CP Client Output Endpoint - Server Overread: pCCrossProcessClientOutputEndpoint=[{pCCrossProcessClientOutputEndpoint}] WritePos=[{WriteBytePos}] ReadPos=[{ReadBytePos}] BytesToWrite=[{BytesToWrite}]
Microsoft-Windows-Audio  |  32        |  Microsoft-Windows-Audio/GlitchDetection  |  Engine Glitch: CP Client Output Endpoint - Read Pointer Overwrite: pCCrossProcessClientOutputEndpoint=[{pCCrossProcessClientOutputEndpoint}] WriteOffset=[{WriteOffset}] ReadOffset=[{ReadOffset}] BytesToWrite=[{BytesToWrite}] EndOfDataOffset=[{EndOfDataOffset}]
Microsoft-Windows-Audio  |  33        |  Microsoft-Windows-Audio/GlitchDetection  |  Engine Glitch: CP Server Input Endpoint - Starvation: pCCrossProcessServerInputEndpoint=[{pCCrossProcessServerInputEndpoint}] WriteOffset=[{WriteOffset}] ReadOffset=[{ReadOffset}] BufferSize=[{BufferSize}] BytesAvail=[{BytesAvailable}]
Microsoft-Windows-Audio  |  34        |  Microsoft-Windows-Audio/GlitchDetection  |  Engine Glitch: CP Server Output Endpoint - Queue Full Packet Drop: pCCrossProcessServerOutputEndpoint=[{pCCrossProcessServerOutputEndpoint}] WritePos=[{WriteBytePos}] DroppedBytes=[{DroppedBytes}] ReadPos=[{ReadBytePos}] BytesToWrite=[{BytesToWrite}]
Microsoft-Windows-Audio  |  35        |  Microsoft-Windows-Audio/GlitchDetection  |  Engine Glitch: CP Server Output Endpoint - Read Pointer Overwrite: pCCrossProcessServerOutputEndpoint=[{pCCrossProcessServerOutputEndpoint}] WriteOffset=[{WriteOffset}] ReadOffset=[{ReadOffset}] BytesToWrite=[{BytesToWrite}]
Microsoft-Windows-Audio  |  36        |  Microsoft-Windows-Audio/GlitchDetection  |  KS Endpoint Glitch: IOMGR No Outstanding Packets: pOwner=[{pOwner}] NextStreamingPacketToComplete=[{NextStreamingPacketToComplete}] MaxPacketCount=[{MaxPacketCount}]
Microsoft-Windows-Audio  |  37        |  Microsoft-Windows-Audio/GlitchDetection  |  KS Endpoint Glitch: IOMGR Ioctl Time Limit Exceeded: pOwner=[{pOwner}] DeltaHNS=[{IoctlTimeHNS}]
Microsoft-Windows-Audio  |  38        |  Microsoft-Windows-Audio/GlitchDetection  |  KS Endpoint Glitch: BASE Output Unexpected Buffer Completed: pCAudioBasePin=[{pCAudioBasePin}] LockedDataPointer=[{pLockedDataPointer}] bLockedEqualsUnrolled=[{bLockedEqualsUnrolled}]
Microsoft-Windows-Audio  |  39        |  Microsoft-Windows-Audio/GlitchDetection  |  KS Endpoint Glitch: BASE Input Null Last Buffer with LockedData != LoopedBuffer: pCAudioBasePin=[{pCAudioBasePin}] LockedDataPointer=[{LockedDataPointer}]
Microsoft-Windows-Audio  |  40        |  Microsoft-Windows-Audio/GlitchDetection  |  KS Endpoint Glitch: BASE Input Buffer Index Mismatch: pCAudioBasePin=[{pCAudioBasePin}] LockedDataPointer=[{LockedDataPointer}]
Microsoft-Windows-Audio  |  41        |  Microsoft-Windows-Audio/GlitchDetection  |  KS Endpoint Glitch: BASE End Glitch: pCAudioBasePin=[{pCAudioBasePin}] StreamPosition=[{GlitchStreamPosition}] GlitchDuration=[{GlitchDuration}]
Microsoft-Windows-Audio  |  42        |  Microsoft-Windows-Audio/GlitchDetection  |  KS Endpoint Glitch: RTCAP StreamPos Ahead of HW Pos: pCAudioCapturePinRealtimeStreaming=[{pCAudioCapturePinRealtimeStreaming}] WritePos=[{WritePosition}] PlayPos=[{PlayPosition}] StreamPos=[{StreamPosition}] StreamPosMinusReadPos=[{StreamPosMinusReadPos}]
Microsoft-Windows-Audio  |  43        |  Microsoft-Windows-Audio/GlitchDetection  |  KS Endpoint Glitch: RTCAP StreamPos Too Far Behind: pCAudioCapturePinRealtimeStreaming=[{pCAudioCapturePinRealtimeStreaming}] WritePos=[{WritePosition}] PlayPos=[{PlayPosition}] StreamPos=[{StreamPosition}] ReadPosMinusStreamPos=[{ReadPosMinusStreamPos}]
Microsoft-Windows-Audio  |  44        |  Microsoft-Windows-Audio/GlitchDetection  |  KS Endpoint Glitch: RTREN WritePos Exceeds TotalPos: pCAudioRenderPinRealtimeStreaming=[{pCAudioRenderPinRealtimeStreaming}] WritePos=[{WritePosition}] PlayPos=[{PlayPosition}] TotalPos=[{TotalPosition}] WritePosMinusTotalPos=[{WritePosMinusTotalPos}]
Microsoft-Windows-Audio  |  45        |  Microsoft-Windows-Audio/GlitchDetection  |  KS Endpoint Glitch: STCAP Capture Ahead: pCAudioCapturePinStandardStreaming=[{pCAudioCapturePinStandardStreaming}] ValidPosEnd=[{ValidPositionEnd}] ValidPosStart=[{ValidPositionStart}] StreamPos=[{StreamPosition}] StreamPosMinusValidPosEnd=[{StreamPosMinusValidPosEnd}]
Microsoft-Windows-Audio  |  46        |  Microsoft-Windows-Audio/GlitchDetection  |  KS Endpoint Glitch: STCAP Capture Behind: pCAudioCapturePinStandardStreaming=[{pCAudioCapturePinStandardStreaming}] ValidPosEnd=[{ValidPositionEnd}] ValidPosStart=[{ValidPositionStart}] StreamPos=[{StreamPosition}] ValidPosStartMinusStreamPos=[{ValidPosStartMinusStreamPos}]
Microsoft-Windows-Audio  |  47        |  Microsoft-Windows-Audio/GlitchDetection  |  KS Endpoint Glitch: STCAP Device Starved: pCAudioCapturePinStandardStreaming=[{pCAudioCapturePinStandardStreaming}] StreamPos=[{StreamPosition}] FrameCount=[{FrameCount}]
Microsoft-Windows-Audio  |  48        |  Microsoft-Windows-Audio/GlitchDetection  |  KS Endpoint Glitch: STREN Device Starved: pCAudioRenderPinStandardStreaming=[{pCAudioRenderPinStandardStreaming}] DevicePos=[{DevicePosition}] StreamPos=[{StreamPosition}] AvailFrames=[{AvailableFrames}]
Microsoft-Windows-Audio  |  49        |  Microsoft-Windows-Audio/GlitchDetection  |  KS Endpoint Glitch: STREN EXCL PULL Invalid Buffer Count: pCAudioRenderPinStandardStreaming=[{pCAudioRenderPinStandardStreaming}] DevicePos=[{DevicePosition}] StreamPos=[{StreamPosition}] AvailFrames=[{AvailableFrames}]
Microsoft-Windows-Audio  |  50        |  Microsoft-Windows-Audio/Informational    |  System effect initialized: CLSID=[{APOCLSID}] AudioSignalProcessingMode=[{AudioSignalProcessingMode}] InitializeForDiscoveryOnly=[{InitializeForDiscoveryOnly}]
Microsoft-Windows-Audio  |  51        |  Microsoft-Windows-Audio/Informational    |  Volume limit event signalled to audiosrv enter
Microsoft-Windows-Audio  |  52        |  Microsoft-Windows-Audio/Informational    |  Volume limit event signalled to audiosrv exit
Microsoft-Windows-Audio  |  53        |  Microsoft-Windows-Audio/Informational    |  AudioSrv published AVLC state
Microsoft-Windows-Audio  |  58        |  Microsoft-Windows-Audio/Informational    |  MMDevAPI: Default device changed triggered
Microsoft-Windows-Audio  |  59        |  Microsoft-Windows-Audio/Informational    |  MMDevAPI: OnMediaNotification Enter
Microsoft-Windows-Audio  |  60        |  Microsoft-Windows-Audio/Informational    |  MMDevAPI: OnMediaNotification Exit
Microsoft-Windows-Audio  |  61        |  Microsoft-Windows-Audio/Informational    |  MMDevAPI: DeviceStateChanged callback
Microsoft-Windows-Audio  |  62        |  Microsoft-Windows-Audio/Informational    |  MMDevAPI: DeviceAdded callback
Microsoft-Windows-Audio  |  63        |  Microsoft-Windows-Audio/Informational    |  MMDevAPI: DeviceRemoved callback
Microsoft-Windows-Audio  |  64        |  Microsoft-Windows-Audio/Informational    |  MMDevAPI: DefaultDeviceChanged callback
Microsoft-Windows-Audio  |  65        |  Microsoft-Windows-Audio/Operational      |  MMDevAPI: Audio device state changed
Microsoft-Windows-Audio  |  101       |  Microsoft-Windows-Audio/Informational    |  MidiRT: Application Suspension Handler
Microsoft-Windows-Audio  |  102       |  Microsoft-Windows-Audio/Informational    |  MidiRT: Application Resume Handler
Microsoft-Windows-Audio  |  103       |  Microsoft-Windows-Audio/Informational    |  MidiRT: Application Entering CS Handler
Microsoft-Windows-Audio  |  104       |  Microsoft-Windows-Audio/Informational    |  MidiRT: Application Resuming from CS Handler
Microsoft-Windows-Audio  |  105       |  Microsoft-Windows-Audio/Informational    |  MidiRT: Device Removal Handler
Microsoft-Windows-Audio  |  106       |  Microsoft-Windows-Audio/Informational    |  MidiRT: Cleanup and release device handle
Microsoft-Windows-Audio  |  107       |  Microsoft-Windows-Audio/Informational    |  MidiRT: Close handle to MIDI Device
Microsoft-Windows-Audio  |  108       |  Microsoft-Windows-Audio/Informational    |  MidiRT: Begin binding to DeviceId: {DeviceId}
Microsoft-Windows-Audio  |  109       |  Microsoft-Windows-Audio/Informational    |  MidiRT: Done binding to device interface
Microsoft-Windows-Audio  |  110       |  Microsoft-Windows-Audio/Informational    |  MidiRT: Create new MidiPortDeviceIoControl
Microsoft-Windows-Audio  |  111       |  Microsoft-Windows-Audio/Informational    |  MidiRT: Beginning Synchronous I/O
Microsoft-Windows-Audio  |  112       |  Microsoft-Windows-Audio/Informational    |  MidiRT: Done with synchronous I/O
Microsoft-Windows-Audio  |  113       |  Microsoft-Windows-Audio/Informational    |  MidiRT: Beginning Asynchronous I/O
Microsoft-Windows-Audio  |  114       |  Microsoft-Windows-Audio/Informational    |  MidiRT: Done with Asynchronous I/O
Microsoft-Windows-Audio  |  115       |  Microsoft-Windows-Audio/Informational    |  CrossProcess packet added
Microsoft-Windows-Audio  |  116       |  Performance                              |  Pump: setting deadline
Microsoft-Windows-Audio  |  117       |  Performance                              |  Pump: cancelling deadline
Microsoft-Windows-Audio  |  118       |  Performance                              |  Pump: missed deadline!
Microsoft-Windows-Audio  |  119       |  Performance                              |  Pump: Start - setting MultimediMode to AVRT_MULTIMEDIA_MODE_BUFFERING
Microsoft-Windows-Audio  |  120       |  Performance                              |  Pump: Stop - setting MultimediMode to AVRT_MULTIMEDIA_MODE_IDLE
Microsoft-Windows-Audio  |  121       |  Performance                              |  Discovering EndpointCharacteristics for [{Endpoint Id}]
Microsoft-Windows-Audio  |  122       |  Performance                              |  Discovered EndpointCharacteristics for [{Endpoint Id}] (hr = {hr})
Microsoft-Windows-Audio  |  123       |  Performance                              |  GetMixFormat starting on endpoint [{Endpoint Id}] (category={category}, raw={Raw}, matchformat={MatchFormat}, connector={ConnectorType})
Microsoft-Windows-Audio  |  124       |  Performance                              |
Microsoft-Windows-Audio  |  125       |  Performance                              |  IsFormatSupported starting on endpoint [{Endpoint Id}] (category={category}, raw={Raw}, matchformat={MatchFormat}, connector={ConnectorType})
Microsoft-Windows-Audio  |  126       |  Performance                              |
Microsoft-Windows-Audio  |  127       |  Performance                              |  Vadserver_CreateStream starting on endpoint [{Endpoint Id}] (category={category}, raw={Raw}, matchformat={MatchFormat}, connector={ConnectorType})
Microsoft-Windows-Audio  |  128       |  Performance                              |
Microsoft-Windows-Audio  |  129       |  Performance                              |
Microsoft-Windows-Audio  |  130       |  Performance                              |
Microsoft-Windows-Audio  |  131       |  Performance                              |
Microsoft-Windows-Audio  |  132       |  Performance                              |
Microsoft-Windows-Audio  |  133       |  Performance                              |  CreateDeviceEndpointInstance starting on endpoint [{Endpoint Id}] (connector={ConnectorType})
Microsoft-Windows-Audio  |  134       |  Performance                              |