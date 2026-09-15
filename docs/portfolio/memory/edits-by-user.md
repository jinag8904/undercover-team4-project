---
name: edits-by-user
description: 편집 주체는 작업마다 다르다 — 착수 전에 무엇을 할지 먼저 말하고 시작할 것
metadata:
  node_type: memory
  type: feedback
  originSessionId: 8d29c383-738b-48f3-b788-fda5cac1f2d1
  modified: 2026-08-08T16:43:17.494Z
---

편집을 누가 하는지는 작업 성격에 따라 갈린다. **묻지 말고 무조건 손을 떼는 것도, 설명 없이
바로 편집하는 것도 둘 다 틀렸다.**

- 초기(2026-07-09 CitizenProfile)에는 "편집은 제가 할거니까 확인만 해주셈"이라고 요청했다.
- 이후 리팩토링·구현 작업(#503 부품 분리 등)은 Claude가 직접 편집하고 커밋까지 한다
  (커밋에 `Co-Authored-By: Claude` 트레일러가 붙어 있다). Unity Editor 작업(프리팹 배선·
  씬 수정)만 사용자 몫이다.

**Why:** 2026-08-08 #503 작업에서 설명 없이 편집부터 시작했다가 "뭐하는건지 말하고 좀 해주실래요"로
중단당했다. 문제는 편집한 것 자체가 아니라 **착수 전 설명이 없었던 것**이다.

**How to apply:** 착수 전에 산출물·커밋 단위·사용자 몫을 짧게 먼저 말한다([[explain-deliverable-per-step]]).
그다음 편집한다. Unity Editor가 필요한 단계(프리팹·씬·`.meta`)는 사용자에게 넘기고 검증 방법을 함께 준다 —
프로젝트 설정이 `Write(./**/*.meta)`·`Write(./**/*.unity)`를 막아 둔 것도 같은 경계다.
관련: [[short-comments-preferred]] · [[csharpier-format-hook]]
