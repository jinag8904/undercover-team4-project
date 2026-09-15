---
name: parallel-git-ops
description: User runs git operations (checkout/pull/merge) in parallel during a session — re-check branch state before git commands
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 686f9a5e-a1f6-45ea-893f-072c59643f6e
---

사용자는 세션 도중 GitHub/로컬에서 직접 git 작업을 한다 (main으로 checkout, pull, PR 웹에서 머지 등). Claude가 브랜치에 있다고 가정하고 작업하는 사이에 브랜치가 바뀌어 있을 수 있다.

**Why:** 2026-07-10 미니맵 PR 작업 중, Claude가 feature 브랜치에 있다고 착각하고 `git commit --amend`를 실행했으나 사용자가 이미 main으로 checkout + pull(PR #71 머지분 반영)한 상태여서, amend 커밋이 main에 얹히는 사고 발생. `git reset --hard origin/main`으로 복구함.

**How to apply:** `commit --amend` / `reset` / `push` 같이 되돌리기 어려운 git 명령 전에는 반드시 `git branch --show-current`와 `git status`로 현재 브랜치·상태를 재확인한다. 브랜치명에서 이슈 번호를 추측하지 말고 `gh issue view`로 검증한다 (이번에 branch `feature/28-minimap`의 28이 실제로는 무관한 아이템 PR이었고 미니맵은 #68이었음). 관련: [[edits-by-user]]
