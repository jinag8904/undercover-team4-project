---
name: minimal-core-first
description: 재활용/구현 시 최소 핵심 뼈대부터 만들고 필요할 때 덧붙이는 방식 선호
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4dfaeda4-80da-4d65-a2b5-afe7dec8b945
---

사용자는 재활용 코드나 신규 구현에서 **꼭 필요한 핵심만 먼저 뼈대로 만들고, 필요해지는 시점에 덧붙이는** 점진적 방식을 선호한다.

**Why:** 한 번에 다 가져오면 안 쓰는 코드·군더더기가 쌓이고 이해·유지가 어려워짐. 최소 동작부터 검증하며 키우는 걸 선호.

**How to apply:** 재활용 코드 제안 시 "이번 목표(이슈)에 실제로 필요한 파일/부분만" 골라서 축소 버전으로 제시하고, 나머지는 "언제 필요해지면 무엇을 덧붙일지"로 정리. 예: #53에는 학원 코드 중 ConnectionMenu 하나만, 그것도 Server 버튼 등은 빼고 축소해서 제안함. 관련: [[network-study-reuse]].
