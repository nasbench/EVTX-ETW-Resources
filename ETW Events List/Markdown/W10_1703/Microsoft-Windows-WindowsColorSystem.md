Provider                              |  Event ID  |  Channel                                           |  Message
--------------------------------------|------------|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-WindowsColorSystem  |  1         |  Microsoft-Windows-WindowsColorSystem/Operational  |  Installed color profile {Profile}.
Microsoft-Windows-WindowsColorSystem  |  2         |  Microsoft-Windows-WindowsColorSystem/Operational  |  Uninstalled color profile {Profile}.
Microsoft-Windows-WindowsColorSystem  |  3         |  Microsoft-Windows-WindowsColorSystem/Operational  |  Associated color profile {Profile} with device {Device} in {Scope} scope.
Microsoft-Windows-WindowsColorSystem  |  4         |  Microsoft-Windows-WindowsColorSystem/Operational  |  Disassociated color profile {Profile} from device {Device} in {Scope} scope.
Microsoft-Windows-WindowsColorSystem  |  5         |  Microsoft-Windows-WindowsColorSystem/Operational  |  Set default profile to {Profile} for device {Device} in {Scope} scope.
Microsoft-Windows-WindowsColorSystem  |  6         |  Microsoft-Windows-WindowsColorSystem/Operational  |  Set the "use per-user profiles" setting for device {Device} to {Setting}.
Microsoft-Windows-WindowsColorSystem  |  8         |  Microsoft-Windows-WindowsColorSystem/Operational  |  Set the default rendering intent to {Intent} in {Scope} scope.
Microsoft-Windows-WindowsColorSystem  |  9         |  Microsoft-Windows-WindowsColorSystem/Operational  |  Unset the default rendering intent in {Scope} scope. The system-wide default rendering intent will now be used.
Microsoft-Windows-WindowsColorSystem  |  10        |  Microsoft-Windows-WindowsColorSystem/Operational  |  Set the default profile for {Intent} rendering intent to {Profile} in {Scope} scope.
Microsoft-Windows-WindowsColorSystem  |  11        |  Microsoft-Windows-WindowsColorSystem/Operational  |  Unset the default profile for {Intent} rendering intent in {Scope} scope. This rendering intent will now use the corresponding system-wide default profile.
Microsoft-Windows-WindowsColorSystem  |  12        |  Microsoft-Windows-WindowsColorSystem/Operational  |  Set the default profile for working space '{WorkingSpace}' to {Profile} in {Scope} scope.
Microsoft-Windows-WindowsColorSystem  |  13        |  Microsoft-Windows-WindowsColorSystem/Operational  |  Unset the default profile for working space '{WorkingSpace}' in {Scope} scope. This working space will now use the corresponding system-wide default profile.
Microsoft-Windows-WindowsColorSystem  |  14        |  Microsoft-Windows-WindowsColorSystem/Operational  |  Set the default CAMP profile to {Profile} in {Scope} scope.
Microsoft-Windows-WindowsColorSystem  |  15        |  Microsoft-Windows-WindowsColorSystem/Operational  |  Unset the default CAMP profile in {Scope} scope. The system-wide default CAMP profile will now be used.
Microsoft-Windows-WindowsColorSystem  |  16        |  Microsoft-Windows-WindowsColorSystem/Debug        |  WCS profile {Profile} is invalid: {Reason}
Microsoft-Windows-WindowsColorSystem  |  19        |  Microsoft-Windows-WindowsColorSystem/Debug        |  V4 LUT elements in '{Tag}' tag: B curves {BCurves}, Matrix {Matrix}, M curves {MCurves}, CLUT {CLut}, A curves {ACurves}.
Microsoft-Windows-WindowsColorSystem  |  20        |  Microsoft-Windows-WindowsColorSystem/Debug        |
Microsoft-Windows-WindowsColorSystem  |  21        |  Microsoft-Windows-WindowsColorSystem/Debug        |
Microsoft-Windows-WindowsColorSystem  |  22        |  Microsoft-Windows-WindowsColorSystem/Debug        |
Microsoft-Windows-WindowsColorSystem  |  23        |  Microsoft-Windows-WindowsColorSystem/Debug        |
Microsoft-Windows-WindowsColorSystem  |  24        |  Microsoft-Windows-WindowsColorSystem/Debug        |
Microsoft-Windows-WindowsColorSystem  |  25        |  Microsoft-Windows-WindowsColorSystem/Debug        |
Microsoft-Windows-WindowsColorSystem  |  26        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Device has extended range: ([{RMin}, {RMax}], [{GMin}, {GMax}], [{BMin}, {BMax}]).
Microsoft-Windows-WindowsColorSystem  |  27        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Destination device lightness range: [{Min}, {Max}].
Microsoft-Windows-WindowsColorSystem  |  28        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Creating gamut map model for {Intent} intent.
Microsoft-Windows-WindowsColorSystem  |  29        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Created standard gamut map model for {Intent} intent.
Microsoft-Windows-WindowsColorSystem  |  31        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Failed to create gamut map model: error {ErrorCode}.
Microsoft-Windows-WindowsColorSystem  |  32        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Opening color profile(CDMP = '{CdmFileName}' ({CdmType}), CAMP = '{CamFileName}' ({CamType}), GMMP = '{GmmFileName}' ({GmmType}), desired access = {Access}, share mode = {Share}, creation mode = {Creation}).
Microsoft-Windows-WindowsColorSystem  |  33        |  Microsoft-Windows-WindowsColorSystem/Debug        |
Microsoft-Windows-WindowsColorSystem  |  34        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Failed to open color profile: error {ErrorCode}.
Microsoft-Windows-WindowsColorSystem  |  35        |  Microsoft-Windows-WindowsColorSystem/Debug        |  ICC profile information: size = {Size} bytes, version = {Version}, class = '{DeviceClass}', data color space = '{ColorSpace}', profile connection space = '{Pcs}'.
Microsoft-Windows-WindowsColorSystem  |  36        |  Microsoft-Windows-WindowsColorSystem/Debug        |
Microsoft-Windows-WindowsColorSystem  |  37        |  Microsoft-Windows-WindowsColorSystem/Debug        |  CITE color transform optimization: {Optimization}.
Microsoft-Windows-WindowsColorSystem  |  38        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Selected {LutType} LUT.
Microsoft-Windows-WindowsColorSystem  |  39        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Selected '{Tag}' tag to create {LutType} LUT for '{Class}' class profile with {Intent} rendering intent.
Microsoft-Windows-WindowsColorSystem  |  40        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Creating color transform(LCS type = {LcsCSType}, intent = {LcsIntent}, source profile = '{SourceProfileName}', destination profile = '{DestProfileName}' ({DestProfileType}), target profile = '{TargetProfileName}' ({TargetProfileType}), flags = {Flags}).
Microsoft-Windows-WindowsColorSystem  |  41        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Creating multi-profile color transform({NumProfiles} profiles, {NumIntents} intents, flags = {Flags}).
Microsoft-Windows-WindowsColorSystem  |  42        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Color transform successfully created: hxform = {HXform}.
Microsoft-Windows-WindowsColorSystem  |  43        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Color transform creation failed: error {ErrorCode}.
Microsoft-Windows-WindowsColorSystem  |  44        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Translating colors(hxform = {HXform}, {NumColors} input colors, input color type = {InColorType}, output color type = {OutColorType}).
Microsoft-Windows-WindowsColorSystem  |  45        |  Microsoft-Windows-WindowsColorSystem/Debug        |  WCS translating colors(hxform = {HXform}, {NumColors} input colors, {NumInChannels} input channels, input data type = {InDataType}, {NumInBytes} input bytes, {NumOutChannels} output channels, output data type = {OutDataType}, {NumOutBytes} output bytes).
Microsoft-Windows-WindowsColorSystem  |  46        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Translating bitmap bits(hxform = {HXform}, input bitmap format = {InBitmapFormat}, width = {Width}, height = {Height}, input stride = {InStride}, output bitmap format = {OutBitmapFormat}, output stride = {OutStride}).
Microsoft-Windows-WindowsColorSystem  |  47        |  Microsoft-Windows-WindowsColorSystem/Debug        |
Microsoft-Windows-WindowsColorSystem  |  48        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Color translation failed: error {ErrorCode}.
Microsoft-Windows-WindowsColorSystem  |  49        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Calibration refresh invoked. Windows calibration state management enabled = {CalibrationManagementEnabled}.
Microsoft-Windows-WindowsColorSystem  |  50        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Refreshing calibration for device '{DeviceName}'. Color profile exists and contains calibration data = {ColorProfileExistsAndContainsCalibrationData}.
Microsoft-Windows-WindowsColorSystem  |  51        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Calibration refresh finished, return code = {ReturnCode}.
Microsoft-Windows-WindowsColorSystem  |  52        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Applying calibration adjustments.  Adapter gamma adjustments = {AdapterGammaAdjustments}, monitor adjustments = {MonitorAdjustments}.
Microsoft-Windows-WindowsColorSystem  |  53        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Setting Windows calibration state management to {NewValue}.
Microsoft-Windows-WindowsColorSystem  |  54        |  Microsoft-Windows-WindowsColorSystem/Debug        |
Microsoft-Windows-WindowsColorSystem  |  55        |  Microsoft-Windows-WindowsColorSystem/Debug        |
Microsoft-Windows-WindowsColorSystem  |  56        |  Microsoft-Windows-WindowsColorSystem/Debug        |
Microsoft-Windows-WindowsColorSystem  |  57        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Loading calibration data from color profile {ProfileName} failed with error {ReturnCode}.
Microsoft-Windows-WindowsColorSystem  |  58        |  Microsoft-Windows-WindowsColorSystem/Debug        |  Applying calibration data failed with error {ReturnCode}.