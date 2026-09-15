---
name: network-study-reuse
description: 재활용 가능한 학원 실습 네트워크 코드 위치와 파일별 용도
metadata: 
  node_type: memory
  type: reference
  originSessionId: 4dfaeda4-80da-4d65-a2b5-afe7dec8b945
---

사용자의 학원 실습 프로젝트에 우리 프로젝트와 **동일 패키지 버전**(Netcode 2.13.0 / services.multiplayer 2.2.4)으로 작성된 네트워크 뼈대가 있음. 컨벤션(`m_`, UniTask)도 우리 CLAUDE.md 규칙과 일치해 거의 그대로 재활용 가능.

**경로:** `C:\Users\hamme\Projects\unity-network-study-jinag8904\Assets\Scripts\`

**파일별 용도:**
- `ConnectionMenu.cs` — NetworkManager `StartHost/StartClient/StartServer` + OnGUI. **#53 로컬 기반의 핵심.** (전용 Server 버튼·장황한 상태 표시는 빼고 축소해서 쓰기)
- `RPCDemo.cs` — `[Rpc(SendTo.Server)]` / `[Rpc(SendTo.ClientsAndHost)]` 최신 RPC 패턴 예제. **복사 말고 참고만** (CCTV 동기화 만들 때 패턴 참조).
- `AuthBootstrap.cs` — UGS 익명 로그인. **#54용.**
- `SessionManager.cs` — Relay 세션 생성/코드참가/QuickJoin (`.WithRelayNetwork()`). **#54 권장.**
- `RelayBootstrap.cs` — 저수준 Relay join코드 방식(UnityTransport.SetRelayServerData). SessionManager의 대안. **#54용.**

사용 계획은 [[network-foundation-work]] 참고.
