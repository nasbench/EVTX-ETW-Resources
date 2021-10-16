Provider                          |  Event ID  |  Channel                                       |  Message
----------------------------------|------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-AssignedAccess  |  10001     |  Microsoft-Windows-AssignedAccess/Admin        |  Could not configure user. The specified SID was not found on this system.
Microsoft-Windows-AssignedAccess  |  10002     |  Microsoft-Windows-AssignedAccess/Admin        |  Could not configure user. The specified SID is an administrator on this system. Locking down administrator users could lead to unconfigurable devices.
Microsoft-Windows-AssignedAccess  |  10003     |  Microsoft-Windows-AssignedAccess/Admin        |  Could not configure user. The specified SID is a domain account.  Only local accounts can be used.
Microsoft-Windows-AssignedAccess  |  10004     |  Microsoft-Windows-AssignedAccess/Admin        |  Could not configure application. The specified AppID may be invalid, or is not installed on this system. The specified user may need to log in and download this application first.
Microsoft-Windows-AssignedAccess  |  10010     |  Microsoft-Windows-AssignedAccess/Admin        |  Could not configure application launching.
Microsoft-Windows-AssignedAccess  |  10020     |  Microsoft-Windows-AssignedAccess/Admin        |  Could not configure keyboard filtering.
Microsoft-Windows-AssignedAccess  |  20000     |  Microsoft-Windows-AssignedAccess/Operational  |  Assigned Access is enabled. For settings to take effect, log off and log back in as this user.
Microsoft-Windows-AssignedAccess  |  20001     |  Microsoft-Windows-AssignedAccess/Operational  |  Assigned Access is disabled.  System will return to original settings.
Microsoft-Windows-AssignedAccess  |  30000     |  Microsoft-Windows-AssignedAccess/Operational  |  {File}({LineNumber}), hr = {ErrorCode}, message = {ErrorCodeExpanded}
Microsoft-Windows-AssignedAccess  |  31000     |  Microsoft-Windows-AssignedAccess/Admin        |  Error {ErrorCode} applying assigned access for current user, signing out...
Microsoft-Windows-AssignedAccess  |  31001     |  Microsoft-Windows-AssignedAccess/Admin        |  Error retrieving assigned access user information for current user: {ErrorCode}
Microsoft-Windows-AssignedAccess  |  31002     |  Microsoft-Windows-AssignedAccess/Admin        |  {Custom}, ErrorCode({ErrorCode})
Microsoft-Windows-AssignedAccess  |  32000     |  Microsoft-Windows-AssignedAccess/Admin        |  {Custom}, ErrorCode({ErrorCode})
Microsoft-Windows-AssignedAccess  |  33000     |  Microsoft-Windows-AssignedAccess/Admin        |  {Custom}, ErrorCode({ErrorCode})