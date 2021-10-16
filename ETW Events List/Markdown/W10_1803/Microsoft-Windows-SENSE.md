Provider                 |  Event ID  |  Channel                              |  Message
-------------------------|------------|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-SENSE  |  1         |  Microsoft-Windows-SENSE/Operational  |  Service is starting (Version {parameter}).
Microsoft-Windows-SENSE  |  2         |  Microsoft-Windows-SENSE/Operational  |  Service is shutting down.
Microsoft-Windows-SENSE  |  3         |  Microsoft-Windows-SENSE/Operational  |  Windows Defender Advanced Threat Protection service failed to start. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  4         |  Microsoft-Windows-SENSE/Operational  |  Contacted server {UInt1} times, all succeeded, URI: {Message1}.
Microsoft-Windows-SENSE  |  5         |  Microsoft-Windows-SENSE/Operational  |  Contacted server {UInt1} times, all failed, URI: {Message1}. Last HTTP error code: {Int1}
Microsoft-Windows-SENSE  |  6         |  Microsoft-Windows-SENSE/Operational  |  Windows Defender Advanced Threat Protection service is not onboarded and no onboarding parameters were found.
Microsoft-Windows-SENSE  |  7         |  Microsoft-Windows-SENSE/Operational  |  Windows Defender Advanced Threat Protection service failed to read the onboarding parameters. Failure: {parameter}
Microsoft-Windows-SENSE  |  8         |  Microsoft-Windows-SENSE/Operational  |  Service failed to clean configuration settings.
Microsoft-Windows-SENSE  |  9         |  Microsoft-Windows-SENSE/Operational  |  Windows Defender Advanced Threat Protection service failed to change its start type. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  10        |  Microsoft-Windows-SENSE/Operational  |  Windows Defender Advanced Threat Protection service failed to persist the onboarding information. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  11        |  Microsoft-Windows-SENSE/Operational  |  Onboarding or re-onboarding of Windows Defender Advanced Threat Protection service completed.
Microsoft-Windows-SENSE  |  12        |  Microsoft-Windows-SENSE/Operational  |  New cloud configuration failed to apply, version: {parameter1}. Also failed to apply last known good configuration, version {parameter2}. Also failed to apply the default configuration.
Microsoft-Windows-SENSE  |  13        |  Microsoft-Windows-SENSE/Operational  |  Windows Defender Advanced Threat Protection machine ID calculated: {parameter}
Microsoft-Windows-SENSE  |  14        |  Microsoft-Windows-SENSE/Operational  |  Windows Defender Advanced Threat Protection cannot calculate machine ID. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  15        |  Microsoft-Windows-SENSE/Operational  |  Windows Defender Advanced Threat Protection cannot start command channel with URL: {parameter}
Microsoft-Windows-SENSE  |  17        |  Microsoft-Windows-SENSE/Operational  |  Windows Defender Advanced Threat Protection service failed to change the Connected User Experiences and Telemetry service location. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  18        |  Microsoft-Windows-SENSE/Operational  |  OOBE (Windows Welcome) is completed.
Microsoft-Windows-SENSE  |  19        |  Microsoft-Windows-SENSE/Operational  |  OOBE (Windows Welcome) has not yet completed.
Microsoft-Windows-SENSE  |  20        |  Microsoft-Windows-SENSE/Operational  |  Cannot wait for OOBE (Windows Welcome) to complete. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  25        |  Microsoft-Windows-SENSE/Operational  |  Service failed to reset health status in the registry. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  26        |  Microsoft-Windows-SENSE/Operational  |  Windows Defender Advanced Threat Protection service failed to set the onboarding status in the registry. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  27        |  Microsoft-Windows-SENSE/Operational  |  Failed to enable Windows Defender Advanced Threat Protection mode in Windows Defender. Onboarding process failed. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  28        |  Microsoft-Windows-SENSE/Operational  |  Connected User Experiences and Telemetry service registration failed with failure code: {HRESULT}. Requested disk quota in MB: {diskSizeQuotaValue}, Requested daily upload quota in MB: {dailyUploadQuotaValue}
Microsoft-Windows-SENSE  |  29        |  Microsoft-Windows-SENSE/Operational  |  Failed to read the offboarding parameters. Error type: {errorType}, Error code: {HRESULT}, Description: {description}
Microsoft-Windows-SENSE  |  30        |  Microsoft-Windows-SENSE/Operational  |  Failed to disable Windows Defender Advanced Threat Protection mode in Windows Defender. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  31        |  Microsoft-Windows-SENSE/Operational  |  Windows Defender Advanced Threat Protection Connected User Experiences and Telemetry service unregistration failed. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  32        |  Microsoft-Windows-SENSE/Operational  |  Windows Defender Advanced Threat Protection service failed to request to stop itself after offboarding process. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  33        |  Microsoft-Windows-SENSE/Operational  |  Windows Defender Advanced Threat Protection service failed to persist SENSE GUID. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  36        |  Microsoft-Windows-SENSE/Operational  |  Connected User Experiences and Telemetry service registration succeeded with completion code: {HRESULT}. Requested disk quota in MB: {diskSizeQuotaValue}, requested daily upload quota in MB: {dailyUploadQuotaValue}
Microsoft-Windows-SENSE  |  37        |  Microsoft-Windows-SENSE/Operational  |  Module: {module}, Quota: {{quotaValue}} {{quotaValueUnit}}, Percentage of quota utilization: {percentageValue}.
Microsoft-Windows-SENSE  |  38        |  Microsoft-Windows-SENSE/Operational  |  Network connection is identified as low. Windows Defender Advanced Threat Protection will contact the server every {pollingInterval} seconds. Metered connection: {meteredConnectionState}, internet available: {internetAvailabilityState}, free network available: {freeNetworkAvailabilityState}, proxy is defined by GP: {proxyDefined}.
Microsoft-Windows-SENSE  |  39        |  Microsoft-Windows-SENSE/Operational  |  Network connection is identified as normal. Windows Defender Advanced Threat Protection will contact the server every {pollingInterval} seconds. Metered connection: {meteredConnectionState}, internet available: {internetAvailabilityState}, free network available: {freeNetworkAvailabilityState}, proxy is defined by GP: {proxyDefined}.
Microsoft-Windows-SENSE  |  40        |  Microsoft-Windows-SENSE/Operational  |  Battery state is identified as low. Windows Defender Advanced Threat Protection will contact the server every {pollingInterval} seconds. AC state: {acPowerState}, battery saver mode : {batterySavingState}, battery low state: {batteryLowState}, battery critical state: {batteryCriticalState}
Microsoft-Windows-SENSE  |  41        |  Microsoft-Windows-SENSE/Operational  |  Battery state is identified as normal. Windows Defender Advanced Threat Protection will contact the server every {pollingInterval} seconds. AC state: {acPowerState}, battery saver mode : {batterySavingState}, battery low state: {batteryLowState}, battery critical state: {batteryCriticalState}
Microsoft-Windows-SENSE  |  42        |  Microsoft-Windows-SENSE/Operational  |  Component failed to perform action. Component: {Component}, Action: {Operation}, Exception Type: {ExceptionType}, Exception message: {ExceptionMessage}
Microsoft-Windows-SENSE  |  43        |  Microsoft-Windows-SENSE/Operational  |  Component failed to perform action. Component: {Component}, Action: {Operation}, Exception Type: {ExceptionType}, Exception Error: {ExceptionErrorCode}, Exception message: {ExceptionMessage}
Microsoft-Windows-SENSE  |  44        |  Microsoft-Windows-SENSE/Operational  |  Offboarding of Windows Defender Advanced Threat Protection service completed.
Microsoft-Windows-SENSE  |  45        |  Microsoft-Windows-SENSE/Operational  |  Failed to register and to start the event trace session [{TraceSessionName}]. Error code: {HRESULT}
Microsoft-Windows-SENSE  |  46        |  Microsoft-Windows-SENSE/Operational  |  Failed to register and start the event trace session [{TraceSessionName}] due to lack of resources. Error code: {HRESULT}. This is most likely because there are too many active event trace sessions. The service will retry in 1 minute.
Microsoft-Windows-SENSE  |  47        |  Microsoft-Windows-SENSE/Operational  |  Successfully registered and started the event trace session - recovered after previous failed attempts.
Microsoft-Windows-SENSE  |  48        |  Microsoft-Windows-SENSE/Operational  |  Failed to add a provider [{ProviderId}] to event trace session [{TraceSessionName}]. Error code: {ErrorCode}. This means that events from this provider will not be reported.
Microsoft-Windows-SENSE  |  49        |  Microsoft-Windows-SENSE/Operational  |  Invalid cloud configuration command received and ignored. Version: {Version}, status: {Status}, error code: {HRESULT}, message: {ErrorMessage}
Microsoft-Windows-SENSE  |  50        |  Microsoft-Windows-SENSE/Operational  |  New cloud configuration applied successfully. Version: {parameter}.
Microsoft-Windows-SENSE  |  51        |  Microsoft-Windows-SENSE/Operational  |  New cloud configuration failed to apply, version: {parameter1}. Successfully applied the last known good configuration, version {parameter2}.
Microsoft-Windows-SENSE  |  52        |  Microsoft-Windows-SENSE/Operational  |  New cloud configuration failed to apply, version: {parameter1}. Also failed to apply last known good configuration, version {parameter2}. Successfully applied the default configuration.
Microsoft-Windows-SENSE  |  53        |  Microsoft-Windows-SENSE/Operational  |  Cloud configuration loaded from persistent storage, version: {parameter}.
Microsoft-Windows-SENSE  |  54        |  Microsoft-Windows-SENSE/Operational  |  Global (per-pattern) state changed. State: {Value1}, pattern: {Value2}
Microsoft-Windows-SENSE  |  55        |  Microsoft-Windows-SENSE/Operational  |  Failed to create the Secure ETW autologger. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  56        |  Microsoft-Windows-SENSE/Operational  |  Failed to remove the Secure ETW autologger. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  57        |  Microsoft-Windows-SENSE/Operational  |  Capturing a snapshot of the machine for troubleshooting purposes.
Microsoft-Windows-SENSE  |  59        |  Microsoft-Windows-SENSE/Operational  |  Starting command: {parameter}
Microsoft-Windows-SENSE  |  60        |  Microsoft-Windows-SENSE/Operational  |  Failed to run command {CommandName}, error: {HRESULT}.
Microsoft-Windows-SENSE  |  61        |  Microsoft-Windows-SENSE/Operational  |  Data collection command parameters are invalid: SasUri: {SasUri}, compressionLevel: {CompressionLevel}.
Microsoft-Windows-SENSE  |  62        |  Microsoft-Windows-SENSE/Operational  |  Failed to start Connected User Experiences and Telemetry service. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  63        |  Microsoft-Windows-SENSE/Operational  |  Updating the start type of external service. Name: {ServiceName}, actual start type: {ActualStartType}, expected start type: {ExpectedStartType}, exit code: {ErrorCode}
Microsoft-Windows-SENSE  |  64        |  Microsoft-Windows-SENSE/Operational  |  Starting stopped external service. Name: {ServiceName}, exit code: {ErrorCode}
Microsoft-Windows-SENSE  |  65        |  Microsoft-Windows-SENSE/Operational  |  Failed to load Microsoft Security Events Component Minifilter driver. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  66        |  Microsoft-Windows-SENSE/Operational  |  Policy update: Latency mode - {parameter}
Microsoft-Windows-SENSE  |  67        |  Microsoft-Windows-SENSE/Operational  |  Contacted server {UInt1} times, failed {UInt2} times and succeeded {UInt3} times. URI: {Message1}. Last HTTP error code: {Int1}
Microsoft-Windows-SENSE  |  68        |  Microsoft-Windows-SENSE/Operational  |  The start type of the service is unexpected. Service name: {ServiceName}, actual start type: {ActualStartType}, expected start type: {ExpectedStartType}
Microsoft-Windows-SENSE  |  69        |  Microsoft-Windows-SENSE/Operational  |  The service is stopped. Service name: {parameter}
Microsoft-Windows-SENSE  |  70        |  Microsoft-Windows-SENSE/Operational  |  Policy update: Allow sample collection - {UInt1}
Microsoft-Windows-SENSE  |  71        |  Microsoft-Windows-SENSE/Operational  |  Succeeded to run command: {parameter}
Microsoft-Windows-SENSE  |  72        |  Microsoft-Windows-SENSE/Operational  |  Tried to send first full machine profile report. Result code: {HRESULT}
Microsoft-Windows-SENSE  |  73        |  Microsoft-Windows-SENSE/Operational  |  Sense starting for platform: {platformBitMask}
Microsoft-Windows-SENSE  |  74        |                                       |  Device tag in registry exceeds length limit. Tag name: {Message1}. Length limit: {UInt1}.
Microsoft-Windows-SENSE  |  75        |  Microsoft-Windows-SENSE/Operational  |  Device tag name in registry exceeds length limit. Tag name: {Message1}. Length limit: {UInt1}.
Microsoft-Windows-SENSE  |  76        |  Microsoft-Windows-SENSE/Operational  |  Number of customer tags in registry exceeds limit. Limit: {UInt1} tags.
Microsoft-Windows-SENSE  |  77        |  Microsoft-Windows-SENSE/Operational  |  Successfully applied protection on Connected User Experiences and Telemetry service
Microsoft-Windows-SENSE  |  78        |  Microsoft-Windows-SENSE/Operational  |  Successfully removed protection from Connected User Experiences and Telemetry service
Microsoft-Windows-SENSE  |  79        |  Microsoft-Windows-SENSE/Operational  |  Failed to apply protection on Connected User Experiences and Telemetry service. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  80        |  Microsoft-Windows-SENSE/Operational  |  Failed to remove protection from Connected User Experiences and Telemetry service. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  81        |  Microsoft-Windows-SENSE/Operational  |  Failed to create Windows Defender Advanced Threat Protection ETW autologger. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  82        |  Microsoft-Windows-SENSE/Operational  |  Failed to remove Windows Defender Advanced Threat Protection ETW autologger. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  83        |  Microsoft-Windows-SENSE/Operational  |  Cyber event may be dropped because its size [{RealValue} bytes] exceeded max size [{quotaValue} bytes] or close to it.
Microsoft-Windows-SENSE  |  84        |  Microsoft-Windows-SENSE/Operational  |  Set Windows Defender Antivirus running mode. Force passive mode: {forcePassiveMode}, result code: {HRESULT}.
Microsoft-Windows-SENSE  |  85        |  Microsoft-Windows-SENSE/Operational  |  Failed to trigger Windows Defender Advanced Threat Protection Incident Response executable. Failure code: {HRESULT}
Microsoft-Windows-SENSE  |  1800      |  Microsoft-Windows-SENSE/Operational  |  CSP: Get Node's Value. NodeId: ({UInt1}), TokenName: ({Message1}).
Microsoft-Windows-SENSE  |  1801      |  Microsoft-Windows-SENSE/Operational  |  CSP: Failed to Get Node's Value. NodeId: ({UInt1}), TokenName: ({Message1}), Result: ({HRESULT}).
Microsoft-Windows-SENSE  |  1802      |  Microsoft-Windows-SENSE/Operational  |  CSP: Get Node's Value complete. NodeId: ({UInt1}), TokenName: ({Message1}), Result: ({HRESULT}).
Microsoft-Windows-SENSE  |  1803      |  Microsoft-Windows-SENSE/Operational  |  CSP: Get Last Connected value complete. Result ({Message1}), IsDefault: ({Boolean1}).
Microsoft-Windows-SENSE  |  1804      |  Microsoft-Windows-SENSE/Operational  |  CSP: Get Org ID value complete. Result: ({Message1}), IsDefault: ({Boolean1}).
Microsoft-Windows-SENSE  |  1805      |  Microsoft-Windows-SENSE/Operational  |  CSP: Get Sense Is Running value complete. Result: ({UInt1}).
Microsoft-Windows-SENSE  |  1806      |  Microsoft-Windows-SENSE/Operational  |  CSP: Get Onboarding State value complete. Result: ({UInt1}), IsDefault: ({Boolean1}).
Microsoft-Windows-SENSE  |  1807      |  Microsoft-Windows-SENSE/Operational  |  CSP: Get Onboarding value complete. Onboarding Blob Hash: ({onboardingBlobHash}), IsDefault: ({isDefaultOnboardingBlob}), Onboarding State: ({onboardingState}), Onboarding State IsDefault: ({isDefaultOnboardingState})
Microsoft-Windows-SENSE  |  1808      |  Microsoft-Windows-SENSE/Operational  |  CSP: Get Offboarding value complete. Offboarding Blob Hash: ({offboardingBlobHash}), IsDefault: ({isDefaultOffboardingBlob}).
Microsoft-Windows-SENSE  |  1809      |  Microsoft-Windows-SENSE/Operational  |  CSP: Get Sample Sharing value complete. Result: ({UInt1}), IsDefault: ({Boolean1}).
Microsoft-Windows-SENSE  |  1810      |  Microsoft-Windows-SENSE/Operational  |  CSP: Onboarding process. Started.
Microsoft-Windows-SENSE  |  1811      |  Microsoft-Windows-SENSE/Operational  |  CSP: Onboarding process. Delete Offboarding blob complete. Result: ({HRESULT}).
Microsoft-Windows-SENSE  |  1812      |  Microsoft-Windows-SENSE/Operational  |  CSP: Onboarding process. Write Onboarding blob complete. Result: ({HRESULT})
Microsoft-Windows-SENSE  |  1813      |  Microsoft-Windows-SENSE/Operational  |  CSP: Onboarding process. The service started successfully.
Microsoft-Windows-SENSE  |  1814      |  Microsoft-Windows-SENSE/Operational  |  CSP: Onboarding process. Pending service running state complete. Result: ({HRESULT}).
Microsoft-Windows-SENSE  |  1815      |  Microsoft-Windows-SENSE/Operational  |  CSP: Set Sample Sharing value complete. Previous Value: ({previousSampleCollectionValue}), IsDefault: ({IsDefault}), New Value: ({newSampleSharing}), Result: ({HRESULT}).
Microsoft-Windows-SENSE  |  1816      |  Microsoft-Windows-SENSE/Operational  |  CSP: Offboarding process. Delete Onboarding blob complete. Result ({HRESULT}).
Microsoft-Windows-SENSE  |  1817      |  Microsoft-Windows-SENSE/Operational  |  CSP: Offboarding process. Write Offboarding blob complete. Result ({HRESULT}).
Microsoft-Windows-SENSE  |  1818      |  Microsoft-Windows-SENSE/Operational  |  CSP: Set Node's Value started. NodeId: ({UInt1}), TokenName: ({Message1}).
Microsoft-Windows-SENSE  |  1819      |  Microsoft-Windows-SENSE/Operational  |  CSP: Failed to Set Node's Value. NodeId: ({UInt1}), TokenName: ({Message1}), Result: ({HRESULT}).
Microsoft-Windows-SENSE  |  1820      |  Microsoft-Windows-SENSE/Operational  |  CSP: Set Node's Value complete. NodeId: ({UInt1}), TokenName: ({Message1}), Result: ({HRESULT}).
Microsoft-Windows-SENSE  |  1821      |  Microsoft-Windows-SENSE/Operational  |  CSP: Set Telemetry Reporting Frequency started. New value: ({UInt1}).
Microsoft-Windows-SENSE  |  1822      |  Microsoft-Windows-SENSE/Operational  |  CSP: Set Telemetry Reporting Frequency complete. Previous value: ({previousLatencyMode}), IsDefault: ({IsDefault}), New value: ({newLatencyMode}), Result: ({HRESULT}).
Microsoft-Windows-SENSE  |  1823      |  Microsoft-Windows-SENSE/Operational  |  CSP: Get Telemetry Reporting Frequency complete. Value: ({UInt1}), Registry Value: ({Message1}), IsDefault: ({Boolean1}).
Microsoft-Windows-SENSE  |  1824      |  Microsoft-Windows-SENSE/Operational  |  CSP: Get Group Ids complete. Value: ({Message1}), IsDefault: ({Boolean1}).
Microsoft-Windows-SENSE  |  1825      |  Microsoft-Windows-SENSE/Operational  |  CSP: Set Group Ids exceeded allowed limit. Allowed: ({UInt1}), Actual: ({UInt2}).
Microsoft-Windows-SENSE  |  1826      |  Microsoft-Windows-SENSE/Operational  |  CSP: Set Group Ids complete. Value: ({Message1}), Result: ({HRESULT}).
Microsoft-Windows-SENSE  |  1827      |  Microsoft-Windows-SENSE/Operational  |  CSP: Onboarding process. Service is running: ({isServiceRunningAlready}), Previous Onboarding Blob Hash: ({previousOnboardingBlobHash}), IsDefault: ({isDefaultOnboardingBlob}), Onboarding State: ({onboardingState}), Onboarding State IsDefault: ({isDefaultOnboardingState}), New Onboarding Blob Hash: ({newOnboardingBlobHash})
Microsoft-Windows-SENSE  |  1828      |  Microsoft-Windows-SENSE/Operational  |  CSP: Onboarding process. Service is running: ({isServiceRunning}), Previous Offboarding Blob Hash: ({previousOffboardingBlobHash}), IsDefault: ({isDefaultOffboardingBlob}), Onboarding State: ({onboardingState}), Onboarding State IsDefault: ({isDefaultOnboardingState}), New Offboarding Blob Hash: ({newOffboardingBlobHash})
Microsoft-Windows-SENSE  |  1829      |  Microsoft-Windows-SENSE/Operational  |  CSP: Failed to Set Sample Sharing Value. Requested Value: ({requestedValue}), Allowed Values between ({minimumAllowedValue}) and ({maximumAllowedValue}).
Microsoft-Windows-SENSE  |  1830      |  Microsoft-Windows-SENSE/Operational  |  CSP: Failed to Set Telemetry Reporting Frequency Value. Requested Value: ({UInt1})
Microsoft-Windows-SENSE  |  1831      |  Microsoft-Windows-SENSE/Operational  |  CSP: Get Sense is running. Service is configured as delay-start, and hasn't started yet.
Microsoft-Windows-SENSE  |  1832      |  Microsoft-Windows-SENSE/Operational  |  CSP: Get Device Tagging Group complete. Value: ({Message1}), IsDefault: ({Boolean1}).
Microsoft-Windows-SENSE  |  1833      |  Microsoft-Windows-SENSE/Operational  |  CSP: Get Device Tagging Criticality value complete. In Registry: ({registryValue}), IsDefault: ({IsDefault}), Conversion Succeeded: ({conversionSucceeded}), Result: ({Result}).
Microsoft-Windows-SENSE  |  1834      |  Microsoft-Windows-SENSE/Operational  |  CSP: Get Device Tagging Identification Method value complete. In Registry: ({registryValue}), IsDefault: ({IsDefault}), Conversion Succeeded: ({conversionSucceeded}), Result: ({Result}).
Microsoft-Windows-SENSE  |  1835      |  Microsoft-Windows-SENSE/Operational  |  CSP: Set Device Tagging Group complete. Value: ({Message1}), Result: ({HRESULT}).
Microsoft-Windows-SENSE  |  1836      |  Microsoft-Windows-SENSE/Operational  |  CSP: Set Device Tagging Group exceeded allowed limit. Allowed: ({UInt1}), Actual: ({UInt2}).
Microsoft-Windows-SENSE  |  1837      |  Microsoft-Windows-SENSE/Operational  |  CSP: Set Device Tagging Criticality value complete. Previous Value: ({previousCriticalityValue}), IsDefault: ({IsDefault}), New Value: ({newCriticalityValue}), Result: ({HRESULT}).
Microsoft-Windows-SENSE  |  1838      |  Microsoft-Windows-SENSE/Operational  |  CSP: Failed to Set Device Tagging Criticality Value. Requested Value: ({requestedValue}), Allowed Values between ({minimumAllowedValue}) and ({maximumAllowedValue}).
Microsoft-Windows-SENSE  |  1839      |  Microsoft-Windows-SENSE/Operational  |  CSP: Set Device Tagging Identification Method value complete. Previous Value: ({previousIdMethodValue}), IsDefault: ({IsDefault}), New Value: ({newIdMethodValue}), Result: ({HRESULT}).
Microsoft-Windows-SENSE  |  1840      |  Microsoft-Windows-SENSE/Operational  |  CSP: Failed to Set Device Tagging Identification Method Value. Requested Value: ({requestedValue}), Allowed Values between ({minimumAllowedValue}) and ({maximumAllowedValue}).