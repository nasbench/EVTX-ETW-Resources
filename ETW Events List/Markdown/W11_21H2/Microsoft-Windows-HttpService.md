Provider                       |  Event ID  |  Channel               |  Message
-------------------------------|------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-HttpService  |  1         |  HTTP Service Channel  |  Request received (request ID {RequestId}) on connection (connection ID {ConnectionId}) from remote address {RemoteAddr}.
Microsoft-Windows-HttpService  |  2         |  HTTP Service Channel  |  Parsed request (request pointer {RequestObj}, method {HttpVerb}) with URI {Url}.
Microsoft-Windows-HttpService  |  3         |  HTTP Service Channel  |  Delivered request to server application (request pointer {RequestObj}, request ID {RequestId}, site ID {SiteId}) from request queue {RequestQueueName} for URI {Url} with status {Status}.
Microsoft-Windows-HttpService  |  4         |  HTTP Service Channel  |  Server application passed response (request ID {RequestId}, connection ID {ConnectionId}, method {Verb}, header length {HeaderLength}, number of entity chunks {EntityChunkCount}, cache policy {CachePolicy}) with status code {StatusCode}.
Microsoft-Windows-HttpService  |  5         |  HTTP Service Channel  |  Server application passed the last response (corresponding to request ID {RequestId}).
Microsoft-Windows-HttpService  |  6         |  HTTP Service Channel  |  Server application passed entity body for request ID {RequestId} (connection ID {ConnectionId}).
Microsoft-Windows-HttpService  |  7         |  HTTP Service Channel  |  Server application passed the last entity body for request ID {RequestId}.
Microsoft-Windows-HttpService  |  8         |  HTTP Service Channel  |  Server application passed response (request ID {RequestId}, connection ID {ConnectionId}, method {Verb}, header length {HeaderLength}, number of entity chunks {EntityChunkCount}, cache policy {CachePolicy}) with status code {StatusCode}.
Microsoft-Windows-HttpService  |  9         |  HTTP Service Channel  |  Server application passed the last response (corresponding to request ID {RequestId}).
Microsoft-Windows-HttpService  |  10        |  HTTP Service Channel  |  Response ready for send (corresponding to request ID {RequestId}) with status code {HttpStatus}.
Microsoft-Windows-HttpService  |  11        |  HTTP Service Channel  |  Cached the response (corresponding to request ID {RequestId}) with status code {HttpStatus}. Response to be sent.
Microsoft-Windows-HttpService  |  12        |  HTTP Service Channel  |  Queued last response (corresponding to request ID {RequestId}) for sending. Status code is {HttpStatus}.
Microsoft-Windows-HttpService  |  13        |  HTTP Service Channel  |  Response sent (corresponding to request ID {RequestId}) with status code {HttpStatus}. If disconnect is required, a TCP FIN has been sent.
Microsoft-Windows-HttpService  |  14        |  HTTP Service Channel  |  Error occurred while sending the last response (corresponding to request ID {RequestId}) with status code {HttpStatus}. A TCP Reset has been sent.
Microsoft-Windows-HttpService  |  15        |  HTTP Service Channel  |  Error {Status} occurred while sending (corresponding to request ID {RequestId}). A TCP Reset will be sent.
Microsoft-Windows-HttpService  |  16        |  HTTP Service Channel  |  Response (request pointer {RequestObj}, site ID {SiteId}, number of bytes {BytesSent}) queued for sending from the cache.
Microsoft-Windows-HttpService  |  16        |  HTTP Service Channel  |  Response (request pointer {RequestObj}, corresponding to request ID {RequestId}, site ID {SiteId}, number of bytes {BytesSent}, encoding {Encoding}) queued for sending from the cache.
Microsoft-Windows-HttpService  |  17        |  HTTP Service Channel  |  Response (request pointer {RequestObj}, site ID {SiteId}, number of bytes {BytesSent}) queued for sending with status code 304 (cache not modified).
Microsoft-Windows-HttpService  |  17        |  HTTP Service Channel  |  Response (request pointer {RequestObj}, site ID {SiteId}, number of bytes {BytesSent}, encoding {Encoding}) queued for sending with status code 304 (cache not modified).
Microsoft-Windows-HttpService  |  18        |  HTTP Service Channel  |  Attempted to reserve URL ({Url}). Status {ReserveStatus}.
Microsoft-Windows-HttpService  |  19        |  HTTP Service Channel  |  Successfully read the IP listen list for IP address {IpAddrLength}.
Microsoft-Windows-HttpService  |  20        |  HTTP Service Channel  |  SSL credentials for IP address and port {Address} successfully created.
Microsoft-Windows-HttpService  |  20        |  HTTP Service Channel  |  SSL credentials for endpoint {Endpoint} successfully created.
Microsoft-Windows-HttpService  |  21        |  HTTP Service Channel  |  New connection created (local IP address {LocalAddr} and remote address {RemoteAddr}).
Microsoft-Windows-HttpService  |  22        |  HTTP Service Channel  |  Connection ID ({ConnectionId}) assigned to connection and request (request ID {RequestId}) will be parsed.
Microsoft-Windows-HttpService  |  23        |  HTTP Service Channel  |  Client closed the connection (connection pointer {ConnectionObj}). Status of whether closed by TCP Reset: {Abortive}.
Microsoft-Windows-HttpService  |  24        |  HTTP Service Channel  |  Connection (connection pointer {ConnectionObj}) cleanup started due to either the sending of a TCP Reset, receiving of a TCP Reset, or after the mutual exchange of TCP Fins.
Microsoft-Windows-HttpService  |  25        |  HTTP Service Channel  |  Successfully added entry (URI {Uri}) to cache.
Microsoft-Windows-HttpService  |  25        |  HTTP Service Channel  |  Successfully added entry (URI {Uri}) to cache (Encoding {Encoding}).
Microsoft-Windows-HttpService  |  26        |  HTTP Service Channel  |  Failed to add an entry (URI {UrlBuffer}) to the cache. Status: {ErrorStatus}.
Microsoft-Windows-HttpService  |  26        |  HTTP Service Channel  |  Failed to add an entry (URI {UrlBuffer}) to the cache. Status: {ErrorStatus}. Encoding: {Encoding}.
Microsoft-Windows-HttpService  |  27        |  HTTP Service Channel  |  Flushed entry (URI {Uri}) from the cache.
Microsoft-Windows-HttpService  |  28        |  HTTP Service Channel  |  Attempted to set URL group property: {Property}. Status: {Status}.
Microsoft-Windows-HttpService  |  29        |  HTTP Service Channel  |  Attempted to set server session property: {Property}. Status: {Status}.
Microsoft-Windows-HttpService  |  30        |  HTTP Service Channel  |  Attempted to set request queue property: {Property}. Status: {Status}.
Microsoft-Windows-HttpService  |  31        |  HTTP Service Channel  |  Attempted to add URL ({Url}) to URL group ({UrlGroupId}). Status: {Status}.
Microsoft-Windows-HttpService  |  32        |  HTTP Service Channel  |  Removed URL ({Url}) from URL group ({UrlGroupId}).
Microsoft-Windows-HttpService  |  33        |  HTTP Service Channel  |  Removed all URLs from URL group {UrlGroupId}.
Microsoft-Windows-HttpService  |  34        |  HTTP Service Channel  |  Initiating SSL connection.
Microsoft-Windows-HttpService  |  35        |  HTTP Service Channel  |  Initiating SSL handshake.
Microsoft-Windows-HttpService  |  36        |  HTTP Service Channel  |  SSL handshake completed with status: {Status}.
Microsoft-Windows-HttpService  |  37        |  HTTP Service Channel  |  Server application is attempting to receive the SSL client certificate, which will be provided if available. If the client certificate is not available, a renegotiation will be initiated.
Microsoft-Windows-HttpService  |  38        |  HTTP Service Channel  |  Attempt by server application to receive client certificate failed with status: {Status}.
Microsoft-Windows-HttpService  |  39        |  HTTP Service Channel  |  Raw SSL data is available for processing.
Microsoft-Windows-HttpService  |  40        |  HTTP Service Channel  |  Decrypted SSL data is available for processing.
Microsoft-Windows-HttpService  |  41        |  HTTP Service Channel  |  Passed plaintext data for encryption.
Microsoft-Windows-HttpService  |  43        |  HTTP Service Channel  |  Attempt (on connection ID {ConnectionId}) to authenticate client completed. Authentication type {AuthType}. Security status: {SecStatus}.
Microsoft-Windows-HttpService  |  43        |  HTTP Service Channel  |  Attempt (on connection ID {ConnectionId}) to authenticate client completed. Authentication type {AuthType}. Security status: {SecStatus}.
Microsoft-Windows-HttpService  |  44        |  HTTP Service Channel  |  Attempted to add entry to the {AuthCacheType} authentication cache. Status: {Status}.
Microsoft-Windows-HttpService  |  45        |  HTTP Service Channel  |  Entry successfully removed from the authentication cache.
Microsoft-Windows-HttpService  |  46        |  HTTP Service Channel  |  Successfully associated QoS flow with connection (connection ID {ConnectionId}). Bandwidth throttled to: {Bandwidth} Bytes per second.
Microsoft-Windows-HttpService  |  47        |  HTTP Service Channel  |  Failed to configure the {Type} logging (directory {Directory}), Status: {Status}.
Microsoft-Windows-HttpService  |  48        |  HTTP Service Channel  |  Successfully configured {Type} logging (directory {Directory}).
Microsoft-Windows-HttpService  |  49        |  HTTP Service Channel  |  Failed to create {Type} log file {Filename}. Status: {Status}.
Microsoft-Windows-HttpService  |  50        |  HTTP Service Channel  |  Successfully created new {Type} log file {Filename}.
Microsoft-Windows-HttpService  |  51        |  HTTP Service Channel  |  Entry has been written to {Type} log file.
Microsoft-Windows-HttpService  |  52        |  HTTP Service Channel  |  Parsing of request (request ID {RequestId}) failed due to reason: {Reason}. Request may not be compliant with HTTP/1.1.
Microsoft-Windows-HttpService  |  53        |  HTTP Service Channel  |  HTTP timer {Timer} expired. The connection will be reset.
Microsoft-Windows-HttpService  |  56        |  HTTP Service Channel  |  Failed to acquire handle for SSL credentials. Failure will be event logged. Security status: {SecStatus}.
Microsoft-Windows-HttpService  |  57        |  HTTP Service Channel  |  SSL connection will be disconnected as initiated by the client.
Microsoft-Windows-HttpService  |  58        |  HTTP Service Channel  |  SSL connection will be disconnected as initiated by the server application. Status: {Status}.
Microsoft-Windows-HttpService  |  59        |  HTTP Service Channel  |  Attempt to decrypt SSL data failed. Security status: {SecStatus}.
Microsoft-Windows-HttpService  |  60        |  HTTP Service Channel  |  Query for SSL connection parameters failed. Security status: {SecStatus}. Connection will be reset.
Microsoft-Windows-HttpService  |  61        |  HTTP Service Channel  |  Cannot find SSL endpoint for inbound connection for local IP address and port {Address}.
Microsoft-Windows-HttpService  |  62        |  HTTP Service Channel  |  Attempt to perform SSL handshake failed. Security status: {SecStatus}.
Microsoft-Windows-HttpService  |  63        |  HTTP Service Channel  |  Attempt to encrypt SSL data failed. Security status: {SecStatus}.
Microsoft-Windows-HttpService  |  64        |  HTTP Service Channel  |  Request (request ID {RequestId}) rejected due to reason: {Reason}.
Microsoft-Windows-HttpService  |  65        |  HTTP Service Channel  |  Server application canceled the processing of its request (request ID {RequestId}).
Microsoft-Windows-HttpService  |  66        |  HTTP Service Channel  |  Http.sys failed to process CPU hot-add. Processor number: {NewProcNumber}, reason: {ReasonString}, status: {Status}.
Microsoft-Windows-HttpService  |  67        |  HTTP Service Channel  |  Hot-add information: Current UxNumberOfProcessors: {NewProcNumber}, comment: {Comment}.
Microsoft-Windows-HttpService  |  68        |  HTTP Service Channel  |  Initialized QoS flow: FlowHandle {FlowHandle}, bandwidth {Bandwidth}, peak bandwidth {PeakBandwidth}, burst size {BurstSize}
Microsoft-Windows-HttpService  |  69        |  HTTP Service Channel  |  Initialized QoS flow: FlowHandle {FlowHandle}, bandwidth {Bandwidth}, peak bandwidth {PeakBandwidth}, burst size {BurstSize}
Microsoft-Windows-HttpService  |  70        |  HTTP Service Channel  |  QoS flow initialization failed: bandwidth {Bandwidth}, peak bandwidth {PeakBandwidth}, burst size {BurstSize}, status {Status}
Microsoft-Windows-HttpService  |  71        |  HTTP Service Channel  |  Setting flow: Connection {Connection}, FlowHandle {FlowHandle}
Microsoft-Windows-HttpService  |  72        |  HTTP Service Channel  |  Assign to Configuration QoS Flow: FlowHandle {FlowHandle}
Microsoft-Windows-HttpService  |  73        |  HTTP Service Channel  |  [re]Setting QoS Flow failed: Connection {Connection}, FlowHandle {FlowHandle}, status {Status}
Microsoft-Windows-HttpService  |  74        |  HTTP Service Channel  |  Response range processing done. Req. {RequestId}, response content size {ContentBytes}, ranges {NumberOfRanges} ({Range1Start}-{Range1End}, {Range2Start}-{Range2End},...)
Microsoft-Windows-HttpService  |  75        |  HTTP Service Channel  |  Begin building slices. Req. {RequestId}, slices {NumberOfSlices} ({SliceIndex1},{SliceIndex2},...), ranges {NumberOfRanges} ({Range1Start}-{Range1End}, {Range2Start}-{Range2End},...)
Microsoft-Windows-HttpService  |  76        |  HTTP Service Channel  |  Send cached slices. Req. {RequestId}, CacheEntry {CacheEntryPtr}, slices {NumberOfSlices} ({SliceIndex1},{SliceIndex2},...), ranges {NumberOfRanges} ({Range1Start}-{Range1End}, {Range2Start}-{RequestId}0,...)
Microsoft-Windows-HttpService  |  77        |  HTTP Service Channel  |  Cached slices match content. Req. {RequestId}, CacheEntry {CacheEntryPtr}, slices {NumberOfSlices} ({SliceIndex1},{SliceIndex2},...), ranges {NumberOfRanges} ({Range1Start}-{Range1End}, {Range2Start}-{RequestId}0,...)
Microsoft-Windows-HttpService  |  78        |  HTTP Service Channel  |  Merge slices to cache. CacheEntry {CacheEntryPtr}, slices to merge {NofSlicesToMerge}, slices to cache {NofSlicesInCache}
Microsoft-Windows-HttpService  |  79        |  HTTP Service Channel  |  Sending range from flat cache entry. CacheEntry {CacheEntryPtr}, range {Range1Start}-{Range1End}
Microsoft-Windows-HttpService  |  80        |  HTTP Service Channel  |  Channel bind ASC parameters: connection {ConnectionId}, buffers {NoBindBuffers}, flags {SecFlags}
Microsoft-Windows-HttpService  |  81        |  HTTP Service Channel  |  Service bind check done. Connection {ConnectionId}, Context {SecContextL}-{SecContextH}, status {SecStatus}, target {Target}
Microsoft-Windows-HttpService  |  82        |  HTTP Service Channel  |  Captured channel bind config. Hardening {Hardening}, flags {Flags}, service count {ServiceNameCount}
Microsoft-Windows-HttpService  |  83        |  HTTP Service Channel  |  Channel bind response config overwrites {ReplaceConfigOf}
Microsoft-Windows-HttpService  |  84        |  HTTP Service Channel  |  Policy-Based QoS: Connection {Connection}, FlowHandle {FlowHandle}
Microsoft-Windows-HttpService  |  85        |  HTTP Service Channel  |  Thread pool extension. Pool type: {PoolType}, active pools: {ActivePools}.
Microsoft-Windows-HttpService  |  86        |  HTTP Service Channel  |  Thread ready. Pool type: {PoolType}, active pools: {ActivePools}, thread count: {ThreadCount}
Microsoft-Windows-HttpService  |  87        |  HTTP Service Channel  |  Thread pool trim. Pool type: {PoolType}, active pools: {ActivePools}.
Microsoft-Windows-HttpService  |  88        |  HTTP Service Channel  |  Thread gone. Pool type: {PoolType}, active pools: {ActivePools}, thread count: {ThreadCount}
Microsoft-Windows-HttpService  |  89        |  HTTP Service Channel  |  SNI parsed for connection: {ConnectionObj} with status: {Status}
Microsoft-Windows-HttpService  |  90        |  HTTP Service Channel  |  Request {RequestId} has initated opaque mode
Microsoft-Windows-HttpService  |  91        |  HTTP Service Channel  |  Endpoint auto-generated for {EndpointName}
Microsoft-Windows-HttpService  |  92        |  HTTP Service Channel  |  Deleted auto-generated endpoint for {EndpointName}
Microsoft-Windows-HttpService  |  93        |  HTTP Service Channel  |  Inbound connection for IP: {IpAddress}, SNI: {SniHostname}. SSL endpoint found: {MatchingEndpointName}
Microsoft-Windows-HttpService  |  94        |  HTTP Service Channel  |  SSL connection with local IP address and port {Address} rejected due to configuration policy.
Microsoft-Windows-HttpService  |  95        |  HTTP Service Channel  |  Parsing of response (response ID {ResponseId}) failed due to reason: {Reason}. Request may not be compliant with HTTP/1.1.
Microsoft-Windows-HttpService  |  96        |  System                |  SSL handshake failed. Local IP: {LocalAddress}, Remote IP: {RemoteAddress}, SNI: {SniHostname}, Thumbprint: {Thumbprint}, Client Initiated Disconnect: {ClientDisconnect}, Abortive Disconnect: {AbortiveDisconnect}, Connection Status: {LocalAddressLength}0
Microsoft-Windows-HttpService  |  97        |  System                |  HTTP error response sent. Url: {Url}, Verb: {Verb}, Status Code: {StatusCode}, Cache Send: {CacheSend}, Request Queue: {RequestQueue}, PID: {ProcessId}, TID: {ThreadId}, Image Name: {ImageFileName}, Working Set(Bytes): {WorkingSetSize}, Send Status: {Url}0, Thread Count: {Url}1, Reason Phrase: {Url}2, Error Cause: {Url}3, Verbosity: {Url}4
Microsoft-Windows-HttpService  |  98        |  System                |  SSL renegotiate timed out. Local IP: {LocalAddress}, Remote IP: {RemoteAddress}, SNI: {SniHostname}, Thumbprint: {Thumbprint}, Connection Buffer Full: {ConnectionBufferFull}
Microsoft-Windows-HttpService  |  99        |  System                |  HTTP 11 Required. Verb: {Verb}, Fault Code: {FaultCode}
Microsoft-Windows-HttpService  |  100       |  System                |  Version: {Version} Counts: {CountsLength}
Microsoft-Windows-HttpService  |  101       |  System                |  Version: {Version} Counts: {CountsLength}
Microsoft-Windows-HttpService  |  105       |  HTTP Service Channel  |  QUIC Connection. QuicConnectionId: {QuicConnectionId}, Connection: {Connection}, Local IP: {LocalAddress}, Remote IP: {RemoteAddress}, SNI: {SniHost}, ErrorCode: {ErrorLogCode}, Status: {QuicConnectionId}0
Microsoft-Windows-HttpService  |  106       |  HTTP Service Channel  |  QUIC Connection Callback. Connection: {Connection}, Event: {Event}, EventParam: {EventParam}
Microsoft-Windows-HttpService  |  107       |  HTTP Service Channel  |  QUIC Stream. QuicStreamId: {QuicStreamId}, Connection: {Connection}, Stream: {Stream}
Microsoft-Windows-HttpService  |  108       |  HTTP Service Channel  |  QUIC Stream Callback. Stream: {Stream}, Connection: {Connection}, StreamType: {StreamType}, Event: {Event}, EventParam: {EventParam}
Microsoft-Windows-HttpService  |  109       |  System                |  QUIC Registration Failed. Status: {Status}
Microsoft-Windows-HttpService  |  110       |  HTTP Service Channel  |  Correlation ID for request {RequestId}: {CorrelationId}