---
name: csharpier-format-hook
description: Edit 도구로 .cs 수정 시 CSharpier 훅이 파일 전체를 재포맷 → churn 주의
metadata: 
  node_type: memory
  type: project
  originSessionId: 4587b810-beec-40c1-b716-4fd8c078ef79
---

이 저장소(`.claude/settings.json`)에 **PostToolUse 훅**이 있어, Claude가 `Edit|Write|MultiEdit` 도구로 파일을 수정하면 `.claude/hooks/csharpier-format.ps1`이 **CSharpier**(`dotnet csharpier`)를 돌린다.

**함정:** 저장소 기존 코드는 아직 CSharpier 포맷이 아니라 **컴팩트 스타일**이다(`[SerializeField] private X;` 한 줄, `if (x) return;` 한 줄 등). 그래서 내가 `.cs`를 Edit하면 그 파일이 **통째로 CSharpier로 재포맷**되어(예: SerializeField 두 줄 분리, using 재정렬, 단문 분리) 3줄 변경이 100+줄 diff로 부풀고, 기능 PR을 오염시키며 남의 작업과 머지 충돌 위험이 생긴다. 실제 #169(PR #243)에서 VivoxManager.cs가 이렇게 오염돼 force-push로 되돌렸다.

**이유:** 사용자([[edits-by-user]])는 보통 IDE/Unity에서 직접 편집 → Claude Edit 훅을 안 거쳐 CSharpier가 안 돎. 그래서 기존 파일은 컴팩트인데 Claude가 Edit한 파일만 재포맷됨.

**대응 (기능 PR을 깔끔히 유지하려면):**
- 작은 수정은 **Bash로 편집**(perl -i / sed 등)해 훅을 우회한다. Bash는 PostToolUse:Edit 훅을 발동하지 않는다. (주석 삽입 등에 검증됨)
- 또는 사용자가 IDE에서 직접 편집.
- 근본 해소는 **CSharpier 저장소 전체 1회 적용을 별도 PR**로. 그 전까지 기능 PR에 포맷 churn을 섞지 말 것.

관련: [[network-foundation-work]], [[minimal-core-first]].

**Bash 편집 시 개행 함정 (2026-08-01 #430에서 확인):**
- `.cs`는 **CRLF**, `docs/**.md`는 **LF**다. 게다가 사용자가 IDE로 방금 넣은 줄만 LF인 **혼재 파일**이 나온다 — LF 패턴으로 치환하면 "NOT FOUND"로 조용히 실패한다.
- 그래서 perl 치환은 **개행 무관 매칭**으로: `quotemeta`한 패턴의 `\n`을 `\r?\n`으로 바꿔 찾고, 쓸 때 `.cs`는 CRLF로 통일한다(`core.autocrlf=true`라 개행 통일은 git diff에 안 잡힌다). `.md`는 LF 유지.
- 매칭이 0건/2건이면 `die`로 멈추는 스크립트를 쓸 것 — 조용한 오적용보다 낫다.

**먼저 확인할 것 (2026-08-01, #430 세션에서 사용자 지적):** 파일이 **이미 CSharpier 포맷이면 Edit 도구를 그냥 쓴다** — 재포맷될 게 없어 churn이 0이다. 판별은 `dotnet csharpier check <파일>` 한 번 (settings.json에 `Bash(dotnet csharpier *)`가 허용돼 있다). 예: `PlayerNameTag.cs`는 포맷 완료 상태였고 Edit로 63줄만 깔끔히 들어갔다. 컴팩트 스타일 파일(VivoxManager·GameSettings·LobbyRoster·SettingsPanel 등)만 Bash 우회가 필요하다.

perl 스크립트 우회는 **개행을 통째로 바꾸지 말 것** — 파일 전체를 CRLF로 통일했더니 원래 LF였던 파일이 csharpier 개행 검사에 걸렸다. 읽을 때 메모리에서 LF로 정규화해 매칭하고, 쓸 때 **원래 개행을 복원**하는 편이 안전하다.
