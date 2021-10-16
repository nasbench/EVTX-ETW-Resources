Provider                       |  Event ID  |  Channel          |  Message
-------------------------------|------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-WorkFolders  |  0         |  Operational      |
Microsoft-Windows-WorkFolders  |  1         |  Operational      |
Microsoft-Windows-WorkFolders  |  2         |  Operational      |  A sync partnership was created between {LocalFolder} and {ServerURI} ({ServerPartnershipId}).
Microsoft-Windows-WorkFolders  |  3         |  Operational      |  A sync partnership between {LocalFolder} and {ServerURI} ({ServerPartnershipId}) was deleted.
Microsoft-Windows-WorkFolders  |  4         |  Operational      |  Resuming sync between {LocalFolder} and {ServerURI} ({ServerPartnershipId}).
Microsoft-Windows-WorkFolders  |  5         |  Operational      |  Attempting to apply the following Work Folders Group Policy configuration:Work Folders URL: {SyncUrl}Force automatic setup: {AutoProvision}
Microsoft-Windows-WorkFolders  |  6         |  Operational      |  Attempting to remove the following Work Folders Group Policy configuration:Discovery URL: {DiscoveryUrl} Server URL: {ServerUrl}
Microsoft-Windows-WorkFolders  |  7         |  Operational      |  Configuring Work Folders through Group Policy with the following options:Partnership ID: {PartnershipId}Partnership type: {PartnershipType}Discovery URL: {DiscoveryUrl}Server URL: {ServerUrl}
Microsoft-Windows-WorkFolders  |  8         |  Operational      |
Microsoft-Windows-WorkFolders  |  9         |  Operational      |  While applying Work Folders configuration through Group Policy, an existing Work Folders configuration was found. Discovery URL: {DiscoveryUrl} Server URL: {ServerUrl}Configured by policy: {ConfiguredByPolicy}
Microsoft-Windows-WorkFolders  |  10        |  Operational      |  Configuration of Work Folders through Group Policy failed. Error: {HResultStr}.
Microsoft-Windows-WorkFolders  |  11        |  Operational      |  There was a problem removing the Work Folders configuration when applying Group Policy. Error: {HResultStr}
Microsoft-Windows-WorkFolders  |  12        |  Operational      |  There was a problem communicating with the Windows Work Folders service. Confirm that this service is running. Error: {HResultStr}
Microsoft-Windows-WorkFolders  |  13        |  Operational      |  There was a problem retrieving your Work Folders Group Policy configuration. Error: {HResultStr}
Microsoft-Windows-WorkFolders  |  14        |  Operational      |  There was a problem retrieving your current Work Folders configuration. Error: {HResultStr}.
Microsoft-Windows-WorkFolders  |  15        |  Operational      |  There was a problem comparing the existing Work Folders configuration to the configuration being applied by Group Policy. Error: {HResultStr}.
Microsoft-Windows-WorkFolders  |  16        |  Operational      |  Server discovery on {DiscoveryURL} found server {ServerURL}.
Microsoft-Windows-WorkFolders  |  17        |  Operational      |  Sync Share discovery succeeded. Server URL: {ServerURL}; Partnership type: {SyncTargetType}; Server partnership id: {ServerPartnershipId}
Microsoft-Windows-WorkFolders  |  18        |  Operational      |  The discovery URL was found from the user's email address. User's email address: {UserEmail}; Discovery URL {DiscoveryURL}
Microsoft-Windows-WorkFolders  |  19        |  Operational      |  This PC is incompatible with the Work Folders server and must be upgraded. Please contact your administrator for instructions on upgrading your PC.
Microsoft-Windows-WorkFolders  |  502       |  Operational      |  A sync partnership between {LocalFolder} and {ServerURI} ({ServerPartnershipId}) failed to create with {HResultStr}.
Microsoft-Windows-WorkFolders  |  503       |  Operational      |  A sync partnership between {LocalFolder} and {ServerURI} ({ServerPartnershipId}) failed to delete with {HResultStr}.
Microsoft-Windows-WorkFolders  |  516       |  Operational      |  Server discovery on {DiscoveryURL} failed with {HResultStr}.
Microsoft-Windows-WorkFolders  |  517       |  Operational      |  Sync Share discovery failed. Server URL: {ServerURL}; Partnership type: {SyncTargetType}; Error: {HResultStr}
Microsoft-Windows-WorkFolders  |  518       |  Operational      |  Searching for a discovery URL from the user's email address failed. User's email address: {UserEmail}; Error: {HResultStr}
Microsoft-Windows-WorkFolders  |  1000      |  Operational      |  Some files cannot be downloaded. Make sure the drive for {Path} has at least {SizeMB} MB free.
Microsoft-Windows-WorkFolders  |  1001      |  Operational      |  Failed to get an ADFS access token from the server. User: {User}. ADFS URI: {StsUri}. Error: {HResultStr}
Microsoft-Windows-WorkFolders  |  1002      |  Operational      |  Failed to get an ADFS refresh token from the server. User: {User}. ADFS URI: {StsUri}. Error: {HResultStr}
Microsoft-Windows-WorkFolders  |  1100      |  Debug            |  Work Folders sucessfully uploaded a file. File name:{FileName}; Sync ID: {SyncId}
Microsoft-Windows-WorkFolders  |  1101      |  Debug            |  Work Folders failed to upload a file. File name:{FileName}; Sync ID: {SyncId}; Error: {HResultStr}
Microsoft-Windows-WorkFolders  |  1102      |  Debug            |  Work Folders sucessfully downloaded a file. File name:{FileName}; Sync ID: {SyncId}
Microsoft-Windows-WorkFolders  |  1103      |  Debug            |  Work Folders failed to download a file. File name:{FileName}; Sync ID: {SyncId}; Error: {HResultStr}
Microsoft-Windows-WorkFolders  |  1104      |  Debug            |  Work Folders sucessfully uploaded a change batch. Partnership ID:{SyncPartnershipId}
Microsoft-Windows-WorkFolders  |  1105      |  Debug            |  Work Folders failed to upload a change batch. Partnership ID:{SyncPartnershipId}; Error: {HResultStr}
Microsoft-Windows-WorkFolders  |  1106      |  Debug            |  Work Folders sucessfully downloaded a change batch. Partnership ID:{SyncPartnershipId}
Microsoft-Windows-WorkFolders  |  1107      |  Debug            |  Work Folders failed to download a change batch. Partnership ID:{SyncPartnershipId}; Error: {HResultStr}
Microsoft-Windows-WorkFolders  |  2000      |  Debug            |  Work Folders couldn't detect changed files using the USN change journal, so it's scanning all files for changes. No action is required. Path: {LocalReplicaRoot}
Microsoft-Windows-WorkFolders  |  2001      |  Debug            |  Sync started. URI: {SessionUri}
Microsoft-Windows-WorkFolders  |  2002      |  Debug            |  Sync completed.  URI: {SessionUri}
Microsoft-Windows-WorkFolders  |  2003      |  Debug            |  Sync batch upload completed.Uploaded {SuccessFileCount} file(s) ({SuccessDataSize} bytes).Failed {FailedFileCount} file(s) ({FailedDataSize} bytes).Elapsed time: {TotalBatchTime} seconds.Rate: {Rate} KBps.
Microsoft-Windows-WorkFolders  |  2004      |  Debug            |  Sync batch download completed.Downloaded {SuccessFileCount} file(s) ({SuccessDataSize} bytes).Failed {FailedFileCount} file(s).Elapsed time: {TotalBatchTime} seconds.Rate: {Rate} KBps.
Microsoft-Windows-WorkFolders  |  2005      |  Debug            |  HTTP request failure.URI: {Uri} Verb: {Verb} Headers: {Headers} Body Length: {BodyLength} HTTP Response: {HttpResponse} Server HRESULT: {ServerCodeStr}
Microsoft-Windows-WorkFolders  |  2006      |  Debug            |  Work Folders skipped uploading a file because of an error. Sync ID: {SyncId}; Error: {HResultStr}
Microsoft-Windows-WorkFolders  |  2007      |  Debug            |  Work Folders will skip downloading files because the user doesn't have enough free space on the drive where Work Folders is located. User: {Username}
Microsoft-Windows-WorkFolders  |  2008      |  Debug            |  Couldn't authenticate the user. User: {Username}
Microsoft-Windows-WorkFolders  |  2009      |  Debug            |  Work Folders successfully synchronized an item. Item: {ItemName}; Sync ID: {SyncGID}; Sync action: {Action}
Microsoft-Windows-WorkFolders  |  2010      |  Debug            |  Work Folders failed to synchronize an item. Item: {ItemName}; Sync ID: {SyncGID}; Sync action: {Action}; Error code: {HResultStr}
Microsoft-Windows-WorkFolders  |  2011      |  Debug            |  Work Folders successfully updated the current state of an item. Item: {ItemName}; Sync ID: {SyncGID}; Update action: {Action}
Microsoft-Windows-WorkFolders  |  2012      |  Debug            |  Work Folders failed to update the current state of an item. Item: {ItemName}; Sync ID: {SyncGID}; Update action: {Action}; Error code: {HResultStr}
Microsoft-Windows-WorkFolders  |  2013      |  Debug            |  Work Folders detected a conflict on an item and decided a conflict resolution. Concurrency conflict: {ConcurrencyConflict}; Source item name: {SourceItemName}; Source sync ID: {SourceSyncGID}; Destination item name: {DestinationItemName}; Destination sync ID: {DestinationSyncGID}; Data winner: {DataWinner}; Namespace winner: {NamespaceWinner}; Attributes winner: {AttributesWinner}; Tie breaker winner: {TieBreakerWinner}
Microsoft-Windows-WorkFolders  |  2014      |  Debug            |
Microsoft-Windows-WorkFolders  |  2015      |  Debug            |
Microsoft-Windows-WorkFolders  |  2100      |  Operational      |  Sync failed. Work Folders path: {LocalReplicaRoot}; Error: {HResultStr}
Microsoft-Windows-WorkFolders  |  2101      |  Operational      |  Work Folders suspended sync. Partnership: {SyncPartnershipId}
Microsoft-Windows-WorkFolders  |  2102      |  Operational      |  Work Folders resumed syncing. Partnership: {SyncPartnershipId}
Microsoft-Windows-WorkFolders  |  2103      |  Operational      |  Work Folders sync stopped because the Enterprise ID for this PC was remotely revoked by the issuing authority. Access to files in Work Folders is blocked on this PC. To resume syncing, in the Work Folders Control Panel, click Stop using Work Folders and then recreate the Work Folders synchronization partnership. Partnership: {SyncPartnershipId}
Microsoft-Windows-WorkFolders  |  2104      |  Operational      |  Work Folders detected a database corruption and recovered. Database path: {DatabasePath}
Microsoft-Windows-WorkFolders  |  2105      |  Operational      |  Work Folders detected a database corruption and recovery failed. Database path: {DatabasePath}; Error: {HResultStr}
Microsoft-Windows-WorkFolders  |  2106      |  Operational      |  Work Folders detected that the server database has been recreated. Local epoch: {LocalEpoch}; Server epoch: {ServerEpoch}
Microsoft-Windows-WorkFolders  |  2107      |  Operational      |  Work Folders detected that an error occured that requires the database to be recreated. Database path: {DatabasePath}; Error code: {HResultStr}
Microsoft-Windows-WorkFolders  |  2108      |  Operational      |  Work Folders synchronization metadata is stale. It will be automatically rebuild. Work Folders path: {LocalReplicaRoot}
Microsoft-Windows-WorkFolders  |  2109      |  Operational      |  The Work Folders synchronization metadata was created. Work Folders path: {LocalReplicaRoot}
Microsoft-Windows-WorkFolders  |  2110      |  Operational      |  The Work Folders synchronization metadata could not be created. Work Folders path: {LocalReplicaRoot}; Error: {HResultStr}
Microsoft-Windows-WorkFolders  |  2111      |  Operational      |  The Work Folders synchronization metadata was deleted. Work Folders path: {LocalReplicaRoot}
Microsoft-Windows-WorkFolders  |  2112      |  Operational      |  The Work Folders synchronization metadata could not be deleted. Work Folders path: {LocalReplicaRoot}; Error: {HResultStr}
Microsoft-Windows-WorkFolders  |  2113      |  Operational      |  Work Folders failed to update the current state of an item. Item: {ItemName}; Sync ID: {SyncGID}; Update action: {Action}; Error code: {HResultStr}
Microsoft-Windows-WorkFolders  |  2114      |  Operational      |  Work Folders failed to synchronize an item. Item: {ItemName}; Sync ID: {SyncGID}; Sync action: {Action}; Error code: {HResultStr}
Microsoft-Windows-WorkFolders  |  8000      |  Analytic         |  Starting sync. Work Folders path: {LocalReplicaRoot}
Microsoft-Windows-WorkFolders  |  8001      |  Analytic         |  Work Folders is looking for changed files. Work Folders path: {LocalReplicaRoot}
Microsoft-Windows-WorkFolders  |  8002      |  Analytic         |  Starting to download files. Work Folders path: {LocalReplicaRoot}
Microsoft-Windows-WorkFolders  |  8003      |  Analytic         |  Starting to upload files. Work Folders path: {LocalReplicaRoot}
Microsoft-Windows-WorkFolders  |  8004      |  Analytic         |  Finished syncing. Work Folders path: {LocalReplicaRoot}
Microsoft-Windows-WorkFolders  |  8005      |  Analytic         |  Starting reconciliation sync. Work Folders path: {LocalReplicaRoot}
Microsoft-Windows-WorkFolders  |  8006      |  Analytic         |  Finished reconciliation sync. Work Folders path: {LocalReplicaRoot}
Microsoft-Windows-WorkFolders  |  8007      |  Analytic         |  Starting sync knowledge upload. Server partnership id: {ServerPartnershipId}
Microsoft-Windows-WorkFolders  |  8008      |  Analytic         |  Starting data transfer for file download. Server partnership id: {ServerPartnershipId}
Microsoft-Windows-WorkFolders  |  8009      |  Analytic         |  Applying downloaded files. Work Folders path: {LocalReplicaRoot}
Microsoft-Windows-WorkFolders  |  8010      |  Analytic         |  Starting sync knowledge download. Server partnership id: {ServerPartnershipId}
Microsoft-Windows-WorkFolders  |  8011      |  Analytic         |  Creating a change batch for upload. Work Folders path: {LocalReplicaRoot}
Microsoft-Windows-WorkFolders  |  8012      |  Analytic         |  Starting data transfer for file upload. Server partnership id: {ServerPartnershipId}
Microsoft-Windows-WorkFolders  |  9001      |  ManagementAgent  |  Credentials required for the user.
Microsoft-Windows-WorkFolders  |  9002      |  ManagementAgent  |  Work Folders detected a sync error. Check partnership status, network connectivity, and disk space.
Microsoft-Windows-WorkFolders  |  9003      |  ManagementAgent  |  Work Folders detected a file error. Check file sizes and types are supported.
Microsoft-Windows-WorkFolders  |  9004      |  ManagementAgent  |  Your PC doesn't comply with your organization's security policies.