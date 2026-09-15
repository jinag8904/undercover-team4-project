---
name: python-launcher-py
description: "이 PC에서 `python`은 Windows Store 스텁이라 실패한다 — `py`를 쓸 것"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 6c8f5c81-cdc2-4049-9996-9ddde8b1322a
  modified: 2026-08-09T02:47:10.371Z
---

Bash 도구에서 `python`을 부르면 Windows Store 스텁이 잡혀 `Python`만 출력하고
**exit 49**로 죽는다. 실제 인터프리터는 `py` 런처다(Python 3.14.5).

**Why:** 스텁이 PATH 앞쪽에 있어 조용히 가로챈다. 에러 메시지가 "Python" 한 줄뿐이라
스크립트 문법 오류로 오해하기 쉽다.

**How to apply:** 임시 분석 스크립트를 돌릴 때 `py script.py`로 쓴다.
`$TMPDIR`도 이 셸에서 비어 있으니 스크래치패드 절대경로를 직접 쓸 것.
`.cs` 정밀 편집에 Python을 쓰는 이유는 [[csharpier-format-hook]] 참고.
