Provider                              |  Level        |  Event ID  |  Version  |  Channel  |  Task  |  Opcode  |  Keyword  |  Message
--------------------------------------|---------------|------------|-----------|-----------|--------|----------|-----------|---------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-MCCS-NetworkHelper  |  Error        |  1         |  0        |           |        |          |  Error    |  Error: HRESULT: {P1_HexInt32} Location: {P2_String} Line Number: {P3_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  Warning      |  2         |  0        |           |        |          |           |  Error Propagated: HRESULT: {P1_HexInt32} Location: {P2_String} Line Number: {P3_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  Warning      |  101       |  0        |           |        |          |           |  NetworkHelper::HttpTransport: Callback error: Handle: {P1_UInt32} Error: {P2_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  Warning      |  102       |  0        |           |        |          |           |  NetworkHelper::HttpTransport: Request Failure: Handle: {P1_UInt32} Error: {P2_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  Warning      |  103       |  0        |           |        |          |           |  NetworkHelper::HttpTransport: Wait Failed on Closing Handle: {P1_UInt32} Wait: {P2_UInt32} Error: {P3_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  Warning      |  104       |  0        |           |        |          |           |  NetworkHelper::HttpTransport: Set Active error: Handle: {P1_UInt32} Error: {P2_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  Warning      |  105       |  0        |           |        |          |           |  NetworkHelper::HttpTransport: Set Dormand error: Handle: {P1_UInt32} Error: {P2_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  Warning      |  106       |  0        |           |        |          |           |  NetworkHelper::HttpTransport: Set completion event error: Handle: {P1_UInt32} Error: {P2_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  Warning      |  107       |  0        |           |        |          |           |  NetworkHelper::HttpTransport: Wait on async request error: Handle: {P1_UInt32} Wait: {P2_UInt32} Error: {P3_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  Warning      |  109       |  0        |           |        |          |           |  NetworkHelper::HttpTransport: Http Status error: Handle: {P1_UInt32} Error: {P2_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  Warning      |  110       |  0        |           |        |          |           |  NetworkHelper::HttpTransport: CmSetRequirement({P1_String}) Failure: Handle: {P2_UInt32} Error: {P3_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  Error        |  111       |  0        |           |        |          |  Error    |  NetworkHelper::CrackUrl Failure. HR: {P1_UInt32} Url: {P2_String}
Microsoft-Windows-MCCS-NetworkHelper  |  Warning      |  201       |  0        |           |        |          |           |  Set PDC Active:{P1_Boolean}; invalid CCT state:{P2_Int32}
Microsoft-Windows-MCCS-NetworkHelper  |  Information  |  202       |  0        |           |        |          |           |  Triggering PDC for sender: {P1_String}; Activate: {P2_Boolean}; Task: {P3_String}; ActivationHandle: {P4_Handle}
Microsoft-Windows-MCCS-NetworkHelper  |  Information  |  203       |  0        |           |        |          |           |  Triggered CCT for sender {P1_String}
Microsoft-Windows-MCCS-NetworkHelper  |  Warning      |  205       |  0        |           |        |          |           |
Microsoft-Windows-MCCS-NetworkHelper  |  Information  |  206       |  0        |           |        |          |           |  Released CCT for sender {P1_String}; Attained CCT {P2_Boolean}
Microsoft-Windows-MCCS-NetworkHelper  |  Warning      |  207       |  0        |           |        |          |           |  Invalid CCT state: {P1_Int32}
Microsoft-Windows-MCCS-NetworkHelper  |  Warning      |  208       |  0        |           |        |          |           |
Microsoft-Windows-MCCS-NetworkHelper  |  Warning      |  209       |  0        |           |        |          |           |  PDC not renewed due to lack of progress; allowing low power state. ActivationHandle: {Message}
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4005      |  0        |           |        |          |  Debug    |  Http: {Prop_ptr}: WINHTTP_CALLBACK_STATUS_{Prop_ansi}
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4006      |  0        |           |        |          |  Debug    |  Http: {Prop_ptr}: WINHTTP_CALLBACK_STATUS_{Prop_ansi}: Bytes received:{Prop_int}
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4007      |  0        |           |        |          |  Debug    |  Http: {Prop_ptr}: WINHTTP_CALLBACK_STATUS_{Prop_ansi}: Socket: {Prop_hexint}
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4008      |  0        |           |        |          |  Debug    |  Http: {Prop_ptr}: WINHTTP_CALLBACK_STATUS_{Prop_ansi}: Status: {Prop_uint}
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4009      |  0        |           |        |          |  Debug    |  Http: {Prop_ptr}: WINHTTP_CALLBACK_STATUS_{Prop_ansi}: Info: {Prop_string}
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4010      |  0        |           |        |          |  Debug    |  Http: {Prop_ptr}: Unknown status: {Prop_uint}
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4020      |  0        |           |        |          |  Debug    |  Http: Setting threshold to {P1_Int32}
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4021      |  0        |           |        |          |  Debug    |  Http: Attributing Http Session to ProductId = {P1_String}
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4022      |  0        |           |        |          |  Debug    |  Http: Set WINHTTP_OPTION_SECONDARY_APP_META_DATA failed. HRESULT = {Prop_hr}
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4023      |  0        |           |        |          |  Debug    |  Http: {Message}: WinHttpCloseHandle
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4024      |  0        |           |        |          |  Debug    |  Http: WFSO timed out waiting on m_hHandleClosingEvent. Waiting again...
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4025      |  0        |           |        |          |  Debug    |  Http: {Prop_string1}:{Prop_string2}
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4030      |  0        |           |        |          |  Debug    |  Http: {Message}: New request handle
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4031      |  0        |           |        |          |  Debug    |  Http: Ignoring status update on failed request
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4032      |  0        |           |        |          |  Debug    |  Http: Total bytes received: {P1_Int32}
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4033      |  0        |           |        |          |  Debug    |  Http: ResponseContentLength({Prop_int1}) != ResponeBodyByteCount({Prop_int2})
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4034      |  0        |           |        |          |  Debug    |  Http: Content size ({Prop_int1}) exceeded threshold ({Prop_int2})
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4040      |  0        |           |        |          |  Debug    |  Http: {Prop_ptr}: HTTP_QUERY_{Prop_ansi}: {Prop_int}
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4041      |  0        |           |        |          |  Debug    |  Http: {Message}: HTTP_QUERY_CONTENT_LENGTH is unknown
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4042      |  0        |           |        |          |  Debug    |  Http: Disallowing WiFi requests based on test hook value
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4043      |  0        |           |        |          |  Debug    |  Http: {Prop_ptr}: {Prop_ansi} {Prop_int} bytes
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4044      |  0        |           |        |          |  Debug    |  Http: {Prop_ptr}: {Prop_ansi} failed synchronously: {Prop_uint}
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4045      |  0        |           |        |          |  Debug    |  Http: {Prop_ptr}: Total Body Bytes sent: {Prop_int}
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4050      |  0        |           |        |          |  Debug    |  Http: ContentLength not specified!
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4051      |  0        |           |        |          |  Debug    |  Http: HTTP Error: {Prop_hexint}
Microsoft-Windows-MCCS-NetworkHelper  |  Verbose      |  4052      |  0        |           |        |          |  Debug    |  Http: Content Lengtgh: {P1_Int32}