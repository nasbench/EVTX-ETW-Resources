Provider                                |  Event ID  |  Channel                                            |  Message
----------------------------------------|------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------
Microsoft-Windows-WCN-Config-Registrar  |  8000      |  Microsoft-Windows-WCN-Config-Registrar/Diagnostic  |  WCN has started a new session.Peer UUID: {PeerUuid}Connect reason: {Trigger}Session GUID: {SessionGuid}
Microsoft-Windows-WCN-Config-Registrar  |  8001      |  Microsoft-Windows-WCN-Config-Registrar/Diagnostic  |  WCN has established a connection.Session GUID: {SessionGuid}
Microsoft-Windows-WCN-Config-Registrar  |  8003      |  Microsoft-Windows-WCN-Config-Registrar/Diagnostic  |  WCN is preparing to parse a message.Session GUID: {SessionGuid}Message: {MessageBlobLength}
Microsoft-Windows-WCN-Config-Registrar  |  8004      |  Microsoft-Windows-WCN-Config-Registrar/Diagnostic  |  WCN has generated a message.Session GUID: {SessionGuid}Message: {MessageBlobLength}
Microsoft-Windows-WCN-Config-Registrar  |  8010      |  Microsoft-Windows-WCN-Config-Registrar/Diagnostic  |  WCN has completed a session successfully.Session GUID: {SessionGuid}
Microsoft-Windows-WCN-Config-Registrar  |  8011      |  Microsoft-Windows-WCN-Config-Registrar/Diagnostic  |  WCN failed to complete a session.Session GUID: {SessionGuid}Error code: {ErrorCode}
Microsoft-Windows-WCN-Config-Registrar  |  8020      |  Microsoft-Windows-WCN-Config-Registrar/Diagnostic  |  WCN received a message.Transport: {Transport}Message: {MessageGuid}
Microsoft-Windows-WCN-Config-Registrar  |  8021      |  Microsoft-Windows-WCN-Config-Registrar/Diagnostic  |  WCN is sending a message.Transport: {Transport}Message: {MessageGuid}
Microsoft-Windows-WCN-Config-Registrar  |  8030      |  Microsoft-Windows-WCN-Config-Registrar/Diagnostic  |  WCN has changed its beacons on transport {Transport}
Microsoft-Windows-WCN-Config-Registrar  |  8031      |  Microsoft-Windows-WCN-Config-Registrar/Diagnostic  |  WCN has changed its probe response on transport {Transport}