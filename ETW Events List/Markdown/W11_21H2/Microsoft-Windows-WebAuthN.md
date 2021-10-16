Provider                    |  Event ID  |  Channel  |  Message
----------------------------|------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-WebAuthN  |  1000      |           |  WebAuthN Ctap MakeCredential started.TransactionId: {TransactionId}
Microsoft-Windows-WebAuthN  |  1001      |           |  WebAuthN Ctap MakeCredential completed.TransactionId: {TransactionId}
Microsoft-Windows-WebAuthN  |  1002      |           |  WebAuthN Ctap MakeCredential completed.TransactionId: {TransactionId}Error: {Error}. {HResult}
Microsoft-Windows-WebAuthN  |  1003      |           |  WebAuthN Ctap GetAssertion started.TransactionId: {TransactionId}
Microsoft-Windows-WebAuthN  |  1004      |           |  WebAuthN Ctap GetAssertion completed.TransactionId: {TransactionId}
Microsoft-Windows-WebAuthN  |  1005      |           |  WebAuthN Ctap GetAssertion completed.TransactionId: {TransactionId}Error: {Error}. {HResult}
Microsoft-Windows-WebAuthN  |  1006      |           |  WebAuthN Ctap SendCommand started.TransactionId: {TransactionId}Ticket: {Ticket}
Microsoft-Windows-WebAuthN  |  1007      |           |  WebAuthN Ctap SendCommand completed.TransactionId: {TransactionId}
Microsoft-Windows-WebAuthN  |  1008      |           |  WebAuthN Ctap SendCommand completed.TransactionId: {TransactionId}Error: {Error}. {HResult}
Microsoft-Windows-WebAuthN  |  1020      |           |  WebAuthN Ngc MakeCredential started.TransactionID: {TransactionId}
Microsoft-Windows-WebAuthN  |  1021      |           |  WebAuthN Ngc MakeCredential completed.TransactionID: {TransactionId}
Microsoft-Windows-WebAuthN  |  1022      |           |  WebAuthN Ngc MakeCredential completed.TransactionID: {TransactionId}Error: {Error}. {HResult}
Microsoft-Windows-WebAuthN  |  1023      |           |  WebAuthN Ngc GetAssertion started.TransactionID: {TransactionId}
Microsoft-Windows-WebAuthN  |  1024      |           |  WebAuthN Ngc GetAssertion completed.TransactionID: {TransactionId}
Microsoft-Windows-WebAuthN  |  1025      |           |  WebAuthN Ngc GetAssertion completed.TransactionID: {TransactionId}Error: {Error}. {HResult}
Microsoft-Windows-WebAuthN  |  1040      |           |  Ngc MakeCredential request.TransactionID: {TransactionId}RpID: {RpId}AccountID: {AccountId}ClientDataHashAlgID: {ClientDataHashAlgId} ClientDataLength: {ClientDataLength} ClientDataHash: {ClientDataHash}ExcludeCredentialCount: {CredentialCount}CredentialParameterCount: {CredentialParameterCount}
Microsoft-Windows-WebAuthN  |  1041      |           |  Ngc MakeCredential response.TransactionID: {TransactionId}AttestationFormatType: {AttestationFormatType}RpIDHash: {RpIdHash}Flags: {Flags}SignCount: {SignCount}AAGuid: {AAGuid}CredentialID: {CredentialId}U2fPublicKey: {TransactionId}0PublicKey: {TransactionId}2Response: {TransactionId}4
Microsoft-Windows-WebAuthN  |  1042      |           |  Ngc GetAssertion request.TransactionID: {TransactionId}RpID: {RpId}ClientDataHashAlgID: {ClientDataHashAlgId} ClientDataLength: {ClientDataLength} ClientDataHash: {ClientDataHash}AllowCredentialCount: {CredentialCount}
Microsoft-Windows-WebAuthN  |  1043      |           |  Ngc GetAssertion response.TransactionID: {TransactionId}RpIDHash: {RpIdHash}Flags: {Flags}SignCount: {SignCount}CredentialID: {CredentialId}%
Microsoft-Windows-WebAuthN  |  1060      |           |  WebAuthN error at: {Action}TransactionID: {TransactionId}Error: {Error}. {HResult}
Microsoft-Windows-WebAuthN  |  1100      |           |  Cbor decode error.TransactionId: {TransactionId}Function: {Function}CborError: {CborError} {CborErrorString}ErrorOffset: {ErrorOffset} LineNumber: {LineNumber}Encoded: {Encoded}
Microsoft-Windows-WebAuthN  |  1101      |           |  Cbor encode MakeCredential request.TransactionId: {TransactionId}RpId: {RpId}UserId: {UserId}ClientDataHashAlgId: {ClientDataHashAlgId} ClientDataLength: {ClientDataLength} ClientDataHash: {ClientDataHash}RequireResidentKey: {RequireResidentKey}ExcludeCredentialCount: {TransactionId}0CredentialParameterCount: {TransactionId}1Request: {TransactionId}3
Microsoft-Windows-WebAuthN  |  1102      |           |  Cbor decode MakeCredential response.TransactionId: {TransactionId}AttestationFormatType: {AttestationFormatType}RpIdHash: {RpIdHash}Flags: {Flags}SignCount: {SignCount}AAGuid: {AAGuid}CredentialId: {CredentialId}U2fPublicKey: {TransactionId}0PublicKey: {TransactionId}2Response: {TransactionId}4
Microsoft-Windows-WebAuthN  |  1103      |           |  Cbor encode GetAssertion request.TransactionID: {TransactionId}RpID: {RpId}ClientDataHashAlgID: {ClientDataHashAlgId} ClientDataLength: {ClientDataLength} ClientDataHash: {ClientDataHash}AllowCredentialCount: {CredentialCount}Request: {Request}
Microsoft-Windows-WebAuthN  |  1104      |           |  Cbor decode GetAssertion response.TransactionId: {TransactionId}RpIdHash: {RpIdHash}Flags: {Flags}SignCount: {SignCount}CredentialId: {CredentialId}Response: {Response}
Microsoft-Windows-WebAuthN  |  2000      |           |
Microsoft-Windows-WebAuthN  |  2001      |           |
Microsoft-Windows-WebAuthN  |  2100      |           |  Ctap {Command} started.TransactionId: {TransactionId}Flags: {Flags}TimeoutMilliseconds: {TimeoutMilliseconds}Ticket: {Ticket}Request: {Request}
Microsoft-Windows-WebAuthN  |  2101      |           |  Ctap command started.Request: {Request}
Microsoft-Windows-WebAuthN  |  2102      |           |  Ctap {Command} completed.TransactionId: {TransactionId}Response: {Response}
Microsoft-Windows-WebAuthN  |  2103      |           |  Ctap {Command} completed.TransactionId: {TransactionId}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2104      |           |  Ctap device info.TransactionId: {TransactionId}ProviderName: {ProviderName}DevicePath: {DevicePath}Manufacturer: {Manufacturer}Product: {Product}AAGuid: {AAGuid}U2fProtocol: {U2fProtocol}
Microsoft-Windows-WebAuthN  |  2105      |           |  Ctap Function: {Function} Location: {Location}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2106      |           |  Ctap Name: {Name} Value: {Value}
Microsoft-Windows-WebAuthN  |  2110      |           |  Ctap device device state info.Transport Type: {Transport}WnfState: {WnfState}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2111      |           |  Ctap device change notify info.  Transport Type:{Transport}
Microsoft-Windows-WebAuthN  |  2200      |           |  Ctap Usb provider thread started.TransactionId: {TransactionId}
Microsoft-Windows-WebAuthN  |  2201      |           |  Ctap Usb provider thread completed.TransactionId: {TransactionId}
Microsoft-Windows-WebAuthN  |  2202      |           |  Ctap Usb provider thread completed.TransactionId: {TransactionId}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2203      |           |  Ctap Usb provider thread completed.TransactionId: {TransactionId}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2210      |           |  Ctap Usb device thread started.TransactionId: {TransactionId}DevicePath: {DevicePath}Manufacturer: {Manufacturer}Product: {Product}
Microsoft-Windows-WebAuthN  |  2211      |           |  Ctap Usb device thread completed.TransactionId: {TransactionId}DevicePath: {DevicePath}Manufacturer: {Manufacturer}Product: {Product}AAGuid: {AAGuid}U2fProtocol: {U2fProtocol}
Microsoft-Windows-WebAuthN  |  2212      |           |  Ctap Usb device thread completed.TransactionId: {TransactionId}DevicePath: {DevicePath}Manufacturer: {Manufacturer}Product: {Product}AAGuid: {AAGuid}U2fProtocol: {U2fProtocol}State: {State}Status: {Status}Error: {Error}. {TransactionId}0
Microsoft-Windows-WebAuthN  |  2213      |           |  Ctap Usb device thread completed.TransactionId: {TransactionId}DevicePath: {DevicePath}Manufacturer: {Manufacturer}Product: {Product}AAGuid: {AAGuid}U2fProtocol: {U2fProtocol}State: {State}Status: {Status}Error: {Error}. {TransactionId}0
Microsoft-Windows-WebAuthN  |  2220      |           |  Ctap Usb add device.TransactionId: {TransactionId}DevicePath: {DevicePath}Manufacturer: {Manufacturer}Product: {Product}
Microsoft-Windows-WebAuthN  |  2221      |           |  Ctap Usb remove device.TransactionId: {TransactionId}DevicePath: {DevicePath}Manufacturer: {Manufacturer}Product: {Product}
Microsoft-Windows-WebAuthN  |  2222      |           |  Ctap Usb device changes.TransactionId: {TransactionId}
Microsoft-Windows-WebAuthN  |  2223      |           |  Ctap Usb U2F device.TransactionId: {TransactionId}DevicePath: {DevicePath}Manufacturer: {Manufacturer}Product: {Product}
Microsoft-Windows-WebAuthN  |  2224      |           |  Ctap Usb connect to device.TransactionId: {TransactionId}DevicePath: {DevicePath}Manufacturer: {Manufacturer}Product: {Product}DeviceErr: {DeviceErr}Status: {Status}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2225      |           |  Ctap Usb Send Receive:TransactionID: {TransactionId}Request Command: {RequestCommand} Response Command: {ResponseCommand}Request: {Request}Response: {Response}
Microsoft-Windows-WebAuthN  |  2226      |           |  Ctap Usb Send Receive:TransactionID: {TransactionId}Request Command: {RequestCommand} Response Command: {ResponseCommand}Request: {Request}Response: {Response}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2250      |           |  Ctap Ble provider thread started. TransactionId: {TransactionId}
Microsoft-Windows-WebAuthN  |  2251      |           |  Ctap Ble provider thread completed. TransactionId: {TransactionId}
Microsoft-Windows-WebAuthN  |  2252      |           |  Ctap Ble provider thread completed. TransactionId: {TransactionId}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2253      |           |  Ctap Ble provider thread completed. TransactionId: {TransactionId}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2260      |           |  Ctap Ble device thread started. TransactionId: {TransactionId}DevicePath: {DevicePath}PairedName: {PairedName}
Microsoft-Windows-WebAuthN  |  2261      |           |  Ctap Ble device thread completed. TransactionId: {TransactionId}DevicePath: {DevicePath}PairedName: {PairedName}AAGuid: {AAGuid}U2fProtocol: {U2fProtocol}
Microsoft-Windows-WebAuthN  |  2262      |           |  Ctap Ble device thread completed. TransactionId: {TransactionId}DevicePath: {DevicePath}PairedName: {PairedName}AAGuid: {AAGuid}U2fProtocol: {U2fProtocol}State: {State}Status: {Status}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2263      |           |  Ctap Ble device thread completed. TransactionId: {TransactionId}DevicePath: {DevicePath}PairedName: {PairedName}AAGuid: {AAGuid}U2fProtocol: {U2fProtocol}State: {State}Status: {Status}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2270      |           |  Ctap Ble Function: {Function} Location: {Location}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2271      |           |  Ctap Ble U2F device. TransactionId: {TransactionId}DevicePath: {DevicePath}PairedName: {PairedName}
Microsoft-Windows-WebAuthN  |  2272      |           |  Ctap Ble Send Receive:TransactionId: {TransactionId}Request Command: {RequestCommand} Response Command: {ResponseCommand}Request: {Request}Response: {Response}
Microsoft-Windows-WebAuthN  |  2273      |           |  Ctap Ble Send Receive:TransactionId: {TransactionId}Request Command: {RequestCommand} Response Command: {ResponseCommand}Request: {Request}Response: {Response}Location: {Location}Error: {Error}. {TransactionId}0
Microsoft-Windows-WebAuthN  |  2300      |           |  Ctap Nfc provider thread started.TransactionID: {TransactionId}
Microsoft-Windows-WebAuthN  |  2301      |           |  Ctap Nfc provider thread completed.TransactionID: {TransactionId}
Microsoft-Windows-WebAuthN  |  2302      |           |  Ctap Nfc provider thread completed.TransactionID: {TransactionId}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2303      |           |  Ctap Nfc provider thread completed.TransactionID: {TransactionId}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2310      |           |  Ctap Nfc reader thread started.TransactionID: {TransactionId}Reader: {Reader}
Microsoft-Windows-WebAuthN  |  2311      |           |  Ctap Nfc reader thread completed.TransactionID: {TransactionId}Reader: {Reader}AAGuid: {AAGuid}U2fProtocol: {U2fProtocol}
Microsoft-Windows-WebAuthN  |  2312      |           |  Ctap Nfc reader thread completed.TransactionID: {TransactionId}Reader: {Reader}AAGuid: {AAGuid}U2fProtocol: {U2fProtocol}State: {State}Status: {Status}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2313      |           |  Ctap Nfc reader thread completed.TransactionID: {TransactionId}Reader: {Reader}AAGuid: {AAGuid}U2fProtocol: {U2fProtocol}State: {State}Status: {Status}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2314      |           |  Ctap Nfc reader manager thread started.TransactionId: {TransactionId}
Microsoft-Windows-WebAuthN  |  2315      |           |  Ctap Nfc reader manager thread completed.TransactionId: {TransactionId}NumberOfTimesScardCancelCommandsSent: {NumberOfTimesScardCancelCommandsSent}
Microsoft-Windows-WebAuthN  |  2316      |           |  Cancelling Reader Threads.TransactionId: {TransactionId}
Microsoft-Windows-WebAuthN  |  2320      |           |  Ctap Nfc add reader.TransactionID: {TransactionId}Reader: {Reader}
Microsoft-Windows-WebAuthN  |  2321      |           |  Ctap Nfc skip reader for: {Action}.TransactionID: {TransactionId}Reader: {Reader}DeviceInstanceID: {DeviceInstanceId}
Microsoft-Windows-WebAuthN  |  2322      |           |  Ctap Nfc transition reader for: {Action}.TransactionID: {TransactionId}Reader: {Reader}
Microsoft-Windows-WebAuthN  |  2323      |           |  Ctap Nfc send message warning for: {Action}.TransactionID: {TransactionId}Reader: {Reader}ApduStatus: {ApduStatus}DeviceStatus: {DeviceStatus}SmartCardError: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2324      |           |  Ctap Nfc send request error for: {Action}.TransactionID: {TransactionId}Reader: {Reader}ApduStatus: {ApduStatus}DeviceStatus: {DeviceStatus}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2325      |           |  Ctap Nfc U2F device.TransactionID: {TransactionId}Reader: {Reader}
Microsoft-Windows-WebAuthN  |  2326      |           |  Ctap Nfc send message at: {Action}.TransactionID: {TransactionId}Reader: {Reader}
Microsoft-Windows-WebAuthN  |  2327      |           |  Ctap Nfc SCardTransmit Request:TransactionID: {TransactionId}Reader: {Reader}Request: {RequestLength} bytes{Request}Response data: {ResponseLength} bytes{Response}Apdu Status: {ApduStatus}
Microsoft-Windows-WebAuthN  |  2328      |           |  Ctap Nfc SCardTransmit Request:TransactionID: {TransactionId}Reader: {Reader}Request: {RequestLength} bytes{Request}Response data: {ResponseLength} bytes{Response}Apdu Status: {ApduStatus}Error: {Error}. {Win32Error}
Microsoft-Windows-WebAuthN  |  2400      |           |  Ctap Test provider thread started.TransactionId: {TransactionId}
Microsoft-Windows-WebAuthN  |  2401      |           |  Ctap Test provider thread completed.TransactionId: {TransactionId}
Microsoft-Windows-WebAuthN  |  2402      |           |  Ctap Test provider thread completed.TransactionId: {TransactionId}Error: {Error}. {Win32Error}