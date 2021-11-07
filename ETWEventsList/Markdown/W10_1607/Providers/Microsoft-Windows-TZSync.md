Provider                  |  Level        |  Event ID  |  Version  |  Channel      |  Task                 |  Opcode  |  Keyword  |  Message
--------------------------|---------------|------------|-----------|---------------|-----------------------|----------|-----------|--------------------------------------------------
Microsoft-Windows-TZSync  |  Information  |  1         |  0        |  Operational  |                       |  Start   |           |
Microsoft-Windows-TZSync  |  Information  |  2         |  0        |  Operational  |                       |  Stop    |           |
Microsoft-Windows-TZSync  |  Information  |  3         |  0        |  Analytic     |  Initialization task  |  Start   |           |
Microsoft-Windows-TZSync  |  Information  |  4         |  0        |  Analytic     |  Initialization task  |  Stop    |           |
Microsoft-Windows-TZSync  |  Information  |  5         |  0        |  Analytic     |  Conversion task      |  Start   |           |
Microsoft-Windows-TZSync  |  Information  |  6         |  0        |  Analytic     |  Conversion task      |  Stop    |           |
Microsoft-Windows-TZSync  |  Information  |  7         |  0        |  Analytic     |  Conversion task      |  Start   |           |  Conversion started for Time Zone: {TimeZoneId}
Microsoft-Windows-TZSync  |  Information  |  8         |  0        |  Analytic     |  Conversion task      |  Stop    |           |  Conversion completed for Time Zone: {TimeZoneId}
Microsoft-Windows-TZSync  |  Error        |  9         |  0        |  Operational  |  Initialization task  |          |           |
Microsoft-Windows-TZSync  |  Error        |  10        |  0        |  Operational  |  Conversion task      |          |           |  Error in conversion for Time Zone: {TimeZoneId}
Microsoft-Windows-TZSync  |  Error        |  11        |  0        |  Operational  |  Conversion task      |          |           |
Microsoft-Windows-TZSync  |  Error        |  12        |  0        |  Operational  |                       |          |           |