Provider                        |  Event ID  |  Channel                                      |  Message
--------------------------------|------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-Crypto-DPAPI  |  1         |  Microsoft-Windows-Crypto-DPAPI/Operational   |  DPAPI created Master key. 	GUID:	{MasterKeyGUID} 	User Storage Area:	{UserStorage}
Microsoft-Windows-Crypto-DPAPI  |  2         |  Microsoft-Windows-Crypto-DPAPI/Operational   |  DPAPI deleted Master key. 	GUID:	{MasterKeyGUID} 	User Storage Area:	{UserStorage}
Microsoft-Windows-Crypto-DPAPI  |  3         |  Microsoft-Windows-Crypto-DPAPI/Operational   |  Master key access failed. 	GUID:			{MasterKeyGUID} 	Success:			{Success} 	Last error:		{LastError} 	Master key disposition:	{LastError}
Microsoft-Windows-Crypto-DPAPI  |  4         |  Microsoft-Windows-Crypto-DPAPI/Operational   |  Password Change triggered. 	Status:	{Status}
Microsoft-Windows-Crypto-DPAPI  |  5         |  Microsoft-Windows-Crypto-DPAPI/Operational   |
Microsoft-Windows-Crypto-DPAPI  |  4097      |  Microsoft-Windows-Crypto-DPAPI/BackUpKeySvc  |
Microsoft-Windows-Crypto-DPAPI  |  4098      |  Microsoft-Windows-Crypto-DPAPI/BackUpKeySvc  |
Microsoft-Windows-Crypto-DPAPI  |  4099      |  Microsoft-Windows-Crypto-DPAPI/BackUpKeySvc  |  DPAPI BackUp service setup of preferred backup keys failed. 	{FailureReason} 	Error code: {Status}
Microsoft-Windows-Crypto-DPAPI  |  8193      |  Microsoft-Windows-Crypto-DPAPI/Debug         |  System credentials creation in LSASS failed.  	Status:	{Status}
Microsoft-Windows-Crypto-DPAPI  |  8194      |  Microsoft-Windows-Crypto-DPAPI/Debug         |  DPAPI Master key file open failed. 	FileName:	{FileName} 	Access:	{Access}
Microsoft-Windows-Crypto-DPAPI  |  8195      |  Microsoft-Windows-Crypto-DPAPI/Debug         |
Microsoft-Windows-Crypto-DPAPI  |  8196      |  Microsoft-Windows-Crypto-DPAPI/Operational   |
Microsoft-Windows-Crypto-DPAPI  |  8197      |  Microsoft-Windows-Crypto-DPAPI/Debug         |  DPAPI Protect failed . 	Status:	{Status} 	ReasonForFailure:	{ReasonForFailure}
Microsoft-Windows-Crypto-DPAPI  |  8198      |  Microsoft-Windows-Crypto-DPAPI/Operational   |  DPAPI Unprotect failed . 	Status:	{Status} 	ReasonForFailure:	{ReasonForFailure}
Microsoft-Windows-Crypto-DPAPI  |  8199      |  Microsoft-Windows-Crypto-DPAPI/Operational   |  Synchronization of Master keys failed.  	Credential Key Identifier:	{CredKeyIdentifier} 	User Name:	{UserName} 	User Sid:	{UserSid}
Microsoft-Windows-Crypto-DPAPI  |  8200      |  Microsoft-Windows-Crypto-DPAPI/Operational   |  Master key's record successfully logged to Diagnostic file. 	GUID:	{MasterKeyGUID} 	EncryptCredID:	{EncryptCredID} 	EncryptCredKey:	{EncryptCredKey}
Microsoft-Windows-Crypto-DPAPI  |  8201      |  Microsoft-Windows-Crypto-DPAPI/Operational   |  Master key's record failed to log to Diagnostic file. 	GUID:	{MasterKeyGUID}
Microsoft-Windows-Crypto-DPAPI  |  8202      |  Microsoft-Windows-Crypto-DPAPI/Operational   |  Master Key decryption failed but a record of this key can be found in the Diagnostic file. 	GUID:	{MasterKeyGUID}
Microsoft-Windows-Crypto-DPAPI  |  8203      |  Microsoft-Windows-Crypto-DPAPI/Operational   |  Master Key decryption failed because no record of this key can be found in the Diagnostic file. 	GUID:	{MasterKeyGUID}
Microsoft-Windows-Crypto-DPAPI  |  8204      |  Microsoft-Windows-Crypto-DPAPI/Operational   |  Master Key decryption failed because the encryption cred mismatches the decryption cred. 	GUID:	{MasterKeyGUID} 	EncryptCredID:	{EncryptCredID} 	EncryptCredKey:	{EncryptCredKey} 	DecryptCredID:	{DecryptCredID} 	DecryptCredKey:	{DecryptCredKey}
Microsoft-Windows-Crypto-DPAPI  |  8205      |  Microsoft-Windows-Crypto-DPAPI/Operational   |  Master Key decryption failed but the encryption cred matches the decryption cred. 	GUID:	{MasterKeyGUID} 	EncryptCredID:	{EncryptCredID} 	EncryptCredKey:	{EncryptCredKey} 	DecryptCredID:	{DecryptCredID} 	DecryptCredKey:	{DecryptCredKey}
Microsoft-Windows-Crypto-DPAPI  |  8206      |  Microsoft-Windows-Crypto-DPAPI/Operational   |
Microsoft-Windows-Crypto-DPAPI  |  8207      |  Microsoft-Windows-Crypto-DPAPI/Operational   |
Microsoft-Windows-Crypto-DPAPI  |  12289     |  Microsoft-Windows-Crypto-DPAPI/Operational   |  DPAPI found credential key. 	Credential Key Identifier:	{CredKeyIdentifier} 	User Name:	{UserName} 	User Sid:	{UserSid}
Microsoft-Windows-Crypto-DPAPI  |  12290     |  Microsoft-Windows-Crypto-DPAPI/Operational   |