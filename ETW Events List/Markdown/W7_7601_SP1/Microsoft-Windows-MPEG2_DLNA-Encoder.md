Provider                              |  Event ID  |  Channel    |  Message
--------------------------------------|------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-MPEG2_DLNA-Encoder  |  0         |  muxencode  |  Starting. Video: {Region} ({VideoX},{VideoY}). Audio Channels: {AudioChannels}, Video Bit Rate: {VideoBitRate}, Audio Bit Rate {AudioBitRate}, Seek Offset {SeekOffsetMs}ms
Microsoft-Windows-MPEG2_DLNA-Encoder  |  1         |  muxencode  |  Stopping. Bytes Muxed: {TotalBytesEncoded}, Video Frames Received: {VideoFramesReceived}, Video Frames Encoded: {VideoFramesEncoded}, Audio Bytes Received: {AudioBytesReceived}, Audio Frames Encoded: {AudioFramesEncoded}
Microsoft-Windows-MPEG2_DLNA-Encoder  |  2         |  muxencode  |  Error: {hr}
Microsoft-Windows-MPEG2_DLNA-Encoder  |  3         |  muxencode  |  Video Frame Received.  Timestamp={Timestamp}, ID={ID}
Microsoft-Windows-MPEG2_DLNA-Encoder  |  4         |  muxencode  |  Video Frame Encoded.  Input Frame ID={InputID}, Input Timestamp={InputTimestamp}, Output Timestamp={TargetTimestamp}
Microsoft-Windows-MPEG2_DLNA-Encoder  |  5         |  muxencode  |  Audio Sample Received.  Timestamp={Timestamp}, Bytes in buffer={Bytes}
Microsoft-Windows-MPEG2_DLNA-Encoder  |  6         |  muxencode  |