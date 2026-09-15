---
name: pr-review-automation
description: PR 리뷰는 자동화된 Claude 리뷰 + 사용자 본인이 직접 코드 검토 — /pr-review 제안 금지
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2e23a04f-4a5b-43f1-92d5-e3591b0c330c
---

PR을 열면 **자동화된 Claude 리뷰가 GitHub에 코멘트로 달리고**, 그와 별개로 **사용자(김진아) 본인이 실제 코드를 직접 검토**한다. 즉 사용자도 리뷰어다.

**정정 (2026-07-19):** 예전엔 "팀장이 자동화"로 적었으나, 사용자는 팀장이 아니다. 리뷰 = 자동 Claude 리뷰 + 사용자 본인 검토.

**Why:** 리뷰는 이미 자동화 + 사용자 본인이 담당하므로 내가 끼어들 필요 없음.
**How to apply:** PR 생성 후 `/pr-review`나 리뷰 실행을 **제안하지 말 것.** 사용자가 직접 요청할 때만 수행. 코드 리뷰는 사용자가 직접 한다 ([[edits-by-user]]).
