---
name: mcp-unity-registration
description: Unity(Coplay MCP for Unity) 서버를 Claude Code에 등록하는 법과 스코프 함정
metadata: 
  node_type: memory
  type: reference
  originSessionId: 407988e0-352f-44d4-aa88-f660c27e52ce
---

프로젝트에 **MCP for Unity(`com.coplaydev.unity-mcp`, Coplay)** 설치돼 있고, Editor의 "Configure Detected Clients"로 클라이언트 자동 구성 가능. 서버는 **로컬 HTTP/WebSocket** 방식 — 엔드포인트 `http://127.0.0.1:8080/mcp` (Editor에서 서버 켜져 있어야 포트 LISTENING).

**함정 (2026-07-12 겪음):** Coplay의 "Configure"는 `claude mcp add`를 실행하는데, **실행 시 cwd 기준 local 스코프**로 등록돼서 **엉뚱한 프로젝트에 들어갈 수 있음**. 실제로 `undercover-team4-project`가 아니라 `C:/Users/hamme/Github/minigame-project-jinag8904` 스코프에 등록돼 이 프로젝트 세션에서 Unity 도구가 안 잡혔음. `~/.claude.json`의 top-level `mcpServers`엔 `GitHub`만 있었고, `projects.<minigame>.mcpServers`에 `UnityMCP`가 있었음.

**해결:** 별도 터미널(실행 중 세션이 종료 때 `~/.claude.json`을 덮어쓸 수 있어 세션 밖에서)에서:
```
claude mcp add --scope user --transport http UnityMCP http://127.0.0.1:8080/mcp
```
`--scope user`면 모든 프로젝트에서 쓰여 스코프 함정 재발 없음. 그 후 **Claude Code 완전 종료→재시작**(MCP는 세션 시작 시 로드).

**확인법:** `~/.claude.json`에서 top-level 또는 현재 프로젝트 `mcpServers`에 `UnityMCP` 있는지. 포트 살아있는지 `127.0.0.1:8080` 소켓 연결. 도구는 `ToolSearch`로 `read_console`/`manage_gameobject`/`manage_scene`/`editor_state`/`run_tests` 검색.

**현재 상태 (2026-07-12 확인):** `~/.claude.json` top-level `mcpServers`엔 여전히 `GitHub`만. `UnityMCP`는 **local(project) 스코프로 두 프로젝트**(`minigame-project-jinag8904`, `undercover-team4-project`)에 등록됨 — 즉 `--scope user`는 결국 안 썼고, 이 프로젝트 로컬 스코프에 직접 들어가 있음. `claude mcp list`(이 프로젝트 cwd에서) → `UnityMCP ✔ Connected`(8080 살아있음). **함정 해소됨.** 남은 유일 이슈는 세션 시작 시점에 서버가 없으면 도구가 그 세션에 안 실림 → **Claude Code 완전 종료→이 프로젝트에서 재시작**하면 로드됨(재등록 불필요).

등록되면 CCTV #43-B 디버깅([[cctv-network-sync-design]])에서 씬·콘솔 직접 확인에 사용.
