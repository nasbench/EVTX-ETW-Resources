Provider                    |  Event ID  |  Channel                    |  Message
----------------------------|------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-Minstore  |  1         |  Minstore Analytic Channel  |  Bucket split
Microsoft-Windows-Minstore  |  2         |  Minstore Analytic Channel  |  Bucket merge
Microsoft-Windows-Minstore  |  10        |  Minstore Analytic Channel  |  Tree update
Microsoft-Windows-Minstore  |  11        |  Minstore Analytic Channel  |  Tree update
Microsoft-Windows-Minstore  |  12        |  Minstore Analytic Channel  |  Start tree update
Microsoft-Windows-Minstore  |  13        |  Minstore Analytic Channel  |  End tree update
Microsoft-Windows-Minstore  |  20        |  Minstore Analytic Channel  |  LFF: Redo log
Microsoft-Windows-Minstore  |  21        |  Minstore Analytic Channel  |  LFF: Protected space
Microsoft-Windows-Minstore  |  22        |  Minstore Debug Channel     |  Allocation range:	Metadata allocation: {IsMetadata} 	Requested tier: {RequestedTier}, actual tier: {ActualTier} 	Requested allocation start: {RequestedStartOfRange}, count: {RequestedCountOfRange} 	Actual allocation start: {AllocatedStartOfRange}, count: {AllocatedCountOfRange}
Microsoft-Windows-Minstore  |  23        |  Minstore Analytic Channel  |  Log tail advance from {Lsn1} to {Lsn2}.Log is {Amount} percent full.
Microsoft-Windows-Minstore  |  24        |  Minstore Analytic Channel  |  Log pulse lazy writer. Log is {Amount} percent full.
Microsoft-Windows-Minstore  |  25        |  Minstore Analytic Channel  |  Container move:	Source tier: {SourceTier}, Target tier: {TargetTier} 	Source start of range: {SourceStartOfRange}, count: {SourceCountOfRange} 	 Target physical offset: {TargetPhysicalOffset} 	SSD Fill Ratio {SsdFillRatio}, HDD Fill Ratio {HddFillRatio} 	Reserved: {IsTargetReserved}	Destaged allocation count: {DestageAllocationCount}	Failed SSD Destage: {SourceTier}0
Microsoft-Windows-Minstore  |  26        |  Minstore Analytic Channel  |  Minstore Redo Log application has been skipped. Minstore will now mount the volume without applying the redo log.
Microsoft-Windows-Minstore  |  27        |  Minstore Analytic Channel  |  An error
Microsoft-Windows-Minstore  |  50        |  Minstore Analytic Channel  |  Two threads tried to read bucket {IdHigh} (table {IdLow}) for level
Microsoft-Windows-Minstore  |  51        |  Minstore Analytic Channel  |  A thread had to wait to lock bucket {IdHigh} (table {IdLow}) for level
Microsoft-Windows-Minstore  |  52        |  Minstore Analytic Channel  |  A thread had to wait for a copy of bucket {IdHigh} (table {IdLow}) for level
Microsoft-Windows-Minstore  |  100       |  Minstore Analytic Channel  |  B+ node CRC mismatch
Microsoft-Windows-Minstore  |  101       |  Minstore Analytic Channel  |  B+ node repaired via redundant copy
Microsoft-Windows-Minstore  |  1000      |  Minstore Analytic Channel  |  B+ tree node started splitting
Microsoft-Windows-Minstore  |  1002      |  Minstore Analytic Channel  |  B+ tree node finished splitting
Microsoft-Windows-Minstore  |  1003      |  Minstore Analytic Channel  |  B+ tree nodes started merging
Microsoft-Windows-Minstore  |  1004      |  Minstore Analytic Channel  |  B+ tree nodes finished merging
Microsoft-Windows-Minstore  |  1005      |  Minstore Analytic Channel  |  B+ tree starting pushing its root
Microsoft-Windows-Minstore  |  1006      |  Minstore Analytic Channel  |  B+ tree finished pushing its root
Microsoft-Windows-Minstore  |  1007      |  Minstore Analytic Channel  |  B+ tree starting popping its root
Microsoft-Windows-Minstore  |  1008      |  Minstore Analytic Channel  |  B+ tree finished popping its root
Microsoft-Windows-Minstore  |  1011      |  Minstore Analytic Channel  |  Analyze pass start
Microsoft-Windows-Minstore  |  1012      |  Minstore Analytic Channel  |  Analyze pass end
Microsoft-Windows-Minstore  |  1013      |  Minstore Analytic Channel  |  Redo pass start
Microsoft-Windows-Minstore  |  1014      |  Minstore Analytic Channel  |  Redo pass end
Microsoft-Windows-Minstore  |  1015      |  Minstore Analytic Channel  |  Flush And Checkpoint start
Microsoft-Windows-Minstore  |  1016      |  Minstore Analytic Channel  |  Flush And Checkpoint end
Microsoft-Windows-Minstore  |  1017      |  Minstore Analytic Channel  |  First redo transaction found
Microsoft-Windows-Minstore  |  1018      |  Minstore Analytic Channel  |  Tree Update Record found
Microsoft-Windows-Minstore  |  1019      |  Minstore Analytic Channel  |  Open Table for redo
Microsoft-Windows-Minstore  |  1020      |  Minstore Analytic Channel  |  Reserve ranges for redo