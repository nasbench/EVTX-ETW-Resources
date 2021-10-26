Provider            |  Level        |  Event ID  |  Version  |  Channel  |  Task  |  Opcode  |  Keyword           |  Message
--------------------|---------------|------------|-----------|-----------|--------|----------|--------------------|----------------------------------------------------------------------------------
DptfCpuEtwProvider  |               |  0         |  0        |           |        |          |                    |  {stringPtr}
DptfCpuEtwProvider  |  Information  |  100       |  0        |           |        |  Start   |  ApiTrace Windows  |  INFO: ISR Start,  Interrupt = {Interrupt}, MessageID = {MessageID}
DptfCpuEtwProvider  |  Information  |  101       |  0        |           |        |  Stop    |  ApiTrace Windows  |  INFO: ISR End,  Status = {Status}
DptfCpuEtwProvider  |               |  102       |  0        |           |        |          |  Windows           |  DEBUG: {String}
DptfCpuEtwProvider  |  Error        |  103       |  0        |           |        |          |  Windows           |  ERROR: {String}
DptfCpuEtwProvider  |  Warning      |  104       |  0        |           |        |          |  Windows           |  WARN: {String}
DptfCpuEtwProvider  |  Information  |  105       |  0        |           |        |          |  Windows           |  INFO: {String}
DptfCpuEtwProvider  |  Information  |  106       |  0        |           |        |          |  Windows           |  INFO: {String}, Status = {Status}
DptfCpuEtwProvider  |  Information  |  107       |  0        |           |        |          |  ApiTrace Windows  |  INFO: DPC Start, Interrupt = {Interrupt}, Associated Object = {AssociatedObject}
DptfCpuEtwProvider  |  Information  |  108       |  0        |           |        |  Stop    |  ApiTrace Windows  |
DptfCpuEtwProvider  |  Information  |  109       |  0        |           |        |          |  Windows           |  INFO: {String}, Data = {Status}