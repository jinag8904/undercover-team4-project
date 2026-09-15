# 포트폴리오 작업 폴더 (개인 · fork 전용)

- `진행표.md` — 슬라이드별 상태·확정 방식·남은 일. **새 세션은 여기서 시작.**
- `figures/` — 슬라이드용 PNG + 원본(HTML/PY). PNG는 headless Chrome으로 렌더:
  `chrome --headless=new --hide-scrollbars --force-device-scale-factor=2 --window-size=W,H --screenshot=out.png file:///.../x.html`
  (montage_real.html·montage_trouble.html은 `--allow-file-access-from-files --virtual-time-budget=3000` 추가)
- `memory/` — Claude Code 프로젝트 메모리 사본. 다른 PC에서는
  `~/.claude/projects/C--Users-hamme-Github-undercover-team4-project/memory/` 에 복사하면 기억이 이어진다.
