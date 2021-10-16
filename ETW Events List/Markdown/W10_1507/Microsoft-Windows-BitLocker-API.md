Provider                         |  Event ID  |  Channel                              |  Message
---------------------------------|------------|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-BitLocker-API  |  513       |  System                               |  BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.Protector GUID: {ProtectorGUID}Volume GUID: {VolumeGUID}
Microsoft-Windows-BitLocker-API  |  514       |  System                               |  Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.Errorcode: {ErrorCode}Protector GUID: {ProtectorGUID}Volume GUID: {VolumeGUID}
Microsoft-Windows-BitLocker-API  |  515       |  System                               |  BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.Protector GUID: {ProtectorGUID}Volume GUID: {VolumeGUID}
Microsoft-Windows-BitLocker-API  |  516       |  System                               |  A BitLocker certificate data recovery agent was created, because it was missing on the volume or added to the list of data recovery agents.Certificate thumbprint: {Thumbprint}Protector GUID: {ProtectorGUID}Volume GUID: {VolumeGUID}
Microsoft-Windows-BitLocker-API  |  517       |  System                               |  A BitLocker certificate data recovery agent was removed, because is no longer in the list of data recovery agents.Certificate thumbprint: {Thumbprint}Protector GUID: {ProtectorGUID}Volume GUID: {VolumeGUID}
Microsoft-Windows-BitLocker-API  |  518       |  System                               |  The attempt to create a data recovery agent protector on the BitLocker volume failed.Errorcode: {ErrorCode}Certificate thumbprint: {Thumbprint}Volume GUID: {VolumeGUID}
Microsoft-Windows-BitLocker-API  |  519       |  System                               |  The servicing of the data recovery agents on the volume failed.Errorcode: {ErrorCode}Volume GUID: {VolumeGUID}
Microsoft-Windows-BitLocker-API  |  520       |  System                               |  The management of the data recovery agents failed on this drive because this feature of BitLocker Drive Encryption is not supported in this edition of the Windows operating system. Errorcode: {ErrorCode}Volume GUID: {VolumeGUID}
Microsoft-Windows-BitLocker-API  |  521       |  System                               |  Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.
Microsoft-Windows-BitLocker-API  |  522       |  System                               |  Bootmgr determined that the following boot application has changed: {BootApplication}
Microsoft-Windows-BitLocker-API  |  523       |  System                               |  Bootmgr determined that the boot configuration data setting {BCDSetting} has changed for the following boot application: {BootApplication}
Microsoft-Windows-BitLocker-API  |  524       |  System                               |  Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.
Microsoft-Windows-BitLocker-API  |  525       |  System                               |  Bootmgr determined that the TPM is disabled.
Microsoft-Windows-BitLocker-API  |  526       |  System                               |  Bootmgr determined that the TPM is not accessible.
Microsoft-Windows-BitLocker-API  |  527       |  System                               |  The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.
Microsoft-Windows-BitLocker-API  |  528       |  System                               |  Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.
Microsoft-Windows-BitLocker-API  |  529       |  System                               |  Bootmgr determined that driver signature enforcement has been disabled.
Microsoft-Windows-BitLocker-API  |  530       |  System                               |  Bootmgr determined that the device was locked out due to too many failed password attempts.
Microsoft-Windows-BitLocker-API  |  531       |  System                               |  Bootmgr determined that the device was locked out due to Device Lockout state validation failure.
Microsoft-Windows-BitLocker-API  |  768       |  Management                           |  BitLocker encryption was started for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  769       |  Management                           |  BitLocker encryption will occur for volume {VolumeMountPoint} when the computer is restarted.
Microsoft-Windows-BitLocker-API  |  770       |  Management                           |  BitLocker decryption was started for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  771       |  Management                           |  BitLocker encryption was stopped for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  772       |  Management                           |  BitLocker encryption was restarted for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  773       |  Management                           |  BitLocker was suspended for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  774       |  Management                           |  BitLocker was resumed for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  775       |  Management                           |  A BitLocker key protector was created.Protector GUID: {ProtectorGUID}Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  776       |  Management                           |  A BitLocker key protector was removed.Protector GUID: {ProtectorGUID}Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  777       |  Management                           |  The PIN was updated for the operating system volume.Protector GUID: {ProtectorGUID}Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  778       |  Management                           |  The BitLocker volume {VolumeMountPoint} was reverted to an unprotected state.
Microsoft-Windows-BitLocker-API  |  779       |  Management                           |  The BitLocker volume {VolumeMountPoint} was erased.
Microsoft-Windows-BitLocker-API  |  780       |  Management                           |  The identification field was changed. Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  781       |  Management                           |  The BitLocker protected volume {VolumeMountPoint} was locked. Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  782       |  Management                           |  The BitLocker protected volume {VolumeMountPoint} was unlocked.Protector GUID: {ProtectorGUID}Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  783       |  Management                           |  BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.Protector GUID: {ProtectorGUID}Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  784       |  Management                           |  BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.Protector GUID: {ProtectorGUID}Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  785       |  Management                           |  Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.Protector GUID: {ProtectorGUID}Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  786       |  Management                           |  BitLocker free space wiping was started for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  787       |  Management                           |  BitLocker free space wiping was stopped for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  788       |  Management                           |  BitLocker free space wiping was restarted for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  789       |  Management                           |
Microsoft-Windows-BitLocker-API  |  790       |  Management                           |  A PIN change attempt failed.Error message: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  791       |  Management                           |
Microsoft-Windows-BitLocker-API  |  792       |  Management                           |  BitLocker encountered a failure to commit metadata changes for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  793       |  Management                           |  BitLocker resealed boot settings to the TPM for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  794       |  Management                           |  BitLocker failed to reseal boot settings to the TPM.Error message: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  795       |  Management                           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint} due to group policy.
Microsoft-Windows-BitLocker-API  |  796       |  Management                           |  BitLocker Drive Encryption is using software-based encryption to protect volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  797       |  Management                           |  Group Policy settings prevented BitLocker Drive Encryption from reverting to BitLocker software-based encryption. Volume {VolumeMountPoint} is not protected by BitLocker.
Microsoft-Windows-BitLocker-API  |  798       |  Management                           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint}.Drive is not provisioned for use with BitLocker hardware encryption:Hardware-based encryption is not activated on this drive.
Microsoft-Windows-BitLocker-API  |  799       |  Management                           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint}.Drive is not provisioned for use with BitLocker hardware encryption:The hardware-based encryption of this drive does not allow BitLocker to cryptographically protect the drive's media encryption key.
Microsoft-Windows-BitLocker-API  |  800       |  Management                           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint}.Drive is not provisioned for use with BitLocker hardware encryption:Hardware-based encryption is either not configured or has been configured improperly on this volume.
Microsoft-Windows-BitLocker-API  |  801       |  Management                           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint}.Drive is not provisioned for use with BitLocker hardware encryption:Hardware-based encryption cannot be used with this drive because the hardware encryption method used by this drive does not comply with the Group Policy requirement for drive encryption.
Microsoft-Windows-BitLocker-API  |  802       |  Management                           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint}.Drive is not provisioned for use with BitLocker hardware encryption:The key length, {ActualKeyLength} bits, required to enable hardware-based encryption is below the minimum key length supported by the drive: {ExpectedKeyLength}.
Microsoft-Windows-BitLocker-API  |  803       |  Management                           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint}.Drive is not provisioned for use with BitLocker hardware encryption:The key length, {ActualKeyLength} bits, required to enable hardware-based encryption is above the maximum key length supported by the drive: {ExpectedKeyLength}.
Microsoft-Windows-BitLocker-API  |  804       |  Management                           |  The target drive ({VolumeMountPoint}) cannot be managed by BitLocker because the drive's hardware encryption feature is already in use.
Microsoft-Windows-BitLocker-API  |  805       |  Management                           |  The BitLocker protected volume was unlocked in the Windows Recovery Environment.Protector GUID: {ProtectorGUID}Identification GUID: {IdentificationGUID}Unlock time: {UnlockTime}
Microsoft-Windows-BitLocker-API  |  806       |  Management                           |  BitLocker resealed boot settings to the TPM in the Windows Recovery Environment.Reseal time: {ResealTime}
Microsoft-Windows-BitLocker-API  |  807       |  Management                           |  BitLocker free space wiping was canceled for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  808       |  Management                           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint}.Drive is not provisioned for use with BitLocker hardware encryption:SID authority is not disabled on this drive.
Microsoft-Windows-BitLocker-API  |  809       |  Management                           |
Microsoft-Windows-BitLocker-API  |  810       |  Management                           |
Microsoft-Windows-BitLocker-API  |  811       |  Management                           |  BitLocker cannot use Secure Boot for integrity because the required UEFI variable '{VariableName}' is not present.
Microsoft-Windows-BitLocker-API  |  812       |  Management                           |  BitLocker cannot use Secure Boot for integrity because the UEFI variable '{VariableName}' could not be read.Error Message: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  813       |  Management                           |  BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for variable '{VariableName}' is missing or invalid.
Microsoft-Windows-BitLocker-API  |  814       |  Management                           |
Microsoft-Windows-BitLocker-API  |  815       |  Management                           |
Microsoft-Windows-BitLocker-API  |  816       |  Management                           |
Microsoft-Windows-BitLocker-API  |  817       |  Management                           |  BitLocker successfully sealed a key to the TPM.PCRs measured include [{PCRBitmap}].The source for these PCRs was: {PCRBitmapSource}.
Microsoft-Windows-BitLocker-API  |  818       |  Management                           |  BitLocker encountered a failure attempting to configure network unlock for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  819       |  Management                           |  The BitLocker service could not resume protection on the OS volume {VolumeMountPoint}, due to the following error: Bootable media in the drive.
Microsoft-Windows-BitLocker-API  |  820       |  Management                           |  The BitLocker service could not resume protection on the OS volume {VolumeMountPoint}, due to the following error: TPM is locked out.
Microsoft-Windows-BitLocker-API  |  821       |  Management                           |  The BitLocker service could not resume protection on the OS volume {VolumeMountPoint}, due to the following error: Group policy conflict.
Microsoft-Windows-BitLocker-API  |  822       |  Management                           |  The BitLocker service could not resume protection on the OS volume {VolumeMountPoint}, due to the following error code: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  823       |  System                               |  Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.
Microsoft-Windows-BitLocker-API  |  824       |  System                               |  Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.
Microsoft-Windows-BitLocker-API  |  825       |  Management                           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint}.This PC's firmware is not capable of supporting hardware encryption.
Microsoft-Windows-BitLocker-API  |  826       |  Management                           |
Microsoft-Windows-BitLocker-API  |  827       |  Management                           |  A password change attempt failed.Error message: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  828       |  Management                           |  BitLocker Drive Encryption recovery information for volume {VolumeMountPoint} was backed up successfully to your Microsoft account.Protector GUID: {ProtectorGUID}
Microsoft-Windows-BitLocker-API  |  829       |  Management                           |  Failed to backup BitLocker Drive Encryption recovery information for volume {VolumeMountPoint} to your Microsoft account.Error: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  830       |  Management                           |
Microsoft-Windows-BitLocker-API  |  831       |  Management                           |  Failed to save BitLocker Drive Encryption recovery information to your Microsoft account due to an error.Error Code: {JsonErrorCode}Localized Error Message: {LocalizedJsonError}
Microsoft-Windows-BitLocker-API  |  832       |  Management                           |  TCG Log parsing failure.Error: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  833       |  Management                           |
Microsoft-Windows-BitLocker-API  |  834       |  Management                           |  BitLocker determined that the TCG log is invalid for use of Secure Boot. The filtered TCG log for PCR[7] is included in this event.
Microsoft-Windows-BitLocker-API  |  835       |  Management                           |
Microsoft-Windows-BitLocker-API  |  836       |  Management                           |
Microsoft-Windows-BitLocker-API  |  837       |  Management                           |
Microsoft-Windows-BitLocker-API  |  838       |  Management                           |
Microsoft-Windows-BitLocker-API  |  839       |  Management                           |
Microsoft-Windows-BitLocker-API  |  840       |  Management                           |  A trusted WIM file has been added for volume {VolumeMountPoint}.The SHA-256 hash of the WIM file is: {BinaryData}
Microsoft-Windows-BitLocker-API  |  841       |  Management                           |  BitLocker was unable to update a key for volume {VolumeMountPoint} due to the following error: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  842       |  Management                           |  BitLocker was unable to reseal boot settings to the TPM in the Windows Recovery Environment.Error: {ErrorCode}Protection has been temporarily suspended.
Microsoft-Windows-BitLocker-API  |  843       |  Management                           |  BitLocker was suspended from within the Windows Recovery Environment.Suspend time: {ResealTime}
Microsoft-Windows-BitLocker-API  |  844       |  Management                           |  BitLocker was unable to recover from device lock in the Windows Recovery Environment.Error: {ErrorCode}Protection has been temporarily suspended.
Microsoft-Windows-BitLocker-API  |  845       |  Management                           |  BitLocker Drive Encryption recovery information for volume {VolumeMountPoint} was backed up successfully to your Azure AD.Protector GUID: {ProtectorGUID}.TraceId: {TraceGUID}
Microsoft-Windows-BitLocker-API  |  846       |  Management                           |  Failed to backup BitLocker Drive Encryption recovery information for volume {VolumeMountPoint} to your Azure AD.TraceId: {TraceGUID}Error: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  847       |  Management                           |  Failed to save BitLocker Drive Encryption recovery information to your Azure AD due to an error.Error Code: {JsonErrorCode}Localized Error Message: {LocalizedJsonError}
Microsoft-Windows-BitLocker-API  |  4096      |  Management                           |  Device Encryption could not be initialized.Error: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  4097      |  Microsoft-Windows-BitLocker/Tracing  |
Microsoft-Windows-BitLocker-API  |  4098      |  Microsoft-Windows-BitLocker/Tracing  |
Microsoft-Windows-BitLocker-API  |  4099      |  Management                           |  Device Encryption failed to process user logon event.Error: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  4100      |  Microsoft-Windows-BitLocker/Tracing  |
Microsoft-Windows-BitLocker-API  |  4101      |  Microsoft-Windows-BitLocker/Tracing  |
Microsoft-Windows-BitLocker-API  |  4102      |  Management                           |  BitLocker failed to recover after Device Lock.Error message: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  4103      |  Management                           |  Failed to automatically enable Device Encryption.Error Message: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  4104      |  Microsoft-Windows-BitLocker/Tracing  |
Microsoft-Windows-BitLocker-API  |  4105      |  Microsoft-Windows-BitLocker/Tracing  |
Microsoft-Windows-BitLocker-API  |  4106      |  Management                           |  Failed to automatically back up recovery password to your Microsoft account.Error Message: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  4107      |  Microsoft-Windows-BitLocker/Tracing  |
Microsoft-Windows-BitLocker-API  |  4108      |  Microsoft-Windows-BitLocker/Tracing  |
Microsoft-Windows-BitLocker-API  |  4109      |  Microsoft-Windows-BitLocker/Tracing  |
Microsoft-Windows-BitLocker-API  |  4110      |  Microsoft-Windows-BitLocker/Tracing  |
Microsoft-Windows-BitLocker-API  |  4111      |  Management                           |  Device Lock recovery event initiated for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  4112      |  Management                           |  MaxPasswordRetry policy enforced with TPM-based hardening for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  4113      |  Management                           |  MaxPasswordRetry policy enforced without hardware based hardening for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  4114      |  Management                           |  Device Lock recovery event initiated due to protected state mismatch for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  4116      |  Microsoft-Windows-BitLocker/Tracing  |  Device Encryption initialization for volume {VolumeMountPoint} start.
Microsoft-Windows-BitLocker-API  |  4117      |  Microsoft-Windows-BitLocker/Tracing  |  Device Encryption initialization for volume {VolumeMountPoint} stop.
Microsoft-Windows-BitLocker-API  |  4118      |  Operational                          |  Volume {VolumeMountPoint} could not be initialized for Device Encryption.Error: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  4119      |  Operational                          |
Microsoft-Windows-BitLocker-API  |  4120      |  Operational                          |
Microsoft-Windows-BitLocker-API  |  4121      |  Operational                          |