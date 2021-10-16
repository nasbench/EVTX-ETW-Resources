Provider                        |  Event ID  |  Channel                                     |  Message
--------------------------------|------------|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-OfflineFiles  |  1         |  Microsoft-Windows-OfflineFiles/Operational  |
Microsoft-Windows-OfflineFiles  |  2         |  Microsoft-Windows-OfflineFiles/Operational  |
Microsoft-Windows-OfflineFiles  |  3         |  Microsoft-Windows-OfflineFiles/Operational  |
Microsoft-Windows-OfflineFiles  |  4         |  Microsoft-Windows-OfflineFiles/Operational  |
Microsoft-Windows-OfflineFiles  |  5         |  Microsoft-Windows-OfflineFiles/Operational  |
Microsoft-Windows-OfflineFiles  |  6         |  System                                      |
Microsoft-Windows-OfflineFiles  |  7         |  Microsoft-Windows-OfflineFiles/Operational  |  User logon detectedAccount: {Account}Session: {Session}
Microsoft-Windows-OfflineFiles  |  8         |  Microsoft-Windows-OfflineFiles/Operational  |  User logoff detectedAccount: {Account}Session: {Session}
Microsoft-Windows-OfflineFiles  |  9         |  Microsoft-Windows-OfflineFiles/Operational  |  Path disconnected.{Path}
Microsoft-Windows-OfflineFiles  |  10        |  Microsoft-Windows-OfflineFiles/Operational  |  Path reconnected.{Path}
Microsoft-Windows-OfflineFiles  |  1000      |  Microsoft-Windows-OfflineFiles/Operational  |  Background agent failed startup, error = {Text}
Microsoft-Windows-OfflineFiles  |  1001      |  Microsoft-Windows-OfflineFiles/Operational  |  Background Synchronization failed on {Path}
Microsoft-Windows-OfflineFiles  |  1002      |  Microsoft-Windows-OfflineFiles/Operational  |
Microsoft-Windows-OfflineFiles  |  1003      |  Microsoft-Windows-OfflineFiles/Operational  |  Background Synchronization has started on {Path} as client has not synced for {MinutesSinceLastSync} minutes.
Microsoft-Windows-OfflineFiles  |  1004      |  Microsoft-Windows-OfflineFiles/Operational  |  Path {Path} transitioned to slow link with latency = {Latency} and bandwidth = {Bandwidth}
Microsoft-Windows-OfflineFiles  |  1005      |  Microsoft-Windows-OfflineFiles/Operational  |  Path {Path} transitioned to online with latency = {Latency}
Microsoft-Windows-OfflineFiles  |  2000      |  Microsoft-Windows-OfflineFiles/SyncLog      |  Sync info for {Path}Only the server copy exists.{Path}0See details for more information.
Microsoft-Windows-OfflineFiles  |  2001      |  Microsoft-Windows-OfflineFiles/SyncLog      |  Sync info for {Path}Only the client copy exists.{Path}2See details for more information.
Microsoft-Windows-OfflineFiles  |  2002      |  Microsoft-Windows-OfflineFiles/SyncLog      |  Sync info for {Path}Both client and server copies exist.{Path}7See details for more information.
Microsoft-Windows-OfflineFiles  |  2003      |  Microsoft-Windows-OfflineFiles/SyncLog      |  Sync info for {Path}Server copy exists, client copy deleted.{Path}3See details for more information.
Microsoft-Windows-OfflineFiles  |  2004      |  Microsoft-Windows-OfflineFiles/SyncLog      |  Sync info for {Path}Server copy exists, client copy replaced then deleted.{Path}0\See details for more information.
Microsoft-Windows-OfflineFiles  |  2005      |  Microsoft-Windows-OfflineFiles/SyncLog      |  Sync succeeded.{Path}Operation: {Operation}
Microsoft-Windows-OfflineFiles  |  2006      |  Microsoft-Windows-OfflineFiles/SyncLog      |  Sync failed.{Path}Operation: {Operation}Result: {Result}
Microsoft-Windows-OfflineFiles  |  2010      |  Microsoft-Windows-OfflineFiles/Operational  |  Creation of new excluded file type {Path} was blocked.
Microsoft-Windows-OfflineFiles  |  2011      |  Microsoft-Windows-OfflineFiles/Operational  |  Rename of file {SourcePath} to file {TargetPath} was blocked. The source and/or target file name is an excluded file type.