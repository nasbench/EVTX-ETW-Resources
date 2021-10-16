Provider                              |  Event ID  |  Channel                                           |  Message
--------------------------------------|------------|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-Devices-Background  |  1         |  System                                            |  {Application} requested task {TriggerID} to service device {Device}.
Microsoft-Windows-Devices-Background  |  2         |  System                                            |  Task {TriggerID} started servicing device {Device} (process {TaskProcessID}).
Microsoft-Windows-Devices-Background  |  3         |  System                                            |  Task {TriggerID} canceled servicing of device {Device} because: {Reason}.
Microsoft-Windows-Devices-Background  |  4         |  System                                            |  Task {TriggerID} finished servicing device {Duration}.
Microsoft-Windows-Devices-Background  |  5         |  System                                            |  Task {TriggerID} request was denied.  {Application} cannot service device {Device} because: {Reason}.
Microsoft-Windows-Devices-Background  |  6         |  System                                            |  Task {TriggerID} request failed.  {Application} cannot service {Device} because: {Error}.
Microsoft-Windows-Devices-Background  |  10        |  System                                            |  {Application} requested task {TriggerID} to access device to access device {Device}.
Microsoft-Windows-Devices-Background  |  11        |  System                                            |  Task {TriggerID} started accessing device {Device} (process {TaskProcessID}).
Microsoft-Windows-Devices-Background  |  12        |  System                                            |  Task {TriggerID} canceled access of device {Device} because: {Reason}.
Microsoft-Windows-Devices-Background  |  13        |  System                                            |  Task {TriggerID} finished accessing device {Duration}.
Microsoft-Windows-Devices-Background  |  14        |  System                                            |  Task {TriggerID} request was denied.  {Application} cannot access device {Device} in the background because: {Reason}.
Microsoft-Windows-Devices-Background  |  15        |  System                                            |  Task {TriggerID} request failed.  {Application} cannot access device {Device} in the background because: {Error}.
Microsoft-Windows-Devices-Background  |  20        |                                                    |
Microsoft-Windows-Devices-Background  |  21        |                                                    |
Microsoft-Windows-Devices-Background  |  22        |                                                    |
Microsoft-Windows-Devices-Background  |  30        |  Microsoft-Windows-Devices-Background/Operational  |  Package {packageName} is attempting to associate with {aepId}