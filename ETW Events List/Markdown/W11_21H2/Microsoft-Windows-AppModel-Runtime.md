Provider                            |  Event ID  |  Channel      |  Message
------------------------------------|------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-AppModel-Runtime  |  1         |               |  Process {ProcessID} started at time {CreateTime} by parent {ParentProcessID} running as package {PackageFullName} with executable {ImageName} is application {PackageRelativeApplicationId}.
Microsoft-Windows-AppModel-Runtime  |  2         |               |  {ErrorCode}: Cannot create the process for package {PackageFullName} because an error was encountered. {ErrorMessage}
Microsoft-Windows-AppModel-Runtime  |  3         |               |  {ErrorCode}: Cannot create the process for package {PackageFullName} because an error was encountered while querying the fast cache. {ErrorMessage}
Microsoft-Windows-AppModel-Runtime  |  4         |               |  {ErrorCode}: Cannot create the process for package {PackageFullName} because an error was encountered while preparing the App credentials. {ErrorMessage}
Microsoft-Windows-AppModel-Runtime  |  5         |               |  {ErrorCode}: Cannot create the process for package {PackageFullName} because an error was encountered while checking the user-level package status. {ErrorMessage}
Microsoft-Windows-AppModel-Runtime  |  6         |               |  {ErrorCode}: Cannot create the process for package {PackageFullName} because an error was encountered while checking the machine-level package status. {ErrorMessage}
Microsoft-Windows-AppModel-Runtime  |  7         |               |  {ErrorCode}: Cannot create the process for package {PackageFullName} because an error was encountered while verifying the App credentials. {ErrorMessage}
Microsoft-Windows-AppModel-Runtime  |  8         |               |  App {PackageFullName} was terminated with error {ErrorCode} because of an issue with application binary {FailedBinary}. This could be because the binary is unsigned, contains an untrusted signature, or has been corrupted or tampered with. Reinstall the application to fix this issue.
Microsoft-Windows-AppModel-Runtime  |  9         |  Application  |  App {PackageFullName} was terminated with error {ErrorCode} because of an issue with Windows binary {FailedBinary}. This could be because the binary is unsigned, contains an untrusted signature, or has been corrupted or tampered with. Refresh your PC to fix this issue.
Microsoft-Windows-AppModel-Runtime  |  11        |               |  App {PackageFullName} prevented the load of generated binary {FailedBinary} due to error {ErrorCode}. This could be because the binary is unsigned, contains an untrusted signature, or has been corrupted or tampered with.
Microsoft-Windows-AppModel-Runtime  |  12        |               |  An app prevented the load of a binary due to error {ErrorCode}. This could be because the binary is unsigned, contains an untrusted signature, or has been corrupted or tampered with.
Microsoft-Windows-AppModel-Runtime  |  14        |               |  {ErrorCode}: Package runtime information {FileName} is corrupted (address={HeaderAddr}, size={Size}, offset={Offset}, section={Section}, processid={ProcessId}). Reinstall the package to fix this issue.
Microsoft-Windows-AppModel-Runtime  |  15        |               |  {ErrorCode}: Package runtime information {FileName} is missing expected data (address={HeaderAddr}, size={Size}, section={Section}, processid={ProcessId}). Reinstall the package to fix this issue.
Microsoft-Windows-AppModel-Runtime  |  16        |               |  {ErrorCode}: Package runtime information {FileName} contains conflicting data (address={HeaderAddr}, size={Size}, offset={Offset}, section={Section}, processid={ProcessId}). Reinstall the package to fix this issue.
Microsoft-Windows-AppModel-Runtime  |  17        |               |  {ErrorCode}: Package runtime information {FileName} contains unexpected data (address={HeaderAddr}, size={Size}, offset={Offset}, section={Section}, processid={ProcessId}). Reinstall the package to fix this issue.
Microsoft-Windows-AppModel-Runtime  |  18        |               |  {ErrorCode}: Package runtime information {FileName} failed to load (processid={ProcessId}).
Microsoft-Windows-AppModel-Runtime  |  19        |               |  Package runtime information {FileName} failed to load because exception {ExceptionCode} occurred.
Microsoft-Windows-AppModel-Runtime  |  20        |               |  {ErrorCode}: Cannot create the process for package {PackageFullName} because an error was encountered while loading the runtime information. {ErrorMessage}
Microsoft-Windows-AppModel-Runtime  |  21        |               |  CreateAppContainerProfile failed for AppContainer {Context} with error {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  22        |               |  DeleteAppContainerProfile failed for AppContainer {Context} with error {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  23        |               |  UpdateAppContainerProfile failed for AppContainer {Context} with error {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  24        |               |  CreateAppContainerProfile failed with error {ErrorCode} because it was unable to create registry key {Context}.
Microsoft-Windows-AppModel-Runtime  |  25        |               |  CreateAppContainerProfile failed with error {ErrorCode} because it was unable to set security on registry key {Context}.
Microsoft-Windows-AppModel-Runtime  |  26        |               |  AppContainer profile failed with error {ErrorCode} because it was unable to delete registry key {Context}.
Microsoft-Windows-AppModel-Runtime  |  27        |               |  CreateAppContainerProfile failed with error {ErrorCode} because it was unable to create folder {Context}.
Microsoft-Windows-AppModel-Runtime  |  28        |               |  CreateAppContainerProfile failed with error {ErrorCode} because it was unable to set attributes on folder {Context}.
Microsoft-Windows-AppModel-Runtime  |  29        |               |  CreateAppContainerProfile failed with error {ErrorCode} because it was unable to verify the existence of registry key {Context}.
Microsoft-Windows-AppModel-Runtime  |  30        |               |  CreateAppContainerProfile failed with error {ErrorCode} because it was unable to verify the existence of folder {Context}.
Microsoft-Windows-AppModel-Runtime  |  31        |               |  CreateAppContainerProfile failed with error {ErrorCode} because it was unable to find the users local app data folder.
Microsoft-Windows-AppModel-Runtime  |  32        |               |  AppContainer profile failed with error {ErrorCode} because it was unable to delete folder {Context} or its contents.
Microsoft-Windows-AppModel-Runtime  |  33        |               |  AppContainer profile failed with error {ErrorCode} because it was unable to look up the AppContainer name.
Microsoft-Windows-AppModel-Runtime  |  34        |               |  AppContainer profile failed with error {ErrorCode} because it was unable to look up the AppContainer display name.
Microsoft-Windows-AppModel-Runtime  |  35        |               |  CreateAppContainerProfile failed with error {ErrorCode} because it was unable to register with the firewall.
Microsoft-Windows-AppModel-Runtime  |  36        |               |  DeleteAppContainerProfile failed with error {ErrorCode} because it was unable to unregister with the firewall.
Microsoft-Windows-AppModel-Runtime  |  37        |               |  App Container profile failed with error {ErrorCode} because it was unable to register the AppContainer SID.
Microsoft-Windows-AppModel-Runtime  |  38        |               |  DeleteAppContainerProfile failed with error {ErrorCode} because it was unable to unregister the AppContainer SID.
Microsoft-Windows-AppModel-Runtime  |  39        |               |  Successfully created AppContainer {AppContainerName}.
Microsoft-Windows-AppModel-Runtime  |  40        |               |  AppContainer {AppContainerName} was not created because it already exists.
Microsoft-Windows-AppModel-Runtime  |  41        |               |  Successfully deleted AppContainer {AppContainerName}.
Microsoft-Windows-AppModel-Runtime  |  42        |               |  Successfully updated AppContainer {AppContainerName}.
Microsoft-Windows-AppModel-Runtime  |  43        |               |  {ErrorCode}: Package runtime information {FileName} is missing expected data (address={HeaderAddr}, size={Size}, section={ApplicationUserModelId}, processid={ProcessId}). Reinstall the package to fix this issue.
Microsoft-Windows-AppModel-Runtime  |  44        |               |  {ErrorCode}: Application identity not accessible while loading package runtime information {FileName} (address={HeaderAddr}, size={Size}, processid={ProcessId}).
Microsoft-Windows-AppModel-Runtime  |  45        |               |  Failed with {ErrorCode} while retrieving AppContainer {Context} information during interaction with Restricted AppContainer.
Microsoft-Windows-AppModel-Runtime  |  46        |               |  Failed with {ErrorCode} while retrieving AppContainer information during interaction with Restricted AppContainer.
Microsoft-Windows-AppModel-Runtime  |  47        |               |  Failed with {ErrorCode} while retrieving AppContainer information. Call invalid from this process type.
Microsoft-Windows-AppModel-Runtime  |  48        |               |  Failed to create shared context object for Restricted AppContainer {Context} with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  49        |               |  Failed to activate Restricted AppContainer {Context} with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  50        |               |  Creation of Restricted AppContainer {Context} failed with {ErrorCode} because an invalid capability was specified.
Microsoft-Windows-AppModel-Runtime  |  51        |               |  Opening existing Restricted AppContainer {Context} failed with {ErrorCode} because the capabilities storage value could not be read.
Microsoft-Windows-AppModel-Runtime  |  52        |               |  Failed to create the capabilities storage value for Restricted AppContainer {Context} with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  53        |               |  The package {PackageFullName} requires validation.
Microsoft-Windows-AppModel-Runtime  |  54        |               |  Modification was detected in package {PackageFullName}.
Microsoft-Windows-AppModel-Runtime  |  55        |               |  Failed to terminate app with package {PackageFullName}.
Microsoft-Windows-AppModel-Runtime  |  56        |               |  Validation of app with package {PackageFullName} was successful.
Microsoft-Windows-AppModel-Runtime  |  57        |               |  Failed with {ErrorCode} to retrieve the trust state of the package {PackageFullName} folder.
Microsoft-Windows-AppModel-Runtime  |  58        |               |  App Integrity check failed with {ErrorCode} while checking {PackageFullName}.
Microsoft-Windows-AppModel-Runtime  |  59        |               |  App Integrity terminated an application. Integrity check for {PackageFullName} returned {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  60        |               |  App Integrity check for {PackageFullName} timed out.
Microsoft-Windows-AppModel-Runtime  |  61        |               |  {ErrorCode}: Cannot create the process for package {PackageFullName} because an error was encountered while performing the integrity check. {ErrorMessage}
Microsoft-Windows-AppModel-Runtime  |  62        |               |  Deployment server integrity check of package {ErrorCode} failed with {PackageFullName}.
Microsoft-Windows-AppModel-Runtime  |  63        |               |  Failed with {ErrorCode} retrieving AppModel Runtime group policy values.
Microsoft-Windows-AppModel-Runtime  |  64        |               |  Failed with {ErrorCode} validating AppModel Runtime group policy values.
Microsoft-Windows-AppModel-Runtime  |  65        |               |  Failed with {ErrorCode} retrieving AppModel Runtime status for package {PackageFullName}.
Microsoft-Windows-AppModel-Runtime  |  66        |               |  Failed with {ErrorCode} retrieving AppModel Runtime status for package {PackageFullName} for user {User}.
Microsoft-Windows-AppModel-Runtime  |  67        |               |  Failed with {ErrorCode} modifying AppModel Runtime status for package {PackageFullName} (current status = {CurrentStatus}, desired status = {DesiredStatus}).
Microsoft-Windows-AppModel-Runtime  |  68        |               |  AppModel Runtime status for package {PackageFullName} successfully updated to {DesiredStatus} (previous status = {CurrentStatus}).
Microsoft-Windows-AppModel-Runtime  |  69        |               |  Failed with {ErrorCode} modifying AppModel Runtime status for package {PackageFullName} for user {User} (current status = {CurrentStatus}, desired status = {DesiredStatus}).
Microsoft-Windows-AppModel-Runtime  |  70        |               |  AppModel Runtime status for package {PackageFullName} for user {User} successfully updated to {DesiredStatus} (previous status = {CurrentStatus}).
Microsoft-Windows-AppModel-Runtime  |  71        |               |  Failed with {ErrorCode} modifying AppModel Runtime status version (context = {Context}).
Microsoft-Windows-AppModel-Runtime  |  72        |               |
Microsoft-Windows-AppModel-Runtime  |  73        |               |  {ErrorCode}: Cannot create the process for package {PackageFullName} because an error was encountered while performing the app data creation. {ErrorMessage}
Microsoft-Windows-AppModel-Runtime  |  74        |               |  Package runtime information {FileName} failed to refresh because the following error {ErrorCode} occurred in operation type {Type}.
Microsoft-Windows-AppModel-Runtime  |  75        |               |  error {ErrorCode}: Cannot register the {PackageFullName} package because the following error was encountered while opening the HKEY_USERS registry key
Microsoft-Windows-AppModel-Runtime  |  76        |               |  error {ErrorCode}: Cannot register the {PackageFullName} package because the following error was encountered while enumerating to remove the {Key}\{Subkey} package family registry key
Microsoft-Windows-AppModel-Runtime  |  77        |               |  error {ErrorCode} : Cannot register the {PackageFullName} package because the following error was encountered while creating the {Key}\{Subkey} package family registry key
Microsoft-Windows-AppModel-Runtime  |  78        |               |  error {ErrorCode}: Cannot register the {PackageFullName} package because the following error was encountered while removing the {Key}\{Subkey} package family registry key
Microsoft-Windows-AppModel-Runtime  |  79        |               |  {ErrorCode}: Package family {PackageFamilyName} runtime information is corrupted. Attempting to correct the issue.
Microsoft-Windows-AppModel-Runtime  |  80        |               |  {ErrorCode}: Package family {PackageFamilyName} runtime information is corrupted but we cannot repair it at this time.
Microsoft-Windows-AppModel-Runtime  |  81        |               |  Failed with {ErrorCode} to get IsPackageStageInPlace info from State Repository cache for package {PackageFullName}. The app will by default require integrity check.
Microsoft-Windows-AppModel-Runtime  |  101       |               |  Creating AppContainer {AppContainerName}.
Microsoft-Windows-AppModel-Runtime  |  102       |               |  Finished creating AppContainer {Context} with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  103       |               |  Deleting AppContainer {AppContainerName}.
Microsoft-Windows-AppModel-Runtime  |  104       |               |  Finished deleting AppContainer {Context} with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  105       |               |  Updating AppContainer {AppContainerName}.
Microsoft-Windows-AppModel-Runtime  |  106       |               |  Finished updating AppContainer {Context} with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  107       |               |  Creating firewall rules for AppContainer {AppContainerName}.
Microsoft-Windows-AppModel-Runtime  |  108       |               |  Finished creating firewall rules for AppContainer {Context} with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  109       |               |  Deleting firewall rules for AppContainer {AppContainerName}.
Microsoft-Windows-AppModel-Runtime  |  110       |               |  Finished deleting firewall rules for AppContainer {Context} with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  111       |               |  Creating Restricted AppContainer {AppContainerName}.
Microsoft-Windows-AppModel-Runtime  |  112       |               |  Finished creating Restricted AppContainer {Context} with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  113       |               |  Deleting Restricted AppContainer {AppContainerName}.
Microsoft-Windows-AppModel-Runtime  |  114       |               |  Finished deleting Restricted AppContainer {Context} with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  115       |               |  Opening Restricted AppContainer {AppContainerName}.
Microsoft-Windows-AppModel-Runtime  |  116       |               |  Finished opening Restricted AppContainer {Context} with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  117       |               |  Enumerating all Restricted AppContainers for {AppContainerName}.
Microsoft-Windows-AppModel-Runtime  |  118       |               |  Finished enumerating all Restricted AppContainers for AppContainer {Context} with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  119       |               |  Launching process in Restricted AppContainer {AppContainerName}.
Microsoft-Windows-AppModel-Runtime  |  120       |               |  Finished launching process in Restricted AppContainer {Context} with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  121       |               |  Terminating all processes in Restricted AppContainer {AppContainerName}.
Microsoft-Windows-AppModel-Runtime  |  122       |               |  Finished terminating all processes in Restricted AppContainer {Context} with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  123       |               |  Checking package graph for {PackageFullName}.
Microsoft-Windows-AppModel-Runtime  |  124       |               |  Package graph check for {PackageFullName} finished with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  125       |               |  Performing app integrity check for package {PackageFullName}.
Microsoft-Windows-AppModel-Runtime  |  126       |               |  App integrity check for package {PackageFullName} finished with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  127       |               |  Performing runtime app integrity check for package {PackageFullName}.
Microsoft-Windows-AppModel-Runtime  |  128       |               |  Runtime app integrity check for package {PackageFullName} finished with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  129       |               |  Firewall Service not running. Skipping creation of firewall rules for AppContainer {AppContainerName}.
Microsoft-Windows-AppModel-Runtime  |  130       |               |  Updating Restricted AppContainer Capabilities {AppContainerName}.
Microsoft-Windows-AppModel-Runtime  |  131       |               |  Finished Updating Restricted AppContainer Capabilities {Context} with {ErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  201       |               |  Created process {ProcessID} for application {ApplicationName} in package {PackageName}. {Message}
Microsoft-Windows-AppModel-Runtime  |  202       |               |  {ErrorCode}: Cannot create the process for package {PackageName} because an error was encountered. {Message}
Microsoft-Windows-AppModel-Runtime  |  203       |               |  {ErrorCode}: Cannot create the process for package {PackageName} because an error was encountered while preparing for activation. {Message}
Microsoft-Windows-AppModel-Runtime  |  204       |               |  {ErrorCode}: Cannot create the process for package {PackageName} because an error was encountered while elevating the token. {Message}
Microsoft-Windows-AppModel-Runtime  |  205       |               |  {ErrorCode}: Cannot create the process for package {PackageName} because UI Access is not supported for Desktop AppX processes. {Message}
Microsoft-Windows-AppModel-Runtime  |  206       |               |  {ErrorCode}: Cannot create the process for package {PackageName} because an error was encountered while adjusting the token. {Message}
Microsoft-Windows-AppModel-Runtime  |  207       |               |  {ErrorCode}: Cannot create the process for package {PackageName} because an error was encountered while launching. {Message}
Microsoft-Windows-AppModel-Runtime  |  208       |               |  {ErrorCode}: Cannot create the process for package {PackageName} because an error was encountered while configuring runtime. {Message}
Microsoft-Windows-AppModel-Runtime  |  209       |               |  {ErrorCode}: Cannot create the process for package {PackageName} because an error was encountered while resuming the thread. {Message}
Microsoft-Windows-AppModel-Runtime  |  210       |               |  Created Desktop AppX container {ContainerId} for package {PackageName}.
Microsoft-Windows-AppModel-Runtime  |  211       |               |  Added process {ProcessID} to Desktop AppX container {ContainerId} for package {PackageName}.
Microsoft-Windows-AppModel-Runtime  |  212       |               |  {ErrorCode}: Cannot add process {ProcessID} to Desktop AppX container {ContainerId} for package {PackageName} because an error was encountered.
Microsoft-Windows-AppModel-Runtime  |  213       |               |  {ErrorCode}: Cannot create the Desktop AppX container for package {PackageName} because an error was encountered creating the job.
Microsoft-Windows-AppModel-Runtime  |  214       |               |  {ErrorCode}: Cannot create the Desktop AppX container for package {PackageName} because an error was encountered creating the description.
Microsoft-Windows-AppModel-Runtime  |  215       |               |  {ErrorCode}: Cannot create the Desktop AppX container for package {PackageName} because an error was encountered converting the job.
Microsoft-Windows-AppModel-Runtime  |  216       |               |  {ErrorCode}: Cannot create the Desktop AppX container for package {PackageName} because an error was encountered configuring the runtime.
Microsoft-Windows-AppModel-Runtime  |  217       |               |  Destroyed Desktop AppX container {ContainerId} for package {PackageName}.
Microsoft-Windows-AppModel-Runtime  |  218       |               |  Cannot destroy Desktop AppX container {MakeTemporaryErrorCode} for package {CleanupContainerErrorCode}.
Microsoft-Windows-AppModel-Runtime  |  219       |               |  PSMFlags for Desktop AppX process {PackageFullName} with applicationID {ApplicationId} is {PsmFlags}.