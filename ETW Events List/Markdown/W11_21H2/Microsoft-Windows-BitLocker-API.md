Provider                         |  Event ID  |  Channel  |  Message
---------------------------------|------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-BitLocker-API  |  513       |  System   |  BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.Protector GUID: {ProtectorGUID}Volume GUID: {VolumeGUID}
Microsoft-Windows-BitLocker-API  |  514       |  System   |  Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.Errorcode: {ErrorCode}Protector GUID: {ProtectorGUID}Volume GUID: {VolumeGUID}
Microsoft-Windows-BitLocker-API  |  515       |  System   |  BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.Protector GUID: {ProtectorGUID}Volume GUID: {VolumeGUID}
Microsoft-Windows-BitLocker-API  |  516       |  System   |  A BitLocker certificate data recovery agent was created, because it was missing on the volume or added to the list of data recovery agents.Certificate thumbprint: {Thumbprint}Protector GUID: {ProtectorGUID}Volume GUID: {VolumeGUID}
Microsoft-Windows-BitLocker-API  |  517       |  System   |  A BitLocker certificate data recovery agent was removed, because is no longer in the list of data recovery agents.Certificate thumbprint: {Thumbprint}Protector GUID: {ProtectorGUID}Volume GUID: {VolumeGUID}
Microsoft-Windows-BitLocker-API  |  518       |  System   |  The attempt to create a data recovery agent protector on the BitLocker volume failed.Errorcode: {ErrorCode}Certificate thumbprint: {Thumbprint}Volume GUID: {VolumeGUID}
Microsoft-Windows-BitLocker-API  |  519       |  System   |  The servicing of the data recovery agents on the volume failed.Errorcode: {ErrorCode}Volume GUID: {VolumeGUID}
Microsoft-Windows-BitLocker-API  |  520       |  System   |  The management of the data recovery agents failed on this drive because this feature of BitLocker Drive Encryption is not supported in this edition of the Windows operating system. Errorcode: {ErrorCode}Volume GUID: {VolumeGUID}
Microsoft-Windows-BitLocker-API  |  521       |  System   |  Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.
Microsoft-Windows-BitLocker-API  |  522       |  System   |  Bootmgr determined that the following boot application has changed: {BootApplication}
Microsoft-Windows-BitLocker-API  |  523       |  System   |  Bootmgr determined that the boot configuration data setting {BCDSetting} has changed for the following boot application: {BootApplication}
Microsoft-Windows-BitLocker-API  |  524       |  System   |  Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.
Microsoft-Windows-BitLocker-API  |  525       |  System   |  Bootmgr determined that the TPM is disabled.
Microsoft-Windows-BitLocker-API  |  526       |  System   |  Bootmgr determined that the TPM is not accessible.
Microsoft-Windows-BitLocker-API  |  527       |  System   |  The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.
Microsoft-Windows-BitLocker-API  |  528       |  System   |  Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.
Microsoft-Windows-BitLocker-API  |  529       |  System   |  Bootmgr determined that driver signature enforcement has been disabled.
Microsoft-Windows-BitLocker-API  |  530       |  System   |  Bootmgr determined that the device was locked out due to too many failed password attempts.
Microsoft-Windows-BitLocker-API  |  531       |  System   |  Bootmgr determined that the device was locked out due to Device Lockout state validation failure.
Microsoft-Windows-BitLocker-API  |  768       |           |  BitLocker encryption was started for volume {VolumeMountPoint} using {AlgorithmType} algorithm.
Microsoft-Windows-BitLocker-API  |  769       |           |  BitLocker encryption will occur for volume {VolumeMountPoint} when the computer is restarted using {AlgorithmType} algorithm.
Microsoft-Windows-BitLocker-API  |  770       |           |  BitLocker decryption was started for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  771       |           |  BitLocker encryption was stopped for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  772       |           |  BitLocker encryption was restarted for volume {VolumeMountPoint} using {AlgorithmType} algorithm.
Microsoft-Windows-BitLocker-API  |  773       |           |  BitLocker was suspended for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  774       |           |  BitLocker was resumed for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  775       |           |  A BitLocker key protector was created.Protector GUID: {ProtectorGUID}Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  776       |           |  A BitLocker key protector was removed.Protector GUID: {ProtectorGUID}Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  777       |           |  The PIN was updated for the operating system volume.Protector GUID: {ProtectorGUID}Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  778       |           |  The BitLocker volume {VolumeMountPoint} was reverted to an unprotected state.
Microsoft-Windows-BitLocker-API  |  779       |           |  The BitLocker volume {VolumeMountPoint} was erased.
Microsoft-Windows-BitLocker-API  |  780       |           |  The identification field was changed. Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  781       |           |  The BitLocker protected volume {VolumeMountPoint} was locked. Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  782       |           |  The BitLocker protected volume {VolumeMountPoint} was unlocked.Protector GUID: {ProtectorGUID}Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  783       |           |  BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.Protector GUID: {ProtectorGUID}Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  784       |           |  BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.Protector GUID: {ProtectorGUID}Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  785       |           |  Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.Protector GUID: {ProtectorGUID}Identification GUID: {IdentificationGUID}
Microsoft-Windows-BitLocker-API  |  786       |           |  BitLocker free space wiping was started for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  787       |           |  BitLocker free space wiping was stopped for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  788       |           |  BitLocker free space wiping was restarted for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  789       |           |
Microsoft-Windows-BitLocker-API  |  790       |           |  A PIN change attempt failed.Error message: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  791       |           |
Microsoft-Windows-BitLocker-API  |  792       |           |  BitLocker encountered a failure to commit metadata changes for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  793       |           |  BitLocker resealed boot settings to the TPM for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  794       |           |  BitLocker failed to reseal boot settings to the TPM.Error message: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  795       |           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint} due to group policy.
Microsoft-Windows-BitLocker-API  |  796       |           |  BitLocker Drive Encryption is using software-based encryption to protect volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  797       |           |  Group Policy settings prevented BitLocker Drive Encryption from reverting to BitLocker software-based encryption. Volume {VolumeMountPoint} is not protected by BitLocker.
Microsoft-Windows-BitLocker-API  |  798       |           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint}.Drive is not provisioned for use with BitLocker hardware encryption:Hardware-based encryption is not activated on this drive.
Microsoft-Windows-BitLocker-API  |  799       |           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint}.Drive is not provisioned for use with BitLocker hardware encryption:The hardware-based encryption of this drive does not allow BitLocker to cryptographically protect the drive's media encryption key.
Microsoft-Windows-BitLocker-API  |  800       |           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint}.Drive is not provisioned for use with BitLocker hardware encryption:Hardware-based encryption is either not configured or has been configured improperly on this volume.
Microsoft-Windows-BitLocker-API  |  801       |           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint}.Drive is not provisioned for use with BitLocker hardware encryption:Hardware-based encryption cannot be used with this drive because the hardware encryption method used by this drive does not comply with the Group Policy requirement for drive encryption.
Microsoft-Windows-BitLocker-API  |  802       |           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint}.Drive is not provisioned for use with BitLocker hardware encryption:The key length, {ActualKeyLength} bits, required to enable hardware-based encryption is below the minimum key length supported by the drive: {ExpectedKeyLength}.
Microsoft-Windows-BitLocker-API  |  803       |           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint}.Drive is not provisioned for use with BitLocker hardware encryption:The key length, {ActualKeyLength} bits, required to enable hardware-based encryption is above the maximum key length supported by the drive: {ExpectedKeyLength}.
Microsoft-Windows-BitLocker-API  |  804       |           |  The target drive ({VolumeMountPoint}) cannot be managed by BitLocker because the drive's hardware encryption feature is already in use.
Microsoft-Windows-BitLocker-API  |  805       |           |  The BitLocker protected volume was unlocked in the Windows Recovery Environment.Protector GUID: {ProtectorGUID}Identification GUID: {IdentificationGUID}Unlock time: {UnlockTime}
Microsoft-Windows-BitLocker-API  |  806       |           |  BitLocker resealed boot settings to the TPM in the Windows Recovery Environment.Reseal time: {ResealTime}
Microsoft-Windows-BitLocker-API  |  807       |           |  BitLocker free space wiping was canceled for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  808       |           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint}.Drive is not provisioned for use with BitLocker hardware encryption:SID authority is not disabled on this drive.
Microsoft-Windows-BitLocker-API  |  809       |           |
Microsoft-Windows-BitLocker-API  |  810       |           |
Microsoft-Windows-BitLocker-API  |  811       |           |  BitLocker cannot use Secure Boot for integrity because the required UEFI variable '{VariableName}' is not present.
Microsoft-Windows-BitLocker-API  |  812       |           |  BitLocker cannot use Secure Boot for integrity because the UEFI variable '{VariableName}' could not be read.Error Message: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  813       |           |  BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for variable '{VariableName}' is missing or invalid.
Microsoft-Windows-BitLocker-API  |  814       |           |
Microsoft-Windows-BitLocker-API  |  815       |           |
Microsoft-Windows-BitLocker-API  |  816       |           |
Microsoft-Windows-BitLocker-API  |  817       |           |  BitLocker successfully sealed a key to the TPM.PCRs measured include [{PCRBitmap}].The source for these PCRs was: {PCRBitmapSource}.
Microsoft-Windows-BitLocker-API  |  818       |           |  BitLocker encountered a failure attempting to configure network unlock for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  819       |           |  The BitLocker service could not resume protection on the OS volume {VolumeMountPoint}, due to the following error: Bootable media in the drive.
Microsoft-Windows-BitLocker-API  |  820       |           |  The BitLocker service could not resume protection on the OS volume {VolumeMountPoint}, due to the following error: TPM is locked out.
Microsoft-Windows-BitLocker-API  |  821       |           |  The BitLocker service could not resume protection on the OS volume {VolumeMountPoint}, due to the following error: Group policy conflict.
Microsoft-Windows-BitLocker-API  |  822       |           |  The BitLocker service could not resume protection on the OS volume {VolumeMountPoint}, due to the following error code: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  823       |  System   |  Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.
Microsoft-Windows-BitLocker-API  |  824       |  System   |  Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.
Microsoft-Windows-BitLocker-API  |  825       |           |  BitLocker failed to initialize hardware encryption for volume {VolumeMountPoint}.This PC's firmware is not capable of supporting hardware encryption.
Microsoft-Windows-BitLocker-API  |  826       |           |
Microsoft-Windows-BitLocker-API  |  827       |           |  A password change attempt failed.Error message: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  828       |           |  BitLocker Drive Encryption recovery information for volume {VolumeMountPoint} was backed up successfully to your Microsoft account.Protector GUID: {ProtectorGUID}
Microsoft-Windows-BitLocker-API  |  829       |           |  Failed to backup BitLocker Drive Encryption recovery information for volume {VolumeMountPoint} to your Microsoft account.Error: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  830       |           |
Microsoft-Windows-BitLocker-API  |  831       |           |  Failed to save BitLocker Drive Encryption recovery information to your Microsoft account due to an error.Error Code: {JsonErrorCode}Localized Error Message: {LocalizedJsonError}
Microsoft-Windows-BitLocker-API  |  832       |           |  TCG Log parsing failure.Error: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  833       |           |
Microsoft-Windows-BitLocker-API  |  834       |           |  BitLocker determined that the TCG log is invalid for use of Secure Boot. The filtered TCG log for PCR[7] is included in this event.
Microsoft-Windows-BitLocker-API  |  835       |           |
Microsoft-Windows-BitLocker-API  |  836       |           |
Microsoft-Windows-BitLocker-API  |  837       |           |
Microsoft-Windows-BitLocker-API  |  838       |           |
Microsoft-Windows-BitLocker-API  |  839       |           |
Microsoft-Windows-BitLocker-API  |  840       |           |  A trusted WIM file has been added for volume {VolumeMountPoint}.The SHA-256 hash of the WIM file is: {BinaryData}
Microsoft-Windows-BitLocker-API  |  841       |           |  BitLocker was unable to update a key for volume {VolumeMountPoint} due to the following error: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  842       |           |  BitLocker was unable to reseal boot settings to the TPM in the Windows Recovery Environment.Error: {ErrorCode}Protection has been temporarily suspended.
Microsoft-Windows-BitLocker-API  |  843       |           |  BitLocker was suspended from within the Windows Recovery Environment.Suspend time: {ResealTime}
Microsoft-Windows-BitLocker-API  |  844       |           |  BitLocker was unable to recover from device lock in the Windows Recovery Environment.Error: {ErrorCode}Protection has been temporarily suspended.
Microsoft-Windows-BitLocker-API  |  845       |           |  BitLocker Drive Encryption recovery information for volume {VolumeMountPoint} was backed up successfully to your Azure AD.Protector GUID: {ProtectorGUID}.TraceId: {TraceGUID}
Microsoft-Windows-BitLocker-API  |  846       |           |  Failed to backup BitLocker Drive Encryption recovery information for volume {VolumeMountPoint} to your Azure AD.TraceId: {TraceGUID}Error: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  847       |           |  Failed to save BitLocker Drive Encryption recovery information to your Azure AD due to an error. Request Id: {JsonRequestId} Response Time: {JsonTime}Error Code: {JsonErrorCode}Error Subcode: {JsonSubCode}Error message: {JsonMessage}
Microsoft-Windows-BitLocker-API  |  848       |           |  Failed to update BCD store with the Recovery URL for OS volume.Error: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  849       |           |  Failed to set the TPM dictionary attack parameters to the legacy behavior.Error: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  850       |           |  Successfully set the TPM dictionary attack parameters to the legacy behavior.
Microsoft-Windows-BitLocker-API  |  851       |           |  Failed to enable Silent Encryption. Error: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  852       |           |  Failed to enable Silent Encryption. Device is not AAD joined. Error: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  853       |           |  Failed to enable Silent Encryption. TPM is not available. Error: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  854       |           |  Failed to enable Silent Encryption. WinRe is not configured. Error: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  855       |           |
Microsoft-Windows-BitLocker-API  |  856       |           |  Failed to initiate the Recovery Password Rotation Error:{ErrorCode}.
Microsoft-Windows-BitLocker-API  |  857       |           |
Microsoft-Windows-BitLocker-API  |  858       |           |  Recovery Password Rotation failed. Error: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  859       |           |  Recovery Password Rotation failed.Volume: {VolumeName}Mount: {VolumeMountPoint}ReqID: {ProtectorGUID}Error:{ErrorCode}.
Microsoft-Windows-BitLocker-API  |  860       |           |  Failed to delete recovery password from AAD.Error:{ErrorCode}.
Microsoft-Windows-BitLocker-API  |  861       |           |  Failed to create clinet recovery password rotation request. volume: {VolumeName}Mount: {VolumeMountPoint}ReqId: {ProtectorGUID}Error: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  862       |           |  Failed to Create AAD recovery Password Delete request.Volume: {VolumeName}Mount: {VolumeMountPoint}ReqID: {ProtectorGUID}Error:{ErrorCode}.
Microsoft-Windows-BitLocker-API  |  863       |           |  Failed to initiate the Recovery Password Rotation and AAD Deletion requests processing Error:{ErrorCode}.
Microsoft-Windows-BitLocker-API  |  864       |           |
Microsoft-Windows-BitLocker-API  |  4096      |           |  Device Encryption could not be initialized.Error: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  4097      |           |
Microsoft-Windows-BitLocker-API  |  4098      |           |
Microsoft-Windows-BitLocker-API  |  4099      |           |  Device Encryption failed to process user logon event.Error: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  4100      |           |
Microsoft-Windows-BitLocker-API  |  4101      |           |
Microsoft-Windows-BitLocker-API  |  4102      |           |  BitLocker failed to recover after Device Lock.Error message: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  4103      |           |  Failed to automatically enable Device Encryption.Error Message: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  4104      |           |
Microsoft-Windows-BitLocker-API  |  4105      |           |
Microsoft-Windows-BitLocker-API  |  4106      |           |  Failed to automatically back up recovery password to your Microsoft account.Error Message: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  4107      |           |
Microsoft-Windows-BitLocker-API  |  4108      |           |
Microsoft-Windows-BitLocker-API  |  4109      |           |
Microsoft-Windows-BitLocker-API  |  4110      |           |
Microsoft-Windows-BitLocker-API  |  4111      |           |  Device Lock recovery event initiated for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  4112      |           |  MaxPasswordRetry policy enforced with TPM-based hardening for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  4113      |           |  MaxPasswordRetry policy enforced without hardware based hardening for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  4114      |           |  Device Lock recovery event initiated due to protected state mismatch for volume {VolumeMountPoint}.
Microsoft-Windows-BitLocker-API  |  4116      |           |  Device Encryption initialization for volume {VolumeMountPoint} start.
Microsoft-Windows-BitLocker-API  |  4117      |           |  Device Encryption initialization for volume {VolumeMountPoint} stop.
Microsoft-Windows-BitLocker-API  |  4118      |           |  Volume {VolumeMountPoint} could not be initialized for Device Encryption.Error: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  4119      |           |
Microsoft-Windows-BitLocker-API  |  4120      |           |
Microsoft-Windows-BitLocker-API  |  4121      |           |
Microsoft-Windows-BitLocker-API  |  4122      |           |  The following DMA (Direct Memory Access) capable devices are not declared as protected from external access, which can block security features such as BitLocker automatic device encryption:{LocalizedText}
Microsoft-Windows-BitLocker-API  |  4123      |           |  BitLocker Drive Encryption recovery information for volume {VolumeMountPoint} was deleted successfully from your Azure AD.Protector GUID: {ProtectorGUIDs}.TraceId: {TraceGUID}
Microsoft-Windows-BitLocker-API  |  4124      |           |
Microsoft-Windows-BitLocker-API  |  4125      |           |  Failed to query HSTI data size. Error: {Data}
Microsoft-Windows-BitLocker-API  |  4126      |           |  Actual HSTI data size: {Data1}.Expected HSTI data size to be at least: {Data2}
Microsoft-Windows-BitLocker-API  |  4127      |           |  HSTI provider count: {Data}
Microsoft-Windows-BitLocker-API  |  4128      |           |  HSTI data version: {Data1}.Expected HSTI data version: {Data2}
Microsoft-Windows-BitLocker-API  |  4129      |           |  HSTI security features size mismatch for HSTI provider {HSTIImplID}: expected {Data1}, actual {Data2}
Microsoft-Windows-BitLocker-API  |  4130      |           |  HSTI provider {HSTIImplID} found with unknown version {Data}. This provider will not be processed
Microsoft-Windows-BitLocker-API  |  4131      |           |  HSTI provider {HSTIImplID} found. Has PLATFORM_SECURITY_ROLE_PLATFORM_REFERENCE: {BoolData}.(Note: there should only be one provider with this role.)
Microsoft-Windows-BitLocker-API  |  4132      |           |  HSTI provider {HSTIImplID} found. Has PLATFORM_SECURITY_ROLE_PLATFORM_REFERENCE: {BoolData}.Since the platform was reported to have at least one other provider with PLATFORM_SECURITY_ROLE_PLATFORM_REFERENCE, HSTI is deemed unsafe
Microsoft-Windows-BitLocker-API  |  4133      |           |
Microsoft-Windows-BitLocker-API  |  4134      |           |  HSTI provider {HSTIImplID} (which is not PLATFORM_SECURITY_ROLE_PLATFORM_REFERENCE) set SecurityFeaturesRequired
Microsoft-Windows-BitLocker-API  |  4135      |           |  HSTI combined results report secure Intel Thunderbolt configuration bit: {BoolData}
Microsoft-Windows-BitLocker-API  |  4136      |           |  Required HSTI features were not verified by any provider. For byte {SecFeatureIndex}, the mask of missing features is: {Data}
Microsoft-Windows-BitLocker-API  |  4137      |           |  HSTI tests failed. Error messages from HSTI Provider {HSTIImplID}: {ProviderErrorMsg}
Microsoft-Windows-BitLocker-API  |  4138      |           |  Successfully setup TPM API callback.
Microsoft-Windows-BitLocker-API  |  4139      |           |  Failed to setup TPM API callback. Error Code: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  4140      |           |  Successfully added predicted TPM protector.
Microsoft-Windows-BitLocker-API  |  4141      |           |  Failed to add predicted TPM protector. Error Code: {ErrorCode}.
Microsoft-Windows-BitLocker-API  |  4142      |           |  Predicted PCR4 value for TPM info based protector. Predicted Value: {BinaryData}.
Microsoft-Windows-BitLocker-API  |  4143      |           |  Failed to evaluate PCR4 predicted value from TPM info. Error Code: {ErrorCode}
Microsoft-Windows-BitLocker-API  |  4144      |           |  Predicted PCR7 value for TPM info based protector. Predicted Value: {BinaryData}.
Microsoft-Windows-BitLocker-API  |  4145      |           |  Failed to evaluate PCR7 predicted value from TPM info. Error Code: {ErrorCode}