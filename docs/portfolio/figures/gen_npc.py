import io
head='''<!doctype html><html><head><meta charset="utf-8">
<style>
 body{margin:0;background:#fff;font-family:"Malgun Gothic","Segoe UI",sans-serif}
 svg{display:block}
 .b{font-weight:700}
 .mono{font-family:Consolas,"Malgun Gothic",monospace}
</style></head><body>
'''
defs='''<defs>
  <marker id="m" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#334155"/></marker>
  <marker id="mb" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#1d4ed8"/></marker>
  <symbol id="npc" viewBox="0 0 40 60">
   <circle cx="20" cy="12" r="9" fill="currentColor"/>
   <rect x="9" y="24" width="22" height="26" rx="6" fill="currentColor"/>
   <rect x="11" y="50" width="7" height="9" rx="2" fill="currentColor"/>
   <rect x="22" y="50" width="7" height="9" rx="2" fill="currentColor"/>
  </symbol>
 </defs>'''

# ---------- A: profile = 6 numbers ----------
chips=[("헤어스타일",3),("머리색",1),("피부색",2),("수염",0),("모자",4),("안경",1)]
cx=''.join(f'<rect x="{20+i*100}" y="30" width="90" height="60" rx="10" fill="#fff" stroke="#a9c0ea" stroke-width="1.5"/><text x="{65+i*100}" y="52" text-anchor="middle" font-size="12" fill="#64748b">{n}</text><text x="{65+i*100}" y="80" text-anchor="middle" class="b mono" font-size="20" fill="#1e3a8a">{v}</text>' for i,(n,v) in enumerate(chips))
A=head+f'''<svg width="900" height="130" viewBox="0 0 900 130" xmlns="http://www.w3.org/2000/svg">{defs}
 <rect x="10" y="20" width="612" height="80" rx="14" fill="#f4f8ff" stroke="#a9c0ea" stroke-width="1.5"/>
 {cx}
 <text x="316" y="118" text-anchor="middle" class="mono" font-size="12" fill="#475569">AppearanceProfile — int × 6</text>
 <line x1="630" y1="60" x2="668" y2="60" stroke="#334155" stroke-width="1.8" marker-end="url(#m)"/>
 <rect x="672" y="30" width="130" height="60" rx="10" fill="#ecfdf5" stroke="#6ee7b7" stroke-width="1.5"/>
 <text x="737" y="55" text-anchor="middle" class="b" font-size="12" fill="#065f46">AppearanceDatabase</text>
 <text x="737" y="74" text-anchor="middle" font-size="11" fill="#065f46">인덱스 → 메시·프리팹·색</text>
 <line x1="810" y1="60" x2="838" y2="60" stroke="#334155" stroke-width="1.8" marker-end="url(#m)"/>
 <use href="#npc" x="846" y="30" width="40" height="60" color="#1e3a8a"/>
</svg></body></html>'''
io.open('npc_a_profile.html','w',encoding='utf-8').write(A)

# ---------- B: sync ----------
B=head+f'''<svg width="900" height="260" viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg">{defs}
 <rect x="20" y="40" width="200" height="180" rx="14" fill="#e8f0fe" stroke="#a9c0ea" stroke-width="1.5"/>
 <text x="120" y="66" text-anchor="middle" class="b" font-size="14" fill="#1e3a8a">서버</text>
 <use href="#npc" x="100" y="80" width="40" height="60" color="#1e3a8a"/>
 <text x="120" y="164" text-anchor="middle" class="mono b" font-size="13" fill="#1e3a8a">{{3,1,2,0,4,1}}</text>
 <text x="120" y="186" text-anchor="middle" class="mono" font-size="11" fill="#475569">AppearanceAssigner</text>
 <text x="120" y="204" text-anchor="middle" class="mono" font-size="11" fill="#475569">→ SetProfile()</text>

 <line x1="220" y1="130" x2="300" y2="130" stroke="#1d4ed8" stroke-width="2" marker-end="url(#mb)"/>
 <rect x="304" y="104" width="230" height="52" rx="26" fill="#fff" stroke="#1d4ed8" stroke-width="2"/>
 <text x="419" y="126" text-anchor="middle" class="mono b" font-size="12" fill="#1d4ed8">NetworkVariable</text>
 <text x="419" y="144" text-anchor="middle" class="mono" font-size="11" fill="#1d4ed8">&lt;AppearanceProfile&gt;</text>

 <g stroke="#1d4ed8" stroke-width="2" fill="none" marker-end="url(#mb)">
  <path d="M 534 130 L 580 130 L 580 60 L 620 60"/>
  <path d="M 580 130 L 620 130"/>
  <path d="M 580 130 L 580 200 L 620 200"/>
 </g>

 <g font-size="12">
  <rect x="624" y="34" width="256" height="52" rx="10" fill="#fff" stroke="#a9c0ea" stroke-width="1.5"/>
  <use href="#npc" x="640" y="40" width="28" height="42" color="#1e3a8a"/>
  <text x="680" y="56" class="b" fill="#1e293b">호스트</text>
  <text x="680" y="74" class="mono" font-size="11" fill="#475569">OnValueChanged → ApplyProfile</text>

  <rect x="624" y="104" width="256" height="52" rx="10" fill="#fff" stroke="#a9c0ea" stroke-width="1.5"/>
  <use href="#npc" x="640" y="110" width="28" height="42" color="#1e3a8a"/>
  <text x="680" y="126" class="b" fill="#1e293b">클라 B</text>
  <text x="680" y="144" class="mono" font-size="11" fill="#475569">OnValueChanged → ApplyProfile</text>

  <rect x="624" y="174" width="256" height="52" rx="10" fill="#fff" stroke="#a9c0ea" stroke-width="1.5"/>
  <use href="#npc" x="640" y="180" width="28" height="42" color="#1e3a8a"/>
  <text x="680" y="196" class="b" fill="#1e293b">클라 C — 늦게 참가</text>
  <text x="680" y="214" class="mono" font-size="11" fill="#475569">스폰 페이로드 → ApplyProfile</text>
 </g>
</svg></body></html>'''
io.open('npc_b_sync.html','w',encoding='utf-8').write(B)

# ---------- C: apply ----------
C=head+f'''<svg width="900" height="260" viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg">{defs}
 <g transform="translate(60,30)">
  <circle cx="90" cy="50" r="36" fill="#dbe4f5" stroke="#1e3a8a" stroke-width="2"/>
  <rect x="45" y="96" width="90" height="100" rx="18" fill="#dbe4f5" stroke="#1e3a8a" stroke-width="2"/>
  <path d="M 54 40 A 36 36 0 0 1 126 40 L 126 30 A 36 30 0 0 0 54 30 Z" fill="#7c3aed"/>
  <rect x="62" y="48" width="22" height="12" rx="4" fill="none" stroke="#7c3aed" stroke-width="2.5"/>
  <rect x="96" y="48" width="22" height="12" rx="4" fill="none" stroke="#7c3aed" stroke-width="2.5"/>
  <line x1="84" y1="54" x2="96" y2="54" stroke="#7c3aed" stroke-width="2.5"/>
  <circle cx="90" cy="14" r="4" fill="#b45309"/>
  <text x="90" y="220" text-anchor="middle" class="mono" font-size="11" fill="#475569">NpcAppearance.ApplyProfile</text>
 </g>

 <line x1="196" y1="176" x2="300" y2="176" stroke="#334155" stroke-width="1.5" marker-end="url(#m)"/>
 <rect x="304" y="150" width="270" height="52" rx="10" fill="#f4f8ff" stroke="#a9c0ea" stroke-width="1.5"/>
 <text x="318" y="172" class="b" font-size="13" fill="#1e3a8a">바디 — 켜기</text>
 <text x="318" y="191" class="mono" font-size="11" fill="#475569">variants[i].SetActive(i == index)</text>

 <line x1="154" y1="44" x2="300" y2="44" stroke="#7c3aed" stroke-width="1.5" marker-end="url(#m)"/>
 <rect x="304" y="18" width="270" height="52" rx="10" fill="#faf5ff" stroke="#c4b5fd" stroke-width="1.5"/>
 <text x="318" y="40" class="b" font-size="13" fill="#5b21b6">프롭 — 붙이기</text>
 <text x="318" y="59" class="mono" font-size="11" fill="#475569">Instantiate(prefab, headAnchor)</text>

 <line x1="186" y1="110" x2="300" y2="110" stroke="#b45309" stroke-width="1.5" marker-end="url(#m)"/>
 <rect x="304" y="84" width="270" height="52" rx="10" fill="#fff6e6" stroke="#e7c48d" stroke-width="1.5"/>
 <text x="318" y="106" class="b" font-size="13" fill="#7c3a00">색 — 칠하기</text>
 <text x="318" y="125" class="mono" font-size="11" fill="#475569">MaterialPropertyBlock · _BaseColor / _Skin_Color</text>

 <rect x="610" y="18" width="270" height="184" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
 <text x="745" y="42" text-anchor="middle" font-size="12" fill="#475569">바디 변형 — 하나만 켠다</text>
 <g>
  <use href="#npc" x="640" y="60" width="34" height="50" color="#cbd5e1"/>
  <use href="#npc" x="690" y="60" width="34" height="50" color="#1e3a8a"/>
  <use href="#npc" x="740" y="60" width="34" height="50" color="#cbd5e1"/>
  <use href="#npc" x="790" y="60" width="34" height="50" color="#cbd5e1"/>
  <use href="#npc" x="840" y="60" width="34" height="50" color="#cbd5e1"/>
  <rect x="684" y="54" width="46" height="62" rx="8" fill="none" stroke="#1e3a8a" stroke-width="2"/>
  <text x="707" y="136" text-anchor="middle" class="mono" font-size="11" fill="#1e3a8a">index 1</text>
  <text x="745" y="170" text-anchor="middle" font-size="11" fill="#64748b">같은 스켈레톤 · 메시 교체 없음</text>
 </g>
</svg></body></html>'''
io.open('npc_c_apply.html','w',encoding='utf-8').write(C)
print("ok")
