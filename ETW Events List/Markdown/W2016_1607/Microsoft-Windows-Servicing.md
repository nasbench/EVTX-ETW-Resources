Provider                     |  Event ID    |  Channel                            |  Message
-----------------------------|--------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-Servicing  |  1           |  Setup                              |  Initiating changes for package {identifier}. Current state is {currentPackageState}. Target state is {targetPackageState}. Client id: {client}.
Microsoft-Windows-Servicing  |  2           |  Setup                              |  Package {identifier} was successfully changed to the {targetPackageState} state.
Microsoft-Windows-Servicing  |  3           |  Setup                              |  Package {identifier} failed to be changed to the {targetPackageState} state. Status: {errorCode}.
Microsoft-Windows-Servicing  |  4           |  Setup                              |  A reboot is necessary before package {identifier} can be changed to the {targetPackageState} state.
Microsoft-Windows-Servicing  |  5           |  Setup                              |  The servicing request received for package {identifier} cannot be satisfied since the package is not applicable.
Microsoft-Windows-Servicing  |  6           |  Setup                              |  Package {identifier} failed to be changed to the {targetPackageState} state and is now partially installed. Status: {errorCode}.
Microsoft-Windows-Servicing  |  7           |  Setup                              |  Initiating changes to turn on update {updateName} of package {identifier}. Client id: {client}.
Microsoft-Windows-Servicing  |  8           |  Setup                              |  Initiating changes to turn off update {updateName} of package {identifier}. Client id: {client}.
Microsoft-Windows-Servicing  |  9           |  Setup                              |  Selectable update {updateName} of package {identifier} was successfully turned on.
Microsoft-Windows-Servicing  |  10          |  Setup                              |  Selectable update {updateName} of package {identifier} was successfully turned off.
Microsoft-Windows-Servicing  |  11          |  Setup                              |  Update {updateName} of package {identifier} failed to be turned on. Status: {errorCode}.
Microsoft-Windows-Servicing  |  12          |  Setup                              |  Update {updateName} of package {identifier} failed to be turned off. Status: {errorCode}.
Microsoft-Windows-Servicing  |  13          |  Setup                              |  A reboot is necessary before the selectable update {updateName} of package {identifier} can be turned on.
Microsoft-Windows-Servicing  |  14          |  Setup                              |  A reboot is necessary before the selectable update {updateName} of package {identifier} can be turned off.
Microsoft-Windows-Servicing  |  15          |  Setup                              |  Selectable update {updateName} of package {identifier} was successfully turned off with its payload removed.
Microsoft-Windows-Servicing  |  16          |  Setup                              |  Update {updateName} of package {identifier} failed to be turned off. Payload removal was requested. Status: {errorCode}.
Microsoft-Windows-Servicing  |  17          |  Microsoft-Windows-Servicing/Debug  |  Report:[{EventReport}]
Microsoft-Windows-Servicing  |  18          |  Microsoft-Windows-Servicing/Debug  |  START [Resolve]:[{EventReport}]
Microsoft-Windows-Servicing  |  20          |  Microsoft-Windows-Servicing/Debug  |  END [Resolve]:[{EventReport}]
Microsoft-Windows-Servicing  |  21          |  Microsoft-Windows-Servicing/Debug  |  START [Execute]:[{EventReport}]
Microsoft-Windows-Servicing  |  23          |  Microsoft-Windows-Servicing/Debug  |  END [Execute]:[{EventReport}]
Microsoft-Windows-Servicing  |  24          |  Microsoft-Windows-Servicing/Debug  |  START [Stage]:[{EventReport}]
Microsoft-Windows-Servicing  |  26          |  Microsoft-Windows-Servicing/Debug  |  END [Stage]:[{EventReport}]
Microsoft-Windows-Servicing  |  33          |  Microsoft-Windows-Servicing/Debug  |  START [DPX Expansion]:[{EventReport}]
Microsoft-Windows-Servicing  |  34          |  Microsoft-Windows-Servicing/Debug  |  END [DPX Expansion]:[{EventReport}]
Microsoft-Windows-Servicing  |  35          |  Microsoft-Windows-Servicing/Debug  |  START [Doq Stage]:[{EventReport}]
Microsoft-Windows-Servicing  |  37          |  Microsoft-Windows-Servicing/Debug  |  END [Doq Stage]:[{EventReport}]
Microsoft-Windows-Servicing  |  38          |  Microsoft-Windows-Servicing/Debug  |  START [Doq Unstage]:[{EventReport}]
Microsoft-Windows-Servicing  |  39          |  Microsoft-Windows-Servicing/Debug  |  END [Doq Unstage]:[{EventReport}]
Microsoft-Windows-Servicing  |  40          |  Microsoft-Windows-Servicing/Debug  |  START [Doq Critical Install]:[{EventReport}]
Microsoft-Windows-Servicing  |  41          |  Microsoft-Windows-Servicing/Debug  |  END [Doq Critical Install]:[{EventReport}]
Microsoft-Windows-Servicing  |  42          |  Microsoft-Windows-Servicing/Debug  |  START [Doq Install]:[{EventReport}]
Microsoft-Windows-Servicing  |  43          |  Microsoft-Windows-Servicing/Debug  |  END [Doq Install]:[{EventReport}]
Microsoft-Windows-Servicing  |  44          |  Microsoft-Windows-Servicing/Debug  |  STARt [Doq Critical Uninstall]:[{EventReport}]
Microsoft-Windows-Servicing  |  45          |  Microsoft-Windows-Servicing/Debug  |  END [Doq Critical Uninstall]:[{EventReport}]
Microsoft-Windows-Servicing  |  46          |  Microsoft-Windows-Servicing/Debug  |  START [Doq Uninstall]:[{EventReport}]
Microsoft-Windows-Servicing  |  47          |  Microsoft-Windows-Servicing/Debug  |  END [Doq Uninstall]:[{EventReport}]
Microsoft-Windows-Servicing  |  48          |  Microsoft-Windows-Servicing/Debug  |  START [Doq Device Install]:[{EventReport}]
Microsoft-Windows-Servicing  |  49          |  Microsoft-Windows-Servicing/Debug  |  END [Doq Device Install]:[{EventReport}]
Microsoft-Windows-Servicing  |  50          |  Microsoft-Windows-Servicing/Debug  |  START [InstallUninstall]:[{EventReport}]
Microsoft-Windows-Servicing  |  51          |  Microsoft-Windows-Servicing/Debug  |  END [InstallUninstall]:[{EventReport}]
Microsoft-Windows-Servicing  |  52          |  Microsoft-Windows-Servicing/Debug  |  START [Poqexec]:[{EventReport}]
Microsoft-Windows-Servicing  |  53          |  Microsoft-Windows-Servicing/Debug  |  END [Poqexec]:[{EventReport}]
Microsoft-Windows-Servicing  |  54          |  Microsoft-Windows-Servicing/Debug  |  START [Shutdown Processing]:[{EventReport}]
Microsoft-Windows-Servicing  |  55          |  Microsoft-Windows-Servicing/Debug  |  END [Shutdown Processing]:[{EventReport}]
Microsoft-Windows-Servicing  |  56          |  Microsoft-Windows-Servicing/Debug  |  START [Non-Critical Doq]:[{EventReport}]
Microsoft-Windows-Servicing  |  57          |  Microsoft-Windows-Servicing/Debug  |  END [Non-Critical Doq]:[{EventReport}]
Microsoft-Windows-Servicing  |  58          |  Microsoft-Windows-Servicing/Debug  |  START [Critical Doq]:[{EventReport}]
Microsoft-Windows-Servicing  |  59          |  Microsoft-Windows-Servicing/Debug  |  END [Critical Doq]:[{EventReport}]
Microsoft-Windows-Servicing  |  60          |  Microsoft-Windows-Servicing/Debug  |  START [Plan Package]:[{EventReport}]
Microsoft-Windows-Servicing  |  61          |  Microsoft-Windows-Servicing/Debug  |  END [Plan Package]:[{EventReport}]
Microsoft-Windows-Servicing  |  62          |  Microsoft-Windows-Servicing/Debug  |  TrustedInstaller Finalize Event Report:[{EventReport}]
Microsoft-Windows-Servicing  |  63          |  Microsoft-Windows-Servicing/Debug  |  TrustedInstaller Initialize Event Report:[{EventReport}]
Microsoft-Windows-Servicing  |  64          |  Microsoft-Windows-Servicing/Debug  |  Doq Stage Progress Event Report:[{EventReport}]
Microsoft-Windows-Servicing  |  65          |  Microsoft-Windows-Servicing/Debug  |  Doq Unstage Progress Event Report:[{EventReport}]
Microsoft-Windows-Servicing  |  66          |  Microsoft-Windows-Servicing/Debug  |  Doq Install Progress Event Report:[{EventReport}]
Microsoft-Windows-Servicing  |  67          |  Microsoft-Windows-Servicing/Debug  |  Doq Uninstall Progress Event Report:[{EventReport}]
Microsoft-Windows-Servicing  |  68          |  Microsoft-Windows-Servicing/Debug  |  Startup Complete Event Report:[{EventReport}]
Microsoft-Windows-Servicing  |  69          |  Microsoft-Windows-Servicing/Debug  |  START [AI Queue Processing]:[{DescString}]
Microsoft-Windows-Servicing  |  70          |  Microsoft-Windows-Servicing/Debug  |  END [AI Queue Processing]:[{DescString}]
Microsoft-Windows-Servicing  |  71          |  Microsoft-Windows-Servicing/Debug  |  START [AI Install]:[Description = [{DescString}], Phase = [{Phase}], Mode = [{Mode}], PrevComponent=[{PrevComponent}], NewComponent=[{NewComponent}]]
Microsoft-Windows-Servicing  |  72          |  Microsoft-Windows-Servicing/Debug  |  END [AI Install]:[Status=[{DescString}]]
Microsoft-Windows-Servicing  |  73          |  Microsoft-Windows-Servicing/Debug  |  Report: [{DescString}]
Microsoft-Windows-Servicing  |  74          |  Microsoft-Windows-Servicing/Debug  |  CSI INSTALL Deployment Event Report: [{DescString}]
Microsoft-Windows-Servicing  |  75          |  Microsoft-Windows-Servicing/Debug  |  CSI UNINSTALL Deployment Event Report: [{DescString}]
Microsoft-Windows-Servicing  |  76          |  Microsoft-Windows-Servicing/Debug  |  START [KTM Transaction]:[{DescString}]
Microsoft-Windows-Servicing  |  77          |  Microsoft-Windows-Servicing/Debug  |  END [KTM Transaction]:[{DescString}]
Microsoft-Windows-Servicing  |  78          |  Microsoft-Windows-Servicing/Debug  |  CSI COMPRESS Event Report: [{DescString}]
Microsoft-Windows-Servicing  |  79          |  Microsoft-Windows-Servicing/Debug  |  CSI Stage Component Event Report: [{DescString}]
Microsoft-Windows-Servicing  |  80          |  Microsoft-Windows-Servicing/Debug  |  CSI AI Completion Event Report: [{DescString}]
Microsoft-Windows-Servicing  |  82          |  Microsoft-Windows-Servicing/Debug  |  START [CSI SMIPI]:[{DescString}]
Microsoft-Windows-Servicing  |  83          |  Microsoft-Windows-Servicing/Debug  |  END [CSI SMIPI]:[{DescString}]
Microsoft-Windows-Servicing  |  84          |  Microsoft-Windows-Servicing/Debug  |  CSI SMIPI INSTALL Event Report: [{DescString}]
Microsoft-Windows-Servicing  |  85          |  Microsoft-Windows-Servicing/Debug  |  CSI Transaction Start Event Report: [{DescString}]
Microsoft-Windows-Servicing  |  86          |  Microsoft-Windows-Servicing/Debug  |  CSI Transaction End Event Report: [{DescString}]
Microsoft-Windows-Servicing  |  87          |  Microsoft-Windows-Servicing/Debug  |  START [CSI Corruption Detection Event]:[{DescString}]
Microsoft-Windows-Servicing  |  88          |  Microsoft-Windows-Servicing/Debug  |  END [CSI Corruption Detection Event]:[{DescString}]
Microsoft-Windows-Servicing  |  89          |  Microsoft-Windows-Servicing/Debug  |  START [CSI Corruption Repair Event]:[{DescString}]
Microsoft-Windows-Servicing  |  90          |  Microsoft-Windows-Servicing/Debug  |  END [CSI Corruption Repair Event]:[{DescString}]
Microsoft-Windows-Servicing  |  91          |  Microsoft-Windows-Servicing/Debug  |  START [CSI Scavenge]:[{DescString}]
Microsoft-Windows-Servicing  |  92          |  Microsoft-Windows-Servicing/Debug  |  END [CSI Scavenge]:[{DescString}]
Microsoft-Windows-Servicing  |  93          |  Microsoft-Windows-Servicing/Debug  |  START [CBS Scavenge]:[{EventReport}]
Microsoft-Windows-Servicing  |  94          |  Microsoft-Windows-Servicing/Debug  |  END [CBS Scavenge]:[{EventReport}]
Microsoft-Windows-Servicing  |  95          |  Microsoft-Windows-Servicing/Debug  |  START [Archive Logs]:[{EventReport}]
Microsoft-Windows-Servicing  |  96          |  Microsoft-Windows-Servicing/Debug  |  END [Archive Logs]:[{EventReport}]
Microsoft-Windows-Servicing  |  97          |  Microsoft-Windows-Servicing/Debug  |  START [Drain Catalogs]:[{EventReport}]
Microsoft-Windows-Servicing  |  98          |  Microsoft-Windows-Servicing/Debug  |  END [Drain Catalogs]:[{EventReport}]
Microsoft-Windows-Servicing  |  99          |  Microsoft-Windows-Servicing/Debug  |  START [Automatic Deepclean]:[{EventReport}]
Microsoft-Windows-Servicing  |  100         |  Microsoft-Windows-Servicing/Debug  |  END [Automatic Deepclean]:[{EventReport}]
Microsoft-Windows-Servicing  |  101         |  Microsoft-Windows-Servicing/Debug  |  START [Manual Deepclean]:[{EventReport}]
Microsoft-Windows-Servicing  |  102         |  Microsoft-Windows-Servicing/Debug  |  END [Manual Deepclean]:[{EventReport}]
Microsoft-Windows-Servicing  |  103         |  Microsoft-Windows-Servicing/Debug  |  START [Delete Session Files]:[{EventReport}]
Microsoft-Windows-Servicing  |  104         |  Microsoft-Windows-Servicing/Debug  |  END [Delete Session Files]:[{EventReport}]
Microsoft-Windows-Servicing  |  105         |  Microsoft-Windows-Servicing/Debug  |  Progress: UI message updated. {EventReport}
Microsoft-Windows-Servicing  |  1000        |  Setup                              |  Windows Servicing is processing hotpatch package {identifier}({releaseType}).
Microsoft-Windows-Servicing  |  1001        |  Setup                              |  Windows Servicing disabled hotpatching for package {identifier}({releaseType}) because update {updateName} is not enabled for hotpatching.
Microsoft-Windows-Servicing  |  1002        |  Setup                              |  Windows Servicing disabled hotpatching for package {identifier}({releaseType}) because servicing is being performed offline.
Microsoft-Windows-Servicing  |  1003        |  Setup                              |  Windows Servicing disabled hotpatching for package {identifier}({releaseType}) because a reboot is required to complete a prior operation.
Microsoft-Windows-Servicing  |  1004        |  Setup                              |  Windows Servicing successfully installed hotpatching package {identifier}({releaseType}).
Microsoft-Windows-Servicing  |  1005        |  Setup                              |  Windows Servicing has required a reboot to complete the installation of hotpatching package {identifier}({releaseType}).
Microsoft-Windows-Servicing  |  1006        |  Setup                              |  Windows Servicing disabled hotpatching for package {identifier}({releaseType}) because a file could not be replaced immediately.
Microsoft-Windows-Servicing  |  1007        |  Setup                              |  Windows Servicing disabled hotpatching for package {identifier}({releaseType}) because required files or custom actions are incompatible with hotpatching.
Microsoft-Windows-Servicing  |  1008        |  Setup                              |  Windows Servicing failed to perform hotpatching for package {identifier}({releaseType}) because the hotpatch installer required a reboot.
Microsoft-Windows-Servicing  |  1009        |  Setup                              |  Windows Servicing failed to perform hotpatching for package {identifier}({releaseType}) because of an error ({errorCode}).
Microsoft-Windows-Servicing  |  1010        |  Setup                              |  Windows Servicing disabled hotpatching for package {identifier}({releaseType}) because update {updateName} is being set to state {updateStateLoc}({updateState}).
Microsoft-Windows-Servicing  |  1011        |  Setup                              |  Windows Servicing disabled hotpatching for package {identifier}({releaseType}) because hotpatch update {updateName} will not be installed.
Microsoft-Windows-Servicing  |  1012        |  Setup                              |  Windows Servicing disabled hotpatching for package {identifier}({releaseType}) to process regular update {updateName}.
Microsoft-Windows-Servicing  |  1013        |  Setup                              |  Initiating system store corruption detection and repair. Detection Only: {detectionType}, Automatically Triggered: {triggerType}.
Microsoft-Windows-Servicing  |  1014        |  Setup                              |  System store corruption detection and repair has completed. Status: {errorCode}, Total instances of corruption found: {totalCorruption}, total instances of corruption repaired: {repaired}.
Microsoft-Windows-Servicing  |  1015        |  Setup                              |  {repaired} of {totalCorruption} instances of system store corruption have been repaired. Unrepaired corruptions may lead to failures in future system servicing.
Microsoft-Windows-Servicing  |  1073746195  |                                     |  Windows Servicing started a process of changing package {identifier}({releaseType}) state from {initialPackageStateLoc}({initialPackageState}) to {packageStateLoc}({packageState})
Microsoft-Windows-Servicing  |  1073746196  |                                     |  Windows Servicing is setting package {identifier}({releaseType}) state to {packageStateLoc}({packageState})
Microsoft-Windows-Servicing  |  1073746197  |                                     |  Windows Servicing successfully set package {identifier}({releaseType}) state to {packageStateLoc}({packageState})
Microsoft-Windows-Servicing  |  2147488022  |                                     |  Windows Servicing identified that package {identifier}({releaseType}) is not applicable for this system
Microsoft-Windows-Servicing  |  3221229847  |                                     |  Windows Servicing failed to complete the process of setting package {identifier} ({releaseType}) into {packageStateLoc}({packageState}) state
Microsoft-Windows-Servicing  |  2147488024  |                                     |  Servicing has required reboot to complete the operation of setting package {identifier}({releaseType}) into {packageStateLoc}({packageState}) state
Microsoft-Windows-Servicing  |  1073746207  |                                     |  Windows Servicing completed the process of changing update {updateName} from package {identifier} ({releaseType}) into {updateStateLoc}({updateState}) state
Microsoft-Windows-Servicing  |  3221229857  |                                     |  Windows Servicing failed to complete the process of changing update {updateName} from package {identifier}({releaseType}) into {updateStateLoc}({updateState}) state
Microsoft-Windows-Servicing  |  2147488034  |                                     |  Windows Servicing required reboot to complete the process of changing update {updateName} from package {identifier}({releaseType}) into {updateStateLoc}({updateState}) state
Microsoft-Windows-Servicing  |  1073746224  |                                     |  Windows Servicing is processing hotpatch package {identifier}({releaseType}).
Microsoft-Windows-Servicing  |  1073746225  |                                     |  Windows Servicing disabled hotpatching for package {identifier}({releaseType}) because update {updateName} is not enabled for hotpatching.
Microsoft-Windows-Servicing  |  1073746226  |                                     |  Windows Servicing disabled hotpatching for package {identifier}({releaseType}) because servicing is being performed offline.
Microsoft-Windows-Servicing  |  1073746227  |                                     |  Windows Servicing disabled hotpatching for package {identifier}({releaseType}) because a reboot is required to complete a prior operation.
Microsoft-Windows-Servicing  |  1073746228  |                                     |  Windows Servicing successfully installed hotpatching package {identifier}({releaseType}).
Microsoft-Windows-Servicing  |  1073746229  |                                     |  Windows Servicing has required a reboot to complete the installation of hotpatching package {identifier}({releaseType}).
Microsoft-Windows-Servicing  |  2147488054  |                                     |  Windows Servicing disabled hotpatching for package {identifier}({releaseType}) because a file could not be replaced immediately.
Microsoft-Windows-Servicing  |  2147488055  |                                     |  Windows Servicing disabled hotpatching for package {identifier}({releaseType}) because required files or custom actions are incompatible with hotpatching.
Microsoft-Windows-Servicing  |  2147488056  |                                     |  Windows Servicing failed to perform hotpatching for package {identifier}({releaseType}) because the hotpatch installer required a reboot.
Microsoft-Windows-Servicing  |  2147488057  |                                     |  Windows Servicing failed to perform hotpatching for package {identifier}({releaseType}) because of an error ({errorCode}).
Microsoft-Windows-Servicing  |  1073746240  |                                     |  Windows Servicing disabled hotpatching for package {identifier}({releaseType}) because update {updateName} is being set to state {updateStateLoc}({updateState}).
Microsoft-Windows-Servicing  |  2147488065  |                                     |  Windows Servicing disabled hotpatching for package {identifier}({releaseType}) because hotpatch update {updateName} will not be installed.
Microsoft-Windows-Servicing  |  2147488066  |                                     |  Windows Servicing disabled hotpatching for package {identifier}({releaseType}) to process regular update {updateName}.