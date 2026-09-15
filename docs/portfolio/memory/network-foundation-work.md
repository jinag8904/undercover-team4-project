---
name: network-foundation-work
description: "사용자가 맡은 네트워크 기반 구축 작업(#53 로컬 /"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4dfaeda4-80da-4d65-a2b5-afe7dec8b945
---

**▶ 최신 상태 (2026-07-19):** 프로젝트 대폭 진행됨(main #242까지). 네트워크 라이프사이클 설계가 `docs/design/network-lifecycle.md`(사용자 작성)로 정립됨 — auth·session·NGO·Vivox 4계층 소유권/이벤트 규칙. 관련 이슈 진행: #166(단일 소유권, NetworkBootstrap 제거) ✅ / #167(끊김 정규화 OnConnectionLost) ✅ / #168(CanSignOut 게이트) ✅ / **#169(통합 teardown 오케스트레이터) ✅ 완료 — PR #243.** #169 산출물: `Assets/Scripts/Network/SessionTeardown.cs`(LeaveToMainAsync = 세션 LeaveAsync→Vivox LogoutAsync→Auth SignOut 순서, 임시 디버그 GUI 버튼) + VivoxManager.LogoutAsync 공개화(await 완료 보장). 로비(#154) 생기면 그 컨트롤러가 LeaveToMainAsync 호출하도록 바꾸고 임시 클래스 제거 예정. 단일 Play 검증 완료(MPPM은 #154 범위).
**미해결 (별건):** Vivox 채널 참가 시 `ArgumentNullException: accessToken`(VivoxManager.JoinChannelAsync). Settings.json은 #67 당시와 동일(server/domain/issuer 채움·tokenKey 빔). 대시보드 미변경·이 PC서 됐던 이력 있음 → 런타임/세션 토큰 상태 의심. 1순위 시도: Auth GUI "New Player(로그아웃+토큰삭제)"로 세션토큰 초기화 후 재시도. teardown과 무관.
사용자 담당 오픈 이슈(2026-07-19): #234(음성채팅 UI)·#226(본부 미니맵)·#223·#222·#221·#218(플레이어 이름표)·#214(씬 전환 흐름)·#154(로비) 등 다수. (아래 07-12 목록은 구식.)

사용자(김진아 / jinag8904)가 **네트워크 기반 구축**을 전담. GitHub 이슈 두 개 본인에게 할당됨:
- **#53 네트워크 로컬 기반 구축 (NetworkManager + 세션 접속)** — ✅ **완료 (2026-07-10)**. `Assets/Scripts/Network/NetworkBootstrap.cs`(ConnectionMenu 축소판, Server 버튼/분기 제거, `m_networkManager` 컨벤션) + 씬에 NetworkManager+UnityTransport(127.0.0.1:7777)+NetworkBootstrap 부착. MPPM 2인(Host/Client)으로 접속·해제 clientId 로그 + 연결 수 표시 검증 완료.
- **#54 네트워크 온라인 접속 (UGS Relay 세션)** — #53에 의존, 나중. UGS 클라우드 프로젝트 연동 + Relay 활성화 선행 필요.

**현재 상태 (2026-07-10 기준):** #53 완료로 NetworkBootstrap + 씬 NetworkManager 구성됨(위 참조). 패키지: Netcode 2.13.0 / services.multiplayer 2.2.4 / playmode 2.0.2. 플레이어 스크립트(PlayerMovement/PlayerInputHandler/PlayerData)는 싱글 테스트용으로 임시 MonoBehaviour 다운그레이드 + `// TODO: 네트워크 테스트 시 ...` 주석 상태 → 이 복구는 별도 이슈 #51 (담당 이현진 추정).

**#53 진행 순서:**
1. `Assets/Scripts/Network/` 폴더 생성, 최소 `NetworkBootstrap.cs`(학원 ConnectionMenu 축소판 — Host/Client 버튼 + 접속 로그 + Shutdown, OnGUI 임시 UI) 작성.
2. 씬에 빈 GameObject → `NetworkManager` + `Unity Transport`(기본 127.0.0.1) + `NetworkBootstrap` 컴포넌트 부착.
3. Unity Console 컴파일 에러 0 확인.
4. Multiplayer Play Mode로 가상 플레이어 2개 → 한쪽 Host, 한쪽 Client → 접속/해제 clientId 로그 확인 = #53 완료.

**#53 이후 → 첫 동기화 검증 대상은 CCTV(#43, 사용자 담당).** 플레이어 스폰(#51)보다 CCTV가 더 간단한 동기화 예제라 첫 검증에 적합. CCTV를 `NetworkObject` + `NetworkBehaviour`로 만들어 `m_currentIndex`를 서버 권위 `NetworkVariable<int>`로 동기화, `[Rpc(SendTo.Server)]`로 전환 요청, `OnValueChanged`→로컬 `Apply()`. 자세한 설계는 [[cctv-network-sync-design]] 참고.

**사용자 할당 이슈 현황 (2026-07-12 GitHub 재확인 — 이전 07-10 목록 대거 정리됨):** 현재 jinag8904 담당 OPEN은 **#54·#67 둘.** (#43은 2026-07-12 CLOSED)
- **#43 CCTV** — ✅**CLOSED (2026-07-12).** #43-B 상호작용 통합까지 마무리. 상세 [[cctv-network-sync-design]].
- **#54 온라인 접속(UGS Relay)** — OPEN, **UGS 계정·Relay 결정 대기(코드 착수 불가).** ※ 2026-07-12 확인: `ProjectSettings.asset`에 `cloudProjectId: a191c418-5b47-4cb7-a082-1c6a5457d807` / `organizationId: zse846` / `projectName: undercover-team4-project`가 **initial commit부터** 박혀 있음 → UGS 프로젝트 **연동은 이미 돼 있음**(이슈 완료기준 1번 상당 부분 충족). 남은 팀 게이트는 **대시보드 서비스 활성화(Authentication 익명 + Relay)·org zse846 소유자/접근권한 확인·요금(무료티어) 인지**. 코드(AuthBootstrap/SessionManager 재활용)는 사용자 단독 가능.
- **#67 음성 무전(UGS Vivox)** — OPEN, **#54와 동일 UGS 선행 대기.**
- **→ 착수 가능한 담당 이슈는 #43-B 하나. #43-B 끝나면 남은 #54·#67은 둘 다 UGS 게이트라 팀 결정 없이는 막힘.** UGS 무관 대안: **#39 스캔 UI(OPEN·미할당, 착수 가능).**

**정리된 이슈 (07-10 목록 대비 변동):** #52(동기화 계약)·#68(미니맵)·#41(판정)·#56(NPC 서버권위)·#51(플레이어 스폰) 모두 **CLOSED**. #55(아이템 서버권위)→**@HanuYat**, #56→**@suk558165 재할당**(사용자 아님). 즉 아래 07-10 메모의 미니맵/#55/#56/#52 서술은 과거 기록이며 현재 담당/상태와 다름.

**#52 재평가 (2026-07-10):** 원격 브랜치·PR 확인 결과 #42/#38/#40/#41 아무도 미착수 → #52 스켈레톤은 시기상조였음(minimal-core 위배). "매 기능마다 사용자가 스켈레톤 공급"은 사용자 일 아님(독립 기능은 각 담당이 자기 netcode: #51/#55/#56/#43). #52는 삭제 대신 JIT 계약 이슈로 수정 유지(이음새 문제는 실재하나 착수 시점에 정의).

**신설 이슈 (2026-07-10, 이슈 없던 GDD 공백):**
- **#67 전역 음성 무전 (UGS Vivox)** — GDD 4-4 근간 시스템인데 이슈 전무였음. 사용자 할당. 텍스트 채팅은 팀 미논의라 범위 제외(음성만). #54와 동일 UGS 세팅 선행 의존 → 지금 코드 착수 불가, UGS 결정 후.
- **#68 미니맵(본부 기능)** — M1 명시("미니맵+CCTV")인데 CCTV(#43)만 있었음. 미할당. 플레이어 위치 서버권위 동기화 + 본부 UI. UGS 무관이라 **지금 착수 가능**. 사용자가 "본부는 기능이 담긴 장소"라고 정정 → 별도 '본부 존 판정' 시스템 불필요(그 이슈는 안 만듦).
- 지금 사용자가 UGS 없이 바로 할 수 있는 것: **#68 미니맵, #39 스캔 UI.**

**▶ 현재 진행 작업 (2026-07-10): #68 미니맵 — 사용자 착수 결정, 본인 할당됨.**
- **채택 설계 (A안):** CCTV 패턴 재활용. 탑다운 Orthographic 카메라 → RenderTexture(`MinimapRT`) → 본부 데스크 모니터 Quad 머티리얼. `CCTVSwitcher`+`cam1RenderTexture`와 동일 구조. 플레이어가 네트워크 위치 동기화만 돼 있으면 위에서 자동으로 찍힘 → **좌표 변환/블립 계산 코드 불필요.**
- **B안(UI 이미지+아이콘 RectTransform 블립)은 폴리싱으로 보류** (world→UI 매핑+레지스트리 필요, 프로토타입엔 오버).
- **의존성:** 원격 플레이어까지 정확히 찍히려면 플레이어가 NetworkObject+NetworkTransform여야 함 → **#51(이현진) 완료 후.** 미니맵 쪽에서 위치 동기화 따로 안 짬(중복). 지금은 Host 본인 플레이어로 세팅·테스트 가능. → **이현진과 "플레이어에 NetworkTransform 붙는지"만 맞추면 됨.**
- **작업량:** 거의 씬 세팅(카메라 배치·Culling Mask·RT 지정·모니터 Quad 머티리얼). 스크립트는 최소(카메라 중심 맞춤/토글 정도, 없어도 시작 가능). 선택: 플레이어 프리팹에 탑다운 가독성용 컬러 블립 Quad 자식(#51 프리팹 손댈 때).
- **다음 스텝 후보:** ① 씬 세팅 단계별 체크리스트(구체 수치), ② 헬퍼 스크립트 초안(컨벤션 준수), ③ 이현진과 NetworkTransform 확인 포인트. 사용자가 편집 주체([[edits-by-user]]) → Claude는 초안·검증.

**게임플레이 스크립트의 네트워크 전환 커버리지 (2026-07-10 정리):** 기존 게임플레이 코드에 `// TODO: 네트워크 테스트 시 ...` 주석으로 전환 지점이 표시돼 있음. 이슈 매핑:
- 플레이어(Movement/Input/Data) → #51 (담당 이현진)
- 라운드/범인/연행/판정 계약 → **#52 (사용자 재할당됨. 메모리 이전판의 '이현진 담당'은 틀림)**
- CCTV 동기화 → #43 (사용자, 동기화 완료 기준 추가함)
- **아이템(ItemBase/Scanner/Handcuffs) 서버권위 전환 → #55 (신설)** — 원래 담당 이슈 없던 빈 구멍
- **NPC(Controller/StateMachine/AnimationDriver) 서버권위 이동·FSM → #56 (신설)** — 빈 구멍. NpcStateMachine에 이미 `OnStateChanged` 훅 있음, NpcAnimationDriver는 enum→int라 거의 재사용 가능
- #55/#56 모두 `네트워크` 라벨 + #53 의존. NpcStateTester/CCTVSwitchTest는 개발용이라 전환 불필요.

재활용 코드 위치·목록은 [[network-study-reuse]]. 작업 방식 선호는 [[minimal-core-first]], [[edits-by-user]].
