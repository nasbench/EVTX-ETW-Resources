Provider                            |  Event ID  |  Channel             |  Message
------------------------------------|------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-SMBWitnessClient  |  1         |  WitnessClientAdmin  |  Witness Client initialization failed with error ({ErrorCode})
Microsoft-Windows-SMBWitnessClient  |  2         |  WitnessClientAdmin  |  Witness Client received registration request for \\{NetName}\{ShareName} with IP address {WitnessServerIP}
Microsoft-Windows-SMBWitnessClient  |  3         |  WitnessClientAdmin  |  Witness Client failed to obtain the list of Witness Servers from IP address {WitnessServerIP} with error ({Error})
Microsoft-Windows-SMBWitnessClient  |  4         |  WitnessClientAdmin  |  Witness Client is waiting to receive list of Witness Servers from IP address {WitnessServerIP}
Microsoft-Windows-SMBWitnessClient  |  5         |  WitnessClientAdmin  |  Witness Client selected {WitnessServerIP} as the Witness Server for NetName \\{NetName}
Microsoft-Windows-SMBWitnessClient  |  6         |  WitnessClientAdmin  |  Witness Client failed to find a Witness Server for NetName \\{NetName} with error ({ErrorCode}). Retrying in ({Sleep}) seconds.
Microsoft-Windows-SMBWitnessClient  |  7         |  WitnessClientAdmin  |  Witness Client successfully registered with Witness Server {WitnessServerIP} for notification on NetName \\{NetName} with IP address {FileServerIP}
Microsoft-Windows-SMBWitnessClient  |  8         |  WitnessClientAdmin  |  Witness Client failed to register with Witness Server {WitnessServerIP} for notification on NetName \\{NetName} with error ({Error})
Microsoft-Windows-SMBWitnessClient  |  9         |  WitnessClientAdmin  |  Witness Client received error ({ErrorCode}) from Witness Server {WitnessServerIP} for NetName \\{NetName}
Microsoft-Windows-SMBWitnessClient  |  10        |  WitnessClientAdmin  |  Witness Client received resource notification {NotificationType} for NetName \\{NetName} from Witness Server {WitnessServerIP}
Microsoft-Windows-SMBWitnessClient  |  11        |  WitnessClientAdmin  |  Witness Client failed resource notification for NetName \\{NetName} with error ({Error})
Microsoft-Windows-SMBWitnessClient  |  12        |  WitnessClientAdmin  |  Witness Client received a request to move to a different file server node for NetName \\{NetName} from Witness Server {WitnessServerIP}
Microsoft-Windows-SMBWitnessClient  |  13        |  WitnessClientAdmin  |  Witness Client failed the move request for NetName \\{NetName} with error ({Error})
Microsoft-Windows-SMBWitnessClient  |  14        |  WitnessClientAdmin  |  Witness Client received unregister request for \\{NetName}\{ShareName}
Microsoft-Windows-SMBWitnessClient  |  15        |  WitnessClientAdmin  |  Witness Client successfully unregistered from Witness Server {WitnessServerIP} for NetName \\{NetName}
Microsoft-Windows-SMBWitnessClient  |  16        |  WitnessClientAdmin  |  Witness Client failed to unregister from Witness Server {WitnessServerIP} for NetName \\{NetName} with error ({Error})
Microsoft-Windows-SMBWitnessClient  |  17        |  WitnessClientAdmin  |  Witness Client is already registered with Witness Server {WitnessServer} for notification on NetName \\{NetName} and IP address {IPAddress}
Microsoft-Windows-SMBWitnessClient  |  18        |  WitnessClientAdmin  |  Witness Client is already registered with Witness Server {WitnessServer} for notification on \\{NetName}\{ShareName} and IP address {IPAddress}
Microsoft-Windows-SMBWitnessClient  |  19        |  WitnessClientAdmin  |  Witness Client received an IP notification for NetName \\{NetName} from Witness Server {WitnessServerIP}
Microsoft-Windows-SMBWitnessClient  |  20        |  WitnessClientAdmin  |  Witness Client received an IP notification for \\{NetName}\{ShareName} from Witness Server {WitnessServerIP}
Microsoft-Windows-SMBWitnessClient  |  21        |  WitnessClientAdmin  |  Witness Client failed the IP notification for NetName \\{NetName} with error ({Error})
Microsoft-Windows-SMBWitnessClient  |  22        |  WitnessClientAdmin  |  Witness Client failed the IP notification for \\{NetName}\{ShareName} with error ({Error})
Microsoft-Windows-SMBWitnessClient  |  23        |  WitnessClientAdmin  |  Witness Client received a share move request for \\{NetName}\{ShareName} from Witness Server {WitnessServer}
Microsoft-Windows-SMBWitnessClient  |  24        |  WitnessClientAdmin  |  Witness Client failed the share move request for \\{NetName}\{ShareName} with error ({Error})
Microsoft-Windows-SMBWitnessClient  |  25        |  WitnessClientAdmin  |  Witness Client failed to unregister for NetName \\{NetName} because it is currently not registered
Microsoft-Windows-SMBWitnessClient  |  26        |  WitnessClientAdmin  |  Witness Client failed to unregister for \\{NetName}\{ShareName} because it is currently not registered
Microsoft-Windows-SMBWitnessClient  |  27        |  WitnessClientAdmin  |  Witness Client selected {WitnessServerIP} as the Witness Server for \\{NetName}\{ShareName}
Microsoft-Windows-SMBWitnessClient  |  28        |  WitnessClientAdmin  |  Witness Client failed to find a Witness Server for \\{NetName}\{ShareName} with error ({ErrorCode}). Retrying in ({Sleep}) seconds.
Microsoft-Windows-SMBWitnessClient  |  29        |  WitnessClientAdmin  |  Witness Client successfully registered with Witness Server {WitnessServerIP} for notification on \\{NetName}\{ShareName} with IP address {FileServerIP}
Microsoft-Windows-SMBWitnessClient  |  30        |  WitnessClientAdmin  |  Witness Client failed to register with Witness Server {WitnessServerIP} for notification on \\{NetName}\{ShareName} with error ({Error})
Microsoft-Windows-SMBWitnessClient  |  31        |  WitnessClientAdmin  |  Witness Client received error ({ErrorCode}) from Witness Server {WitnessServerIP} for \\{NetName}\{ShareName}
Microsoft-Windows-SMBWitnessClient  |  32        |  WitnessClientAdmin  |  Witness Client received resource notification {NotificationType} for \\{NetName}\{ShareName} from Witness Server {WitnessServerIP}
Microsoft-Windows-SMBWitnessClient  |  33        |  WitnessClientAdmin  |  Witness Client failed resource notification for \\{NetName}\{ShareName} with error ({Error})
Microsoft-Windows-SMBWitnessClient  |  34        |  WitnessClientAdmin  |  Witness Client received a request to move to a different file server node for \\{NetName}\{ShareName} from Witness Server {WitnessServerIP}
Microsoft-Windows-SMBWitnessClient  |  35        |  WitnessClientAdmin  |  Witness Client failed the move request for \\{NetName}\{ShareName} with error ({Error})
Microsoft-Windows-SMBWitnessClient  |  36        |  WitnessClientAdmin  |  Witness Client successfully unregistered from Witness Server {WitnessServerIP} for \\{NetName}\{ShareName}
Microsoft-Windows-SMBWitnessClient  |  37        |  WitnessClientAdmin  |  Witness Client failed to unregister from Witness Server {WitnessServerIP} for \\{NetName}\{ShareName} with error ({Error})
Microsoft-Windows-SMBWitnessClient  |  38        |  WitnessClientAdmin  |  Witness Client failed to unregister notification for NetName \\{NetName} with error ({Error})
Microsoft-Windows-SMBWitnessClient  |  39        |  WitnessClientAdmin  |  Witness Client failed to unregister notification for \\{NetName}\{ShareName} with error ({Error})
Microsoft-Windows-SMBWitnessClient  |  40        |  WitnessClientAdmin  |  Witness Client failed registration request for \\{NetName}\{ShareName} with error ({ErrorCode})
Microsoft-Windows-SMBWitnessClient  |  41        |  WitnessClientAdmin  |  Witness Client obtained the list of Witness Servers from IP address {WitnessServerIP} with error ({Error})