---
name: issue-222-faction-symbol
description: "이슈 #222 세력 문양 대조 — 확정 설계·진행 상태(1~3단계 완료, 4단계부터 재개)"
metadata: 
  node_type: memory
  type: project
  originSessionId: c935baf7-ad70-4283-9008-d1a2693b044f
  modified: 2026-07-26T11:25:27.491Z
---

이슈 #222(세력 문양 대조) 작업 중. 브랜치 `feature/222-faction-symbol`.
**정본 계획·진행 상태는 저장소의 `docs/issue-222-faction-symbol-plan.md`** — 메모리는 이 PC 로컬이라 다른 PC에서는 그 문서를 볼 것.

**핵심 설계**: 세력마다 비슷한 문양 여러 개(variant) → **세션(방) 시작 시 1회** 세력별 '진짜' index를 랜덤 선정하고 그 방 동안 고정(라운드마다 재추첨 아님). 위조범은 이름·문양 중 하나만 오염(택1), None 세력은 배정 제외, variant 2개 미만이면 이름 위조로 폴백. 본부 대조자료 뷰는 Directory 옆.

**2026-07-26 시점**: 1) OfficialRecords variant 세트 ✅ (API명은 `GetVariants`/`GetVariantsCount`) 2) FactionSymbolManager(세션 상주 NetworkList, TeamFund와 동일 패턴)+App 등록+프리팹 ✅ 3) per-NPC 문양 동기화(CitizenProfile.m_symbolIndexView / CitizenData.SymbolIndex / CriminalAssigner 배정) ✅ → **4단계 스캔 UI 문양 표시부터 재개**.

**Why:** 세션 스코프(방 단위 고정)를 라운드 스코프로 착각하면 설계가 어긋난다 — 사용자가 명시적으로 정정한 지점.

**How to apply:** 재개 시 계획 문서의 "3-1. 진행 상태" 표를 먼저 읽고, 남은 에디터 배선(DefaultNetworkPrefabs·SessionObjectSpawner 등록, variant 이미지) 확인부터. 단계별 설명은 [[explain-deliverable-per-step]] 방식, 코드 편집은 [[edits-by-user]].
