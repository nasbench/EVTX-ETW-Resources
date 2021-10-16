Provider                 |  Event ID  |  Channel                              |  Message
-------------------------|------------|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-VHDMP  |  1         |  Microsoft-Windows-VHDMP/Operational  |  The VHD {VhdFileName} has come online (surfaced) as disk number {VhdDiskNumber}.
Microsoft-Windows-VHDMP  |  2         |  Microsoft-Windows-VHDMP/Operational  |  The VHD {VhdFileName} has been removed (unsurfaced) as disk number {VhdDiskNumber}.
Microsoft-Windows-VHDMP  |  3         |  Microsoft-Windows-VHDMP/Operational  |  Failed to surface VHD {VhdFileName}. Error status {Status}.
Microsoft-Windows-VHDMP  |  4         |  Microsoft-Windows-VHDMP/Operational  |  Failed to surface VHD {VhdFileName}. Surface attempt was cancelled.
Microsoft-Windows-VHDMP  |  5         |  Microsoft-Windows-VHDMP/Operational  |  Failed to {VhdMetaOps} VHD {VhdFileName}. Error status {Status}.
Microsoft-Windows-VHDMP  |  6         |  Microsoft-Windows-VHDMP/Operational  |  Operation failed on VHD {VhdFileName}. {VhdIoType} Error status {Status}.
Microsoft-Windows-VHDMP  |  7         |                                       |
Microsoft-Windows-VHDMP  |  8         |  Microsoft-Windows-VHDMP/Operational  |  Change Tracking has been enabled for the VHD {VhdFileName} ({VirtualDisk}) with log file {LogFileName}.
Microsoft-Windows-VHDMP  |  9         |  Microsoft-Windows-VHDMP/Operational  |  Change Tracking has been disabled for the VHD {VhdFileName} ({VirtualDisk}).
Microsoft-Windows-VHDMP  |  10        |  Microsoft-Windows-VHDMP/Operational  |  Change Tracking for the VHD {VirtualDisk} to the log file {LogFileName} has been stopped due to the error {Status}.
Microsoft-Windows-VHDMP  |  11        |  Microsoft-Windows-VHDMP/Operational  |  Flushing of the header of the log file {LogFileName} has failed due to error {Status}.
Microsoft-Windows-VHDMP  |  12        |  Microsoft-Windows-VHDMP/Operational  |  Flushing of the buffers to the log file {LogFileName} has failed due to error {Status}.
Microsoft-Windows-VHDMP  |  13        |  Microsoft-Windows-VHDMP/Operational  |  Opening the log file {LogFileName} for tracking has failed due to error {Status}.
Microsoft-Windows-VHDMP  |  14        |  Microsoft-Windows-VHDMP/Operational  |  Offline changes are detected for VHD {VhdFileName}. Log file: {LogFileName}, VHD time: {VHDFileTime}, Log file time: {LogFileTime}