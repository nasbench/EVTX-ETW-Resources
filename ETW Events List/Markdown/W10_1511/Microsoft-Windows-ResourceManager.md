Provider                           |  Event ID  |  Channel  |  Message
-----------------------------------|------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Microsoft-Windows-ResourceManager  |  100       |           |  Resource Enforcer Set Apply Status={FuncHr}, ProcessId={ProcessId}, Priority={Priority}, CpuReserve={CpuReserve}, CpuHardLimit={HardCpuLimit}, FreezeProcess={FreezeProcess}, MemoryLimit={MemoryLimit}, NoCpuReservation={NoCpuReservation}
Microsoft-Windows-ResourceManager  |  103       |           |  Resource Enforcer Message, Flags={Flags}, ProcessId={ProcessId}, ProcessCommit={ProcessCommit}
Microsoft-Windows-ResourceManager  |  105       |           |  Resource Enforcer NT Error, Function={FuncName}, Line={Line}, NTSTATUS Error={FuncStatus}
Microsoft-Windows-ResourceManager  |  106       |           |  Resource Swap Job, Status={Status}, ProcessId={ProcessId}, JobHandle={JobHandle}
Microsoft-Windows-ResourceManager  |  107       |           |  Resource Empty Process, Win32 Code={ErrorCode}, ProcessId={ProcessId}, Flags={Flags}
Microsoft-Windows-ResourceManager  |  108       |           |
Microsoft-Windows-ResourceManager  |  400       |           |
Microsoft-Windows-ResourceManager  |  401       |           |
Microsoft-Windows-ResourceManager  |  402       |           |
Microsoft-Windows-ResourceManager  |  403       |           |
Microsoft-Windows-ResourceManager  |  404       |           |
Microsoft-Windows-ResourceManager  |  405       |           |
Microsoft-Windows-ResourceManager  |  406       |           |  Resource Manager: Low Memory Handler: Terminating pid {IntVal}.
Microsoft-Windows-ResourceManager  |  407       |           |
Microsoft-Windows-ResourceManager  |  408       |           |  Resource Manager: SHTerminateProcessForOOM pid={IntVal1} cbAllocation={IntVal2} fReboot={IntVal3}.
Microsoft-Windows-ResourceManager  |  409       |           |  Resource Manager: Low Memory Handler: Commit memory is low. Rebooting. Commit=[{CommitUsage}] CommitPeak=[{PeakCommitUsage}] CommitLimit=[{CommitLimit}] SharedCommit=[{SharedCommit}] NonPagedPool=[{NonPagedPool}] PagedPool=[{PagedPool}]
Microsoft-Windows-ResourceManager  |  410       |           |
Microsoft-Windows-ResourceManager  |  411       |           |
Microsoft-Windows-ResourceManager  |  412       |           |  Resource Manager: Process being applied is already dead - PID={IntVal}
Microsoft-Windows-ResourceManager  |  413       |           |  Resource Manager: ApplyResourceSet - pResSet={pResSet}, HR={hr}, MemLimit={memLimit}, PriorityClass={priorityClass}, PID={pid}, Type={type}, Terminal={terminal}
Microsoft-Windows-ResourceManager  |  414       |           |  Resource Manager: UnapplyResourceSet - pResSet={pResSet}, HR={hr}, PID={pid}, Type={type}, Terminal={terminal}
Microsoft-Windows-ResourceManager  |  415       |           |  Resource Manager: OnProcessTerminated - PID={IntVal}
Microsoft-Windows-ResourceManager  |  416       |           |  Resource Manager: OnProcessCommitWarning - PID={pid}, HR={hr}, cbCommit={cbCommit}
Microsoft-Windows-ResourceManager  |  417       |           |  Resource Manager: TerminateProcessForOom - PID={pid}, cbFailed={cbFailed}, fReboot={fReboot}
Microsoft-Windows-ResourceManager  |  418       |           |  Resource Manager: ResourceSet::CreateInstance - pResSet={pResSet}, HR={hr}, Type={type}, Pending={fBool}
Microsoft-Windows-ResourceManager  |  419       |           |  Resource Manager: ReleaseResources - pResSet={pResSet}, HR={hr}, Type={type}, Terminal={fBool}
Microsoft-Windows-ResourceManager  |  420       |           |  Resource Manager: Low Memory Handler: NeedCommit={p4_Boolean}
Microsoft-Windows-ResourceManager  |  421       |           |  Resource Manager: Low Memory Handler: NeedPhysical={p4_Boolean}
Microsoft-Windows-ResourceManager  |  422       |           |  Resource Manager: Low Memory Handler: NeedNonPagedPool={p4_Boolean}
Microsoft-Windows-ResourceManager  |  423       |           |  Resource Manager: Low Memory Handler: NeedMemory={p1_Boolean}, NeedCommit={p2_Boolean}, NeedPhysical={p3_Boolean}, NeedNonPagedPool={p4_Boolean}
Microsoft-Windows-ResourceManager  |  424       |           |
Microsoft-Windows-ResourceManager  |  426       |           |  Resource Manager: AcquireResourceSet - pResSet={pResSet}, HR={hr}, Type={type}, Pending={fBool}, Previous={pPreviousResSet}
Microsoft-Windows-ResourceManager  |  428       |           |  Resource Manager: AcquireResources - cRequests={cRequests}, priority={priority}, cmsAcquireDelay={cmsAcquireDelay}, pidRequesting={pidRequesting}, fForcePending={fForcePending}, pendtype={pendtype}, HR={hr}
Microsoft-Windows-ResourceManager  |  435       |           |  External Resource Manager: RegisterResources - ResourceType={ResourceType}, Amount={p1_UINT32}, HR={HRESULT}
Microsoft-Windows-ResourceManager  |  436       |           |  External Resource Manager: RMAccessCheck - ResourceType={ResourceType}, PID={p1_UINT32}, HR={HRESULT}
Microsoft-Windows-ResourceManager  |  437       |           |  External Resource Manager: AcquireResources_ServerThunk - pResourceHandle={pResourceHandle}, cRequests={cRequests}, priority={priority}, callerPid={callerPid}, pidRequesting={pidRequesting}, grfFlags={grfFlags}, pendtype={pendtype}, fPending={fPending}, HR={hr}
Microsoft-Windows-ResourceManager  |  438       |           |  External Resource Manager: RMAvailabilityCheck - cRequests={cRequests}, priority={priority}, pidRequesting={pidRequesting}, HR={hr}
Microsoft-Windows-ResourceManager  |  439       |           |  External Resource Manager: RMGetNotification - pResourceHandle={pResourceHandle}, HR={hr}
Microsoft-Windows-ResourceManager  |  440       |           |  External Resource Manager: RMReleaseResources_Manager - pResourceHandle={pResourceHandle}, HR={hr}
Microsoft-Windows-ResourceManager  |  441       |           |  External Resource Manager: RMQueueMessages - pResourceHandle={pResourceHandle}, ExternalNotificationType={ExternalNotificationType}, ResourceType={ResourceType}, ReleaseReason={ReleaseReason}, HR={hr}
Microsoft-Windows-ResourceManager  |  442       |           |  Resource Manager: Block resource set ({p2_RSType}) for product {p1_String} with mask {p3_UInt32} block({p4_Boolean}), HR={p5_UInt32}
Microsoft-Windows-ResourceManager  |  443       |           |  Resource Manager: Can Block resource set ({p2_RSType}) for product {p1_String} with mask {p3_UInt32} block({p4_Boolean}), HR={p5_UInt32}
Microsoft-Windows-ResourceManager  |  444       |           |  Resource Manager: Check and Revoke resource set for product {p1_String} revoke({p2_Boolean}), HR={p3_UInt32}
Microsoft-Windows-ResourceManager  |  445       |           |  Resource Manager: Check and Revoke resource set for PFM {p1_String}
Microsoft-Windows-ResourceManager  |  446       |           |  Resource Manager: Check and Revoke resource set by type for PFM {p1_String}({p2_UInt32}), HR={p3_UInt32}
Microsoft-Windows-ResourceManager  |  447       |           |  Resource Manager: OnApplicationTerminated - PSMKey={p1_String}, ActivationType={p2_UInt32}
Microsoft-Windows-ResourceManager  |  448       |           |  Resource Manager: ReclaimMemory - pResSet={pResSet}, HR={hr}
Microsoft-Windows-ResourceManager  |  449       |           |  External Resource Manager: Watchdog Expired. pResourceHandle={pResourceHandle}, App PID={pidRequesting}
Microsoft-Windows-ResourceManager  |  450       |           |  Resource Manager: AcquireAdditionalResources - pResSet={pResSet}, Cpu={CPU}, Mem={RAM}, Io={IO}, HR={hr}, Pending={Pending}, TempRS={TempRS}
Microsoft-Windows-ResourceManager  |  451       |           |  Resource Manager: CompleteAcquireAdditionalResources - pResSet={p1_Pointer}, TempRS={p2_Pointer}
Microsoft-Windows-ResourceManager  |  452       |           |  Resource Manager: RevokeResources - PSMKey={p1_String}, ActivationType={p2_UInt32}
Microsoft-Windows-ResourceManager  |  453       |           |  Resource Manager: MemoryLimitNotification - PSMKey={PsmKey}, Sid={UserSid}, Session={SessionId}, ActivationType={HostJobType}, PrivUsage={Commit}, SharedUsage={SharedCommit}, Adjustment={CommitAdjustment}, Cap={PsmKey}0, LowLimit={NotificationLowLimit}, HighLimit={NotificationHighLimit}
Microsoft-Windows-ResourceManager  |  454       |           |  Resource Manager: ForceReleaseExternalResources - PID={p1_PID}
Microsoft-Windows-ResourceManager  |  455       |           |  Resource Manager: Acquiring Memory for FG sharing. FG Resource Set = {pResSet}, Amount = {Amount}, HR = {hr}
Microsoft-Windows-ResourceManager  |  456       |           |  Resource Manager: Releasing Memory for FG sharing. FG Resource Set = {pResSet}, Amount = {Amount}, HR = {hr}
Microsoft-Windows-ResourceManager  |  457       |           |  Resource Manager: Host terminated due to quota exhaustion - PSMKey={p1_String} ActivationType={p2_UInt32}
Microsoft-Windows-ResourceManager  |  458       |           |  Resource Manager: Failed to transition FG memory sharing. New Resource Set = {pResSet}, HR = {hr}
Microsoft-Windows-ResourceManager  |  459       |           |  Resource Manager: ModernResourceEnforcer failed! - PSMKey={p1_String}, ActivationType={p2_UInt32}  HR = {p3_UInt32}
Microsoft-Windows-ResourceManager  |  461       |           |  Resource Manager: OnAcquired - pResSet={ResourceSet}, IsLegacy={IsLegacy}, CallbackId={CallbackId} HR={HRESULT}
Microsoft-Windows-ResourceManager  |  462       |           |  Resource Manager: MemoryLimitNotification - PSMKey={PsmKey}, ActivationType={UserSid}, Sid={SessionId}, Session={HostJobType}, Cap={CommitCap}, LowLimit={NotificationLowLimit}, HighLimit={NotificationHighLimit}, HR={hr}
Microsoft-Windows-ResourceManager  |  463       |           |  Resource Manager: TerminateModernAppForOOM PSMKey={PsmKey}, UserSid={UserSid}, SessionId={SessionId}, ActivationType={HostJobType}, AllocationSize={FailedAllocationSize}, ShouldReboot={RebootDecision}  HR={hr}
Microsoft-Windows-ResourceManager  |  464       |           |  Resource Manager: RevokeResources - pResSet={pResSet}, PID={pid}
Microsoft-Windows-ResourceManager  |  465       |           |  Resource Manager: ReleaseTerminal - pResSet={p1_Pointer} PID={p2_PID} Product={p3_String} ActivationType={p4_ActType} HR={p5_HRESULT}
Microsoft-Windows-ResourceManager  |  466       |           |  Resource Manager: UnapplyResourceSet_Modern - pResSet={pResSet}, HR={hr}
Microsoft-Windows-ResourceManager  |  467       |           |
Microsoft-Windows-ResourceManager  |  468       |           |
Microsoft-Windows-ResourceManager  |  469       |           |
Microsoft-Windows-ResourceManager  |  470       |           |  Resource Manager: ApplyResourceSet - pResSet={pResSet}, HR={hr}, MemLimit={memLimit}, PriorityClass={priorityClass}, PID={pid}, Type={type}, Terminal={terminal}
Microsoft-Windows-ResourceManager  |  471       |           |  Resource Manager: AcquireAdditionalResources - pResSet={pResSet}, Mem={RAM}, HR={hr}, Pending={Pending}, TempRS={TempRS}
Microsoft-Windows-ResourceManager  |  472       |           |  Resource Manager: MemoryLimitNotification - PSMKey={PsmKey}, Sid={UserSid}, Session={SessionId}, ActivationType={HostJobType}, PrivUsage={Commit}, SharedUsage={SharedCommit}, Adjustment={CommitAdjustment}, Cap={PsmKey}0, LowLimit={NotificationLowLimit}, HighLimit={NotificationHighLimit}
Microsoft-Windows-ResourceManager  |  473       |           |  Resource Manager: Acquiring Memory for FG sharing. FG Resource Set = {pResSet}, Amount = {Amount}, HR = {hr}
Microsoft-Windows-ResourceManager  |  474       |           |  Resource Manager: Releasing Memory for FG sharing. FG Resource Set = {pResSet}, Amount = {Amount}, HR = {hr}
Microsoft-Windows-ResourceManager  |  550       |           |  PsmServiceExtHost: Failed in call to BiTerminateApplicationHost - Status={p0_UInt32}, PsmKey={p1_UnicodeString}, HostJobType={p2_UInt32}, Action={p3_UInt32}, Force={p4_Boolean}
Microsoft-Windows-ResourceManager  |  8199      |           |  [Info]: {p1_String}
Microsoft-Windows-ResourceManager  |  8200      |           |  Modern Enforcer: Failed to call SetApplicationProperties - Status={Status}, PsmKey={PsmKey}, User={UserSid}, Session={SessionId}, HostJobType={HostJobType}: ({Status}1, {Status}2, {Status}3, {Status}4, {Status}5) - CpuRate={CpuRate}, HardMemoryLimit={HardMemoryLimit}, NotifyMemoryLowLimit={NotifyMemoryLowLimit}, NotifyMemoryHighLimit={NotifyMemoryHighLimit}, Priority={Status}0
Microsoft-Windows-ResourceManager  |  8201      |           |  Modern Enforcer: Failed to call QueryApplicationProperties - Status={Status}, PsmKey={PsmKey}, User={UserSid}, Session={SessionId}, HostJobType={HostJobType}, CpuRate={CpuRate}, HardMemoryLimit={HardMemoryLimit}, NotifyMemoryLowLimit={NotifyMemoryLowLimit}, NotifyMemoryHighLimit={NotifyMemoryHighLimit}, Priority={Status}0
Microsoft-Windows-ResourceManager  |  8202      |           |  Modern Enforcer: Failed to call QueryMemoryUsage - Status={Status}, PsmKey={PsmKey}, User={UserSid}, Session={SessionId}, HostJobType={HostJobType}, MemoryUsage={MemoryUsage}
Microsoft-Windows-ResourceManager  |  8203      |           |  Modern Enforcer: Failed to call QuerySharedCommit- Status={Status}, PsmKey={PsmKey}, User={UserSid}, Session={SessionId}, HostJobType={HostJobType}, SharedMemoryUsage={MemoryUsage}
Microsoft-Windows-ResourceManager  |  8204      |           |  Modern Enforcer: SetApplicationProperties - Status={Status}, PsmKey={PsmKey}, User={UserSid}, Session={SessionId}, HostJobType={HostJobType}: ({Status}1, {Status}2, {Status}3, {Status}4, {Status}5) - CpuRate={CpuRate}, HardMemoryLimit={HardMemoryLimit}, NotifyMemoryLowLimit={NotifyMemoryLowLimit}, NotifyMemoryHighLimit={NotifyMemoryHighLimit}, Priority={Status}0
Microsoft-Windows-ResourceManager  |  8205      |           |  Modern Enforcer: QueryApplicationProperties - Status={Status}, PsmKey={PsmKey}, User={UserSid}, Session={SessionId}, HostJobType={HostJobType}, CpuRate={CpuRate}, HardMemoryLimit={HardMemoryLimit}, NotifyMemoryLowLimit={NotifyMemoryLowLimit}, NotifyMemoryHighLimit={NotifyMemoryHighLimit}, Priority={Status}0
Microsoft-Windows-ResourceManager  |  8210      |           |  Modern Enforcer: PSM GroupOwnershipNotification - Status={Status}, PsmKey={PsmKey}, User={UserSid}, Session={SessionId}, HostJobType={HostJobType}, {AcquireRelease}, fUpdateRate={UpdateRate}
Microsoft-Windows-ResourceManager  |  8211      |           |  Modern Enforcer: PSM HostEmpty Notification - PsmKey={PsmKey}, User={UserSid}, Session={SessionId}, HostJobType={HostJobType}
Microsoft-Windows-ResourceManager  |  8212      |           |  Modern Enforcer: PsmApplicationStateNotification - User={UserSid}, Session={SessionId}, PsmKey={PsmKey}, State={State}
Microsoft-Windows-ResourceManager  |  8213      |           |  Modern Enforcer: PsmHostStateNotification - User={UserSid}, Session={SessionId}, PsmKey={PsmKey}, HostJobType={HostJobType}, State={State}
Microsoft-Windows-ResourceManager  |  8214      |           |  Modern Enforcer: SwapModernApplication - Status={Status}, PsmKey={PsmKey}, User={UserSid}, Session={SessionId}
Microsoft-Windows-ResourceManager  |  8215      |           |  Modern Enforcer: EmptyModernApplication - Status={Status}, PsmKey={PsmKey}, User={UserSid}, Session={SessionId}, ProcessId={ProcessId}, EmptyFlags={EmptyFlags}