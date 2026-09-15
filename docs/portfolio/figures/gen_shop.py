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
  <marker id="mr" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#b91c1c"/></marker>
  <marker id="mg" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#0f766e"/></marker>
 </defs>'''

def chip(x,y,w,h,label,fill,stroke,star=False,sub=None,dash=False):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.5" {"stroke-dasharray=\"5 4\"" if dash else ""}/>'
    s+=f'<text x="{x+w/2}" y="{y+h/2+(0 if sub else 4)}" text-anchor="middle" font-size="12" class="b" fill="#1e293b">{("★ " if star else "")+label}</text>'
    if sub: s+=f'<text x="{x+w/2}" y="{y+h/2+16}" text-anchor="middle" font-size="11" fill="#64748b">{sub}</text>'
    return s

# ---------- A: lineup roll ----------
cat_star=[("힐팩",2000),("부활 키트",5000),("구역 스캔",3000)]
cat_rand=[("휴대용 미니맵",3000),("홈런 진압봉",10000),("테이저",0),("장난감 망치",0),("신호 해석기 ⌂",0),("사이렌 버튼 ⌂",0)]
A=head+f'''<svg width="900" height="270" viewBox="0 0 900 270" xmlns="http://www.w3.org/2000/svg">{defs}
 <!-- catalog -->
 <rect x="20" y="20" width="300" height="230" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
 <text x="170" y="44" text-anchor="middle" class="b" font-size="13" fill="#1e293b">ShopCatalog (SO) — 판매 후보 9종</text>
 <text x="40" y="66" font-size="11" fill="#b45309" class="b">★ staple 고정 그룹</text>
 {''.join(chip(40+i*90,74,84,28,n,'#fff6e6','#e7c48d',star=True) for i,(n,p) in enumerate(cat_star))}
 <text x="40" y="126" font-size="11" fill="#64748b" class="b">나머지 — 랜덤 그룹</text>
 {''.join(chip(40+(i%3)*90,134+(i//3)*36,84,28,n,'#fff','#cbd5e1') for i,(n,p) in enumerate(cat_rand))}
 <text x="40" y="238" font-size="10" fill="#94a3b8">⌂ 설치형 · index = 네트워크 계약</text>

 <!-- roll -->
 <line x1="320" y1="135" x2="356" y2="135" stroke="#334155" stroke-width="2" marker-end="url(#m)"/>
 <rect x="360" y="90" width="150" height="90" rx="12" fill="#e8f0fe" stroke="#a9c0ea" stroke-width="1.5"/>
 <text x="435" y="114" text-anchor="middle" class="b" font-size="13" fill="#1e3a8a">라운드당 1회 추첨</text>
 <text x="435" y="136" text-anchor="middle" font-size="12" fill="#1e3a8a">★에서 5칸 (중복 가능)</text>
 <text x="435" y="154" text-anchor="middle" font-size="12" fill="#1e3a8a">나머지에서 2칸 → 섞기</text>
 <text x="435" y="172" text-anchor="middle" font-size="10" fill="#475569" class="mono">ShopLineup (서버)</text>
 <line x1="510" y1="135" x2="546" y2="135" stroke="#334155" stroke-width="2" marker-end="url(#m)"/>

 <!-- 7 slots -->
 <rect x="550" y="20" width="330" height="230" rx="14" fill="#f4f8ff" stroke="#a9c0ea" stroke-width="1.5"/>
 <text x="715" y="44" text-anchor="middle" class="b" font-size="13" fill="#1e3a8a">이번 라운드 칸 7개</text>
 <text x="715" y="60" text-anchor="middle" font-size="10" class="mono" fill="#475569">NetworkList&lt;Slot&gt; — 전 클라 복제</text>
 {chip(566,72,94,40,"힐팩",'#fff6e6','#e7c48d',star=True,sub="2,000")}
 {chip(668,72,94,40,"홈런 진압봉",'#fff','#cbd5e1',sub="10,000")}
 {chip(770,72,94,40,"부활 키트",'#fff6e6','#e7c48d',star=True,sub="5,000")}
 {chip(566,120,94,40,"구역 스캔",'#fff6e6','#e7c48d',star=True,sub="3,000")}
 {chip(668,120,94,40,"힐팩",'#fff6e6','#e7c48d',star=True,sub="2,000")}
 {chip(770,120,94,40,"휴대용 미니맵",'#fff','#cbd5e1',sub="3,000")}
 {chip(566,168,94,40,"부활 키트",'#fff6e6','#e7c48d',star=True,sub="5,000")}
 <text x="740" y="192" font-size="11" fill="#64748b">★ 5칸 = 필수품은 항상 있다</text>
 <text x="740" y="208" font-size="11" fill="#64748b">□ 2칸 = 매 라운드 달라진다</text>
 <text x="566" y="236" font-size="10" fill="#94a3b8">이어하기 시 같은 라운드면 세이브에서 복원 (#925)</text>
</svg></body></html>'''
io.open('shop_a_roll.html','w',encoding='utf-8').write(A)

# ---------- B: order flow ----------
B=head+f'''<svg width="900" height="230" viewBox="0 0 900 230" xmlns="http://www.w3.org/2000/svg">{defs}
 <!-- client -->
 <rect x="20" y="40" width="190" height="150" rx="14" fill="#faf5ff" stroke="#c4b5fd" stroke-width="1.5"/>
 <text x="115" y="64" text-anchor="middle" class="b" font-size="13" fill="#5b21b6">클라이언트 주문창</text>
 {chip(40,80,150,40,"3번 칸  [주문]",'#fff','#c4b5fd',sub="힐팩 2,000")}
 <text x="115" y="146" text-anchor="middle" font-size="11" fill="#64748b">보내는 것은 칸 번호뿐</text>
 <text x="115" y="164" text-anchor="middle" class="mono" font-size="11" fill="#5b21b6">RequestPurchaseRpc(3)</text>

 <line x1="210" y1="100" x2="256" y2="100" stroke="#1d4ed8" stroke-width="2" marker-end="url(#mb)"/>

 <!-- server -->
 <rect x="260" y="20" width="400" height="190" rx="14" fill="#e8f0fe" stroke="#a9c0ea" stroke-width="1.5"/>
 <text x="460" y="44" text-anchor="middle" class="b" font-size="13" fill="#1e3a8a">서버 — 품목·가격·상태의 주인</text>
 <g font-size="12">
  <rect x="280" y="58" width="360" height="30" rx="8" fill="#fff" stroke="#a9c0ea"/>
  <text x="292" y="78" fill="#1e293b">① 3번 칸이 뭔지 <tspan class="mono">NetworkList</tspan>에서 본다 → 힐팩 · 2,000</text>
  <rect x="280" y="94" width="360" height="30" rx="8" fill="#fff" stroke="#a9c0ea"/>
  <text x="292" y="114" fill="#1e293b">② 이미 <tspan class="b" fill="#b91c1c">SoldOut</tspan>인가? → 거절 회신</text>
  <rect x="280" y="130" width="360" height="30" rx="8" fill="#fff" stroke="#a9c0ea"/>
  <text x="292" y="150" fill="#1e293b">③ <tspan class="mono">TeamFund.TrySpend(2000)</tspan> 부족? → 거절 회신</text>
  <rect x="280" y="166" width="360" height="30" rx="8" fill="#ecfdf5" stroke="#6ee7b7"/>
  <text x="292" y="186" fill="#065f46">④ 칸 상태 = SoldOut · 구매 목록에 추가 → <tspan class="b">전 클라 복제</tspan></text>
 </g>

 <!-- replies -->
 <line x1="660" y1="100" x2="706" y2="100" stroke="#0f766e" stroke-width="2" marker-end="url(#mg)"/>
 <rect x="710" y="40" width="170" height="150" rx="14" fill="#fff" stroke="#cbd5e1" stroke-width="1.5"/>
 <text x="795" y="64" text-anchor="middle" class="b" font-size="13" fill="#1e293b">모든 클라</text>
 <text x="795" y="90" text-anchor="middle" font-size="12" fill="#475569">NetworkList 바뀜</text>
 <text x="795" y="108" text-anchor="middle" font-size="12" fill="#475569">→ 3번 칸 품절 표시</text>
 <text x="795" y="140" text-anchor="middle" font-size="11" fill="#64748b">주문한 사람에게만</text>
 <text x="795" y="156" text-anchor="middle" class="mono" font-size="11" fill="#0f766e">ReplyRpc(성공/품절/자금부족)</text>
</svg></body></html>'''
io.open('shop_b_order.html','w',encoding='utf-8').write(B)
print('ok')
