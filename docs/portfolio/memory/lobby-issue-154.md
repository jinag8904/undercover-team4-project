---
name: lobby-issue-154
description: 이슈
metadata: 
  node_type: memory
  type: project
  originSessionId: 437a6c4d-cde6-439a-90c8-69c62b70d323
---

이슈 #154 "로비 구현" (김진아 배정). 게임 시작 전 대기 → 호스트가 시작하면 라운드 시작. 로비는 **별도 씬이 아니라 같은 씬 내**.

**확정 설계 (2026-07-19):**
- **로비 = 플레이 맵 안의 본부(HQ)를 그대로 사용.** 전용 로비 맵은 미정 → 안 만듦.
- 그래서 **`TeleportRpc` 보류(안 만듦)** — 플레이어가 이미 본부에 스폰돼 그 자리에서 게임 시작. 역할별(관제/현장) 위치가 달라 "전원 한 지점 텔레포트" 개념 자체가 안 맞음. 스폰 위치 보정은 기존 `PlayerMovement.ApplyServerSpawnPose`가 처리.
- 게임 시작 트리거는 **독립 `LobbyManager` (MonoBehaviour)** — 사용자가 분리 선택.
- 대기 중 본부 밖 배회는 옵션(a) "허용"(빈 맵이라 무해) → 격리 벽/NavMesh 작업 이번엔 안 함.

**남은 작업:**
- 코드: `LobbyManager` 하나만. 호스트 전용 OnGUI "게임 시작" 버튼 → `RoundManager.StartRound()`. IsServer 가드로 클라 권한 차단. (1단계 RoundManager 자동 시작 제거는 완료)
- 씬/인스펙터: `PlayerSpawnManager.m_spawnPoint` → 본부 스폰 지점. `LobbyManager` 컴포넌트 씬에 추가.

**라운드 종료 후 로비 복귀 (후속 이슈):** 유력 경로는 **A. 세션 유지 + NGO 서버 권위 씬 재로드**(`NetworkManager.Singleton.SceneManager.LoadScene(..., Single)`) — 상태 시스템이 많아(아이템·HP·자금·수배·이벤트) 전부 공짜 리셋되는 A가 인플레이스 리셋(B)보다 견고. A는 텔레포트 불필요. 현재 `RoundEndResetter`(#188)는 세션까지 내리는 하드 리셋이라, "세션 유지 씬 로드"로 바꾸면 A로 진화. 즉시 복귀(로딩 없음)가 꼭 필요할 때만 B + TeleportRpc 국소 추가.

편집은 사용자가 직접 ([[edits-by-user]]). RPC는 신형 `[Rpc(SendTo.Owner)]` 스타일(Scanner.cs). 브랜치 `feature/154-lobby`.
