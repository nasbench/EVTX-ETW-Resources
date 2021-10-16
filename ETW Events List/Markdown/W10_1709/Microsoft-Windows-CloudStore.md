Provider                      |  Event ID  |  Channel                                   |  Message
------------------------------|------------|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-CloudStore  |  1         |  Microsoft-Windows-CloudStore/Operational  |  Error {Type} occurred. See event details for more information.
Microsoft-Windows-CloudStore  |  1000      |  Microsoft-Windows-CloudStore/Debug        |  Discovered schema provider {SchemaProvider}.
Microsoft-Windows-CloudStore  |  1001      |  Microsoft-Windows-CloudStore/Debug        |  Successfully loaded {ProviderCount} schemas.
Microsoft-Windows-CloudStore  |  2001      |  Microsoft-Windows-CloudStore/Operational  |  Ignoring ommitted field {FieldId} with unknown type {BondDataType}.
Microsoft-Windows-CloudStore  |  2003      |  Microsoft-Windows-CloudStore/Operational  |  Conflict resolution of type {QualifiedTypeName} started. 'Yours' data is version {YoursVersion} with size {YoursSize}. See event details for more information. Extended information may be available in the Debug log.
Microsoft-Windows-CloudStore  |  2004      |  Microsoft-Windows-CloudStore/Debug        |  Conflict resolution of type {QualifiedTypeName} started. See event details for more information.
Microsoft-Windows-CloudStore  |  2005      |  Microsoft-Windows-CloudStore/Operational  |  Conflict resolution of type {QualifiedTypeName} complete. Result is version {Version} with size {Size}. See event details for more information. Extended information may be available in the Debug log.
Microsoft-Windows-CloudStore  |  2006      |  Microsoft-Windows-CloudStore/Debug        |  Conflict resolution of type {QualifiedTypeName} complete. See event details for more information.
Microsoft-Windows-CloudStore  |  2007      |  Microsoft-Windows-CloudStore/Operational  |  Resolved a set containing duplicated values. The duplicate values were ignored. See event details for more information.
Microsoft-Windows-CloudStore  |  2008      |  Microsoft-Windows-CloudStore/Operational  |  The 'original' version ({OriginalVersion}) of type {QualifiedTypeName} is more recent than the 'theirs' version ({TheirsVersion}) or the 'yours' version ({YoursVersion}). Healing the store by using the most recent version ({ResolvedVersion}). See event details for more information.
Microsoft-Windows-CloudStore  |  2009      |  Microsoft-Windows-CloudStore/Operational  |  Type {QualifiedTypeName} was not registered by any schema provider.
Microsoft-Windows-CloudStore  |  3002      |  Microsoft-Windows-CloudStore/Debug        |  Sucessfully deleted {Id}. New version is {Version}.
Microsoft-Windows-CloudStore  |  3003      |  Microsoft-Windows-CloudStore/Debug        |  Saving {Id} and merging with 'theirs' data. 'Theirs' data has size {Size} and is version {Version}.
Microsoft-Windows-CloudStore  |  3004      |  Microsoft-Windows-CloudStore/Debug        |  Saving {Id} without 'theirs' data.
Microsoft-Windows-CloudStore  |  3005      |  Microsoft-Windows-CloudStore/Operational  |  Overwriting {Id} with 'yours' data to repair inaccessible store (access failed with error code {ErrorCode}).
Microsoft-Windows-CloudStore  |  3006      |  Microsoft-Windows-CloudStore/Operational  |  Uploading {Id} failed with error code {ErrorCode}. The data was sucessfully stored locally and will be uploaded later.
Microsoft-Windows-CloudStore  |  3007      |  Microsoft-Windows-CloudStore/Debug        |  Successfully loaded {Id}. See event details for more information.
Microsoft-Windows-CloudStore  |  3008      |  Microsoft-Windows-CloudStore/Debug        |  Successfully saved {Id}. See event details for more information.
Microsoft-Windows-CloudStore  |  3010      |  Microsoft-Windows-CloudStore/Debug        |  Successfully saved cloud data for {Id}. See event details for more information.
Microsoft-Windows-CloudStore  |  3012      |  Microsoft-Windows-CloudStore/Debug        |  Successfully saved merged cloud data for {Id}. See event details for more information.
Microsoft-Windows-CloudStore  |  3013      |  Microsoft-Windows-CloudStore/Operational  |  Downloading {Id} failed with error code {ErrorCode}.
Microsoft-Windows-CloudStore  |  3014      |  Microsoft-Windows-CloudStore/Debug        |  Delete of {Id} was ignored because the data changed after it was deleted. See event details for more information.
Microsoft-Windows-CloudStore  |  3015      |  Microsoft-Windows-CloudStore/Operational  |  The attempt to load {Id} failed because the data was corrupt. See event details for more information.
Microsoft-Windows-CloudStore  |  3016      |  Microsoft-Windows-CloudStore/Operational  |  The value {Id} was garbage collected from the local cache because it was not reachable.
Microsoft-Windows-CloudStore  |  4000      |  Microsoft-Windows-CloudStore/Operational  |
Microsoft-Windows-CloudStore  |  4001      |  Microsoft-Windows-CloudStore/Operational  |