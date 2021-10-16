Provider                              |  Event ID  |  Channel     |  Message
--------------------------------------|------------|--------------|-------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-NFC-ClassExtension  |  1         |  Analytical  |  Write NCI packet payload (MessageType: {MessageType}, PacketBoundaryFlag: {PacketBoundaryFlag}, Size: {PacketSize}).
Microsoft-Windows-NFC-ClassExtension  |  2         |  Analytical  |  Received NCI packet payload (MessageType: {MessageType}, PacketBoundaryFlag: {PacketBoundaryFlag}, Size: {PacketSize}).
Microsoft-Windows-NFC-ClassExtension  |  3         |  Analytical  |  Write NCI packet (MessageType: {MessageType}, PacketBoundaryFlag: {PacketBoundaryFlag}, Size: {PacketSize}).
Microsoft-Windows-NFC-ClassExtension  |  4         |  Analytical  |  Received NCI packet (MessageType: {MessageType}, PacketBoundaryFlag: {PacketBoundaryFlag}, Size: {PacketSize}).
Microsoft-Windows-NFC-ClassExtension  |  101       |  Analytical  |  NFP client created (FileObject: {FileObject}, Role: {Role}).
Microsoft-Windows-NFC-ClassExtension  |  102       |  Analytical  |  NFP client destroyed (FileObject: {FileObject}, Role: {Role}).
Microsoft-Windows-NFC-ClassExtension  |  103       |  Analytical  |  NFP set payload (FileObject: {FileObject}, PayloadSize: {PayloadSize}).
Microsoft-Windows-NFC-ClassExtension  |  104       |  Analytical  |  NFP get next subscribed message start (FileObject: {FileObject}).
Microsoft-Windows-NFC-ClassExtension  |  105       |  Analytical  |  NFP get next subscribed message completed (FileObject: {FileObject}, Status: {Status}, Information: {Information}).
Microsoft-Windows-NFC-ClassExtension  |  106       |  Analytical  |  NFP get next transmitted message start (FileObject: {FileObject}).
Microsoft-Windows-NFC-ClassExtension  |  107       |  Analytical  |  NFP get next transmitted message completed (FileObject: {FileObject}, Status: {Status}).
Microsoft-Windows-NFC-ClassExtension  |  201       |  Analytical  |  Power set radio state (RadioIsOn: {RadioIsOn}).
Microsoft-Windows-NFC-ClassExtension  |  301       |  Analytical  |  RF interface initialization started.
Microsoft-Windows-NFC-ClassExtension  |  302       |  Analytical  |  RF interface initialization completed (Status: {Status}).
Microsoft-Windows-NFC-ClassExtension  |  303       |  Analytical  |  RF firmware version is: {Version}.
Microsoft-Windows-NFC-ClassExtension  |  304       |  Analytical  |  RF firmware download started (File: {FirmwareFile}, ForceDownload: {Force}).
Microsoft-Windows-NFC-ClassExtension  |  305       |  Analytical  |  RF firmware download completed (Status: {Status}).
Microsoft-Windows-NFC-ClassExtension  |  306       |  Analytical  |  RF event: {RfArrivalDepartureEvent}.
Microsoft-Windows-NFC-ClassExtension  |  307       |  Analytical  |  RF NDEF tag read start.
Microsoft-Windows-NFC-ClassExtension  |  308       |  Analytical  |  RF NDEF tag read stop (Status: {Status}, Length: {Length}).
Microsoft-Windows-NFC-ClassExtension  |  309       |  Analytical  |  RF NDEF tag write start (Length: {Length}).
Microsoft-Windows-NFC-ClassExtension  |  310       |  Analytical  |  RF NDEF tag write stop (Status: {Status}).
Microsoft-Windows-NFC-ClassExtension  |  401       |  Analytical  |  Device registry settings.
Microsoft-Windows-NFC-ClassExtension  |  402       |  Analytical  |  Device persisted registry settings.