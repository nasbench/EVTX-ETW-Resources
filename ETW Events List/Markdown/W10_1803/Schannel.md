Provider  |  Event ID  |  Channel  |  Message
----------|------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Schannel  |  36864     |  System   |
Schannel  |  36865     |  System   |  A fatal error occurred while opening the system {ModuleName} cryptographic module. Operations that require the SSL or TLS cryptographic protocols will not work correctly. The error code is {Error}.
Schannel  |  36867     |  System   |  Creating a TLS {Type} credential.
Schannel  |  36868     |  System   |  The TLS {Type} credential's private key has the following properties:   CSP name: {CSPName}   CSP type: {CSPType}   Key name: {KeyName}   Key Type: {KeyType}   Key Flags: {KeyFlags} The attached data contains the certificate.
Schannel  |  36869     |  System   |  The TLS {Type} credential's certificate does not have a private key information property attached to it. This most often occurs when a certificate is backed up incorrectly and then later restored. This message can also indicate a certificate enrollment failure.
Schannel  |  36870     |  System   |  A fatal error occurred when attempting to access the TLS {Type} credential private key. The error code returned from the cryptographic module is {ErrorCode}. The internal error state is {ErrorStatus}.
Schannel  |  36871     |  System   |  A fatal error occurred while creating a TLS {Type} credential. The internal error state is {ErrorState}.
Schannel  |  36872     |  System   |  The TLS {Type} specified certificate's chain could not be retrieved:   Failure Status: {ErrorCode}   Flags: {CertFlags} The attached data contains the certificate.
Schannel  |  36873     |  System   |
Schannel  |  36874     |  System   |  An {Protocol} connection request was received from a remote client application, but none of the cipher suites supported by the client application are supported by the server. The TLS connection request has failed.
Schannel  |  36875     |  System   |
Schannel  |  36876     |  System   |  The certificate received from the remote server has not validated correctly. The error code is {ErrorCode}. The TLS connection request has failed. The attached data contains the server certificate.
Schannel  |  36877     |  System   |  The certificate received from the remote client application has not validated correctly. The error code is {ErrorCode}. The attached data contains the client certificate.
Schannel  |  36878     |  System   |  The certificate received from the remote client application is not suitable for direct mapping to a client system account, possibly because the authority that issuing the certificate is not sufficiently trusted. The error code is {ErrorCode}. The attached data contains the client certificate.
Schannel  |  36879     |  System   |  The certificate received from the remote client application was not successfully mapped to a client system account. The error code is {ErrorCode}. This is not necessarily a fatal error, as the server application may still find the certificate acceptable.
Schannel  |  36880     |  System   |  A TLS {Type} handshake completed successfully. The negotiated cryptographic parameters are as follows.   Protocol version: {Protocol}   CipherSuite: {CipherSuite}   Exchange strength: {ExchangeStrength} bits   Context handle: {ContextHandle}   Target name: {TargetName}   Local certificate subject name: {LocalCertSubjectName}   Remote certificate subject name: {RemoteCertSubjectName}
Schannel  |  36881     |  System   |  The certificate received from the remote server has either expired or is not yet valid. The TLS connection request has failed. The attached data contains the server certificate.
Schannel  |  36882     |  System   |  The certificate received from the remote server was issued by an untrusted certificate authority. Because of this, none of the data contained in the certificate can be validated. The TLS connection request has failed. The attached data contains the server certificate.
Schannel  |  36883     |  System   |  The certificate received from the remote server has been revoked. This means that the certificate authority that issued the certificate has invalidated it. The TLS connection request has failed. The attached data contains the server certificate.
Schannel  |  36884     |  System   |  The certificate received from the remote server does not contain the expected name. It is therefore not possible to determine whether we are connecting to the correct server. The server name we were expecting is {Name}. The TLS connection request has failed. The attached data contains the server certificate.
Schannel  |  36885     |  System   |
Schannel  |  36886     |  System   |
Schannel  |  36887     |  System   |  A fatal alert was received from the remote endpoint. The TLS protocol defined fatal alert code is {AlertDesc}.
Schannel  |  36888     |  System   |  A fatal alert was generated and sent to the remote endpoint. This may result in termination of the connection. The TLS protocol defined fatal alert code is {AlertDesc}.   Target name: {TargetName}The TLS alert registry can be found at http://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml#tls-parameters-6
Schannel  |  36889     |  System   |  The TLS {Type} specified certificate's chain is incomplete:   Failure Status: {ErrorCode} This can cause trust validation failures or interoperability problems. For more information see KB 954755 The attached data contains the certificate.
Schannel  |  36896     |  System   |
Schannel  |  36897     |  System   |
Schannel  |  36898     |  System   |
Schannel  |  36899     |  System   |
Schannel  |  36912     |  System   |  The key material used to protect TLS Session Tickets was not found at {Path}.