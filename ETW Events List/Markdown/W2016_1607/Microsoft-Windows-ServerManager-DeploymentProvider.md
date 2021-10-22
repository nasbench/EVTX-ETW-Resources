Provider                                            |  Event ID  |  Channel      |  Message
----------------------------------------------------|------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-ServerManager-DeploymentProvider  |  100       |  Debug        |  GetServerComponentAsync method started.
Microsoft-Windows-ServerManager-DeploymentProvider  |  101       |  Debug        |  GetServerComponentAsync method returned Completed.  Restart required: {restartRequired}
Microsoft-Windows-ServerManager-DeploymentProvider  |  102       |  Debug        |  GetServerComponentAsync method returned InProgress. {ticks} of {totalTicks}
Microsoft-Windows-ServerManager-DeploymentProvider  |  103       |  Operational  |  GetServerComponentAsync method returned Failed. Error: {message}
Microsoft-Windows-ServerManager-DeploymentProvider  |  104       |  Debug        |  GetEnumerationState method started.
Microsoft-Windows-ServerManager-DeploymentProvider  |  105       |  Debug        |  GetEnumerationState method returned Completed. Restart required: {restartRequired}
Microsoft-Windows-ServerManager-DeploymentProvider  |  106       |  Debug        |  GetEnumerationState method returned InProgress. {ticks} of {totalTicks}
Microsoft-Windows-ServerManager-DeploymentProvider  |  107       |  Operational  |  GetEnumerationState method returned Failed. Error: {message}
Microsoft-Windows-ServerManager-DeploymentProvider  |  108       |  Debug        |  GetServerComponent request started on a separate thread.
Microsoft-Windows-ServerManager-DeploymentProvider  |  109       |  Debug        |  GetServerComponent request ended on a separate thread.
Microsoft-Windows-ServerManager-DeploymentProvider  |  110       |  Debug        |  Generic Deployment Error: {message}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  111       |  Operational  |  Starting a GetServerComponent request.
Microsoft-Windows-ServerManager-DeploymentProvider  |  112       |  Operational  |  Completed processing the GetServerComponent request.  Restart required: {restartRequired}
Microsoft-Windows-ServerManager-DeploymentProvider  |  113       |  Operational  |  An error occured while processing the GetServerComponent. Error: {message}
Microsoft-Windows-ServerManager-DeploymentProvider  |  114       |  Operational  |  An error occured while creating Wbem CIM entry: {message} ClassName: {message2} Error: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  115       |  Debug        |  Component {ptzMessage} has invalid DISM state {value}
Microsoft-Windows-ServerManager-DeploymentProvider  |  200       |  Debug        |  AddServerComponentAsync method started. Adding ClassNames: {serverComponentNames}
Microsoft-Windows-ServerManager-DeploymentProvider  |  201       |  Debug        |  AddServerComponentAsync method returned InProgress. {ticks} of {totalTicks}
Microsoft-Windows-ServerManager-DeploymentProvider  |  202       |  Operational  |  AddServerComponentAsync method returned Failed. {message}
Microsoft-Windows-ServerManager-DeploymentProvider  |  203       |  Operational  |  Processing request to add Server Components: {serverComponentNames}
Microsoft-Windows-ServerManager-DeploymentProvider  |  204       |  Operational  |  Add request complete. Server Components added: {serverComponentNames}
Microsoft-Windows-ServerManager-DeploymentProvider  |  300       |  Debug        |  RemoveServerComponentAsync method started. Removing ClassNames: {serverComponentNames}
Microsoft-Windows-ServerManager-DeploymentProvider  |  301       |  Debug        |  RemoveServerComponentAsync method returned InProgress. {ticks} of {totalTicks}
Microsoft-Windows-ServerManager-DeploymentProvider  |  302       |  Operational  |  RemoveServerComponentAsync method returned Failed. Error: {message}
Microsoft-Windows-ServerManager-DeploymentProvider  |  303       |  Operational  |  Processing request to remove Server Components: {serverComponentNames}
Microsoft-Windows-ServerManager-DeploymentProvider  |  304       |  Operational  |  Remove request complete. Server Components removed: {serverComponentNames}
Microsoft-Windows-ServerManager-DeploymentProvider  |  400       |  Debug        |  GetAlterationState method started.
Microsoft-Windows-ServerManager-DeploymentProvider  |  401       |  Debug        |  GetAlterationState method ended. Reboot required: {restartRequired}
Microsoft-Windows-ServerManager-DeploymentProvider  |  402       |  Debug        |  GetAlterationState method returned InProgress. {ticks} of {totalTicks}
Microsoft-Windows-ServerManager-DeploymentProvider  |  403       |  Operational  |  GetAlterationState method returned Failed. Error: {message}
Microsoft-Windows-ServerManager-DeploymentProvider  |  450       |  Debug        |  Calling MI_RefuseUnload method.
Microsoft-Windows-ServerManager-DeploymentProvider  |  451       |  Debug        |  Calling MI_RequestUnload method.
Microsoft-Windows-ServerManager-DeploymentProvider  |  452       |  Debug        |  CreateEvent method call failed.
Microsoft-Windows-ServerManager-DeploymentProvider  |  453       |  Debug        |  CreateMutex method call failed.
Microsoft-Windows-ServerManager-DeploymentProvider  |  454       |  Debug        |  MI_PostResult method call failed.
Microsoft-Windows-ServerManager-DeploymentProvider  |  455       |  Debug        |  MI_Application_Initialize method call failed.
Microsoft-Windows-ServerManager-DeploymentProvider  |  456       |  Debug        |  MI_Application_Close method call failed.
Microsoft-Windows-ServerManager-DeploymentProvider  |  457       |  Debug        |  MI_RefuseUnload method call failed.
Microsoft-Windows-ServerManager-DeploymentProvider  |  458       |  Debug        |  MI_RequestUnload method call failed.
Microsoft-Windows-ServerManager-DeploymentProvider  |  459       |  Debug        |  The KeepAlive Callback method threw an exception.
Microsoft-Windows-ServerManager-DeploymentProvider  |  460       |  Debug        |  Starting the KeepAlive Mechanism.
Microsoft-Windows-ServerManager-DeploymentProvider  |  461       |  Debug        |  The KeepAlive Mechanism started on another thread.
Microsoft-Windows-ServerManager-DeploymentProvider  |  462       |  Debug        |
Microsoft-Windows-ServerManager-DeploymentProvider  |  463       |  Debug        |
Microsoft-Windows-ServerManager-DeploymentProvider  |  464       |  Debug        |
Microsoft-Windows-ServerManager-DeploymentProvider  |  465       |  Operational  |  Invalid Request GUID: {ptzMessage}
Microsoft-Windows-ServerManager-DeploymentProvider  |  466       |  Operational  |  A WMI operation failed. Op: {message} ErrorCode: {value}
Microsoft-Windows-ServerManager-DeploymentProvider  |  467       |  Operational  |  Exception detected while reporting a failure. Unable to recover. {ptzMessage}
Microsoft-Windows-ServerManager-DeploymentProvider  |  500       |  Debug        |  ExecuteEnumerationCommand {serverComponentNames} Guid {requestGuid}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  501       |  Debug        |  ExecuteEnumerationCommand ReadFromCache {serverComponentNames} Guid {requestGuid}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  502       |  Debug        |  ExecuteEnumerationCommand SpawnThread {serverComponentNames} Guid {requestGuid}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  503       |  Debug        |  Enumerate Function Call {serverComponentNames} Guid {requestGuid}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  504       |  Debug        |  Component Repository LoadFromCache {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  505       |  Debug        |  Component Repository BuildRelationshipModel {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  506       |  Debug        |  Component Repository ScanSystem {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  507       |  Debug        |  Create DismSessionManager {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  508       |  Debug        |  LoadRepository delete existing components {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  509       |  Debug        |  LoadRepository DismGetFeaturesEx API {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  510       |  Debug        |  LoadRepository add updates {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  511       |  Debug        |  LoadRepository add components {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  512       |  Debug        |  LoadRepository validate components {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  513       |  Debug        |  Original Server components, Update WMI CLass definitions {serverComponentNames} Guid {requestGuid}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  514       |  Debug        |  Write component results to registry {serverComponentNames} Guid {requestGuid}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  515       |  Debug        |  Write ServiceReport to registry {serverComponentNames} Guid {requestGuid}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  516       |  Debug        |  Consequtive Get Status requests {serverComponentNames} Guid {requestGuid}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  517       |  Debug        |  Consequtive Get requests read from registry {StartStop} Guid {requestGUID}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  518       |  Debug        |  Consequtive Get requests build sorted component tree {StartStop} Guid {requestGUID}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  519       |  Debug        |  Consequtive Get request select based on component names {StartStop} Guid {requestGUID}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  520       |  Debug        |  Consequtive Get request returning InProgress {StartStop} Guid {requestGUID}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  521       |  Debug        |  Add server component {serverComponentNames} Guid {requestGuid}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  522       |  Debug        |  Add server component on vhd {serverComponentNames} Guid {requestGuid}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  523       |  Debug        |  Reset component repository before Add {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  524       |  Debug        |  Prepare components for Add {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  525       |  Debug        |  Validate Mutual exclusion groups before add {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  526       |  Debug        |  Open Dism session for adding components {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  527       |  Debug        |  Get updates to deploy {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  528       |  Debug        |  DismEnableFeatures API {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  529       |  Debug        |  DismCommitImage API called after EnableFeatures {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  530       |  Debug        |  Refresh state fo modified components {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  531       |  Debug        |  Remove server component {serverComponentNames} Guid {requestGuid}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  532       |  Debug        |  Remove server component on vhd {serverComponentNames} Guid {requestGuid}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  533       |  Debug        |  Reset repository before removing components {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  534       |  Debug        |  Prepare components for remove {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  535       |  Debug        |  Create a list of components that are left installed after remove {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  536       |  Debug        |  Refresh the state of the modified components after refresh {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  537       |  Debug        |  Get the list of updates to remove {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  538       |  Debug        |  Update the children of Dism updates for removal {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  539       |  Debug        |  Add unused dism updates to the list for removal {serverComponentNames}..
Microsoft-Windows-ServerManager-DeploymentProvider  |  540       |  Debug        |  DismDisableFeatures API {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  541       |  Debug        |  DismCommitImage API for remove {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  542       |  Debug        |  Refresh the state of the modified components after refresh {serverComponentNames}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  543       |  Debug        |  Submit Alteration request {serverComponentNames} Guid {requestGuid}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  544       |  Debug        |  Convert Ids to unique names and save config data {serverComponentNames} Guid {requestGuid}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  545       |  Debug        |  Validate component identities {serverComponentNames} Guid {requestGuid}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  546       |  Debug        |  Mount Image {ptzMessage1} Image {ptzMessage2}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  547       |  Debug        |  Renmount Image {ptzMessage1} Image {ptzMessage2}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  548       |  Debug        |  Unmount Image {ptzMessage1} Image {ptzMessage2}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  549       |  Debug        |  UpdateImageInfo {ptzMessage1} Image {ptzMessage2}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  550       |  Debug        |  CBS Restart Check {ptzMessage}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  1281      |  Operational  |  Unknown MUM2 element detected. FeatureName: {ptzMessage1} UnknownElement: {ptzMessage2}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1282      |  Operational  |  Unknown MUM2 attribute detected. FeatureName: {ptzMessage1} Element: {ptzMessage2} UnknownAttribute: {ptzMessage3}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1283      |  Operational  |  Server components require the Id property. Container Update: {ptzMessage}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1284      |  Operational  |  Server components require the UniqueName property. Feature: {ptzMessage}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1285      |  Operational  |  Server components require the DisplayName property. Container Update: {ptzMessage}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1286      |  Operational  |  Server components require the Description property. Feature: {ptzMessage}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1287      |  Operational  |  Server component's parent not found. Container Update: {ptzMessage}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1288      |  Operational  |  Server components require the Version property. Container Update: {ptzMessage}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1289      |  Operational  |  Server component's deploys section contains an update that was not found. Container Update: {ptzMessage1}. Deploys Update: {ptzMessage2}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1290      |  Operational  |  Mutual Exclusion conflict detected. Components "{ptzMessage1}" are all members of group "{ptzMessage2}"
Microsoft-Windows-ServerManager-DeploymentProvider  |  1291      |  Operational  |  Failed to parse MUM2 Xml blob for update {message} hResult: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1292      |  Operational  |  Invalid MUM2 configuration status detected. Missing registry value. FeatureName: {ptzMessage}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1293      |  Debug        |  Internal fatal error while parsing MUM2 data. hResult: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1294      |  Debug        |  Internal fatal error. Op: {message} hResult: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1295      |  Operational  |  CBS Session {message} status. IsComplete: {message2} hResult: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1296      |  Debug        |  Task Start:  {ptzMessage}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1297      |  Debug        |  Task Stop:   {ptzMessage}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1298      |  Operational  |  Failed to read ConfigurationStatus from registry. Update {ptzMessage1} Key: {ptzMessage2} Value: {ptzMessage3}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1299      |  Operational  |  Using existing component cache from memory. Count: {value}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1300      |  Operational  |  Component cache read from registry. Count: {value}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1301      |  Operational  |  Component cache loaded from Dism. Count: {value}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1302      |  Operational  |  Unknown MUM2 value detected. FeatureName: {ptzMessage1} Attribute: {ptzMessage2} UnknownValue: {ptzMessage3}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1303      |  Operational  |  Failed to parse MUM2 for feature {ptzMessage}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1304      |  Debug        |  Found unknown update. FeatureName {ptzMessage}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1305      |  Operational  |  Unable to find component {ptzMessage1} referenced by component {ptzMessage2}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1306      |  Operational  |  Component {message} has invalid ServerComponentType {value}. This type is only valid if the component has a parent.
Microsoft-Windows-ServerManager-DeploymentProvider  |  1307      |  Operational  |  Failed to unmount image - {ptzMessage}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  1308      |  Operational  |  Internal fatal error. Op: {message} hResult: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1309      |  Operational  |  Partial install detected. Component {ptzMessage1} depends on uninstalled component {ptzMessage2}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1310      |  Operational  |  Invalid Mum2 detected for component {ptzMessage}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  1311      |  Operational  |
Microsoft-Windows-ServerManager-DeploymentProvider  |  1312      |  Operational  |  Failure loading OptionalCompanionFor from registry. Error: {ErrorCode}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  1313      |  Operational  |  Failed to load cache from registry. Error: {ErrorCode} Attempting to load components from system.
Microsoft-Windows-ServerManager-DeploymentProvider  |  1314      |  Operational  |  Update {ptzMessage1} is not present. ServerComponent {ptzMessage2} will be removed from the Role and Feature list.
Microsoft-Windows-ServerManager-DeploymentProvider  |  1315      |  Operational  |  Exception Detected: {ptzMessage1} ErrorID: {ptzMessage2}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1316      |  Debug        |  Unknown Parent {ptzMessage1} required by {ptzMessage2}. Removing {ptzMessage2} from feature list.
Microsoft-Windows-ServerManager-DeploymentProvider  |  1317      |  Operational  |  Unknown dependency {ptzMessage1} required by {ptzMessage2}. Removing {ptzMessage2} from feature list.
Microsoft-Windows-ServerManager-DeploymentProvider  |  1318      |  Debug        |  Unknown optional tool {ptzMessage1} for feature {ptzMessage2}.
Microsoft-Windows-ServerManager-DeploymentProvider  |  1537      |  Operational  |  Unable to open installer session. Error Code: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1538      |  Operational  |  Unable to initialize installer. Error Code: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1539      |  Operational  |  Failed to obtain status information from mounted images. hResult: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1540      |  Operational  |  Failed to mount image. ImageFile: {message} MountPath: {message2} hResult: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1541      |  Operational  |  Failed read features from system. hResult: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1542      |  Operational  |  Failed read feature info. Feature: {message} hResult: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1543      |  Operational  |  Failed get the last CBS session ID. hResult: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1544      |  Operational  |  Failed get the state from CBS session ID {message}. hResult: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1545      |  Operational  |  Failed to unmount image. ImageFile: {message} MountPath: {message2} hResult: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1546      |  Operational  |  Failed to remount image. ImageFile: {message} MountPath: {message2} hResult: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1547      |  Operational  |  Unable to install updates {message}. hResult: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1548      |  Operational  |  Unable to uninstall updates {message}. hResult: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1549      |  Debug        |  Dism session busy. Retry: {value}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1550      |  Debug        |  Attempting to enable updates via Dism: {ptzMessage}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1551      |  Debug        |  Attempting to disable updates via Dism: {ptzMessage}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1552      |  Debug        |  CBS session busy. Retry: {value}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1553      |  Operational  |  Internal fatal error. Op: {ptzMessage1} Message: {ptzMessage2}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1554      |  Operational  |  Error reading configuration status for {message}. Error: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1555      |  Operational  |  Failed to load module {message}. Error: {ErrorCode}
Microsoft-Windows-ServerManager-DeploymentProvider  |  1556      |  Operational  |  Failed to resource ID {value} from module {message}.