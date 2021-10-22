Provider                                             |  Event ID  |  Channel      |  Message
-----------------------------------------------------|------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  256       |  Debug        |  Configure-SMRemoting.exe -GET begins
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  257       |  Debug        |  Configure-SMRemoting.exe -GET ends
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  512       |  Debug        |  Configure-SMRemoting.exe -ENABLE begins
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  513       |  Debug        |  Configure-SMRemoting.exe -ENABLE ends
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  514       |  Debug        |  Configure-SMRemoting.exe -ENABLE invokes PowerShell.exe Enable-PSRemoting
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  515       |  Debug        |  Configure-SMRemoting.exe -ENABLE completes PowerShell.exe Enable-PSRemoting
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  516       |  Debug        |  Configure-SMRemoting.exe -ENABLE Enable-PSRemoting reported error {ErrorCode}
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  517       |  Debug        |  Configure-SMRemoting.exe -ENABLE Enable-PSRemoting execution failed with errorcode {ErrorCode}
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  768       |  Debug        |  Configure-SMRemoting.exe -DISABLE begins
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  769       |  Debug        |  Configure-SMRemoting.exe -DISABLE ends
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  1024      |  Debug        |  Configure-SMRemoting.exe writes to STDOUT: {ptzMessage}
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  1025      |  Debug        |  Configure-SMRemoting.exe writes to STDERR: {ptzMessage}
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  1026      |  Debug        |  WinRM API invoked: action {Action} parameters {Parameters}
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  1027      |  Debug        |  WinRM API return: action {Action} parameters {Parameters} ErrorCode {ErrorCode} result {Result}
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  1281      |  Operational  |  The testability key HKLM\\SOFTWARE\\Microsoft\\ServerManager\\Testability is present. This registry key is for debugging purposes only and can override the normal behavior of Configure-SMRemoting.exe. It is recommended to delete this key.
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  1282      |  Operational  |  Configure-SMRemoting.exe failed due to an internal error. Error: {ptzMessage}
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  1283      |  Operational  |  Configure-SMRemoting.exe -ENABLE failed to enable the WinRM service. Error: {ptzMessage}
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  1284      |  Operational  |  Configure-SMRemoting.exe -ENABLE failed to enable remoting. Error: {ptzMessage}
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  1285      |  Operational  |  Configure-SMRemoting.exe -DISABLE failed to disable remoting. Error: {ptzMessage}
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  1286      |  Operational  |  Configure-SMRemoting.exe -ENABLE generated this message while enabling PowerShell remoting: {ptzMessage}
Microsoft-Windows-ServerManager-ConfigureSMRemoting  |  1287      |  Operational  |  Configure-SMRemoting.exe -ENABLE enabled remoting, but generated this error message while attempting to enable PowerShell remoting: {ptzMessage}