Provider                             |  Event ID  |  Channel      |  Message
-------------------------------------|------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-Kerberos-KdcProxy  |  1         |  Operational  |  Service stopped with a failure: error code {ErrorCode}
Microsoft-Windows-Kerberos-KdcProxy  |  2         |  Operational  |  Failed to initialize Group Policy: error code {ErrorCode}
Microsoft-Windows-Kerberos-KdcProxy  |  3         |  Operational  |  Failed to read Group Policy: error code {ErrorCode}
Microsoft-Windows-Kerberos-KdcProxy  |  4         |  Operational  |  Failed to start the HTTP service: error code {ErrorCode}
Microsoft-Windows-Kerberos-KdcProxy  |  5         |  Operational  |  Service failed to register UrlPrefix {UrlPrefix}: error code {ErrorCode}. Contact your administrator to make sure {UrlPrefix} is properly reserved.
Microsoft-Windows-Kerberos-KdcProxy  |  6         |  Operational  |  Service failed to start because system is not domain-joined: error code {ErrorCode}.
Microsoft-Windows-Kerberos-KdcProxy  |  100       |  Operational  |  HttpReceiveHttpRequest API failed to receive an HTTP request from the network: error code {ErrorCode}. This may indicate a failure where no future HTTP requests can be received by the service.
Microsoft-Windows-Kerberos-KdcProxy  |  101       |  Operational  |  Service failed to create a new IO object to service an HTTP request from the network: error code {ErrorCode}. This may indicate a failure where no future HTTP requests can be received by the service.
Microsoft-Windows-Kerberos-KdcProxy  |  102       |  Operational  |  Failed to unpack {PduType}: error code {ErrorCode}
Microsoft-Windows-Kerberos-KdcProxy  |  103       |  Operational  |  Failed to locate a domain controller in domain {TargetDomain} with locator flags {Flags}: error code {ErrorCode}.
Microsoft-Windows-Kerberos-KdcProxy  |  200       |  Operational  |  Retry ({RetryNumber}) connection to KDC in {TargetDomain}
Microsoft-Windows-Kerberos-KdcProxy  |  300       |  Operational  |
Microsoft-Windows-Kerberos-KdcProxy  |  301       |  Operational  |
Microsoft-Windows-Kerberos-KdcProxy  |  302       |  Operational  |
Microsoft-Windows-Kerberos-KdcProxy  |  303       |  Operational  |
Microsoft-Windows-Kerberos-KdcProxy  |  304       |  Operational  |
Microsoft-Windows-Kerberos-KdcProxy  |  305       |  Operational  |
Microsoft-Windows-Kerberos-KdcProxy  |  306       |  Operational  |  Rediscover KDC for domain {TargetDomain}
Microsoft-Windows-Kerberos-KdcProxy  |  307       |  Operational  |  Hash table was expanded from ({BeginNonEmptyBuckets}/{BeginTotalBuckets} buckets, {BeginTotalEntries} entries) to ({NonEmptyBuckets}/{TotalBuckets} buckets, {TotalEntries} entries) in {TimeSpent} milliseconds
Microsoft-Windows-Kerberos-KdcProxy  |  308       |  Operational  |  Hash table was contracted from ({BeginNonEmptyBuckets}/{BeginTotalBuckets} buckets, {BeginTotalEntries} entries) to ({NonEmptyBuckets}/{TotalBuckets} buckets, {TotalEntries} entries) in {TimeSpent} milliseconds
Microsoft-Windows-Kerberos-KdcProxy  |  309       |  Operational  |  Rediscovered KDC {KDCAddress}({KDCName}) for domain {TargetDomain}
Microsoft-Windows-Kerberos-KdcProxy  |  400       |  Operational  |
Microsoft-Windows-Kerberos-KdcProxy  |  401       |  Operational  |
Microsoft-Windows-Kerberos-KdcProxy  |  402       |  Operational  |  Client certificate is not valid to establish an HTTP connection: trust status {TrustStatus}
Microsoft-Windows-Kerberos-KdcProxy  |  403       |  Operational  |  The account (Domain: {DomainName}, User: {UserName}) has {NumerOfFailures} password failures. It is locked out for the next {LockedOutPeriod} seconds
Microsoft-Windows-Kerberos-KdcProxy  |  404       |  Operational  |  The account (Domain: {DomainName}, User: {UserName}) is rejected due to the usage of an unarmored Kerberos message