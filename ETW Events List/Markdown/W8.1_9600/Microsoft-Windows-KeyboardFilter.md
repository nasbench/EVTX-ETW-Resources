Provider                          |  Event ID  |  Channel                                       |  Message
----------------------------------|------------|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-KeyboardFilter  |  10001     |  Microsoft-Windows-KeyboardFilter/Admin        |  The Keyboard Filter Service was unable to obtain the session token from the session id: {Message} ({ErrorCode}).   Please verify that Terminal Services client is installed and the service is running under the LocalSystem user.
Microsoft-Windows-KeyboardFilter  |  10002     |  Microsoft-Windows-KeyboardFilter/Admin        |  The Keyboard Filter Service was unable to obtain access to Terminal Services: {Message} ({ErrorCode}). Please verify that the Terminal Services client is installed and the service is running under the LocalSystem user.
Microsoft-Windows-KeyboardFilter  |  10003     |  Microsoft-Windows-KeyboardFilter/Admin        |  Could not obtain a lock on local policy settings for update detection, {Message} ({ErrorCode}).
Microsoft-Windows-KeyboardFilter  |  10004     |  Microsoft-Windows-KeyboardFilter/Admin        |  Could not update keyboard filter subsystem, {Message} ({ErrorCode}).
Microsoft-Windows-KeyboardFilter  |  10005     |  Microsoft-Windows-KeyboardFilter/Admin        |  The Keyboard Filter Service could not start session monitor. The session monitor ensures keyboard layout changes are reflected within the service and that on-screen keyboards work correctly.  Check to make sure system permissions are set up correctly.  Reason, {Message} ({ErrorCode}).
Microsoft-Windows-KeyboardFilter  |  10006     |  Microsoft-Windows-KeyboardFilter/Admin        |  Session Manager handle to Keyboard Filter process was abandoned. Handle will be removed from the session list.
Microsoft-Windows-KeyboardFilter  |  10007     |  Microsoft-Windows-KeyboardFilter/Admin        |  The Keyboard Filter Service failed to launch hook process.  Reason: {Message}
Microsoft-Windows-KeyboardFilter  |  10008     |  Microsoft-Windows-KeyboardFilter/Admin        |  'sdbinst -q ({SdbPath})' has probably failed, exit code of ({ExitCode}).
Microsoft-Windows-KeyboardFilter  |  10009     |  Microsoft-Windows-KeyboardFilter/Admin        |  Unsupported (e.g. remote) session was disconnected by Keyboard Filter Service.
Microsoft-Windows-KeyboardFilter  |  10010     |  Microsoft-Windows-KeyboardFilter/Admin        |  Keyboard Filter Driver could not start and has unloaded.  Reason, {ErrorCode} ({Reason}).
Microsoft-Windows-KeyboardFilter  |  10011     |  Microsoft-Windows-KeyboardFilter/Admin        |  The Keyboard Filter Driver could not attach to keyboard.  Reason, {ErrorCode} ({Reason}).
Microsoft-Windows-KeyboardFilter  |  10012     |  Microsoft-Windows-KeyboardFilter/Admin        |  The Keyboard Filter Driver could not properly filter keystroke information.  Reason, {ErrorCode} ({Reason}).
Microsoft-Windows-KeyboardFilter  |  10013     |  Microsoft-Windows-KeyboardFilter/Admin        |  The Keyboard Filter Driver could not update filter configuration.  Reason, {ErrorCode} ({Reason}).
Microsoft-Windows-KeyboardFilter  |  10014     |  Microsoft-Windows-KeyboardFilter/Admin        |  A non-empty list of keyboard filter rules resulted in an empty scancode list.
Microsoft-Windows-KeyboardFilter  |  10015     |  Microsoft-Windows-KeyboardFilter/Admin        |  Error was returned when trying to transform a keyboard filter rule to a scancode.
Microsoft-Windows-KeyboardFilter  |  10016     |  Microsoft-Windows-KeyboardFilter/Operational  |  Attempting to launch the keyboard filter hook process.
Microsoft-Windows-KeyboardFilter  |  10101     |  Microsoft-Windows-KeyboardFilter/Operational  |  The Keyboard Filter Service has Started
Microsoft-Windows-KeyboardFilter  |  10102     |  Microsoft-Windows-KeyboardFilter/Operational  |  The Keyboard Filter Service has stopped
Microsoft-Windows-KeyboardFilter  |  10103     |  Microsoft-Windows-KeyboardFilter/Operational  |  Generic Keyboard Filter Service message: {Command}
Microsoft-Windows-KeyboardFilter  |  10104     |  Microsoft-Windows-KeyboardFilter/Operational  |  'sdbinst -q ({SdbPath})' executed, exit code ({ExitCode})
Microsoft-Windows-KeyboardFilter  |  10201     |  Microsoft-Windows-KeyboardFilter/Operational  |  Administrator user {UserName} is now logged on, keyboard filtering is disabled for this session.
Microsoft-Windows-KeyboardFilter  |  10202     |  Microsoft-Windows-KeyboardFilter/Operational  |  User {UserName} logged off. Keyboard filtering is disabled for the Windows Logon Screen.
Microsoft-Windows-KeyboardFilter  |  10203     |  Microsoft-Windows-KeyboardFilter/Operational  |  User {UserName} logged off. Keyboard filtering is disabled.
Microsoft-Windows-KeyboardFilter  |  10204     |  Microsoft-Windows-KeyboardFilter/Operational  |  User {UserName} is now logged on. Keyboard filtering is now in effect.
Microsoft-Windows-KeyboardFilter  |  10205     |  Microsoft-Windows-KeyboardFilter/Operational  |  The Keyboard Filter Service has detected Policy changes and is reloading them
Microsoft-Windows-KeyboardFilter  |  10206     |  Microsoft-Windows-KeyboardFilter/Operational  |  The Keyboard Filter Service has detected a layout change to {Layout}.
Microsoft-Windows-KeyboardFilter  |  10207     |  Microsoft-Windows-KeyboardFilter/Operational  |  The Keyboard Filter Service has found the following enabled policies.
Microsoft-Windows-KeyboardFilter  |  10208     |  Microsoft-Windows-KeyboardFilter/Operational  |  The Keyboard Filter Service is sending scancodes to the Filter Driver.
Microsoft-Windows-KeyboardFilter  |  10301     |  Microsoft-Windows-KeyboardFilter/Admin        |  A custom filter ({Filter}) appears to have an invalid modifier (system) key. Valid modifiers include Ctrl or Control, Alt, Shift, and Win or Windows. Each key must be separated from the one that follows with a plus (+).
Microsoft-Windows-KeyboardFilter  |  10302     |  Microsoft-Windows-KeyboardFilter/Admin        |  A custom filter ({Filter}) appears to have an invalid key. Keys can be any character on the system's keyboard or it's name. Please see documentation for the names of all valid keys.
Microsoft-Windows-KeyboardFilter  |  10303     |  Microsoft-Windows-KeyboardFilter/Admin        |  A custom filter ({Filter}) appears to be invalid.  A valid filter has zero or more modifiers, and a single key.  Each modifier and key must be separated by (+).
Microsoft-Windows-KeyboardFilter  |  10304     |  Microsoft-Windows-KeyboardFilter/Admin        |  Too many custom filters have been enabled.  No more than {Maximum} custom and fixed filters may be defined.
Microsoft-Windows-KeyboardFilter  |  11000     |  Microsoft-Windows-KeyboardFilter/Performance  |
Microsoft-Windows-KeyboardFilter  |  11001     |  Microsoft-Windows-KeyboardFilter/Performance  |
Microsoft-Windows-KeyboardFilter  |  11002     |  Microsoft-Windows-KeyboardFilter/Performance  |
Microsoft-Windows-KeyboardFilter  |  11003     |  Microsoft-Windows-KeyboardFilter/Performance  |
Microsoft-Windows-KeyboardFilter  |  11004     |  Microsoft-Windows-KeyboardFilter/Performance  |
Microsoft-Windows-KeyboardFilter  |  11005     |  Microsoft-Windows-KeyboardFilter/Performance  |
Microsoft-Windows-KeyboardFilter  |  11006     |  Microsoft-Windows-KeyboardFilter/Performance  |
Microsoft-Windows-KeyboardFilter  |  11007     |  Microsoft-Windows-KeyboardFilter/Performance  |
Microsoft-Windows-KeyboardFilter  |  11008     |  Microsoft-Windows-KeyboardFilter/Performance  |
Microsoft-Windows-KeyboardFilter  |  11009     |  Microsoft-Windows-KeyboardFilter/Performance  |
Microsoft-Windows-KeyboardFilter  |  11010     |  Microsoft-Windows-KeyboardFilter/Performance  |
Microsoft-Windows-KeyboardFilter  |  11011     |  Microsoft-Windows-KeyboardFilter/Performance  |
Microsoft-Windows-KeyboardFilter  |  11012     |  Microsoft-Windows-KeyboardFilter/Performance  |
Microsoft-Windows-KeyboardFilter  |  11013     |  Microsoft-Windows-KeyboardFilter/Performance  |