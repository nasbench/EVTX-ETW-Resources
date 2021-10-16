Provider                            |  Event ID  |  Channel                                         |  Message
------------------------------------|------------|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-RemoteAssistance  |  1         |  Microsoft-Windows-RemoteAssistance/Tracing      |  Entering function {FuncName}
Microsoft-Windows-RemoteAssistance  |  2         |  Microsoft-Windows-RemoteAssistance/Tracing      |  Leaving function {FuncName}
Microsoft-Windows-RemoteAssistance  |  3         |  Application                                     |  Application will terminate, a critical error was detected in {file} Line {line} Function {function}
Microsoft-Windows-RemoteAssistance  |  4         |  Microsoft-Windows-RemoteAssistance/Tracing      |  Hit exception block of code at {file} Line {line} in function {function}
Microsoft-Windows-RemoteAssistance  |  5         |  Microsoft-Windows-RemoteAssistance/Tracing      |  Branching on Line:{line} File:{file} with the string {Condition}
Microsoft-Windows-RemoteAssistance  |  6         |  Microsoft-Windows-RemoteAssistance/Tracing      |  Switching on Line:{line} File:{file} with the value {Condition}
Microsoft-Windows-RemoteAssistance  |  7         |  Microsoft-Windows-RemoteAssistance/Tracing      |  Entering conditional block at Line:{line} File:{File}
Microsoft-Windows-RemoteAssistance  |  8         |  Microsoft-Windows-RemoteAssistance/Tracing      |  Exiting conditional block at Line:{line} File:{File}
Microsoft-Windows-RemoteAssistance  |  9         |  Microsoft-Windows-RemoteAssistance/Admin        |  There was a problem interacting with COM object {FuncName}.  An outdated version might be installed, or the component might not be installed at all.
Microsoft-Windows-RemoteAssistance  |  10        |  Microsoft-Windows-RemoteAssistance/Admin        |  A user tried to use Remote Assistance and send an invitation for help through their default email client, but Remote Assistance failed to successfully send the invitation.  It is possible the email client configured as the default client does not support SMAPI calls, or that the email client is improperly configured.  It is also possible that the user closed the email client without sending the message.
Microsoft-Windows-RemoteAssistance  |  11        |  Microsoft-Windows-RemoteAssistance/Admin        |  A user opened a Remote Assistance invitation, but the invitation was closed due to too many bad password attempts to connect to the machine.
Microsoft-Windows-RemoteAssistance  |  12        |  Microsoft-Windows-RemoteAssistance/Admin        |  A user tried to use Remote Assistance, group policy requires a session log to be maintained, and a session log couldn't be created.  Remote Assistance was terminated.  Check the disk to see if there are problems with the disk or if it is full.
Microsoft-Windows-RemoteAssistance  |  13        |  Microsoft-Windows-RemoteAssistance/Operational  |  Remote Assistance started with:    {FuncName}    as the command line parameters.
Microsoft-Windows-RemoteAssistance  |  14        |  Microsoft-Windows-RemoteAssistance/Operational  |  A Remote Assistance Invitation was successfully opened.
Microsoft-Windows-RemoteAssistance  |  15        |  Microsoft-Windows-RemoteAssistance/Operational  |  An RDP connection was successfully made.
Microsoft-Windows-RemoteAssistance  |  16        |  Microsoft-Windows-RemoteAssistance/Operational  |  The Remote Assistance password was verified.  The Remote Assistance session has begun.
Microsoft-Windows-RemoteAssistance  |  17        |  Microsoft-Windows-RemoteAssistance/Operational  |  The Remote Assistance password provided was incorrect.  The RDP session was terminated.
Microsoft-Windows-RemoteAssistance  |  17        |  Microsoft-Windows-RemoteAssistance/Operational  |  The Remote Assistance password provided was incorrect.  The RDP session was terminated, IP address of the connecting machine is {FuncName}
Microsoft-Windows-RemoteAssistance  |  18        |  Microsoft-Windows-RemoteAssistance/Operational  |  The Remote Assistance session was disconnected remotely.
Microsoft-Windows-RemoteAssistance  |  19        |  Microsoft-Windows-RemoteAssistance/Operational  |  The Remote Assistance session was disconnected locally.
Microsoft-Windows-RemoteAssistance  |  20        |  Microsoft-Windows-RemoteAssistance/Operational  |  The Remote Assistance invitation was closed, any information concerning it given out is now invalid.
Microsoft-Windows-RemoteAssistance  |  21        |  Microsoft-Windows-RemoteAssistance/Operational  |  The helper is sharing control.
Microsoft-Windows-RemoteAssistance  |  22        |  Microsoft-Windows-RemoteAssistance/Operational  |  The helper can now view the screen.
Microsoft-Windows-RemoteAssistance  |  23        |  Microsoft-Windows-RemoteAssistance/Operational  |  Remote Assistance detected that it didn't restore the background and screen settings before shutting down.  An attempt was made to restore these settings.
Microsoft-Windows-RemoteAssistance  |  24        |  Microsoft-Windows-RemoteAssistance/Operational  |  The time limit of offered invitations has been reached.
Microsoft-Windows-RemoteAssistance  |  25        |  Microsoft-Windows-RemoteAssistance/Operational  |  User setting value currently applied is {Code}
Microsoft-Windows-RemoteAssistance  |  26        |  Microsoft-Windows-RemoteAssistance/Operational  |  The system or GP settings do not allow an Remote Assistance invitation to be created.  This action has been blocked by the application.
Microsoft-Windows-RemoteAssistance  |  27        |  Microsoft-Windows-RemoteAssistance/Operational  |  The system or GP settings do not allow a helper to share control.  This action has been blocked by the application.
Microsoft-Windows-RemoteAssistance  |  28        |  Microsoft-Windows-RemoteAssistance/Operational  |  The Windows firewall has been checked and it appears that it is configured so that it will stop Remote Assistance from working.
Microsoft-Windows-RemoteAssistance  |  29        |  Microsoft-Windows-RemoteAssistance/Operational  |  The error message:    {FuncName}    has been shown to the user.
Microsoft-Windows-RemoteAssistance  |  30        |  Microsoft-Windows-RemoteAssistance/Operational  |  Remote Assistance has ended.
Microsoft-Windows-RemoteAssistance  |  31        |  Microsoft-Windows-RemoteAssistance/Operational  |  Remote Assistance COM server has started.
Microsoft-Windows-RemoteAssistance  |  32        |  Microsoft-Windows-RemoteAssistance/Operational  |  Remote Assistance COM server has ended.
Microsoft-Windows-RemoteAssistance  |  33        |  Microsoft-Windows-RemoteAssistance/Operational  |  The Remote Assistance ticket contained the following IP addresses: {FuncName}
Microsoft-Windows-RemoteAssistance  |  34        |  Microsoft-Windows-RemoteAssistance/Operational  |  A PNRP Node was created at the following address: {FuncName}
Microsoft-Windows-RemoteAssistance  |  35        |  Microsoft-Windows-RemoteAssistance/Operational  |  The following PNRP clouds were detected: {FuncName}
Microsoft-Windows-RemoteAssistance  |  36        |  Microsoft-Windows-RemoteAssistance/Operational  |  A PNRP Node was released at the following address: {FuncName}
Microsoft-Windows-RemoteAssistance  |  37        |  Microsoft-Windows-RemoteAssistance/Operational  |  Started looking for PNRP node with the following address: {FuncName}
Microsoft-Windows-RemoteAssistance  |  38        |  Microsoft-Windows-RemoteAssistance/Operational  |  Stopped looking for PNRP node, address: {FuncName}
Microsoft-Windows-RemoteAssistance  |  39        |  Microsoft-Windows-RemoteAssistance/Admin        |  There was a problem interacting with the PNRP service.  This component might not be installed correctly. The error code received was: {FuncName}
Microsoft-Windows-RemoteAssistance  |  40        |  Microsoft-Windows-RemoteAssistance/Operational  |  Diagnosis Repro Attempt resulted in a success.
Microsoft-Windows-RemoteAssistance  |  41        |  Microsoft-Windows-RemoteAssistance/Operational  |  Diagnosis Repro Attempt resulted in a failure.
Microsoft-Windows-RemoteAssistance  |  42        |  Microsoft-Windows-RemoteAssistance/Tracing      |  Current time on NTP Server: {FuncName}
Microsoft-Windows-RemoteAssistance  |  43        |  Microsoft-Windows-RemoteAssistance/Tracing      |  Remote Assistance troubleshooting rejected problem {Code}.
Microsoft-Windows-RemoteAssistance  |  44        |  Microsoft-Windows-RemoteAssistance/Operational  |  Remote Assistance troubleshooting has confirmed the problem: {FuncName}.
Microsoft-Windows-RemoteAssistance  |  45        |  Microsoft-Windows-RemoteAssistance/Operational  |  Remote Assistance troubleshooting is starting to repair the identified problem: {FuncName}.
Microsoft-Windows-RemoteAssistance  |  46        |  Microsoft-Windows-RemoteAssistance/Operational  |  Remote Assistance troubleshooting successfully repaired the problem: {FuncName}.
Microsoft-Windows-RemoteAssistance  |  47        |  Microsoft-Windows-RemoteAssistance/Operational  |  Remote Assistance troubleshooting failed to repair the problem: {FuncName}.
Microsoft-Windows-RemoteAssistance  |  100       |  Microsoft-Windows-RemoteAssistance/Tracing      |  Remote OS Type : {Code}.
Microsoft-Windows-RemoteAssistance  |  101       |  Microsoft-Windows-RemoteAssistance/Tracing      |  Remote Assistance connection attempt failed with error code: {Code}.
Microsoft-Windows-RemoteAssistance  |  102       |  Microsoft-Windows-RemoteAssistance/Tracing      |  Remote Assistance reproduced the problem and created following ticket to verify the problem: {FuncName}.