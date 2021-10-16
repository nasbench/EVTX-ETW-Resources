Provider                              |  Event ID  |  Channel  |  Message
--------------------------------------|------------|-----------|---------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-MCCS-NetworkHelper  |  1         |           |  Error: HRESULT: {P1_HexInt32} Location: {P2_String} Line Number: {P3_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  2         |           |  Error Propagated: HRESULT: {P1_HexInt32} Location: {P2_String} Line Number: {P3_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  101       |           |  NetworkHelper::HttpTransport: Callback error: Handle: {P1_UInt32} Error: {P2_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  102       |           |  NetworkHelper::HttpTransport: Request Failure: Handle: {P1_UInt32} Error: {P2_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  103       |           |  NetworkHelper::HttpTransport: Wait Failed on Closing Handle: {P1_UInt32} Wait: {P2_UInt32} Error: {P3_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  104       |           |  NetworkHelper::HttpTransport: Set Active error: Handle: {P1_UInt32} Error: {P2_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  105       |           |  NetworkHelper::HttpTransport: Set Dormand error: Handle: {P1_UInt32} Error: {P2_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  106       |           |  NetworkHelper::HttpTransport: Set completion event error: Handle: {P1_UInt32} Error: {P2_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  107       |           |  NetworkHelper::HttpTransport: Wait on async request error: Handle: {P1_UInt32} Wait: {P2_UInt32} Error: {P3_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  109       |           |  NetworkHelper::HttpTransport: Http Status error: Handle: {P1_UInt32} Error: {P2_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  110       |           |  NetworkHelper::HttpTransport: CmSetRequirement({P1_String}) Failure: Handle: {P2_UInt32} Error: {P3_UInt32}
Microsoft-Windows-MCCS-NetworkHelper  |  111       |           |  NetworkHelper::CrackUrl Failure. HR: {P1_UInt32} Url: {P2_String}
Microsoft-Windows-MCCS-NetworkHelper  |  201       |           |  Set PDC Active:{P1_Boolean}, invalid CCT state:{P2_Int32}
Microsoft-Windows-MCCS-NetworkHelper  |  202       |           |  Triggering PDC for sender: {P1_String}, Activate: {P2_Boolean}, Task: {P3_String}, ActivationHandle: {P4_Handle}
Microsoft-Windows-MCCS-NetworkHelper  |  203       |           |  Triggered CCT for sender {P1_String}
Microsoft-Windows-MCCS-NetworkHelper  |  205       |           |
Microsoft-Windows-MCCS-NetworkHelper  |  206       |           |  Released CCT for sender {P1_String}; Attained CCT {P2_Boolean}
Microsoft-Windows-MCCS-NetworkHelper  |  207       |           |  Invalid CCT state: {P1_Int32}
Microsoft-Windows-MCCS-NetworkHelper  |  208       |           |
Microsoft-Windows-MCCS-NetworkHelper  |  209       |           |  PDC not renewed due to lack of progress, allowing low power state. ActivationHandle: {Message}
Microsoft-Windows-MCCS-NetworkHelper  |  4005      |           |  Http: {Prop_ptr}: WINHTTP_CALLBACK_STATUS_{Prop_ansi}
Microsoft-Windows-MCCS-NetworkHelper  |  4006      |           |  Http: {Prop_ptr}: WINHTTP_CALLBACK_STATUS_{Prop_ansi}: Bytes received:{Prop_int}
Microsoft-Windows-MCCS-NetworkHelper  |  4007      |           |  Http: {Prop_ptr}: WINHTTP_CALLBACK_STATUS_{Prop_ansi}: Socket: {Prop_hexint}
Microsoft-Windows-MCCS-NetworkHelper  |  4008      |           |  Http: {Prop_ptr}: WINHTTP_CALLBACK_STATUS_{Prop_ansi}: Status: {Prop_uint}
Microsoft-Windows-MCCS-NetworkHelper  |  4009      |           |  Http: {Prop_ptr}: WINHTTP_CALLBACK_STATUS_{Prop_ansi}: Info: {Prop_string}
Microsoft-Windows-MCCS-NetworkHelper  |  4010      |           |  Http: {Prop_ptr}: Unknown status: {Prop_uint}
Microsoft-Windows-MCCS-NetworkHelper  |  4020      |           |  Http: Setting threshold to {P1_Int32}
Microsoft-Windows-MCCS-NetworkHelper  |  4021      |           |  Http: Attributing Http Session to ProductId = {P1_String}
Microsoft-Windows-MCCS-NetworkHelper  |  4022      |           |  Http: Set WINHTTP_OPTION_SECONDARY_APP_META_DATA failed. HRESULT = {Prop_hr}
Microsoft-Windows-MCCS-NetworkHelper  |  4023      |           |  Http: {Message}: WinHttpCloseHandle
Microsoft-Windows-MCCS-NetworkHelper  |  4024      |           |  Http: WFSO timed out waiting on m_hHandleClosingEvent. Waiting again...
Microsoft-Windows-MCCS-NetworkHelper  |  4025      |           |  Http: {Prop_string1}:{Prop_string2}
Microsoft-Windows-MCCS-NetworkHelper  |  4030      |           |  Http: {Message}: New request handle
Microsoft-Windows-MCCS-NetworkHelper  |  4031      |           |  Http: Ignoring status update on failed request
Microsoft-Windows-MCCS-NetworkHelper  |  4032      |           |  Http: Total bytes received: {P1_Int32}
Microsoft-Windows-MCCS-NetworkHelper  |  4033      |           |  Http: ResponseContentLength({Prop_int1}) != ResponeBodyByteCount({Prop_int2})
Microsoft-Windows-MCCS-NetworkHelper  |  4034      |           |  Http: Content size ({Prop_int1}) exceeded threshold ({Prop_int2})
Microsoft-Windows-MCCS-NetworkHelper  |  4040      |           |  Http: {Prop_ptr}: HTTP_QUERY_{Prop_ansi}: {Prop_int}
Microsoft-Windows-MCCS-NetworkHelper  |  4041      |           |  Http: {Message}: HTTP_QUERY_CONTENT_LENGTH is unknown
Microsoft-Windows-MCCS-NetworkHelper  |  4042      |           |  Http: Disallowing WiFi requests based on test hook value
Microsoft-Windows-MCCS-NetworkHelper  |  4043      |           |  Http: {Prop_ptr}: {Prop_ansi} {Prop_int} bytes
Microsoft-Windows-MCCS-NetworkHelper  |  4044      |           |  Http: {Prop_ptr}: {Prop_ansi} failed synchronously: {Prop_uint}
Microsoft-Windows-MCCS-NetworkHelper  |  4045      |           |  Http: {Prop_ptr}: Total Body Bytes sent: {Prop_int}
Microsoft-Windows-MCCS-NetworkHelper  |  4050      |           |  Http: ContentLength not specified!
Microsoft-Windows-MCCS-NetworkHelper  |  4051      |           |  Http: HTTP Error: {Prop_hexint}
Microsoft-Windows-MCCS-NetworkHelper  |  4052      |           |  Http: Content Lengtgh: {P1_Int32}