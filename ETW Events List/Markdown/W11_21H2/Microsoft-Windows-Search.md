Provider                  |  Event ID    |  Channel  |  Message
--------------------------|--------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-Search  |  1073742827  |           |  The Windows Search Service started.{ExtraInfo}
Microsoft-Windows-Search  |  1073742828  |           |  The Windows Search service is creating the new search index {Reason: {Reason}}. {ExtraInfo}
Microsoft-Windows-Search  |  1073742829  |           |  The Windows Search Service has successfully created the new search index. {ExtraInfo}
Microsoft-Windows-Search  |  3221226478  |           |  The Windows Search Service has failed to create the new search index. Internal error <{Phase}, {HR}, {DiagnosticsInfo}>. {ExtraInfo}
Microsoft-Windows-Search  |  3221226479  |           |  The Windows Search Service was unable to allocate memory.{ExtraInfo}
Microsoft-Windows-Search  |  2147484656  |           |  The Windows Search Service is starting up and attempting to remove the old search index {Reason: {Reason}}. {ExtraInfo}
Microsoft-Windows-Search  |  3221226481  |           |  An exception occurred in {Address}. Check other related Event Log messages.{ExtraInfo}
Microsoft-Windows-Search  |  1073742834  |           |  The Windows Search Service has successfully removed the old search index. {ExtraInfo}
Microsoft-Windows-Search  |  3221226483  |           |  The Windows Search Service has failed to remove the old search index. Internal error <{Phase},{HR}>. {ExtraInfo}
Microsoft-Windows-Search  |  1073742837  |           |  Windows Search Service stopped normally.{ExtraInfo}
Microsoft-Windows-Search  |  2147484662  |           |  The Windows Search Service has failed to create one or more path rules.  The service will continue creating the SystemIndex search index.  Debug information: <{DebugInfo}>. {ExtraInfo}
Microsoft-Windows-Search  |  2147484663  |           |  Event ID {EventID} for the Windows Search Service has been suppressed {RepeatCount} time(s) since {ReferenceTime}. This event is used to suppress Windows Search Service events that have occurred frequently within a short period of time.  See Event ID {EventID} for further details on this event.{ExtraInfo}
Microsoft-Windows-Search  |  3221226488  |           |  The Windows Search Service failed to move Index files from {OldIndexPath} to {NewIndexPath} with the following error: <{Phase},{ErrorCode}>. This might be because the target directory is not empty, or because the SYSTEM account doesn't have write access to the target directory. {ExtraInfo}
Microsoft-Windows-Search  |  1073742841  |           |  The Windows Search Service successfully moved index files from {OldIndexPath} to {NewIndexPath}. {ExtraInfo}
Microsoft-Windows-Search  |  2147484666  |           |  While rolling back the index, the Windows Search Service encountered the following error: <{Phase},{ErrorCode}>. Index files were not moved from {OldIndexPath} to {NewIndexPath}. {ExtraInfo}
Microsoft-Windows-Search  |  3221226491  |           |  Windows Search Service failed to process the list of included and excluded locations with the error <{Phase}, {ErrorCode}, "{Path}">. {ExtraInfo}
Microsoft-Windows-Search  |  2147484692  |           |  An error occurred in configuration file <{FileName}>.{ExtraInfo}
Microsoft-Windows-Search  |  2147484701  |           |  The system exception {Code} occurred and will be handled.  If this causes problems, contact Microsoft Product Support Services and include the stack trace in the event. {StackTrace}.
Microsoft-Windows-Search  |  3221228475  |           |  A configuration error occurred.{ExtraInfo}
Microsoft-Windows-Search  |  3221228478  |           |  Performance monitoring cannot be initialised for the gatherer service, because the counters are not loaded or the shared memory object cannot be opened. This only affects availability of the perfmon counters. Restart the computer.{ExtraInfo}
Microsoft-Windows-Search  |  3221228479  |           |  Performance monitoring cannot be initialised for the gatherer object, because the counters are not loaded or the shared memory object cannot be opened. This only affects availability of the perfmon counters. Restart the computer.{ExtraInfo}
Microsoft-Windows-Search  |  3221228480  |           |  The entry <{Entry}> cannot be inserted into the history.{ExtraInfo}
Microsoft-Windows-Search  |  3221228481  |           |  The transaction object cannot be created.{ExtraInfo}
Microsoft-Windows-Search  |  3221228482  |           |  The transaction cannot be appended to the queue. File: {FilePath}.{ExtraInfo}
Microsoft-Windows-Search  |  3221228483  |           |  The transaction cannot be updated in the queue. File: {FilePath}.{ExtraInfo}
Microsoft-Windows-Search  |  3221228485  |           |  The entry <{Entry}> in the hash map cannot be updated.{ExtraInfo}
Microsoft-Windows-Search  |  3221228486  |           |  An exception occurred. ID: {ID}. This is an internal error. Reproduce the error with the debugger attached and enable exceptions, then contact product support. One of the components loaded in your system is bad. You may be able to avoid the problem by recreating the index.{ExtraInfo}
Microsoft-Windows-Search  |  3221228487  |           |  The transaction file cannot be read.{ExtraInfo}
Microsoft-Windows-Search  |  3221228492  |           |  Internal gatherer error {ErrorCode} occurred. Please contact Microsoft Product Support Services.{ExtraInfo}
Microsoft-Windows-Search  |  2147486671  |           |  The update cannot be started because all of the content sources were excluded by site path rules or removed from the index configuration.{ExtraInfo}
Microsoft-Windows-Search  |  2147486672  |           |  The update cannot be started because the content sources cannot be accessed. Fix the errors and try the update again.{ExtraInfo}
Microsoft-Windows-Search  |  3221228497  |           |  Critical error {ErrorCode} occurred and the index was shut down. The system is probably low on resources. Free up resources and restart the service.{ExtraInfo}
Microsoft-Windows-Search  |  3221228498  |           |  Advise Status Change failed. The system is probably low on resources. Free up resources and restart the service.{ExtraInfo}
Microsoft-Windows-Search  |  3221228499  |           |  The URL <{URL}> cannot be crawled.{ExtraInfo}
Microsoft-Windows-Search  |  3221228500  |           |  The gatherer object cannot be initialised.{ExtraInfo}
Microsoft-Windows-Search  |  3221228501  |           |  The plug-in in <{Plugin}> cannot be initialised.{ExtraInfo}
Microsoft-Windows-Search  |  3221228502  |           |  The gatherer service cannot be initialised.{ExtraInfo}
Microsoft-Windows-Search  |  3221228503  |           |  A document ID cannot be allocated.{ExtraInfo}
Microsoft-Windows-Search  |  3221228504  |           |  A document ID cannot be freed.{ExtraInfo}
Microsoft-Windows-Search  |  3221228505  |           |  A new queue file cannot be created.{ExtraInfo}
Microsoft-Windows-Search  |  3221228506  |           |  The registry version does not match with the expected <{ExpectedVersion}>, or the registry cannot be accessed because the service account does not have the correct permissions.  Uninstall the previous version before installing the new one.{ExtraInfo}
Microsoft-Windows-Search  |  2147486684  |           |  Crawl could not be completed on content source <{URL}>.{ExtraInfo}
Microsoft-Windows-Search  |  2147486685  |           |  Crawl could not be started on content source <{URL}>.{ExtraInfo}
Microsoft-Windows-Search  |  2147486686  |           |  The gatherer is unable to read the registry {RegPath}.{ExtraInfo}
Microsoft-Windows-Search  |  2147486687  |           |  A request to start the update has been ignored because the update is already in progress or is scheduled on one or more content sources.{ExtraInfo}
Microsoft-Windows-Search  |  3221228512  |           |  The status change request {RequestedStatusMessage} cannot be processed.{ExtraInfo}
Microsoft-Windows-Search  |  1073744865  |           |  The index is being reset.{ExtraInfo}
Microsoft-Windows-Search  |  2147486690  |           |  The index was paused.{ExtraInfo}
Microsoft-Windows-Search  |  1073744868  |           |  The gatherer index resumed.{ExtraInfo}
Microsoft-Windows-Search  |  2147486693  |           |  The automatic description length was adjusted from {OldLength} to {NewLength}.{ExtraInfo}
Microsoft-Windows-Search  |  2147486694  |           |  The update for the index cannot be started because the specified content sources were not configured for updates. Add at least one content source.{ExtraInfo}
Microsoft-Windows-Search  |  3221228520  |           |  No documents were accessed because no email address is specified in the content index server properties. Specify the email address in the service configuration.{ExtraInfo}
Microsoft-Windows-Search  |  3221228522  |           |  Unvisited items cannot be deleted from the history after a full update.{ExtraInfo}
Microsoft-Windows-Search  |  1073744876  |           |  The crawl was requested to be stopped.{ExtraInfo}
Microsoft-Windows-Search  |  2147486701  |           |  The previous update was reset, or was otherwise interrupted. A full update of all content sources will be automatically started. {ExtraInfo}
Microsoft-Windows-Search  |  2147486702  |           |  The update has been delayed because a disk is full. Check the system default temp location and the drive on which search catalogue is created. The system default temp location is used for creation of temporary files during crawling. If it is full, crawling pauses. If the system default temp location is full, change the location to a disk with more free space and restart the computer. Changes to the system temp location do not take effect for system services until the computer is restarted.{ExtraInfo}
Microsoft-Windows-Search  |  2147486703  |           |  The gatherer property mapping file cannot be opened. The default values are being used. You may have to copy the property mapping file from the setup CD, or reinstall the application.{ExtraInfo}
Microsoft-Windows-Search  |  2147486704  |           |  The automatic description encoding tag value is invalid. The gatherer is setting this value to "yes". Fix the gthrprm.txt file.{ExtraInfo}
Microsoft-Windows-Search  |  3221228529  |           |  The plug-in manager <{PluginManager}> cannot be initialised.{ExtraInfo}
Microsoft-Windows-Search  |  3221228530  |           |  The application cannot be initialised.{ExtraInfo}
Microsoft-Windows-Search  |  3221228531  |           |  The update cannot be initialised.{ExtraInfo}
Microsoft-Windows-Search  |  1073744884  |           |  An update cannot begin because the content source <{URL}> is in use by another update already in progress. The update will start as soon as all its content sources are released by updates already in progress.{ExtraInfo}
Microsoft-Windows-Search  |  2147486709  |           |  The gatherer log cannot be created.{ExtraInfo}
Microsoft-Windows-Search  |  2147486710  |           |  The word breaker for language <{Locale}> cannot be loaded.{ExtraInfo}
Microsoft-Windows-Search  |  2147486720  |           |  The gatherer is recovering after an improper shutdown.  This will delay availability of gathering functions, and may result in some noncritical data loss.{ExtraInfo}
Microsoft-Windows-Search  |  2147486721  |           |  The gatherer detected pages in the history during recovery that cannot be read and repaired them.  However, statistical data for some URLs may have been lost.  This can be caused by restarting a computer without first shutting down Windows, or by disk failure.{ExtraInfo}
Microsoft-Windows-Search  |  2147486726  |           |  The Windows Search Service stopped the Protocol Host process because it was consuming too many resources.  A new Protocol Host process will be started.  No user action is required.{ExtraInfo}
Microsoft-Windows-Search  |  3221228551  |           |  Notifications for the volume {VolumeName} are not active. {ExtraInfo}
Microsoft-Windows-Search  |  3221228555  |           |  The protocol handler {ProtocolHandler} cannot be loaded. Error description: {ErrorMessage}. {ExtraInfo}
Microsoft-Windows-Search  |  3221228556  |           |  Failed to load protocol handler {ProtocolHandler}. Error description: {ErrorMessage}. {ExtraInfo}
Microsoft-Windows-Search  |  3221228557  |           |  The application network access account is invalid.  Update the account with a valid username and password. {ExtraInfo}
Microsoft-Windows-Search  |  2147486734  |           |  The system locale has changed. Existing data will be deleted and the index must be recreated.{ExtraInfo}
Microsoft-Windows-Search  |  3221228559  |           |  The gatherer files cannot be flushed, and this action cannot be completed. The gatherer will attempt to flush files again. If the problem persists, restart the service, free system resources, or verify that your hardware is working properly. {ExtraInfo}
Microsoft-Windows-Search  |  3221228560  |           |  The checkpoint record cannot be updated, and this action cannot be completed. The gatherer will attempt to update the checkpoint record again. If the problem persists, restart the service, free system resources, or verify that your hardware is working properly. {ExtraInfo}
Microsoft-Windows-Search  |  3221228561  |           |  The gatherer files cannot be saved, and this action cannot be completed. The gatherer will attempt to save the files again. If the problem persists, restart the service, free system resources, or verify that your hardware is working properly. {ExtraInfo}
Microsoft-Windows-Search  |  3221228562  |           |  The gatherer files from the previous checkpoint cannot be restored, and this action cannot be completed. The gatherer will attempt to restore the files again. If the problem persists, restart the service, free system resources, or verify that your hardware is working properly. {ExtraInfo}
Microsoft-Windows-Search  |  3221228563  |           |  The checkpoint record cannot be read, and this action cannot be completed.  If the problem persists, restart the service, free system resources, or verify that your hardware is working properly. {ExtraInfo}
Microsoft-Windows-Search  |  3221228564  |           |  The project cannot be initialised, because the checkpoint record cannot be read. The data structures on the disk will be reset.  Verify that your hardware is working properly. {ExtraInfo}
Microsoft-Windows-Search  |  3221228565  |           |  The project cannot be initialised, because one of the checkpoint files is missing. The data structures on the disk will be reset.  Check to see if someone is manually deleting files, and verify that your hardware is working properly. {ExtraInfo}
Microsoft-Windows-Search  |  1073744919  |           |  The group {Domain}\{Account} contains {Users} members. Groups over {MaxUsers} members are not expanded. {ExtraInfo}
Microsoft-Windows-Search  |  1073744920  |           |  The local groups cache was flushed, because {Reason}. {ExtraInfo}
Microsoft-Windows-Search  |  3221228569  |           |  The gatherer did not connect to the SQLServer instance.{ExtraInfo}
Microsoft-Windows-Search  |  3221228571  |           |  Unable to terminate notifications normally.  Restart the service or contact Product Support.{ExtraInfo}
Microsoft-Windows-Search  |  3221228572  |           |  Unable to initialise the filter host process. Terminating.{ExtraInfo}
Microsoft-Windows-Search  |  3221228573  |           |  The filter host process could not be terminated.
Microsoft-Windows-Search  |  1073745927  |           |  {ExtraInfo}A master merge has completed for catalogue {CatalogName}.
Microsoft-Windows-Search  |  1073745928  |           |  {ExtraInfo}A master merge has been paused for catalogue {CatalogName} due to error {ErrorMessage}. It will be rescheduled later.
Microsoft-Windows-Search  |  3221229577  |           |  {ExtraInfo}A master merge cannot be started for catalogue {CatalogName} due to error {ErrorMessage}.
Microsoft-Windows-Search  |  3221229578  |           |  {ExtraInfo}A master merge cannot be restarted for catalogue {CatalogName} due to error {ErrorMessage}.
Microsoft-Windows-Search  |  1073745945  |           |  {ExtraInfo}A master merge has restarted for catalogue {CatalogName}.
Microsoft-Windows-Search  |  1073745962  |           |  An index corruption was detected in component {Component} in catalogue {CatalogName}.{ExtraInfo}
Microsoft-Windows-Search  |  1073745987  |           |  {ExtraInfo}A master merge has been paused for catalogue {CatalogName} due to low disk space. The merge will be rescheduled later.  Please free some disk space for indexing to continue.
Microsoft-Windows-Search  |  1073745988  |           |  {ExtraInfo}Catalogue: {CatalogName}. A master merge was started due to an external request.
Microsoft-Windows-Search  |  1073745989  |           |  {ExtraInfo}Catalogue: {CatalogName}. A master merge was started because the catalogue reached the maximum number of indexes on the last level ({IndexesPerMergeLevel}).
Microsoft-Windows-Search  |  1073745990  |           |  {ExtraInfo}Catalogue: {CatalogName}. A master merge was started because the expected number of documents in the catalogue ({ExpectedDocCount}) were indexed.
Microsoft-Windows-Search  |  1073745991  |           |  {ExtraInfo}Catalogue: {CatalogName}. The master merge was started because of internal reason number {MasterMergeReason}.
Microsoft-Windows-Search  |  2147487816  |           |  {ExtraInfo} Unable to create the query engine's first request item due to error {ErrorMessage}. It's possible that the MSFTESQL service account is invalid or the password has expired.
Microsoft-Windows-Search  |  2147487817  |           |  Error ID {Phase} happened in Windows Search recovery stage, please restart the service. If this error persists, please recreate the index.{ExtraInfo}
Microsoft-Windows-Search  |  3221232473  |           |  The schema file <{SrcFile}> cannot be copied to <{DstFile}>.{ExtraInfo}
Microsoft-Windows-Search  |  3221232482  |           |  The index cannot be initialised.{ExtraInfo}
Microsoft-Windows-Search  |  3221232483  |           |  Directory location <{Directory}> is invalid. The application configuration cannot be read.  Reinstall the application.{ExtraInfo}
Microsoft-Windows-Search  |  3221232485  |           |  The update was paused because the disk <{Directory}> is full. Free up disk space to continue crawling the index.{ExtraInfo}
Microsoft-Windows-Search  |  3221232512  |           |  The search service has detected corrupted data files in the index {id={CorruptionId}}. The service will attempt to automatically correct this problem by rebuilding the index.{ExtraInfo}
Microsoft-Windows-Search  |  1073748866  |           |  The Windows Search Service is being stopped because there is a problem with the indexer: {Reason}.{ExtraInfo}
Microsoft-Windows-Search  |  3221232515  |           |  The index cannot be loaded.{ExtraInfo}
Microsoft-Windows-Search  |  3221232536  |           |  Performance monitoring cannot be initialised because the counters are not loaded or the shared memory object cannot be opened. Stop and restart the search service.  If this error continues, reinstall the application.{ExtraInfo}
Microsoft-Windows-Search  |  3221232538  |           |  Configuration directory {Directory} is missing, and disaster recovery must be performed. If there are existing indexes, they must be restored from the last backup. If there is no backup of index data, then delete the catalogues and recreate them.{ExtraInfo}
Microsoft-Windows-Search  |  3221232540  |           |  The registry cannot be read, possibly because the registry keys for this index are missing. You may have to delete and recreate the index {ExtraInfo}.
Microsoft-Windows-Search  |  3221232542  |           |  The Windows Search Service added catalogue {ExtraInfo}
Microsoft-Windows-Search  |  3221232543  |           |  The Windows Search Service removed index {ExtraInfo}
Microsoft-Windows-Search  |  3221234472  |           |  The Windows Search Service cannot open the Jet property store.{ExtraInfo}
Microsoft-Windows-Search  |  3221234473  |           |  The Windows Search Service cannot create a Jet property store.{ExtraInfo}
Microsoft-Windows-Search  |  3221234474  |           |  The Windows Search Service cannot load the property store information.{ExtraInfo}
Microsoft-Windows-Search  |  2147492651  |           |  The Windows Search Service cannot initialise multi-instancing in Jet. If the application is used in a cluster environment, all applications using Jet will fail in the same group.{ExtraInfo}
Microsoft-Windows-Search  |  2147493661  |           |  The noise files cannot be renamed.{ExtraInfo}
Microsoft-Windows-Search  |  2147493662  |           |  The noise file "{OldNoiseFile}" cannot be renamed to ""{NewNoiseFile}"".{ExtraInfo}
Microsoft-Windows-Search  |  2147493668  |           |  Performance counters could not be loaded for {Driver} for instance {InstanceName} {InstanceNum} due to the following error: {ErrorMessage}.
Microsoft-Windows-Search  |  2147493669  |           |  Could not get performance counter registry information for {Driver} for instance {InstanceName} {InstanceNum} due to the following error: {ErrorMessage}.
Microsoft-Windows-Search  |  2147493670  |           |  Performance counters will not be loaded because the named objects (shared memory or events) are in use for {Driver} for instance {InstanceName} {InstanceNum}.
Microsoft-Windows-Search  |  2147493671  |           |  The protocol host process {ProtocolHostProcessID} did not respond and is being forcibly terminated {filter host process {FilterHostProcessID}}. {ExtraInfo}
Microsoft-Windows-Search  |  2147493672  |           |  The filter host process {FilterHostProcessID} did not respond and is being forcibly terminated. {ExtraInfo}
Microsoft-Windows-Search  |  2147493673  |           |  The search service has failed to create database instance for the index {{ExtraInfo}} due to the maximum number of instances reached. Please re-configure the maximum value and restart the service.
Microsoft-Windows-Search  |  2147493674  |           |  The search service has failed to configure the maximum number of database instances. {{ExtraInfo}}. Please re-configure the maximum value and restart the service.
Microsoft-Windows-Search  |  2147493675  |           |  The search service has failed to create or load catalogue for a user with SID {{SID}}. Please check that a profile directory for the user is accessible. You should restart the search service after fixing any issue found from the profile directory. {ExtraInfo}
Microsoft-Windows-Search  |  2147493676  |           |  The search service has failed to unload catalogue for a user with SID {{SID}}. {ExtraInfo}