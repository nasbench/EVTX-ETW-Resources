Provider                       |  Event ID  |  Channel                       |  Message
-------------------------------|------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-MediaEngine  |  100       |  Media Foundation MediaEngine  |  TransferFrame Start id({id})
Microsoft-Windows-MediaEngine  |  101       |  Media Foundation MediaEngine  |  TransferFrame Stop id({id}) hr({hr})
Microsoft-Windows-MediaEngine  |  102       |  Media Foundation MediaEngine  |  TransferFrameRemote Start id({id})
Microsoft-Windows-MediaEngine  |  103       |  Media Foundation MediaEngine  |  TransferFrameRemote Stop id({id}) hr({hr})
Microsoft-Windows-MediaEngine  |  104       |  Media Foundation MediaEngine  |  Initialize id({id}) hr({hr})
Microsoft-Windows-MediaEngine  |  105       |  Media Foundation MediaEngine  |  Created id({id})
Microsoft-Windows-MediaEngine  |  106       |  Media Foundation MediaEngine  |  PlaybackRateChange id({id}) hr({rate})
Microsoft-Windows-MediaEngine  |  107       |  Media Foundation MediaEngine  |  Play Start id({id})
Microsoft-Windows-MediaEngine  |  108       |  Media Foundation MediaEngine  |  Play Stop id({id}) hr({hr})
Microsoft-Windows-MediaEngine  |  109       |  Media Foundation MediaEngine  |  Pause Start id({id})
Microsoft-Windows-MediaEngine  |  110       |  Media Foundation MediaEngine  |  Pause Stop id({id}) hr({hr})
Microsoft-Windows-MediaEngine  |  111       |  Media Foundation MediaEngine  |  Seek Start id({id})
Microsoft-Windows-MediaEngine  |  112       |  Media Foundation MediaEngine  |  Seek Stop id({id}) hr({hr})
Microsoft-Windows-MediaEngine  |  113       |  Media Foundation MediaEngine  |  Destroyed id({id})
Microsoft-Windows-MediaEngine  |  114       |  Media Foundation MediaEngine  |  Dropped Frame id({id}) location({location}) pts({pts}) clock({clock})
Microsoft-Windows-MediaEngine  |  115       |  Media Foundation MediaEngine  |  Presented Frame id({id}) pts({pts}) clock({clock})
Microsoft-Windows-MediaEngine  |  116       |  Media Foundation MediaEngine  |  PresentAt({object}): Submitted frame pts({sampleTime}) QPC({QPC})
Microsoft-Windows-MediaEngine  |  117       |  Media Foundation MediaEngine  |  PresentAt({object}): Queued frame pts({sampleTime}) QPC({QPC}) QPC_snapped({QPC_snapped}) Flags({PresentFlags})
Microsoft-Windows-MediaEngine  |  118       |  Media Foundation MediaEngine  |  PresentAt({object}): Presented frame pts({sampleTime}) QPC_target({QPC_target}) QPC_actual({QPC_actual})
Microsoft-Windows-MediaEngine  |  119       |  Media Foundation MediaEngine  |  PresentAt({object}): Video frame glitch pts({sampleTime}) FramesLate({FramesLate})
Microsoft-Windows-MediaEngine  |  120       |  Media Foundation MediaEngine  |  PresentAt({object}) Sleep Start
Microsoft-Windows-MediaEngine  |  121       |  Media Foundation MediaEngine  |  PerfTrack: Media Foundation Play: object({object})
Microsoft-Windows-MediaEngine  |  123       |  Media Foundation MediaEngine  |  PerfTrack: Media Foundation Play Cancelled: object({object})
Microsoft-Windows-MediaEngine  |  125       |  Media Foundation MediaEngine  |  PerfTrack: First Frame After Play Presented: object({object})
Microsoft-Windows-MediaEngine  |  127       |  Media Foundation MediaEngine  |  PresentAt({object}): QueueStats Len({Length}) Queued({MaxPresentLatency}) Free({Queued}) DeltaToTarget({QueuedWithRepeats} ms) SubmittedAheadDelta({EstimatedFramesNeeded} ms) TimeInQueue({Free} ms) MinLatency({DeltaToTarget} ms) MaxLatency({SubmittedAheadDelta} ms) FramePeriod ({object}0 us)
Microsoft-Windows-MediaEngine  |  128       |  Media Foundation MediaEngine  |  Suspended id({id}) paused({paused})
Microsoft-Windows-MediaEngine  |  129       |  Media Foundation MediaEngine  |  Restored id({id}) resumed({resumed})
Microsoft-Windows-MediaEngine  |  130       |  Media Foundation MediaEngine  |  Not visible id({id}) thinning({thinning})
Microsoft-Windows-MediaEngine  |  131       |  Media Foundation MediaEngine  |  Not visible timer id({id}) thinning({thinning})
Microsoft-Windows-MediaEngine  |  132       |  Media Foundation MediaEngine  |  Visible id({id}) resumed({resumed})
Microsoft-Windows-MediaEngine  |  133       |  Media Foundation MediaEngine  |  Set GPU Priority id({id}) priority({priority})
Microsoft-Windows-MediaEngine  |  134       |  Media Foundation MediaEngine  |  PerfTrack: Video Glitch - ({NumGlitches}) frames glitched
Microsoft-Windows-MediaEngine  |  135       |  Media Foundation MediaEngine  |  Save image: object({object})
Microsoft-Windows-MediaEngine  |  136       |  Media Foundation MediaEngine  |  Save image: object({object}) native resolution ({NativeWidth}x{NativeHeight}) encoded resolution ({EncodedWidth}x{EncodedHeight}) encoded size ({EncodedSize}B) error code ({ErrorCode})
Microsoft-Windows-MediaEngine  |  137       |  Media Foundation MediaEngine  |  SetSource operation: object({object})
Microsoft-Windows-MediaEngine  |  138       |  Media Foundation MediaEngine  |  SetSource operatione: object({object}) error code ({ErrorCode})
Microsoft-Windows-MediaEngine  |  139       |  Media Foundation MediaEngine  |  PresentAt({object}): Video frame early pts({sampleTime}) FramesEarly({FramesEarly})
Microsoft-Windows-MediaEngine  |  140       |  Media Foundation MediaEngine  |  PresentAt({object}): ProcessVSync QPC_Prev({QPC_Prev} us) frames({Delta_us}) frameIndex( {Delta_Frames} ) framerate( {DeltaPerFrame_us} ) QPC_Actual ( {RatioToPrimary} us) QPC_Smoothed ( {InputFrameIndex} us)
Microsoft-Windows-MediaEngine  |  141       |  Media Foundation MediaEngine  |  GetCorrelatedTimeStart Object( {object} )
Microsoft-Windows-MediaEngine  |  142       |  Media Foundation MediaEngine  |  PresentAt({object}): IgnoreVSync QPC( {QPC} us) Delta( {Delta} us) frames( {Frames} )
Microsoft-Windows-MediaEngine  |  143       |  Media Foundation MediaEngine  |  RequestNetwork: object({object}) requested({Requested}) refcount({ReferenceCounter})
Microsoft-Windows-MediaEngine  |  144       |  Media Foundation MediaEngine  |  Batch start: object({object})
Microsoft-Windows-MediaEngine  |  145       |  Media Foundation MediaEngine  |  Batch end: object({object})
Microsoft-Windows-MediaEngine  |  146       |  Media Foundation MediaEngine  |  Decode Swapchain Created: object({object}) swapchain({Swapchain}) texture array({TextureArray})
Microsoft-Windows-MediaEngine  |  147       |  Media Foundation MediaEngine  |  YUV Swapchain Configured: object({object}) swapchain({Swapchain}) srcRect={SrcRect_Left},{SrcRect_Top},{SrcRect_Right},{SrcRect_Bottom} dstRect={DstRect_Left},{DstRect_Top},{DstRect_Right},{object}0 dstSize={object}1x{object}2
Microsoft-Windows-MediaEngine  |  148       |  Media Foundation MediaEngine  |  Decode Swapchain Destroyed: object({object}) swapchain({Swapchain}) swapchain state({SwapchainState})
Microsoft-Windows-MediaEngine  |  149       |  Media Foundation MediaEngine  |  Decode Swapchain Not Used: object({object}) swapchain state({SwapchainState})
Microsoft-Windows-MediaEngine  |  151       |  Media Foundation MediaEngine  |  Format Invalidated Seek id({id}), time({rate})
Microsoft-Windows-MediaEngine  |  152       |  Media Foundation MediaEngine  |  SVRSink({object}): GlitchCount={NumGlitches} SampleTime={SampleTime} GlitchDuration={GlitchDuration}
Microsoft-Windows-MediaEngine  |  153       |  Media Foundation MediaEngine  |  Content Frame Rate Detected: object({object}) frame duration({FrameDuration})
Microsoft-Windows-MediaEngine  |  154       |  Media Foundation MediaEngine  |  Custom Refresh Rate Requested: object({object}) frame duration({FrameDuration}) requested present duration({RefreshDuration})
Microsoft-Windows-MediaEngine  |  155       |  Media Foundation MediaEngine  |  Custom Refresh Rate Enabled: object({object}) requested present duration({RequestedRefreshDuration}) actual present duration({ActualRefreshDuration})
Microsoft-Windows-MediaEngine  |  156       |  Media Foundation MediaEngine  |  Custom Refresh Rate Disabled: object({object}) reason ({State})
Microsoft-Windows-MediaEngine  |  157       |  Media Foundation MediaEngine  |  Custom Refresh Rate State Change: object({object}) state ({State})
Microsoft-Windows-MediaEngine  |  158       |  Media Foundation MediaEngine  |  VRSink({object}): UpdateVideo dst=({Dst_left},{Dst_top},{Dst_right},{Dst_bottom}) src=({Src_left},{Src_top},{Src_right},{Src_bottom}) flags={object}0
Microsoft-Windows-MediaEngine  |  159       |  Media Foundation MediaEngine  |  Normal (non-decode) Swapchain Created: object({object}) swapchain({Swapchain}) format({Format}) width({Width}) height({Height}) backbuffers({Backbuffers}) flags({Flags}) colorspacetype({ColorSpaceType}) swapchaintype({SwapChainType}) swapchainrotation({object}0)
Microsoft-Windows-MediaEngine  |  160       |  Media Foundation MediaEngine  |  Sample Received object({object}) sample({Sample}) Timestamp({TimeStamp}) Duration({Duration}) FirstFrame({FirstFrameReady}) Dropped({Dropped})
Microsoft-Windows-MediaEngine  |  161       |  Media Foundation MediaEngine  |  PurgedFrames object({object}) count({Count})
Microsoft-Windows-MediaEngine  |  162       |  Media Foundation MediaEngine  |  YUVSwapchainQueue object({object}) count({Count})
Microsoft-Windows-MediaEngine  |  163       |  Media Foundation MediaEngine  |  GPU Wait object({object})
Microsoft-Windows-MediaEngine  |  164       |  Media Foundation MediaEngine  |  GPUSwapchainWaitStop object({object})
Microsoft-Windows-MediaEngine  |  165       |  Media Foundation MediaEngine  |  GetPresentStats object({object})
Microsoft-Windows-MediaEngine  |  166       |  Media Foundation MediaEngine  |  PruneHistory object({object}) PresentCount({PresentCount})
Microsoft-Windows-MediaEngine  |  167       |  Media Foundation MediaEngine  |  PresentAt({object}): InitVSyncRefreshRate framerate {object} reason {FrameRate}
Microsoft-Windows-MediaEngine  |  168       |  Media Foundation MediaEngine  |  ClockSmooth Object( {object} ) ts0({ClockTime0_us} us) qpc0( {QPC0_us} ) qpc0_new ( {SmoothedQPC0_us} us) Delta( {QPCDelta_us} us)
Microsoft-Windows-MediaEngine  |  169       |  Media Foundation MediaEngine  |  QuantizeFrame object({object}) sample time {sampleTime_us} orig {OrigTargetQPC_us} target {TargetQPC_us} diff {DeltaQPC_us}
Microsoft-Windows-MediaEngine  |  170       |  Media Foundation MediaEngine  |  updatelongrunning object({object}) state({newState})
Microsoft-Windows-MediaEngine  |  171       |  Media Foundation MediaEngine  |  MapSample Object( {object} ) QPC_now({QPCnow_us} us) rate( {rate} ) ClockTime0( {ClockTime0_us} us) QPC0( {QPC0_us} us) SampleTime ( {SampleTime_us} us) SampleQPC ( {SampleQPC_us} us)
Microsoft-Windows-MediaEngine  |  172       |  Media Foundation MediaEngine  |  GetCorrelatedTimeStop Object( {object} ) QPC_now({QPCnow_us} us) ClockTime0( {ClockTime0_us} us) QPC0( {QPC0_us} us)
Microsoft-Windows-MediaEngine  |  173       |  Media Foundation MediaEngine  |  PresentAt({object}): ProcessFlipMode LastQueuedQPC({SampleTime} us) TargetQPC({LastQueuedStartQPC}) frames( {TargetQPC} ) adjust( {nowQPC} )
Microsoft-Windows-MediaEngine  |  174       |  Media Foundation MediaEngine  |  ShiftSample Object( {object} ) SampleQPC ( {QPCtarget_us} us) Delta( {Delta_us} us) AverageLateness ( {Delta_us} us)
Microsoft-Windows-MediaEngine  |  175       |  Media Foundation MediaEngine  |  MinLatencyDone object({object}) time remaining({TimeRemaining})
Microsoft-Windows-MediaEngine  |  176       |  Media Foundation MediaEngine  |  VRSink({object}): MirrorVideo old={old} new={new} hr={hr}
Microsoft-Windows-MediaEngine  |  177       |  Media Foundation MediaEngine  |  updatedeadline object({object}) deadline({deadline}) delta({hnsDeltaFromNow})
Microsoft-Windows-MediaEngine  |  178       |  Media Foundation MediaEngine  |  GetEngineStatistics Start id({id})
Microsoft-Windows-MediaEngine  |  179       |  Media Foundation MediaEngine  |  GetEngineStatistics Stop id({id}) hr({hr})
Microsoft-Windows-MediaEngine  |  180       |  Media Foundation MediaEngine  |  SVRSink({object}): Count={RequestsPending} FrameQueueCount={FrameQueueCount}
Microsoft-Windows-MediaEngine  |  181       |  Media Foundation MediaEngine  |  PresentAt({object}): GPUBoost timetodeadline ( {TimeToDeadline_us} us)
Microsoft-Windows-MediaEngine  |  182       |  Media Foundation MediaEngine  |  PresentAt({object}): AddHistoryRecord pRecord({pRecord}) ListLength({ListCount}) DecodeYUV({DecodeYUV}) FrameCount({FrameCount}) PresentCount({PresentCount}) Repeat({Repeat}) SampleTime ({SampleTime}) TargetQPC ({TargetQPC})
Microsoft-Windows-MediaEngine  |  183       |  Media Foundation MediaEngine  |  PresentAt({object}): RemoveHistoryRecord pRecord({pRecord}) PresentCount({PresentCount})
Microsoft-Windows-MediaEngine  |  184       |  Media Foundation MediaEngine  |  ClearHistory object({object}) listLen({ListCount}) location({Location})
Microsoft-Windows-MediaEngine  |  185       |  Media Foundation MediaEngine  |  ME GetCurrentTimeStart Object( {object} )
Microsoft-Windows-MediaEngine  |  186       |  Media Foundation MediaEngine  |  GetCurrentTimeStop Object( {object} ) now({now} us)
Microsoft-Windows-MediaEngine  |  187       |  Media Foundation MediaEngine  |  updateGPUdeadline object({object}) dxobject({DXObject}) dxtype({DXType}) deadline({deadline}) deltaFromNow({hnsDeltaFromNow})
Microsoft-Windows-MediaEngine  |  188       |  Media Foundation MediaEngine  |  PresentAt({object}): ComputeRatioToPrimary object {object} ratio {Ratio} x100 {Ratio_x100}
Microsoft-Windows-MediaEngine  |  189       |  Media Foundation MediaEngine  |  PresentAt({object}): UpdateRatioToPrimary object {object} ratio {Ratio}
Microsoft-Windows-MediaEngine  |  190       |  Media Foundation MediaEngine  |  YUVSwapchainQueueDrain_Start object({object}) count({Count})
Microsoft-Windows-MediaEngine  |  191       |  Media Foundation MediaEngine  |  YUVSwapchainQueueDrain_Stop object({object}) count({Count})
Microsoft-Windows-MediaEngine  |  200       |  Media Foundation MediaEngine  |  NeedKey: length({length}) data({data})
Microsoft-Windows-MediaEngine  |  201       |  Media Foundation MediaEngine  |  Create MediaKeys: key system({keysystem}) default cdm store path ({defaultCdmStorePath}) inprivate cdm store path ({inprivateCdmStorePath}) MediaKeys object({object}) error code({ErrorCode})
Microsoft-Windows-MediaEngine  |  202       |  Media Foundation MediaEngine  |  Create MediaKeySession:  session id({sessionId}) key system({keySystem}) type({type}) length({length}) init data({data}) error code({ErrorCode})
Microsoft-Windows-MediaEngine  |  203       |  Media Foundation MediaEngine  |  Close MediaKeySession: session id({sessionId})
Microsoft-Windows-MediaEngine  |  204       |  Media Foundation MediaEngine  |  KeyMessage: session id({sessionId}) destination URL({url}) length({length}) data({data})
Microsoft-Windows-MediaEngine  |  205       |  Media Foundation MediaEngine  |  KeyError: session id({sessionId}) code({code}) systemcode({systemError})
Microsoft-Windows-MediaEngine  |  206       |  Media Foundation MediaEngine  |  KeyAdded: session id({sessionId})
Microsoft-Windows-MediaEngine  |  207       |  Media Foundation MediaEngine  |  Update: session id({sessionId}) length({length}) data({data}) error code({ErrorCode})
Microsoft-Windows-MediaEngine  |  208       |  Media Foundation MediaEngine  |  put keys attribute value ({object})
Microsoft-Windows-MediaEngine  |  209       |  Media Foundation MediaEngine  |  BeginEnableContent: enabler type({enable type}) error code({ErrorCode})
Microsoft-Windows-MediaEngine  |  210       |  Media Foundation MediaEngine  |  EndEnableContent: error code({ErrorCode})
Microsoft-Windows-MediaEngine  |  212       |  Media Foundation MediaEngine  |  BatchingReason: object({object}) ok({Ok}) bits({Bits}) fullscreenpercent({FullScreenPercent}) fullscreenthreshold({FullScreenThreshold})
Microsoft-Windows-MediaEngine  |  213       |  Media Foundation MediaEngine  |  MediaBuffer({buffer}) sampleTime({sampleTime}) sampleDuration({sampleDuration})
Microsoft-Windows-MediaEngine  |  214       |  Media Foundation MediaEngine  |  Playback has reached the end of the source
Microsoft-Windows-MediaEngine  |  215       |  Media Foundation MediaEngine  |  PresentAt({object}) PresentDelayStart
Microsoft-Windows-MediaEngine  |  216       |  Media Foundation MediaEngine  |  PresentTimerStart: object({Object}) period({Period} hns)
Microsoft-Windows-MediaEngine  |  217       |  Media Foundation MediaEngine  |  PresentTimerStop: object({Object}) period({Period} hns)
Microsoft-Windows-MediaEngine  |  218       |  Media Foundation MediaEngine  |  PresentTimeCriticalStart: object({Object}) period({TimeDelta} hns)
Microsoft-Windows-MediaEngine  |  219       |  Media Foundation MediaEngine  |  PresentTimeCriticalStop: object({Object}) period({TimeDelta} hns)
Microsoft-Windows-MediaEngine  |  220       |  Media Foundation MediaEngine  |  TimedTextDtvCCSample Decode Start
Microsoft-Windows-MediaEngine  |  221       |  Media Foundation MediaEngine  |  TimedTextDtvCCSample Decode Stop
Microsoft-Windows-MediaEngine  |  222       |  Media Foundation MediaEngine  |  TimedTextSendCue Start
Microsoft-Windows-MediaEngine  |  223       |  Media Foundation MediaEngine  |  TimedTextSendCue Received
Microsoft-Windows-MediaEngine  |  224       |  Media Foundation MediaEngine  |
Microsoft-Windows-MediaEngine  |  225       |  Media Foundation MediaEngine  |
Microsoft-Windows-MediaEngine  |  226       |  Media Foundation MediaEngine  |
Microsoft-Windows-MediaEngine  |  227       |  Media Foundation MediaEngine  |
Microsoft-Windows-MediaEngine  |  228       |  Media Foundation MediaEngine  |
Microsoft-Windows-MediaEngine  |  229       |  Media Foundation MediaEngine  |
Microsoft-Windows-MediaEngine  |  230       |  Media Foundation MediaEngine  |
Microsoft-Windows-MediaEngine  |  231       |  Media Foundation MediaEngine  |
Microsoft-Windows-MediaEngine  |  232       |  Media Foundation MediaEngine  |
Microsoft-Windows-MediaEngine  |  233       |  Media Foundation MediaEngine  |
Microsoft-Windows-MediaEngine  |  234       |  Media Foundation MediaEngine  |
Microsoft-Windows-MediaEngine  |  235       |  Media Foundation MediaEngine  |
Microsoft-Windows-MediaEngine  |  236       |  Media Foundation MediaEngine  |  Resized swapchain: width({Width}) height({Height}) length({Backbuffers}) format({Format}) flags({Flags})
Microsoft-Windows-MediaEngine  |  237       |  Media Foundation MediaEngine  |  Remove MediaKeySession: session id({sessionId})
Microsoft-Windows-MediaEngine  |  238       |  Media Foundation MediaEngine  |  GenerateRequest MediaKeySession: session id({sessionId})
Microsoft-Windows-MediaEngine  |  239       |  Media Foundation MediaEngine  |  Load MediaKeySession: session id({sessionId})
Microsoft-Windows-MediaEngine  |  240       |  Media Foundation MediaEngine  |  Encrypted: length({length}) data({data})
Microsoft-Windows-MediaEngine  |  241       |  Media Foundation MediaEngine  |  Create MediaKeySession: session type({SessionType}) key system({keySystem}) usedistinctive({UseDistinctiveIdentifier})
Microsoft-Windows-MediaEngine  |  242       |  Media Foundation MediaEngine  |  KeyMessage2: messageType({sessionId}) session id({MessageType}) destination URL({url}) length({length}) data({data})
Microsoft-Windows-MediaEngine  |  243       |  Media Foundation MediaEngine  |  KeyStatusChange MediaKeySession: session id({sessionId})
Microsoft-Windows-MediaEngine  |  244       |  Media Foundation MediaEngine  |  MediaKeysSerServerCertificate: length({length}) data({data})
Microsoft-Windows-MediaEngine  |  245       |  Media Foundation MediaEngine  |  Create MediaKeys2: key system({keysystem}) CDMAccess ({CDMAccess}) CDMConfig ({CDMCustomConfig}) MediaKeys object({MediaKeysObject}) SoftwareOverride({SoftwareOverride})
Microsoft-Windows-MediaEngine  |  246       |  Media Foundation MediaEngine  |  Create MediaKeys2: key system({keysystem}) configCount ({configCount}) selectedConfigCount ({selectedConfigCount}) MediaKeySystemAccess object({object})
Microsoft-Windows-MediaEngine  |  247       |  Media Foundation MediaEngine  |  PresentRestart: object({Object}) presentcount({PresentCount})
Microsoft-Windows-MediaEngine  |  248       |  Media Foundation MediaEngine  |  Display rotation:({Rotation})
Microsoft-Windows-MediaEngine  |  249       |  Media Foundation MediaEngine  |  DecodeSwapchainState: object({object}) state({DecodeSwapchainState})
Microsoft-Windows-MediaEngine  |  250       |  Media Foundation MediaEngine  |  ConfigureSwapchain: object({object}) isdecode({IsDecode}) format({DxgiFormat}) colorspace({Width}) flags({Height})
Microsoft-Windows-MediaEngine  |  251       |  Media Foundation MediaEngine  |  MMCSSRequestStart: object({Object})
Microsoft-Windows-MediaEngine  |  252       |  Media Foundation MediaEngine  |  MMCSSRequestStop: object({Object})
Microsoft-Windows-MediaEngine  |  253       |  Media Foundation MediaEngine  |  ScrubbingState: ({ScrubbingState})
Microsoft-Windows-MediaEngine  |  254       |  Media Foundation MediaEngine  |  DXPresent_Start: object({Object}) index({Index}) interval({Inverval}) flags({Flags})
Microsoft-Windows-MediaEngine  |  255       |  Media Foundation MediaEngine  |  DXPresent_Stop: object({Object}) index({Index}) hrResult({hrResult})
Microsoft-Windows-MediaEngine  |  256       |  Media Foundation MediaEngine  |  EnumMonitors_Start: object({Object})
Microsoft-Windows-MediaEngine  |  257       |  Media Foundation MediaEngine  |  EnumMonitors_Stop: object({Object})
Microsoft-Windows-MediaEngine  |  258       |  Media Foundation MediaEngine  |  HandleMonitorChange_Start: object({Object})
Microsoft-Windows-MediaEngine  |  259       |  Media Foundation MediaEngine  |  HandleMonitorChange_Stop: object({Object})
Microsoft-Windows-MediaEngine  |  260       |  Media Foundation MediaEngine  |  ProcessIdleTasks_Start: object({Object})
Microsoft-Windows-MediaEngine  |  261       |  Media Foundation MediaEngine  |  ProcessIdleTasks_Stop: object({Object})
Microsoft-Windows-MediaEngine  |  262       |  Media Foundation MediaEngine  |  DXWorkComplete_Start: object({Object}) sample({Sample})
Microsoft-Windows-MediaEngine  |  263       |  Media Foundation MediaEngine  |  DXWorkComplete_Stop: object({Object}) sample({Sample}) hrResult({hrResult})
Microsoft-Windows-MediaEngine  |  264       |  Media Foundation MediaEngine  |  Spherical video enabled ({IsEnabled}) format({Format}) projectionMode({ProjectionMode})
Microsoft-Windows-MediaEngine  |  265       |  Media Foundation MediaEngine  |  Spherical video properties. ViewDirection: W({Quaternion.W}) X({Quaternion.X}) Y({Quaternion.Y}) Z({Quaternion.Z}) fieldOfView({FieldOfView})
Microsoft-Windows-MediaEngine  |  266       |  Media Foundation MediaEngine  |  Profile check: present({Present}) value({DcValue}) provisioned({Provisioned}) mem({QoS})
Microsoft-Windows-MediaEngine  |  267       |  Media Foundation MediaEngine  |  SetHDRMetadata display metadata ({IsDisplayMetadata}) min_luminance ({MinLuminance}) max_luminance ({MaxLuminance})
Microsoft-Windows-MediaEngine  |  268       |  Media Foundation MediaEngine  |  EDRStateChanged enabled ({Enabled}) IsAC ({IsAC}) IsMediaOptimizedForDisplayQuality ({IsMediaOptimizedForDisplayQuality}) IsLowerScreenBrightnessActive ({IsLowerScreenBrightnessActive}) IsBrightnessPolicyActive({IsBrightnessPolicyActive}) max_content_luminance ({ContentMaxLuminance}) max_display_luminance ({DisplayMaxLuminance})
Microsoft-Windows-MediaEngine  |  269       |  Media Foundation MediaEngine  |  PresentAt({object}) Sleep Stop
Microsoft-Windows-MediaEngine  |  270       |  Media Foundation MediaEngine  |  PresentAt({object}) ProcessFrame Start
Microsoft-Windows-MediaEngine  |  271       |  Media Foundation MediaEngine  |  PresentAt({object}) ProcessFrame Stop
Microsoft-Windows-MediaEngine  |  272       |  Media Foundation MediaEngine  |  WindowResizeOptimizationStart Object( {object} )
Microsoft-Windows-MediaEngine  |  273       |  Media Foundation MediaEngine  |  WindowResizeOptimizationStop Object( {object} )
Microsoft-Windows-MediaEngine  |  274       |  Media Foundation MediaEngine  |  ProcessIdleEDRTasks_Start: object({Object})
Microsoft-Windows-MediaEngine  |  275       |  Media Foundation MediaEngine  |  ProcessIdleEDRTasks_Stop: object({Object})
Microsoft-Windows-MediaEngine  |  276       |  Media Foundation MediaEngine  |  ProcessPolicyEvent_Start: object({Object})
Microsoft-Windows-MediaEngine  |  277       |  Media Foundation MediaEngine  |  ProcessPolicyEvent_Stop: object({Object})
Microsoft-Windows-MediaEngine  |  278       |  Media Foundation MediaEngine  |  PresentAt({object}): Delay({Delay} ms) TimeToDeadline({TimeToDeadline} hns) Location({Location})
Microsoft-Windows-MediaEngine  |  279       |  Media Foundation MediaEngine  |  PresentAt({object}) UpdateHistoryStart
Microsoft-Windows-MediaEngine  |  280       |  Media Foundation MediaEngine  |  PresentAt({object}) UpdateHistoryStop
Microsoft-Windows-MediaEngine  |  281       |  Media Foundation MediaEngine  |  CallMarshaling: call started - object({Object}) call id({CallId}) id({Id})
Microsoft-Windows-MediaEngine  |  282       |  Media Foundation MediaEngine  |  CallMarshaling: call returned - object({Object}) call id({CallId}) id({Id}) hresult({hrResult})
Microsoft-Windows-MediaEngine  |  283       |  Media Foundation MediaEngine  |  CallMarshaling: call started - object({Object}) call id({CallId}) id({Id})
Microsoft-Windows-MediaEngine  |  284       |  Media Foundation MediaEngine  |  CallMarshaling: call returned - object({Object}) call id({CallId}) id({Id}) hresult({hrResult})
Microsoft-Windows-MediaEngine  |  285       |  Media Foundation MediaEngine  |  Long call detected: object({Object}) call id({CallId}) id({Id}) start({Start}) now({Now})
Microsoft-Windows-MediaEngine  |  286       |  Media Foundation MediaEngine  |  Call marshaling slots are full: object({Object})
Microsoft-Windows-MediaEngine  |  287       |  Media Foundation MediaEngine  |  FrameNotPresented object({object}) timestamps({Timestamp})
Microsoft-Windows-MediaEngine  |  288       |  Media Foundation MediaEngine  |  PresentedContentPresentationHandler Created object({Object}), resourceManagerObject({ResourceManagerObject})
Microsoft-Windows-MediaEngine  |  289       |  Media Foundation MediaEngine  |  PresentedContentPresentationHandler_ResourcesAllocated object({object}) format({Format}) width({Width}) height({Height}) bufferCount({bufferCount}) miscFlags({MiscFlags})
Microsoft-Windows-MediaEngine  |  290       |  Media Foundation MediaEngine  |  PresentedContentPresentationHandler_Bind object({object}) bufferCount({bufferCount}) format({Format}) colorSpaceType({colorSpaceType}) isHWProtected({isHWProtected}) width({width}) height({height})
Microsoft-Windows-MediaEngine  |  291       |  Media Foundation MediaEngine  |  PresentedContentPresentationHandler_PresentSubmitted object({object}) presentID({presentId}) sampleTime({sampleTime}) targetTime({targetTime}) ahead({Ahead})