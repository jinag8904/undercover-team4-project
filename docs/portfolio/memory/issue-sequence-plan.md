---
name: issue-sequence-plan
description: 사용자가 진행 중인 이슈 작업 순서 (2026-07-19 확정)
metadata: 
  node_type: memory
  type: project
  originSessionId: 437a6c4d-cde6-439a-90c8-69c62b70d323
---

김진아 진행 이슈 순서 (2026-07-19 확정): **#218 → #234 → #222 → #223 → #221**

- #218 플레이어 이름표(UGS PlayerName) → #234 이름표 스피커 아이콘(발화 UI) — #234는 #218 선행.
- #222 본부 Faction(문양) 대조 데이터 → #223 시민 인명부 본부 배치 — **#222 하드 선행**(인명부가 문양 심볼 소비). 둘이 본부 대조(Papers-Please식) 세로 슬라이스.
- #221 몽타주 데이터 세분화 = 외형 축(`AppearanceProfile`/`Database`/`WantedEntry`), Faction 축(`OfficialRecords`/`CitizenProfile`)과 SO가 안 겹쳐 독립 → 리워크 손해 없어 마지막. 단 수배리스트/육안관찰 기능이 활발히 쌓이는 중이면 #221을 앞당기는 게 마이그레이션 비용 절감.

**참고:** #222 스캐폴딩 이미 존재 — `OfficialRecords.Faction` enum·`FactionSymbol[]`·`GetFactionSymbol`, `CitizenProfile.m_symbolView`·`Initialize`. #222 남은 일은 AI 심볼 이미지 세트 + 라운드 랜덤 매칭.

**#169는 완료(CLOSED, PR #243).** #154 로비는 PR #248로 올림 ([[lobby-issue-154]]).
