---
name: portfolio-fork-remote
description: 포트폴리오용 문서 작업은 팀 origin이 아니라 본인 포크(fork remote)로 푸시한다
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e0598003-8b7b-4f92-a3e6-59844fd17a07
  modified: 2026-09-08T14:33:29.710Z
---

포트폴리오 목적의 문서(README 등) 커밋은 **팀 원본 저장소(`origin` = hyunjin0814/undercover-team4-project)가 아니라
본인 포크로 푸시한다.** 2026-09-08에 remote `fork`(https://github.com/jinag8904/undercover-team4-project)를 추가했다.

**Why:** 로컬 체크아웃의 `origin`이 팀 원본을 가리키고 있어, "main에 올려"를 그대로 따르면 팀 공용 main이 바뀐다.
사용자가 말하는 "여기/main"은 자기 포크를 뜻한다.

**How to apply:** 푸시 전 `git remote -v`로 대상을 확인하고, 개인 산출물은 `git push fork main`.
팀 저장소에 올릴 일이 생기면 브랜치 + PR로 간다([[pr-review-automation]] — 리뷰는 팀장이 자동화).

관련: [[portfolio-implementation-writeup]], [[parallel-git-ops]], [[user-profile]]
