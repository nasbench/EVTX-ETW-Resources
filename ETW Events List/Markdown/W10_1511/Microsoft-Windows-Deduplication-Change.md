Provider                                |  Event ID  |  Channel  |  Message
----------------------------------------|------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-Deduplication-Change  |  16384     |           |  Create chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc)
Microsoft-Windows-Deduplication-Change  |  16385     |           |  Create chunk container completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16386     |           |  Copy chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc)
Microsoft-Windows-Deduplication-Change  |  16387     |           |  Copy chunk container completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16388     |           |  Delete chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc)
Microsoft-Windows-Deduplication-Change  |  16389     |           |  Delete chunk container completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16390     |           |  Rename chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc{InvalidFileName})
Microsoft-Windows-Deduplication-Change  |  16391     |           |  Rename chunk container completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16392     |           |  Flush chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc)
Microsoft-Windows-Deduplication-Change  |  16393     |           |  Flush chunk container completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16394     |           |  Rollback chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc)
Microsoft-Windows-Deduplication-Change  |  16395     |           |  Rollback chunk container completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16396     |           |  Mark chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc) read-only
Microsoft-Windows-Deduplication-Change  |  16397     |           |  Mark chunk container read-only completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16398     |           |  Write chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc) redirection table at offset {ContainerOffset} (Entries: StartIndex {StartIndex}, Count {EntryCount})
Microsoft-Windows-Deduplication-Change  |  16399     |           |  Write chunk container redirection table completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16400     |           |  Write chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc) header at offset {ContainerOffset} (Header: USN {UpdateSequenceNumber}, VDL {Signature}0, #Chunk {Signature}1, NextLocalId {Signature}2, Flags {Signature}3, LastAppendTime {Signature}4, BackupRedirectionTableOfset {Signature}5, LastReconciliationLocalId {Signature}6)
Microsoft-Windows-Deduplication-Change  |  16401     |           |  Write chunk container header completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16402     |           |  Insert data chunk header to chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc) at offset {WriteOffset} (Chunk: IsBatched {IsBatched} IsCorupted {IsCorrupted}, DataSize {DataSize})
Microsoft-Windows-Deduplication-Change  |  16403     |           |  Insert data chunk header completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16404     |           |  Insert data chunk body to chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc) at offset {WriteOffset} (Chunk: IsBatched {IsBatched} IsCorrupted {IsCorrupted}, DataSize {DataSize})
Microsoft-Windows-Deduplication-Change  |  16405     |           |  Insert data chunk body completed {CompletionStatus} with ChunkId {ChunkId}
Microsoft-Windows-Deduplication-Change  |  16408     |           |  Write delete log ({ChunkStoreType} - {ContainerId}.{LogNumber}.delete.log) header
Microsoft-Windows-Deduplication-Change  |  16409     |           |  Write delete log header completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16410     |           |  Append delete log ({ChunkStoreType} - {ContainerId}.{LogNumber}.delete.log) entries at offset {FileExtension} (Entries: StartIndex {DeleteLogOffset}, Count {StartIndex})
Microsoft-Windows-Deduplication-Change  |  16411     |           |  Append delete log entries completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16412     |           |  Delete delete log ({ChunkStoreType} - {ContainerId}.{LogNumber}.delete.log)
Microsoft-Windows-Deduplication-Change  |  16413     |           |  Delete delete log completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16414     |           |  Rename delete log ({ChunkStoreType} - {ContainerId}.{LogNumber}.delete.log)
Microsoft-Windows-Deduplication-Change  |  16415     |           |  Rename delete log completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16416     |           |  Write chunk container bitmap ({ChunkStoreType} - {FileName}) for chunk container ({ChunkStoreType} - {ContainerId}.{Generation}) (Bitmap: BitLength {BitLength}, StartIndex {StartIndex}, Count {EntryCount})
Microsoft-Windows-Deduplication-Change  |  16417     |           |  Write chunk container bitmap completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16418     |           |  Delete chunk container bitmap ({ChunkStoreType} - {FileName}) for chunk container ({ChunkStoreType} - {ContainerId}.{Generation})
Microsoft-Windows-Deduplication-Change  |  16419     |           |  Delete chunk container bitmap completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16420     |           |  Write merge log ({ChunkStoreType} - {ContainerId}.{LogNumber}.merge.log) header
Microsoft-Windows-Deduplication-Change  |  16421     |           |  Write merge log header completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16422     |           |  Insert hotspot chunk header to chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc) at offset {WriteOffset} (Chunk: IsBatched {IsBatched} IsCorrupted {IsCorrupted}, DataSize {DataSize})
Microsoft-Windows-Deduplication-Change  |  16423     |           |  Insert hotspot chunk header completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16424     |           |  Insert hotspot chunk body to chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc) at offset {WriteOffset} (Chunk: IsBatched {IsBatched} IsCorrupted {IsCorrupted}, DataSize {DataSize})
Microsoft-Windows-Deduplication-Change  |  16425     |           |  Insert hotspot chunk body completed {CompletionStatus} with ChunkId {ChunkId}
Microsoft-Windows-Deduplication-Change  |  16426     |           |  Insert stream map chunk header to chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc) at offset {WriteOffset} (Chunk: IsBatched {IsBatched} IsCorrupted {IsCorrupted}, DataSize {DataSize})
Microsoft-Windows-Deduplication-Change  |  16427     |           |  Insert stream map chunk header completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16428     |           |  Insert stream map chunk body to chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc) at offset {WriteOffset} (Chunk: IsBatched {IsBatched} IsCorrupted {IsCorrupted}, DataSize {DataSize}) (Entries: StartIndex {StartIndex}, Count {EntryCount})
Microsoft-Windows-Deduplication-Change  |  16429     |           |  Insert stream map chunk body completed {CompletionStatus} with ChunkId {ChunkId}
Microsoft-Windows-Deduplication-Change  |  16430     |           |  Append merge log ({ChunkStoreType} - {ContainerId}.{LogNumber}.merge.log) entries at offset {MergeLogOffset} (Entries: StartIndex {StartIndex}, Count {EntryCount})
Microsoft-Windows-Deduplication-Change  |  16431     |           |  Append merge log entries completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16432     |           |  Delete merge log ({ChunkStoreType} - {ContainerId}.{LogNumber}.merge.log)
Microsoft-Windows-Deduplication-Change  |  16433     |           |  Delete merge log completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16434     |           |  Flush merge log ({ChunkStoreType} - {ContainerId}.{LogNumber}.merge.log)
Microsoft-Windows-Deduplication-Change  |  16435     |           |  Flush merge log completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16436     |           |  Update file list entries (Remove: {EntryToRemove}, Add: {EntryToAdd})
Microsoft-Windows-Deduplication-Change  |  16437     |           |  Update file list entries completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16438     |           |  Set dedup reparse point on {FilePath} (FileId {FileId}) (ReparsePoint: SizeBackedByChunkStore {SizeBackedByChunkStore}, StreamMapInfoSize {StreamMapInfoSize}, StreamMapInfo {StreamMapInfo})
Microsoft-Windows-Deduplication-Change  |  16439     |           |  Set dedup reparse point completed {CompletionStatus} ({ReparsePointSet})
Microsoft-Windows-Deduplication-Change  |  16440     |           |  Set dedup zero data on {FilePath} (FileId {FileId})
Microsoft-Windows-Deduplication-Change  |  16441     |           |  Set dedup zero data completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16442     |           |  Flush reparse point files
Microsoft-Windows-Deduplication-Change  |  16443     |           |  Flush reparse point files completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16444     |           |  Set sparse on file id {FileId}
Microsoft-Windows-Deduplication-Change  |  16445     |           |  Set sparse completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16446     |           |  FSCTL_SET_ZERO_DATA on file id {FileId} at offset {Offset} and BeyondFinalZero {BeyondFinalZero}
Microsoft-Windows-Deduplication-Change  |  16447     |           |  FSCTL_SET_ZERO_DATA completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16448     |           |  Rename chunk container bitmap ({ChunkStoreType} - {FileName}) for chunk container ({ChunkStoreType} - {ContainerId}.{Generation})
Microsoft-Windows-Deduplication-Change  |  16449     |           |  Rename chunk container bitmap completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16450     |           |  Insert padding chunk header to chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc) at offset {WriteOffset} (Chunk: IsBatched {IsBatched} IsCorupted {IsCorrupted}, DataSize {DataSize})
Microsoft-Windows-Deduplication-Change  |  16451     |           |  Insert padding chunk header completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16452     |           |  Insert padding chunk body to chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc) at offset {WriteOffset} (Chunk: IsBatched {IsBatched} IsCorrupted {IsCorrupted}, DataSize {DataSize})
Microsoft-Windows-Deduplication-Change  |  16453     |           |  Insert padding chunk body completed {CompletionStatus} with ChunkId {ChunkId}
Microsoft-Windows-Deduplication-Change  |  16454     |           |  Insert batch of chunks to chunk container ({ChunkStoreType} - {ContainerId}.{Generation}.ccc) at offset {WriteOffset} (BatchChunkCount {BatchChunkCount}, BatchDataSize {BatchDataSize})
Microsoft-Windows-Deduplication-Change  |  16455     |           |  Insert batch of chunks completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16456     |           |  Write chunk container directory ({ChunkStoreType} - {FileName}) for chunk container ({ChunkStoreType} - {ContainerId}.{Generation}) (Directory: EntryCount {FileCopyLevel})
Microsoft-Windows-Deduplication-Change  |  16457     |           |  Write chunk container directory completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16458     |           |  Delete chunk container directory ({ChunkStoreType} - {FileName}) for chunk container ({ChunkStoreType} - {ContainerId}.{Generation})
Microsoft-Windows-Deduplication-Change  |  16459     |           |  Delete chunk container directory completed {CompletionStatus}
Microsoft-Windows-Deduplication-Change  |  16460     |           |  Rename chunk container directory ({ChunkStoreType} - {FileName}) for chunk container ({ChunkStoreType} - {ContainerId}.{Generation})
Microsoft-Windows-Deduplication-Change  |  16461     |           |  Rename chunk container directory completed {CompletionStatus}