Provider                       |  Level        |  Event ID  |  Version  |  Channel  |  Task                           |  Opcode  |  Keyword                    |  Message
-------------------------------|---------------|------------|-----------|-----------|---------------------------------|----------|-----------------------------|---------------------------------------------------------------
Microsoft-Windows-MapControls  |  Information  |  12        |  0        |           |  MosThread-CreateInstance       |  Start   |  Performance Map            |
Microsoft-Windows-MapControls  |  Information  |  13        |  0        |           |  MosThread-CreateInstance       |  Stop    |  Performance Map            |
Microsoft-Windows-MapControls  |  Information  |  14        |  0        |           |  MosThread-InitializeMos        |  Start   |  Performance Map            |
Microsoft-Windows-MapControls  |  Information  |  15        |  0        |           |  MosThread-InitializeMos        |  Stop    |  Performance Map            |
Microsoft-Windows-MapControls  |  Information  |  5001      |  0        |           |  RouterAdapter-Init             |  Start   |  Performance Queries        |
Microsoft-Windows-MapControls  |  Information  |  5002      |  0        |           |  RouterAdapter-Init             |  Stop    |  Performance Queries        |
Microsoft-Windows-MapControls  |  Information  |  5003      |  0        |           |  RouterAdapter-Uninit           |  Start   |  Performance Queries        |
Microsoft-Windows-MapControls  |  Information  |  5004      |  0        |           |  RouterAdapter-Uninit           |  Stop    |  Performance Queries        |
Microsoft-Windows-MapControls  |  Information  |  5005      |  0        |           |  RouterAdapter-CalculateRoute   |          |  Queries                    |  [{Id}] RouterAdapter CalculateRoute
Microsoft-Windows-MapControls  |  Information  |  5006      |  0        |           |  RouterAdapter-CalculateRoute   |  Start   |  Performance Queries        |  [{Id}] RouterAdapter CalculateRoute
Microsoft-Windows-MapControls  |  Information  |  5009      |  0        |           |  RouterAdapter-OnRouteDone      |          |  Queries                    |  [{Id}] RouterAdapter OnRouteDone
Microsoft-Windows-MapControls  |  Information  |  5010      |  0        |           |  RouterAdapter-OnRouteDone      |  Stop    |  Performance Queries        |
Microsoft-Windows-MapControls  |  Information  |  5011      |  0        |           |  RouterAdapter-Cancel           |          |  Performance Queries        |  [{Id}] RouterAdapter Cancel
Microsoft-Windows-MapControls  |  Information  |  5012      |  0        |           |  RouterAdapter-OnRouteProgress  |          |  Queries                    |  [{Id}] RouterAdapter OnRouteProgress
Microsoft-Windows-MapControls  |  Verbose      |  5020      |  0        |           |  Route-Initialize               |          |  Queries                    |  Route Initialize
Microsoft-Windows-MapControls  |  Verbose      |  5021      |  0        |           |  RouteLeg-Initialize            |          |  Queries                    |  RouteLeg Initialize
Microsoft-Windows-MapControls  |  Verbose      |  5022      |  0        |           |  RouteManeuver-Initialize       |          |  Queries                    |  RouteManeuver Initialize
Microsoft-Windows-MapControls  |  Information  |  5023      |  0        |           |  Route-Serialize                |          |  Serialization              |  Route Serialize. [{Hr}]; [{LegCount}]
Microsoft-Windows-MapControls  |  Information  |  5024      |  0        |           |  Route-Deserialize              |          |  Serialization              |  Route Deserialize. [{Hr}]; [{LegCount}]
Microsoft-Windows-MapControls  |  Information  |  5025      |  0        |           |  Route-Serialize                |  Start   |  Performance Serialization  |
Microsoft-Windows-MapControls  |  Information  |  5026      |  0        |           |  Route-Deserialize              |  Stop    |  Performance Serialization  |
Microsoft-Windows-MapControls  |  Information  |  5027      |  0        |           |  Route-Deserialize              |  Start   |  Performance Serialization  |
Microsoft-Windows-MapControls  |  Information  |  5028      |  0        |           |  Route-Deserialize              |  Stop    |  Performance Serialization  |
Microsoft-Windows-MapControls  |  Information  |  11001     |  0        |           |  PointerEvent                   |          |  Touch                      |
Microsoft-Windows-MapControls  |  Information  |  11002     |  0        |           |  PointerEvent                   |          |  Touch                      |
Microsoft-Windows-MapControls  |  Information  |  11003     |  0        |           |  PointerEvent                   |          |  Touch                      |
Microsoft-Windows-MapControls  |  Information  |  11004     |  0        |           |  PointerEvent                   |          |  Touch                      |
Microsoft-Windows-MapControls  |  Information  |  11042     |  0        |           |  JupiterMapOverlay              |          |                             |  [JupiterMapOverlay] UI positioned: ({dipX}; {dipY})
Microsoft-Windows-MapControls  |  Information  |  11043     |  0        |           |  JupiterMapOverlay              |          |                             |  [JupiterMapOverlay] DComp positioned: ({dipX}; {dipY})
Microsoft-Windows-MapControls  |  Information  |  11044     |  0        |           |  JupiterMapOverlay              |          |                             |  [JupiterMapOverlay] Hit test positioned: ({dipX}; {dipY})
Microsoft-Windows-MapControls  |  Information  |  11045     |  0        |           |  JupiterMapOverlay              |  Start   |                             |
Microsoft-Windows-MapControls  |  Information  |  11046     |  0        |           |  JupiterMapOverlay              |  Stop    |                             |
Microsoft-Windows-MapControls  |  Information  |  11047     |  0        |           |  JupiterMapOverlay              |          |                             |
Microsoft-Windows-MapControls  |  Information  |  11048     |  0        |           |  JupiterMapOverlay              |          |                             |
Microsoft-Windows-MapControls  |  Information  |  11049     |  0        |           |  NoOutstandingMapControls       |          |  Map                        |
Microsoft-Windows-MapControls  |  Information  |  13001     |  0        |           |  Map-Authentication             |          |  MapAuthentication          |  [MapAuthentication] SetMapServiceToken_MapControlAPI
Microsoft-Windows-MapControls  |  Information  |  13002     |  0        |           |  Map-Authentication             |          |  MapAuthentication          |  [MapAuthentication] SetServiceToken_HeadlessAPI
Microsoft-Windows-MapControls  |  Information  |  13003     |  0        |           |  Map-Authentication             |          |  MapAuthentication          |  [MapAuthentication] MapsSettings_SetBingMapsKey
Microsoft-Windows-MapControls  |  Information  |  13004     |  0        |           |  Map-Authentication             |          |  MapAuthentication          |  [MapAuthentication] MapsSettings_SetBingAuthenticationKey
Microsoft-Windows-MapControls  |  Information  |  13005     |  0        |           |  Map-Authentication             |          |  MapAuthentication          |  [MapAuthentication] MapsSettings_OnKeyValidationStatusChanged
Microsoft-Windows-MapControls  |  Information  |  13006     |  0        |           |  Map-Finder                     |          |  MapFinder                  |  [MapFinder] StartUnifiedFinderCall