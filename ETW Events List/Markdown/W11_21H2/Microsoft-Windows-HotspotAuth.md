Provider                       |  Event ID  |  Channel                                    |  Message
-------------------------------|------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-HotspotAuth  |  1001      |  Microsoft-Windows-HotspotAuth/Analytic     |  Hotspot authentication started for interface {InterfaceGuid}
Microsoft-Windows-HotspotAuth  |  1002      |  Microsoft-Windows-HotspotAuth/Operational  |  Hotspot authentication successfully completed for interface {InterfaceGuid}
Microsoft-Windows-HotspotAuth  |  1003      |  Microsoft-Windows-HotspotAuth/Operational  |  Hotspot authentication failed for interface {InterfaceGuid} with status ({Result}) and response code ({ResponseCode})
Microsoft-Windows-HotspotAuth  |  1004      |  Microsoft-Windows-HotspotAuth/Operational  |  Hotspot authentication has been cancelled for interface {InterfaceGuid}
Microsoft-Windows-HotspotAuth  |  1005      |  Microsoft-Windows-HotspotAuth/Analytic     |  Hotspot authentication has completed for interface {InterfaceGuid} with status ({AuthenticationScenarioType})
Microsoft-Windows-HotspotAuth  |  1006      |  Microsoft-Windows-HotspotAuth/Analytic     |  Hotspot authentication scenario has cancelled for interface {InterfaceGuid}
Microsoft-Windows-HotspotAuth  |  2001      |  Microsoft-Windows-HotspotAuth/Analytic     |  Discovering WISPr has started for interface {InterfaceGuid}
Microsoft-Windows-HotspotAuth  |  2002      |  Microsoft-Windows-HotspotAuth/Analytic     |  The hotspot on interface {InterfaceGuid} supports WISPr
Microsoft-Windows-HotspotAuth  |  2003      |  Microsoft-Windows-HotspotAuth/Operational  |  WISPr detection failed for interface {InterfaceGuid} with error ({Result})
Microsoft-Windows-HotspotAuth  |  2004      |  Microsoft-Windows-HotspotAuth/Analytic     |  WISPr detection completed for interface {InterfaceGuid} with status ({WisprScenarioType})
Microsoft-Windows-HotspotAuth  |  2005      |  Microsoft-Windows-HotspotAuth/Analytic     |  WISPr detection scenario has cancelled for interface {InterfaceGuid}
Microsoft-Windows-HotspotAuth  |  2006      |  Microsoft-Windows-HotspotAuth/Operational  |  The hotspot on interface {InterfaceGuid} does not support WISPr
Microsoft-Windows-HotspotAuth  |  2007      |  Microsoft-Windows-HotspotAuth/Operational  |  No WISPr discovery performed for the hotspot on interface {InterfaceGuid}
Microsoft-Windows-HotspotAuth  |  3001      |  Microsoft-Windows-HotspotAuth/Operational  |  No hotspot detected on interface {InterfaceGuid}
Microsoft-Windows-HotspotAuth  |  3002      |  Microsoft-Windows-HotspotAuth/Analytic     |  Interface {InterfaceGuid} disconnected