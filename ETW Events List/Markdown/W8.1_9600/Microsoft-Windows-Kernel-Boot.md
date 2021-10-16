Provider                       |  Event ID  |  Channel                                    |  Message
-------------------------------|------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-Kernel-Boot  |  1         |  Microsoft-Windows-Kernel-Boot/Analytic     |  System was booted in {Width}x{Height}@{BitsPerPixel}bpp.
Microsoft-Windows-Kernel-Boot  |  2         |  Microsoft-Windows-Kernel-Boot/Analytic     |  BootUX screen was displayed in {Width}x{Height}@{BitsPerPixel}bpp.
Microsoft-Windows-Kernel-Boot  |  3         |  Microsoft-Windows-Kernel-Boot/Analytic     |  Video bit transfer rate is {BytesPerMs} bytes per ms.
Microsoft-Windows-Kernel-Boot  |  4         |  Microsoft-Windows-Kernel-Boot/Analytic     |  Boot library accessed file {FileName} on Device {DeviceID}. Read {BytesRead} bytes and wrote {BytesWritten} bytes.
Microsoft-Windows-Kernel-Boot  |  5         |  Microsoft-Windows-Kernel-Boot/Analytic     |  File IO for boot application {ApplicationGuid}: Total Bytes Read = {BytesRead}, Total Bytes Written = {BytesWritten}.
Microsoft-Windows-Kernel-Boot  |  6         |  Microsoft-Windows-Kernel-Boot/Analytic     |  Image {ImageName} failed IntegrityCheck reason is {Reason}. Image flags are {ImageFlags}. Error ignored due to debugger {ErrorIgnored}.
Microsoft-Windows-Kernel-Boot  |  7         |  Microsoft-Windows-Kernel-Boot/Analytic     |  Bootmgr duration is {BootmgrTime} milliseconds.
Microsoft-Windows-Kernel-Boot  |  8         |  Microsoft-Windows-Kernel-Boot/Analytic     |  Image {ImageName} is not self-signed.
Microsoft-Windows-Kernel-Boot  |  9         |  Microsoft-Windows-Kernel-Boot/Analytic     |  A device ({DriveNumber}) that was enumerated by the BIOS was inaccessible to the boot environment.
Microsoft-Windows-Kernel-Boot  |  10        |  System                                     |  The system firmware has allocated a memory region previously determined to be unreliable. This has the potential to cause system instability and/or data corruption.
Microsoft-Windows-Kernel-Boot  |  11        |  Microsoft-Windows-Kernel-Boot/Analytic     |  The time elapsed before Bootmgr, based on the TSC, is {PreBootMgrTime} ms.
Microsoft-Windows-Kernel-Boot  |  12        |  Microsoft-Windows-Kernel-Boot/Analytic     |  Variable {UefiVariableName} requires {Size} bytes and was set with status {Status}.
Microsoft-Windows-Kernel-Boot  |  13        |  Microsoft-Windows-Kernel-Boot/Analytic     |  Element {Element} of application {ApplicationGuid} was not in policy.
Microsoft-Windows-Kernel-Boot  |  14        |  Microsoft-Windows-Kernel-Boot/Analytic     |  A Secure Boot Policy update resulted in status {Status}.
Microsoft-Windows-Kernel-Boot  |  15        |  Microsoft-Windows-Kernel-Boot/Analytic     |  A Secure Boot Revocation List update resulted in status {Status}.
Microsoft-Windows-Kernel-Boot  |  16        |  System                                     |  Windows failed to resume from hibernate with error status {FailureStatus}.
Microsoft-Windows-Kernel-Boot  |  17        |  System                                     |  The boot manager multi OS selection screen was displayed.
Microsoft-Windows-Kernel-Boot  |  18        |  System                                     |  There are {EntryCount} boot options on this system.
Microsoft-Windows-Kernel-Boot  |  19        |  System                                     |  There are {ToolsCount} boot tool options on this system.
Microsoft-Windows-Kernel-Boot  |  20        |  System                                     |  The last shutdown's success status was {LastShutdownGood}. The last boot's success status was {LastBootGood}.
Microsoft-Windows-Kernel-Boot  |  21        |  System                                     |  The OS loader advanced options menu was displayed and the user selected option {OptionSelected}.
Microsoft-Windows-Kernel-Boot  |  22        |  System                                     |  The OS loader edit options menu was displayed.
Microsoft-Windows-Kernel-Boot  |  23        |  System                                     |  The Windows key was pressed during boot.
Microsoft-Windows-Kernel-Boot  |  24        |  System                                     |  The F8 key was pressed during boot.
Microsoft-Windows-Kernel-Boot  |  25        |  System                                     |  The boot menu policy was {BootMenuPolicy}.
Microsoft-Windows-Kernel-Boot  |  26        |  System                                     |  A one-time boot sequence was used during this boot.
Microsoft-Windows-Kernel-Boot  |  27        |  System                                     |  The boot type was {BootType}.
Microsoft-Windows-Kernel-Boot  |  28        |                                             |
Microsoft-Windows-Kernel-Boot  |  29        |  System                                     |  Windows failed fast startup with error status {FailureStatus}.
Microsoft-Windows-Kernel-Boot  |  30        |  System                                     |  The firmware reported boot metrics.
Microsoft-Windows-Kernel-Boot  |  31        |  Microsoft-Windows-Kernel-Boot/Analytic     |  Initialization of the firmware crypto hash provider resulted in status {Status}.
Microsoft-Windows-Kernel-Boot  |  32        |  System                                     |  The bootmgr spent {BitlockerUserInputTime} ms waiting for user input.
Microsoft-Windows-Kernel-Boot  |  33        |  Microsoft-Windows-Kernel-Boot/Analytic     |  The firmware update capsule ({ImageName}) failed to load with status {ImageLoadStatus}.
Microsoft-Windows-Kernel-Boot  |  34        |  Microsoft-Windows-Kernel-Boot/Analytic     |  The PE/COFF image firmware update capsule ({PeImageName}) failed to load with status {PeImageLoadStatus}.
Microsoft-Windows-Kernel-Boot  |  35        |  Microsoft-Windows-Kernel-Boot/Analytic     |  The Efi UpdateCapsule failed to apply updates with status {UpdateCapsuleStatus}.
Microsoft-Windows-Kernel-Boot  |  36        |  Microsoft-Windows-Kernel-Boot/Analytic     |  Firmware update supported status is {UpdateSupportedStatus}. The BitLocker device flags are {DeviceFlags} and the PCR bitmap is {PcrBitmap}.
Microsoft-Windows-Kernel-Boot  |  37        |  Microsoft-Windows-Kernel-Boot/Analytic     |  The firmware update capsule ({ImageName}) code integrity check failed with status {ImageLoadStatus}.
Microsoft-Windows-Kernel-Boot  |  38        |  Microsoft-Windows-Kernel-Boot/Operational  |  Windows failed to load the required system file {ImageName} with error status {ImageLoadStatus}.
Microsoft-Windows-Kernel-Boot  |  39        |  Microsoft-Windows-Kernel-Boot/Operational  |  Windows failed to load the system registry file {HiveName} with error status {HiveLoadStatus}.
Microsoft-Windows-Kernel-Boot  |  40        |  Microsoft-Windows-Kernel-Boot/Operational  |  Windows failed to initialize the ACPI with error status {Status}.
Microsoft-Windows-Kernel-Boot  |  41        |  Microsoft-Windows-Kernel-Boot/Operational  |  Windows failed to load with error status {Status}.
Microsoft-Windows-Kernel-Boot  |  42        |  Microsoft-Windows-Kernel-Boot/Operational  |  Windows failed to load image {FailedPath} imported from {Path} with error status {Status}.
Microsoft-Windows-Kernel-Boot  |  43        |  Microsoft-Windows-Kernel-Boot/Operational  |  Windows failed to import {Import} from image {Path} with error status {Status}.