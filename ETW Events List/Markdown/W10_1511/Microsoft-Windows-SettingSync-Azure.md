Provider                             |  Event ID  |  Channel                                          |  Message
-------------------------------------|------------|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-SettingSync-Azure  |  5001      |  Microsoft-Windows-SettingSync-Azure/Operational  |  {ApiName} - Collection: {CollectionId}, ProviderOp: {ProviderOp}, Duration: {Duration}, HRESULT: {HRESULT}, CorrelationId: {CorrelationId}
Microsoft-Windows-SettingSync-Azure  |  5002      |  Microsoft-Windows-SettingSync-Azure/Operational  |  GetToken - Status: {WebTokenRequestStatus}, Result: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  5003      |  Microsoft-Windows-SettingSync-Azure/Operational  |  Failed to apply a setting unit to cloud for collection: {CollectionId} due to error HRESULT: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  5004      |  Microsoft-Windows-SettingSync-Azure/Operational  |  Call to register collections, operation: {UInt32}, HRESULT: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  5005      |  Microsoft-Windows-SettingSync-Azure/Operational  |  Unexpected object in data converter HRESULT: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  5006      |  Microsoft-Windows-SettingSync-Azure/Operational  |  Failed to convert FspFile {Filename} to a SettingUnit HRESULT: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  5007      |  Microsoft-Windows-SettingSync-Azure/Operational  |  Failed to transform unit {UnitId} to a transformed unit HRESULT: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  5008      |  Microsoft-Windows-SettingSync-Azure/Operational  |  Failed to convert unit {UnitId} to a FspFile HRESULT: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  5009      |  Microsoft-Windows-SettingSync-Azure/Operational  |  SettingDataConverter failed to initialize - CollectionId: {CollectionId}, HResult: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  5010      |  Microsoft-Windows-SettingSync-Azure/Operational  |  Failed to register collection: {String}, operation: {UInt32}, HRESULT: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  5011      |  Microsoft-Windows-SettingSync-Azure/Operational  |  Initialize Azure WNS registrar failed, HRESULT: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  6001      |  Microsoft-Windows-SettingSync-Azure/Debug        |  {ApiName} - Collection: {CollectionId}, ProviderOp: {ProviderOp}, Duration: {Duration}, HRESULT: {HRESULT}, CorrelationId: {CorrelationId}
Microsoft-Windows-SettingSync-Azure  |  6003      |  Microsoft-Windows-SettingSync-Azure/Debug        |  Call to initialize new Azure Settings WNF state name, New name: {Name0Data0} {Name0Data1}, HRESULT: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  6004      |  Microsoft-Windows-SettingSync-Azure/Debug        |  Call to uninitialize old Azure Settings WNF state name, Old name: {Name0Data0} {Name0Data1}, New Name: {Name1Data0} {Name1Data1}, HRESULT: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  6005      |  Microsoft-Windows-SettingSync-Azure/Debug        |  Call to register collections, operation: {UInt32}, HRESULT: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  6006      |  Microsoft-Windows-SettingSync-Azure/Debug        |  Ensure WNF state names initialized, HRESULT: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  6008      |  Microsoft-Windows-SettingSync-Azure/Debug        |  Bind WNF state name to WNS App Id, HRESULT: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  6009      |  Microsoft-Windows-SettingSync-Azure/Debug        |  Renew registrations, HRESULT: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  6010      |  Microsoft-Windows-SettingSync-Azure/Debug        |  Unregister unneeded registrations, HRESULT: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  6011      |  Microsoft-Windows-SettingSync-Azure/Debug        |  Cancel registrations, HRESULT: {HRESULT}
Microsoft-Windows-SettingSync-Azure  |  6012      |  Microsoft-Windows-SettingSync-Azure/Debug        |  Download remote interest, HRESULT: {HRESULT}