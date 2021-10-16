Provider                                |  Event ID  |  Channel  |  Message
----------------------------------------|------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-MCCS-DavSyncProvider  |  1         |           |  Error: {P1_HResult} Location: {P2_String} Line Number: {P3_UInt32}
Microsoft-Windows-MCCS-DavSyncProvider  |  2         |           |  Error Propagated: {P1_HResult} Location: {P2_String} Line Number: {P3_UInt32}
Microsoft-Windows-MCCS-DavSyncProvider  |  101       |           |  DavSyncProvider: Ignoring unsolicited item in a multi-get response (id: {Prop_Id}).
Microsoft-Windows-MCCS-DavSyncProvider  |  102       |           |  DavSyncProvider: Requested item missing from the multi-get response (id: {Prop_Id}).
Microsoft-Windows-MCCS-DavSyncProvider  |  103       |           |  DavSyncProvider: Handling download result for an existing item (id: {Prop_Id}, tag: {Prop_String}, status {Prop_Dword}, item data available: {Prop_Bool}).
Microsoft-Windows-MCCS-DavSyncProvider  |  104       |           |  DavSyncProvider: The download result for an existing item has successful status and empty data (id: {Prop_Id}, status {Prop_Dword}).
Microsoft-Windows-MCCS-DavSyncProvider  |  105       |           |  DavSyncProvider: Handled download result with item not found status by deleting the local item (id: {Prop_Id}, status: {Prop_Dword}).
Microsoft-Windows-MCCS-DavSyncProvider  |  106       |           |  DavSyncProvider: Handled download result for an existing item (id: {Prop_Id}, new tag: {Prop_String}, result {Prop_HResult}).
Microsoft-Windows-MCCS-DavSyncProvider  |  107       |           |  DavSyncProvider: Handling download result for a new item (id: {Prop_Id}, tag: {Prop_String}, status {Prop_Dword}, item data available: {Prop_Bool}).
Microsoft-Windows-MCCS-DavSyncProvider  |  108       |           |  DavSyncProvider: The download result for a new item has successful status and empty data (id: {Prop_Id}, status {Prop_Dword}).
Microsoft-Windows-MCCS-DavSyncProvider  |  109       |           |  DavSyncProvider: Handled download result for an existing item (id: {Prop_Id}, new tag: {Prop_String}, result {Prop_HResult}).
Microsoft-Windows-MCCS-DavSyncProvider  |  110       |           |  DavSyncProvider: Item added to the download batch (id: {Prop_Id}, server tag: {Prop_String1}, local tag: {Prop_String2}, new item: {Prop_Bool}).
Microsoft-Windows-MCCS-DavSyncProvider  |  111       |           |  DavSyncProvider: Collection tag changed, downloading server changes (id: {Prop_Id}, server tag: {Prop_String1}, local tag: {Prop_String2}, session id: {Prop_Dword}).
Microsoft-Windows-MCCS-DavSyncProvider  |  112       |           |  DavSyncProvider: Downloading changed items batch (id: {Prop_Id}, size: {Prop_Dword}).
Microsoft-Windows-MCCS-DavSyncProvider  |  113       |           |  DavSyncProvider: Deleting all local items which no longer exist on the server (collection id: {Prop_Id}, session id: {Prop_Dword}).
Microsoft-Windows-MCCS-DavSyncProvider  |  114       |           |  DavSyncProvider: Local item deleted because it no longer exists on the server (id: {Prop_Id}).
Microsoft-Windows-MCCS-DavSyncProvider  |  115       |           |  DavSyncProvider: Successfully deleted all local items which no longer exist on the server (collection id: {Prop_Id}, session id: {Prop_Dword}).
Microsoft-Windows-MCCS-DavSyncProvider  |  116       |           |  DavSyncProvider: Successfully downloaded server changes (id: {Prop_Id}, new tag: {Prop_String}, session id: {Prop_Dword}).
Microsoft-Windows-MCCS-DavSyncProvider  |  117       |           |  DavSyncProvider: Deleting the local collection with id: {Prop_Id}.
Microsoft-Windows-MCCS-DavSyncProvider  |  118       |           |  DavSyncProvider: Deleted local collection (last collection: {Prop_Bool}, id: {Prop_Id})
Microsoft-Windows-MCCS-DavSyncProvider  |  119       |           |  DavSyncProvider: Purging the local collection with id: {Prop_Id}.
Microsoft-Windows-MCCS-DavSyncProvider  |  120       |           |  DavSyncProvider: Purged local collection (id: {Prop_Id}).
Microsoft-Windows-MCCS-DavSyncProvider  |  121       |           |  DavSyncProvider: Synchronizing the list of collections (session id: {Prop_Dword}).
Microsoft-Windows-MCCS-DavSyncProvider  |  122       |           |  DavSyncProvider: Local collection created (collection id: {Prop_Id}, description: {Prop_String}, session id: {Prop_Dword}).
Microsoft-Windows-MCCS-DavSyncProvider  |  123       |           |  DavSyncProvider: Local collection updated (collection id: {Prop_Id}, description: {Prop_String}, session id: {Prop_Dword}).
Microsoft-Windows-MCCS-DavSyncProvider  |  124       |           |  DavSyncProvider: Deleting all local collections which no longer exist on the server (session id: {Prop_Dword}).
Microsoft-Windows-MCCS-DavSyncProvider  |  125       |           |  DavSyncProvider: Local collection deleted because it no longer exists on the server (collection id: {Prop_Id}).
Microsoft-Windows-MCCS-DavSyncProvider  |  126       |           |  DavSyncProvider: Successfully deleted all local collections which no longer exist on the server (session id: {Prop_Dword}).
Microsoft-Windows-MCCS-DavSyncProvider  |  127       |           |  DavSyncProvider: Successfully synchronized the list of collections (session id: {Prop_Dword}).
Microsoft-Windows-MCCS-DavSyncProvider  |  128       |           |  DavSyncProvider: The property status {Prop_Dword} returned for a null property is invalid and was coreced to 404.
Microsoft-Windows-MCCS-DavSyncProvider  |  129       |           |  DavSyncProvider: Received a non-successful ctag property response (collection id: {Prop_Id}, status {Prop_Dword}).
Microsoft-Windows-MCCS-DavSyncProvider  |  130       |           |  DavSyncProvider: Uploading change (item id: {Prop_Id}, type: {Prop_Type}).
Microsoft-Windows-MCCS-DavSyncProvider  |  131       |           |  DavSyncProvider: Uploaded change (item id: {Prop_Id}, type: {Prop_Type}, status: {Prop_Dword}).
Microsoft-Windows-MCCS-DavSyncProvider  |  132       |           |  DavSyncProvider: Deleted successfuly uploaded item because it has the same Uri as a previously downloaded item (item id: {Prop_Id}).
Microsoft-Windows-MCCS-DavSyncProvider  |  133       |           |  DavSyncProvider: Failed to upload change (item id: {Prop_Id}, retry: {Prop_Bool}).
Microsoft-Windows-MCCS-DavSyncProvider  |  134       |           |  DavSyncProvider: Deleted local tombstone (item id: {Prop_Id}).
Microsoft-Windows-MCCS-DavSyncProvider  |  135       |           |  DavSyncProvider: Modification change uploaded successfully (item id: {Prop_Id}, tag: {Prop_String}).
Microsoft-Windows-MCCS-DavSyncProvider  |  136       |           |  DavSyncProvider: New item uploaded successfully (uid: {Prop_Id1}, item id: {Prop_Id2}, tag: {Prop_String}).
Microsoft-Windows-MCCS-DavSyncProvider  |  137       |           |  DavSyncProvider: Uploading local changes (collection id: {Prop_Id}).
Microsoft-Windows-MCCS-DavSyncProvider  |  138       |           |  DavSyncProvider: Finished uploading the local changes (collection id: {Prop_Id}, uploaded changes: {Prop_Bool}).
Microsoft-Windows-MCCS-DavSyncProvider  |  161       |           |
Microsoft-Windows-MCCS-DavSyncProvider  |  162       |           |
Microsoft-Windows-MCCS-DavSyncProvider  |  166       |           |
Microsoft-Windows-MCCS-DavSyncProvider  |  171       |           |  DavSyncProvider: Failed to fetch attachment, uri hash {Prop_String}.
Microsoft-Windows-MCCS-DavSyncProvider  |  172       |           |  DavSyncProvider: Delay uploading item (uri hash: {Prop_Id}) changes.
Microsoft-Windows-MCCS-DavSyncProvider  |  201       |           |
Microsoft-Windows-MCCS-DavSyncProvider  |  202       |           |