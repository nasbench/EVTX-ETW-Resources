Provider                                             |  Level        |  Event ID  |  Version  |  Channel    |  Task  |  Opcode  |  Keyword  |  Message
-----------------------------------------------------|---------------|------------|-----------|-------------|--------|----------|-----------|------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  10        |  0        |  Admin      |        |          |           |  Configuring ProvXML with category '{Message1}'.ProvXML data:{Message2}
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  11        |  0        |  Admin      |        |          |           |  ProvXML category '{Message1}' completed successfully. {Message2}
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  12        |  0        |  Admin      |        |          |           |  ProvXML category '{Message1}' failed with '{HRESULT}' at CSP node '{Message2}'. {Message3}
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  20        |  0        |  Admin      |        |          |           |  Applying package '{Message1}' ID: {Message2}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  21        |  0        |  Admin      |        |          |           |  Package '{Message1}' has completed.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  22        |  0        |  Admin      |        |          |           |  Package '{Message1}' failed with '{HRESULT}'.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  30        |  0        |  Admin      |        |          |           |  Initiating provisioning turn '{Int1}'.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  31        |  0        |  Admin      |        |          |           |  Provisioning turn '{Int1}' has completed.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  32        |  0        |  Admin      |        |          |           |  Provisioning turn '{Int1}' failed with '{HRESULT}'.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Warning      |  40        |  0        |  Admin      |        |          |           |  Registry specified search path is invalid: {Message1}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Warning      |  100       |  0        |  AutoPilot  |        |          |           |  AutoPilot policy [{Message1}] not found.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  101       |  0        |  AutoPilot  |        |          |           |  AutoPilotGetPolicyDwordByName succeeded:  policy name = {Message1}; policy value = {Int1}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  102       |  0        |  AutoPilot  |        |          |           |  AutoPilotGetPolicyDwordByName error:  policy name = {Message1}; HRESULT = {HRESULT}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  103       |  0        |  AutoPilot  |        |          |           |  AutoPilotGetPolicyStringByName succeeded:  policy name = {Message1}; policy value = {Message2}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  104       |  0        |  AutoPilot  |        |          |           |  AutoPilotGetPolicyStringByName error:  policy name = {Message1}; HRESULT = {HRESULT}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  105       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  106       |  0        |  AutoPilot  |        |          |           |  AutoPilotDisable error:  HRESULT = {HRESULT}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  107       |  0        |  AutoPilot  |        |          |           |  AutoPilot state = {Message1}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  108       |  0        |  AutoPilot  |        |          |           |  AutoPilotIsDisabled error:  HRESULT = {HRESULT}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  109       |  0        |  AutoPilot  |        |          |           |  AutoPilotGetOobeSettingsOverride succeeded:  OOBE setting = {Message1}; state = {Message2}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  110       |  0        |  AutoPilot  |        |          |           |  AutoPilotGetOobeSettingsOverride error:  OOBE setting = {Message1}; HRESULT = {HRESULT}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  111       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  112       |  0        |  AutoPilot  |        |          |           |  AutoPilotRetrieveSettings error:  HRESULT = {HRESULT}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  113       |  0        |  AutoPilot  |        |          |           |  AutoPilot reported the DLL was unloaded while there were {Int1} outstanding calls.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  114       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  150       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  151       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  152       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  153       |  0        |  AutoPilot  |        |          |           |  AutoPilotManager reported the state changed from {InitialState} to {UpdateState}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  154       |  0        |  AutoPilot  |        |          |           |  AutoPilotManager failed to start MSA service.  HRESULT = {HRESULT}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  155       |  0        |  AutoPilot  |        |          |           |  AutoPilotManager failed to start TPM task.  HRESULT = {HRESULT}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  156       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  160       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  161       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  162       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  163       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  164       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Warning      |  165       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  166       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  167       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  168       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  169       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  170       |  0        |  AutoPilot  |        |          |           |
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  171       |  0        |  AutoPilot  |        |          |           |  AutoPilotManager failed to set TPM identity confirmed.  HRESULT = {HRESULT}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  172       |  0        |  AutoPilot  |        |          |           |  AutoPilotManager failed to set AutoPilot profile as available.  HRESULT = {HRESULT}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  173       |  0        |  AutoPilot  |        |          |           |  AutoPilotManager failed to register for network availability.  HRESULT = {HRESULT}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  174       |  0        |  AutoPilot  |        |          |           |  AutoPilotManager failed to register for device identity availability.  HRESULT = {HRESULT}
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  175       |  0        |  AutoPilot  |        |          |           |  AutoPilotManager failed to register for device identity task update.  HRESULT = {HRESULT}
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  300       |  0        |  AutoPilot  |        |          |           |  AutoPilotManager device enrollment reported an initialization failure.  HRESULT = {HRESULT}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  301       |  0        |  AutoPilot  |        |          |           |  AutoPilotManager device enrollment reported a blocking failure.  Overall error {HRESULT}; last reported stage {State}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Error        |  302       |  0        |  AutoPilot  |        |          |           |  AutoPilotManager device enrollment failed during stage {State} with error {HRESULT}.
Microsoft-Windows-Provisioning-Diagnostics-Provider  |  Information  |  303       |  0        |  AutoPilot  |        |          |           |  AutoPilotManager device enrollment succeeded.  Last valid stage: {State}.