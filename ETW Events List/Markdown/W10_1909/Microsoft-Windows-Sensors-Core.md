Provider                        |  Event ID  |  Channel  |  Message
--------------------------------|------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-Sensors-Core  |  1001      |           |  [SensorsCx] Sensor Class extension failed to initalize file context policy for DeviceInit ({WdfDeviceInit}). 'UmdfFsContextUsePolicy' is not set to 'CannotUseFsContexts'
Microsoft-Windows-Sensors-Core  |  1002      |           |  [SensorsCx] Device ({WdfDevice}) does not implement all required sensor DDI callbacks
Microsoft-Windows-Sensors-Core  |  1003      |           |  [SensorsCx] Device ({WdfDevice}) Supports state change notification=({IsStateChangeSupported})
Microsoft-Windows-Sensors-Core  |  1004      |           |  [SensorsCx] Device ({WdfDevice}) is power policy owner=({IsDriverPowerPolicyOwner})
Microsoft-Windows-Sensors-Core  |  1005      |           |  [SensorsCx] Sensor ({SENSOROBJECT}) exposed by Device ({WdfDevice}) supports SensorType=({SensorType}) with PersistentUniqueID=({PersistentUniqueID})
Microsoft-Windows-Sensors-Core  |  1006      |           |  [SensorsCx] Custom Sensor ({SENSOROBJECT}) exposed by Device ({WdfDevice}) with SubType=({SENSOROBJECT}) and PersistentUniqueID=({VendorDefinedSubType})
Microsoft-Windows-Sensors-Core  |  1007      |           |  [SensorsCx] Sensor ({SENSOROBJECT}) with PersistentUniqueID=({PersistentUniqueID}) exposed by Device=({WdfDevice}) missing vendor defined sub type
Microsoft-Windows-Sensors-Core  |  1008      |           |  [SensorsCx] Published device interface of Class=({SensorType}) with ReferenceString=({PersistentUniqueID}) for Sensor ({SENSOROBJECT}) exposed by Device ({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1009      |           |  [SensorsCx] Sensor Category missing in Sensor ({SENSOROBJECT})
Microsoft-Windows-Sensors-Core  |  1010      |           |  [SensorsCx] Found Enumeration Property({{FmtId}}-{Pid}) in Sensor ({SENSOROBJECT}) exposed by Device ({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1011      |           |  [SensorsCx] Default Report Interval ({IntervalMs}) in Sensor ({SENSOROBJECT}) exposed by Device ({WdfDevice}) is <= 1ms
Microsoft-Windows-Sensors-Core  |  1012      |           |  [SensorsCx] Minimum Report Interval ({IntervalMs}) in Sensor ({SENSOROBJECT}) exposed by Device ({WdfDevice}) is 0
Microsoft-Windows-Sensors-Core  |  1013      |           |  [SensorsCx] MaxDataSize ({MaxDataSize}) in Sensor ({SENSOROBJECT}) exposed by Device ({WdfDevice}) is <= sizeof(SENSOR_COLLECTION_LIST)
Microsoft-Windows-Sensors-Core  |  1014      |           |  [SensorsCx] PKEY_Sensor_MaximumDataFieldSize_Bytes value=({MaxDataSize}) in Sensor ({SENSOROBJECT}) exposed by Device ({WdfDevice}) is incorrect. Please  use CollectionsListGetMarshalledSize() instead of SENSOR_COLLECTION_LIST_SIZE() to compute the value for that property.
Microsoft-Windows-Sensors-Core  |  1015      |           |  [SensorsCx] Batch Size ({BatchSize}) in Sensor ({SENSOROBJECT}) exposed by Device ({WdfDevice}) is more than the maximum amount
Microsoft-Windows-Sensors-Core  |  1016      |           |
Microsoft-Windows-Sensors-Core  |  1017      |           |
Microsoft-Windows-Sensors-Core  |  1018      |           |
Microsoft-Windows-Sensors-Core  |  1019      |           |  [SensorsCx] Get Data Interval DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT}) pIntervalMs=({pIntervalMs})]
Microsoft-Windows-Sensors-Core  |  1020      |           |  [SensorsCx] Set Data Interval DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT}) IntervalMs=({IntervalMs})]
Microsoft-Windows-Sensors-Core  |  1021      |           |  [SensorsCx] Get Data Thresholds DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT}) pThresholds=({pThresholds}) pSize=({pSize})]
Microsoft-Windows-Sensors-Core  |  1022      |           |  [SensorsCx] Set Data Thresholds DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT}) pThresholds=({pThresholds})]
Microsoft-Windows-Sensors-Core  |  1023      |           |  [SensorsCx] Get Properties DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT}) pProperties=({pProperties}) pSize=({pSize})]
Microsoft-Windows-Sensors-Core  |  1024      |           |  [SensorsCx] Get Supported Datafields DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT}) pDatafields=({pProperties}) pSize=({pSize})]
Microsoft-Windows-Sensors-Core  |  1025      |           |  [SensorsCx] Get Datafield Properties DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT}) pDatafield=({pDatafield}) pProperties=({pProperties}) pSize=({pSize})]
Microsoft-Windows-Sensors-Core  |  1026      |           |  [SensorsCx] Start Sensor DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT})]
Microsoft-Windows-Sensors-Core  |  1027      |           |  [SensorsCx] Stop Sensor DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT})]
Microsoft-Windows-Sensors-Core  |  1028      |           |  [SensorsCx] Start Sensor History DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT})]
Microsoft-Windows-Sensors-Core  |  1029      |           |  [SensorsCx] Stop Sensor History DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT})]
Microsoft-Windows-Sensors-Core  |  1030      |           |  [SensorsCx] Start Sensor History DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT}) pHistoryCollection=({pHistoryCollection}) Size=({Size})]
Microsoft-Windows-Sensors-Core  |  1031      |           |  [SensorsCx] Start Sensor History DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT}) pSize=({pBytesWritten})]
Microsoft-Windows-Sensors-Core  |  1032      |           |  [SensorsCx] Clear Sensor History DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT})]
Microsoft-Windows-Sensors-Core  |  1033      |           |  [SensorsCx] Start Set Report Latency DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT}) ReportLatencyMs=({ReportLatencyMs})]
Microsoft-Windows-Sensors-Core  |  1034      |           |  [SensorsCx] Enable Wake DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT})]
Microsoft-Windows-Sensors-Core  |  1035      |           |  [SensorsCx] Disable Wake DDI call failed with NTSTATUS=({NtStatus}) [Device=({WdfDevice}) Sensor=({SENSOROBJECT})]
Microsoft-Windows-Sensors-Core  |  1036      |           |  [SensorsCx] Sensor Rundown: Device=({WdfDevice}) Sensor=({SENSOROBJECT}) Type=({Type}) Category=({Category}) SubType=({SubType}) UniqueId=({PeristentUniqueId}) Name=({Name}) Model=({Model}) Manufacturer=({Manufacturer})
Microsoft-Windows-Sensors-Core  |  1100      |           |  [SensorsCx] Sensor Subscriber Rundown: UniqueId=({PeristentUniqueId}) ProcessId=({ProcessId}) ReportIntervalMs=({ReportIntervalMs}) ReportLatency=({ReportLatencyMs}) IsStreaming=({IsStreaming})
Microsoft-Windows-Sensors-Core  |  1101      |           |  [Sensors] Found Interface=({Interface})
Microsoft-Windows-Sensors-Core  |  1102      |           |  [Sensors] Picked Interface=({Interface}) as the default interface
Microsoft-Windows-Sensors-Core  |  1103      |           |  [Sensors] Interface=({Interface}) marked as primary
Microsoft-Windows-Sensors-Core  |  1104      |           |  [Sensors] Interface=({Interface}) marked as integrated
Microsoft-Windows-Sensors-Core  |  1105      |           |  [Sensors] Interface=({Interface}) has power usage set to ({PowerUsage})
Microsoft-Windows-Sensors-Core  |  1106      |           |  [Sensors] Interface=({Interface}) marked as supporting history
Microsoft-Windows-Sensors-Core  |  1107      |           |  [Sensors] Interface=({Interface}) marked as Auto-brightness preferred
Microsoft-Windows-Sensors-Core  |  1108      |           |  [Sensors] Interface=({Interface}) marked as color capable
Microsoft-Windows-Sensors-Core  |  1200      |           |  [SensorsHid] Found Sensor=({Usage}) WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1201      |           |  [SensorsHid] Skipping unsupported Sensor=({Usage}) WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1202      |           |  [SensorsHid] Incorrect Report ID found in capabilities and reports of Sensor=({SensorUsage}) don't match. Report ID found on capabilities is ({ReportIdInCaps}). Report ID found on report is ({ReportIdInReport}). WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1203      |           |  [SensorsHid] Sensor=({SensorUsage}) with ReportId=({ReportId}) supports history. WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1204      |           |  [SensorsHid] Feature Usage=({Usage}) reported by Sensor=({SensorUsage}) with ReportId=({ReportId}) must be a selector usage. WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1205      |           |  [SensorsHid] Datafield {{fmtid}-{pid}} was added for input Usage=({Usage}) reported by Sensor=({SensorUsage}) with ReportId=({ReportId}) must be a selector usage. WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1206      |           |  [SensorsHid] Property {{fmtid}-{pid}} was added for input Usage=({Usage}) reported by Sensor=({SensorUsage}) with ReportId=({ReportId}) must be a selector usage. WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1207      |           |  [SensorsHid] Threshold {{fmtid}-{pid}} was added for input Usage=({Usage}) reported by Sensor=({SensorUsage}) with ReportId=({ReportId}) must be a selector usage. WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1208      |           |  [SensorsHid] Timestamp usage reported by Sensor=({SensorUsage}) with ReportId=({ReportId}) is ignored since it does not have right capabilities. (Expected Report Size={BitSize}) (Actual Report Size={ExpectedBitSize}) (Expected Report Count={ReportCount}) (Actual Report Count={ExpectedReportCount}) (Expected Exponent={Exponent}) (Actual Exponent={ExpectedExponent}). WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1209      |           |  [SensorsHid] Report Interval is supported by Sensor=({SensorUsage}) with ReportId=({ReportId}). WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1210      |           |  [SensorsHid] Report Interval is missing in Sensor=({SensorUsage}) with ReportId=({ReportId}). WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1211      |           |  [SensorsHid] Reporting State is supported by Sensor=({SensorUsage}) with ReportId=({ReportId}). WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1212      |           |  [SensorsHid] Reporting State is missing in Sensor=({SensorUsage}) with ReportId=({ReportId}). WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1213      |           |  [SensorsHid] Power State is supported by Sensor=({SensorUsage}) with ReportId=({ReportId}). WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1214      |           |  [SensorsHid] Power State is missing in Sensor=({SensorUsage}) with ReportId=({ReportId}). WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1215      |           |  [SensorsHid] Report Latency is supported by Sensor=({SensorUsage}) with ReportId=({ReportId}). WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1216      |           |  [SensorsHid] Report Latency is marked as not supported by Sensor=({SensorUsage}) with ReportId=({ReportId}) since timestamp is missing. WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1217      |           |  [SensorsHid] Sensor State is supported by Sensor=({SensorUsage}) with ReportId=({ReportId}). WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1218      |           |  [SensorsHid] Wake is supported by Sensor=({SensorUsage}) with ReportId=({ReportId}). WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1219      |           |  [SensorsHid] IsWakeReportingStateSupported=({IsWakeReportingStateSupported}) and IsWakePowerStateSupported=({IsWakePowerStateSupported}). Wake is not supported by Sensor=({SensorUsage}) with ReportId=({ReportId}). WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1220      |           |  [SensorsHid] Incorrect Report ID found in report ({ReportIdInReport}). WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1221      |           |  [SensorsHid] Failed to get input report from Sensor=({SensorUsage}) with ReportId=({ReportId}) NTSTATUS=({NtStatus}). WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1222      |           |  [SensorsHid] Failed to get feature report from Sensor=({SensorUsage}) with ReportId=({ReportId}) NTSTATUS=({NtStatus}). WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1223      |           |  [SensorsHid] Failed to set feature report from Sensor=({SensorUsage}) with ReportId=({ReportId}) NTSTATUS=({NtStatus}). WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1224      |           |  [SensorsHid] Sensor=({SensorUsage}) with ReportId=({ReportId}) is color capable. WdfDevice=({WdfDevice})
Microsoft-Windows-Sensors-Core  |  1300      |           |  [SensorsHid] Using Accelerometer=({Interface}) to create Software SDO
Microsoft-Windows-Sensors-Core  |  1301      |           |  [SensorsHid] Using Hardware Offloaded SDO=({Interface}) to create hardware SDO
Microsoft-Windows-Sensors-Core  |  1302      |           |  [SensorsHid] Removing SDO based on sensor=({Interface})