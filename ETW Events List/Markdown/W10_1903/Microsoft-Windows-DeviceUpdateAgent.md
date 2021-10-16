Provider                             |  Event ID  |  Channel                                  |  Message
-------------------------------------|------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-DeviceUpdateAgent  |  100       |  Device Update Agent operational channel  |  A new deployment session was created with session ID {Prop_SessionId}
Microsoft-Windows-DeviceUpdateAgent  |  101       |  Device Update Agent operational channel  |  Failed to create a new deployment session with error {HRESULT}
Microsoft-Windows-DeviceUpdateAgent  |  200       |  Device Update Agent operational channel  |  Failed to generate a list of files to download with error {HRESULT}
Microsoft-Windows-DeviceUpdateAgent  |  201       |  Device Update Agent operational channel  |  Requesting {Prop_NumFiles} files with total size {Prop_RequestSize}
Microsoft-Windows-DeviceUpdateAgent  |  300       |  Device Update Agent operational channel  |  Failed to install updates with error {HRESULT}
Microsoft-Windows-DeviceUpdateAgent  |  301       |  Device Update Agent operational channel  |  Update '{Prop_UnicodeString}' encountered install error {Win32Error}
Microsoft-Windows-DeviceUpdateAgent  |  302       |  Device Update Agent operational channel  |  Update '{Prop_UnicodeString}' encountered import error {Win32Error}
Microsoft-Windows-DeviceUpdateAgent  |  303       |  Device Update Agent operational channel  |  Update '{Prop_UnicodeString}' should have already existed on the machine, but was missing.  Error = {Win32Error}
Microsoft-Windows-DeviceUpdateAgent  |  304       |  Device Update Agent operational channel  |  Installation of update set '{Prop_Id}' requires the system to be rebooted
Microsoft-Windows-DeviceUpdateAgent  |  305       |  Device Update Agent operational channel  |  Installation of update '{Prop_Id}' requires the system to be rebooted
Microsoft-Windows-DeviceUpdateAgent  |  306       |  Device Update Agent operational channel  |  Installation of update set '{Prop_SetId}' is complete.  {Prop_SuccessfulUpdates} updates out of {Prop_TotalUpdates} updates were successfully installed in {Prop_ElapsedMilliseconds} milliseconds
Microsoft-Windows-DeviceUpdateAgent  |  307       |  Device Update Agent operational channel  |  Updated product '{Prop_ProductId}' to version '{Prop_ProductVersion}'
Microsoft-Windows-DeviceUpdateAgent  |  400       |  Device Update Agent operational channel  |  Failed to commit updates with error {HRESULT}
Microsoft-Windows-DeviceUpdateAgent  |  500       |  Device Update Agent operational channel  |  Failed to clean up updates with error {HRESULT}
Microsoft-Windows-DeviceUpdateAgent  |  600       |  Device Update Agent operational channel  |  Failed to cancel updates with error {HRESULT}
Microsoft-Windows-DeviceUpdateAgent  |  601       |  Device Update Agent operational channel  |  Updates were cancelled with reason {HRESULT}
Microsoft-Windows-DeviceUpdateAgent  |  700       |  Device Update Agent operational channel  |  Failed to merge updates with error {HRESULT}
Microsoft-Windows-DeviceUpdateAgent  |  800       |  Device Update Agent operational channel  |  Failed to get update result post reboot with error {HRESULT}
Microsoft-Windows-DeviceUpdateAgent  |  801       |  Device Update Agent operational channel  |
Microsoft-Windows-DeviceUpdateAgent  |  802       |  Device Update Agent operational channel  |
Microsoft-Windows-DeviceUpdateAgent  |  900       |  Device Update Agent operational channel  |  Failed to perform post download operation with error {HRESULT}