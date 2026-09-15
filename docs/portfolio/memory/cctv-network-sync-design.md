---
name: cctv-network-sync-design
description: CCTV 화면 전환을 멀티플레이 동기화하는 설계(NetworkVariable + Rpc)
metadata: 
  node_type: memory
  type: project
  originSessionId: 4dfaeda4-80da-4d65-a2b5-afe7dec8b945
---

CCTV 모니터(#43, 사용자 담당)에서 **누가 화면 전환을 눌러도 모든 클라이언트 화면이 같이 바뀌게** 하는 동기화 설계. 현재 `Assets/Scripts/CCTV/CCTVSwitcher.cs`는 로컬 `MonoBehaviour`라 각자 로컬에서만 바뀜.

**핵심 원칙:** "몇 번 카메라인지"(인덱스)만 동기화하고, 실제 카메라 렌더링/RenderTexture 적용은 각 클라 로컬. RenderTexture·카메라 렌더는 원래 로컬 시각 처리라 네트워크로 보낼 필요 없음.

**설계:**
- `CCTVSwitcher`를 `NetworkBehaviour`로. 모니터 오브젝트에 `NetworkObject` 필요(프리팹이면 `DefaultNetworkPrefabs.asset` 등록, 씬 배치면 자동 스폰).
- `m_currentIndex`를 서버 권위 `NetworkVariable<int>`(Read=Everyone, Write=Server).
- 상호작용 → `[Rpc(SendTo.Server)]` 로 전환 요청(소유권 불필요; 모니터 앞 아무나). 서버가 `m_currentIndex.Value` 갱신.
- `m_currentIndex.OnValueChanged` → 모든 클라에서 로컬 `Apply()`(선택된 카메라만 targetTexture=RT, 나머지 enabled=false).
- **`OnNetworkSpawn`에서 `Apply()` 1회 호출** — OnValueChanged는 값이 바뀔 때만 불려서, 늦게 접속한 사람은 현재 값으로 한 번 그려줘야 함. 기존 `Start()=>Apply()`는 제거.
**#43 두 단계로 분리 (2026-07-10 확정):** 이슈에 동기화와 상호작용 통합이 묶여 있으나 성격이 다름. 동기화는 트리거(무엇이 전환을 쏘는지)와 무관하므로 분리해서 진행:
- **1단계 (동기화, #43-A) — ✅완료 (2026-07-10, PR #62 머지).** 위 설계대로 NetworkBehaviour/NetworkVariable/RPC 구현. 트리거는 기존 `CCTVSwitchTest`(Q/E) 임시 유지하되 `RequestSwitchNextRpc/PrevRpc`(SendTo.Server) 호출로 변경. MPPM 2인 동기화 + 늦은 접속 화면 일치 검증 완료.
- **2단계 (상호작용 통합, #43-B) — ✅완료. #43 이슈 CLOSED (2026-07-12).** 런타임 무반응 원인이던 모니터 오브젝트 Layer(`Interactable`) 설정으로 해결된 것으로 보임(사용자 마무리 보고). **#5(IInteractable, 담당 이현진) ✅완료·PR #69 머지** → 더 이상 대기 아님. 구현 방법 확정: `CCTVSwitcher`가 `IInteractable`을 **직접 구현**(별도 컴포넌트 X, minimal-core) → `Interact(GameObject)`에서 기존 `RequestSwitchNextRpc()` 호출. 트리거만 Q/E→상호작용으로 교체, #43-A RPC 입구는 영구 유지.
  - **정리 대상:** 씬 모니터에서 `CCTVSwitchTest` 컴포넌트 제거 후 `CCTVSwitchTest.cs`(+`.meta`) 삭제. 단발 E라 도달 못 하는 `RequestSwitchPrevRpc()`도 삭제 권장(UI 생기면 부활).
  - **씬 세팅:** 모니터(=CCTVSwitcher+NetworkObject)나 자식에 Collider 부착. `PlayerInteractor`가 `GetComponentInParent<IInteractable>()`로 찾음. **실제 Player.prefab 값: `m_range=5`, `m_interactMask`는 `~0`이 아니라 `Interactable` 레이어(7)만 (m_Bits=128).** → **콜라이더 붙은 오브젝트가 반드시 `Interactable` 레이어여야 레이가 잡힘.** (레이어명: 0 Default…6 OwnBody, 7 Interactable)
  - **상호작용 시스템 사실관계:** `PlayerInteractor`(NetworkBehaviour, 오너만 활성)가 카메라 레이캐스트 → `OnInteractPerformed`(=Interact/E) 시 `CurrentInteractable.Interact(gameObject)` **로컬 호출**. CCTV는 그 안에서 서버 RPC 쏨. Interact가 단발이든 홀드든 CCTV는 performed에 반응만 하므로 입력 스킴 결정에 안 막힘.

**#43-B 진행 상태 (2026-07-12 갱신):**
- **코드 편집 완료·정상.** `CCTVSwitcher : NetworkBehaviour, IInteractable` + `public void Interact(GameObject interactor) => RequestSwitchNextRpc();`. `RequestSwitchPrevRpc()`는 단발 E라 주석 처리됨. (파일: `Assets/Scripts/CCTV/CCTVSwitcher.cs`)
- **씬 정리·통합 완료 (작업 트리 기준, 미커밋).** `CCTVSwitchTest.cs`(+meta) 삭제됨. `CCTVSwitcher`+`NetworkObject`를 별도 빈 오브젝트에서 **`CCTVMonitor`로 이설** → 콜라이더와 같은 오브젝트. `CCTV.unity`에서 `PlayerPrefab`도 이제 지정됨(예전 `fileID:0`).
- **코드+씬 정합 검증 완료 (정적 분석):** ②모니터 MeshCollider(enabled, 큐브) 있음 / ③콜라이더가 스위처와 같은 오브젝트 → `GetComponentInParent<IInteractable>` 성립 / 플레이어 스폰됨(PlayerPrefab 지정) / ⑥`m_cameras` 3개·RT 할당 / Interact 액션은 Hold 없는 순수 Button(`<Keyboard>/e`)이라 **E 탭에 `performed` 발동**(PlayerInputHandler "Hold 3초" 주석은 실제 설정과 불일치, 무해). 초기 "E 전환 안 됨"은 씬 수정 전(PlayerPrefab=0, 스위처가 콜라이더 없는 별도 오브젝트) 탓으로 판단.
- **런타임 검증 (2026-07-12): E 눌러도 무반응·로그 없음.** 근본 원인 = **모니터 오브젝트 레이어 미설정.** `PlayerInteractor.m_interactMask`가 `Interactable`(7)만 감지하는데 `CCTVMonitor`가 그 레이어가 아니라 레이가 통과 → `CurrentInteractable=null`. **수정: `CCTVMonitor`(콜라이더 오브젝트) Layer를 `Interactable`로.** 코드 변경 불필요. (`m_camera`는 프리팹에 이미 할당돼 있어 카메라는 원인 아니었음.)
- **진단법(실패 시):** 임시 `Debug.Log` 2개 — `PlayerInteractor.HandleInteract`(target/interactable) + `CCTVSwitcher.Interact`(IsSpawned). 로그 안 뜸=①/⑤, `interactable=null`=조준/사거리, `Interact 수신`=RPC/인덱스.

**주의:** `m_monitorRt`는 공유 애셋. 한 씬에 CCTV 모니터가 여러 개면 같은 RT 공유 시 충돌 → 모니터별 별도 RT 또는 런타임 생성.

**의존성:** #53(네트워크 로컬 기반) ✅완료. CCTV가 #53 이후 **첫 동기화 검증 대상**. 전체 흐름은 [[network-foundation-work]]. 작업 방식은 [[minimal-core-first]].
