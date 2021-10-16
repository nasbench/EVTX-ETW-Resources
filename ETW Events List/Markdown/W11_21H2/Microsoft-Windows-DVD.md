Provider               |  Event ID  |  Channel        |  Message
-----------------------|------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-DVD  |  1         |  DVD Navigator  |  Nav SendSample Object={Object} treamID={Object} StreamType={StreamID} IsRunning={StreamType} rtTimestamp={IsRunning} rtNow={rtTimestamp} rtAhead={rtNow} SyncPoint={SyncPoint} TimeDisc={TimeDisc}
Microsoft-Windows-DVD  |  2         |  DVD Navigator  |  Nav BeginFlush object={Object}
Microsoft-Windows-DVD  |  3         |  DVD Navigator  |  Nav EndFlush object={Object}
Microsoft-Windows-DVD  |  5         |  DVD Navigator  |  Nav StillTimerOn object={Object} time={Duration}
Microsoft-Windows-DVD  |  6         |  DVD Navigator  |  Nav StillTimerOff object={Object} time={Duration}
Microsoft-Windows-DVD  |  7         |  DVD Navigator  |  Nav ParsePCI object={Object} wStreamID={HaveRun} type={IsRunning} fIsRunning={UsedGetTime} rtStart={SetTimeToNow} rtNow={CellTimeDisc} rtDistAheadOfClock={rtNow}
Microsoft-Windows-DVD  |  8         |  DVD Navigator  |  Nav Throttle start object={Object} dur={Duration} max_lat={Max Latency}
Microsoft-Windows-DVD  |  9         |  DVD Navigator  |  Nav Throttle end object={Object}
Microsoft-Windows-DVD  |  10        |  DVD Navigator  |  Nav PumpWait start object={Object} handleMask={HandleMask}
Microsoft-Windows-DVD  |  11        |  DVD Navigator  |  Nav PumpWait end object={Object} WakeIndex={WakeIndex} Error={LastError} IOIndex={IOIndex} ExtraInfo={ExtraEventInfo}
Microsoft-Windows-DVD  |  12        |  DVD Navigator  |  Nav SendEventNotification object={Object} type={Type} param1={Param1} param2={Param2}
Microsoft-Windows-DVD  |  13        |  DVD Navigator  |  Nav DomainChange object={Object} domain={Domain} VTSN={VTSN}
Microsoft-Windows-DVD  |  14        |  DVD Navigator  |  Nav SendErrorNotification object={Object} param1={Param1} param2={Param2}
Microsoft-Windows-DVD  |  15        |  DVD Navigator  |  Nav StartStreamingStart object={Object}
Microsoft-Windows-DVD  |  16        |  DVD Navigator  |  Nav StartStreamingStop object={Object}
Microsoft-Windows-DVD  |  17        |  DVD Navigator  |  Nav CreateFileStart filename={Object}
Microsoft-Windows-DVD  |  18        |  DVD Navigator  |  Nav CreateFileStop hr={Object}
Microsoft-Windows-DVD  |  19        |  DVD Navigator  |  Nav MutexLockStart lock={Object}
Microsoft-Windows-DVD  |  20        |  DVD Navigator  |  Nav MutexLockStop lock={Object}
Microsoft-Windows-DVD  |  21        |  DVD Navigator  |  Nav SpinDownStart drive {DriveLetter}
Microsoft-Windows-DVD  |  22        |  DVD Navigator  |  Nav SpinDownStop hr {hr}
Microsoft-Windows-DVD  |  23        |  DVD Navigator  |  Nav CheckRegionStart obj={Object} drive {CSSEnabled}
Microsoft-Windows-DVD  |  24        |  DVD Navigator  |  Nav CheckRegionStop obj={Object} hr {hr}
Microsoft-Windows-DVD  |  25        |  DVD Navigator  |  Nav NegotiateDiscKeyStart obj={Object}
Microsoft-Windows-DVD  |  26        |  DVD Navigator  |  Nav NegotiateDiscKeyStop obj={Object} hr {hr}
Microsoft-Windows-DVD  |  27        |  DVD Navigator  |  Nav SetCurrentLatency obj={Object} old {old} attempted {attempted} new {new}
Microsoft-Windows-DVD  |  28        |  DVD Navigator  |  Nav NegotiateTitleKeyStart obj={Object} size {FileSizeInBlocks} offset {FileOffsetHint} ignoreerrors {IgnoreKeyFailures}
Microsoft-Windows-DVD  |  29        |  DVD Navigator  |  Nav NegotiateTitleKeyStop obj={Object} hr {hr}
Microsoft-Windows-DVD  |  30        |  DVD Navigator  |  Nav NegotiateTitleKeyStreamStart obj={Object} stream {StreamID} sector {Sector}
Microsoft-Windows-DVD  |  31        |  DVD Navigator  |  Nav NegotiateTitleKeyStreamStop obj={Object} hr {StreamID}
Microsoft-Windows-DVD  |  32        |  DVD Navigator  |  Nav DriveIOCTLStart obj={Object} func {Func} in {In} out {Out}
Microsoft-Windows-DVD  |  33        |  DVD Navigator  |  Nav DriveIOCTLStop obj={Object} hr {hr}