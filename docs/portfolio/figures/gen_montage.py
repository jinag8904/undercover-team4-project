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

# ---------- A: layers ----------
# layer card drawn as tilted square with face element
def card(x,y,label,on,body):
    fill='#fff' if on else '#f1f5f9'; stroke='#7c3aed' if on else '#cbd5e1'
    return f'''<g transform="translate({x},{y})">
  <rect x="0" y="0" width="110" height="110" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="2" {'stroke-dasharray="5 4"' if not on else ''}/>
  {body if on else ''}
  <text x="55" y="132" text-anchor="middle" font-size="12" fill="{'#5b21b6' if on else '#94a3b8'}" class="b">{label}</text>
  <text x="55" y="148" text-anchor="middle" font-size="11" fill="{'#5b21b6' if on else '#94a3b8'}">{'공개' if on else '미공개 → 안 그림'}</text>
 </g>'''
base='<circle cx="55" cy="50" r="30" fill="#e2e8f0" stroke="#94a3b8"/><rect x="35" y="80" width="40" height="22" rx="6" fill="#e2e8f0" stroke="#94a3b8"/>'
hair='<path d="M 25 50 A 30 30 0 0 1 85 50 L 80 50 A 25 25 0 0 0 30 50 Z" fill="#7c3aed"/>'
beard='<path d="M 35 62 Q 55 90 75 62 Q 55 74 35 62 Z" fill="#7c3aed"/>'
hat='<rect x="20" y="24" width="70" height="10" rx="3" fill="#7c3aed"/><rect x="32" y="8" width="46" height="18" rx="4" fill="#7c3aed"/>'
glasses='<rect x="30" y="44" width="20" height="12" rx="4" fill="none" stroke="#7c3aed" stroke-width="3"/><rect x="60" y="44" width="20" height="12" rx="4" fill="none" stroke="#7c3aed" stroke-width="3"/><line x1="50" y1="50" x2="60" y2="50" stroke="#7c3aed" stroke-width="3"/>'
A=head+f'''<svg width="900" height="170" viewBox="0 0 900 170" xmlns="http://www.w3.org/2000/svg">{defs}
 <text x="20" y="24" font-size="12" fill="#64748b">겹침 순서 = 자식 순서 →</text>
 {card(20,36,'베이스 (항상)',True,base)}
 {card(150,36,'머리',True,hair)}
 {card(280,36,'수염',False,beard)}
 {card(410,36,'모자',True,hat)}
 {card(540,36,'안경',False,glasses)}
 <line x1="662" y1="91" x2="700" y2="91" stroke="#334155" stroke-width="1.8" marker-end="url(#m)"/>
 <g transform="translate(704,36)">
  <rect x="0" y="0" width="150" height="110" rx="8" fill="#fff" stroke="#1e3a8a" stroke-width="2"/>
  <g transform="translate(20,0)">{base}{hair}{hat}</g>
  <text x="75" y="132" text-anchor="middle" font-size="12" class="b" fill="#1e3a8a">몽타주</text>
  <text x="75" y="148" text-anchor="middle" font-size="11" fill="#64748b">공개 축 = {{머리, 모자}}</text>
 </g>
</svg></body></html>'''
io.open('montage_a_layers.html','w',encoding='utf-8').write(A)

# ---------- B: clarity ----------
# 16x16 bitmap of a head silhouette with hair (values 0..1 gray)
import math
N=32
bmp=[[1.0]*N for _ in range(N)]
for y in range(N):
    for x in range(N):
        dx=x-15.5; dy=y-14.0
        if dx*dx/112+dy*dy/136<=1: bmp[y][x]=0.82   # face
        if dx*dx/120+dy*dy/136<=1 and y<=10: bmp[y][x]=0.25 # hair
        if 12<=y<=13 and (7<=x<=11 or 20<=x<=24): bmp[y][x]=0.35 # brows
        if 15<=y<=16 and (8<=x<=10 or 21<=x<=23): bmp[y][x]=0.3 # eyes
        if 21<=y<=22 and 11<=x<=20: bmp[y][x]=0.45 # mouth
        if y>=28 and 11<=x<=20: bmp[y][x]=0.7 # neck
def down(b,f):
    n=len(b)//f; out=[[0]*n for _ in range(n)]
    for Y in range(n):
        for X in range(n):
            s=0
            for yy in range(f):
                for xx in range(f): s+=b[Y*f+yy][X*f+xx]
            out[Y][X]=s/(f*f)
    return out
def draw(b,x0,y0,size=128):
    n=len(b); c=size/n; out=''
    for y in range(n):
        for x in range(n):
            v=int(b[y][x]*255); out+=f'<rect x="{x0+x*c:.1f}" y="{y0+y*c:.1f}" width="{c+0.4:.1f}" height="{c+0.4:.1f}" fill="rgb({v},{v},{v})"/>'
    return out
steps=[(bmp,'라운드 1','128 px'),(down(bmp,2),'라운드 2','64 px'),(down(bmp,4),'라운드 3','32 px'),(down(bmp,8),'라운드 4+','16 px')]
cells=''
for i,(b,r,px) in enumerate(steps):
    x=20+i*215
    cells+=f'<rect x="{x-6}" y="30" width="140" height="140" rx="8" fill="#fff" stroke="#cbd5e1"/>{draw(b,x,36)}<text x="{x+64}" y="194" text-anchor="middle" font-size="12" class="b" fill="#1e293b">{r}</text><text x="{x+64}" y="210" text-anchor="middle" font-size="11" class="mono" fill="#64748b">{px}</text>'
    if i<3: cells+=f'<line x1="{x+142}" y1="100" x2="{x+200}" y2="100" stroke="#334155" stroke-width="1.8" marker-end="url(#m)"/>'
B=head+f'''<svg width="900" height="230" viewBox="0 0 900 230" xmlns="http://www.w3.org/2000/svg">{defs}
 {cells}
 
</svg></body></html>'''
io.open('montage_b_clarity.html','w',encoding='utf-8').write(B)

# ---------- C: wanted list ----------
C=head+f'''<svg width="900" height="250" viewBox="0 0 900 250" xmlns="http://www.w3.org/2000/svg">{defs}
 <!-- server list -->
 <rect x="20" y="30" width="330" height="190" rx="14" fill="#e8f0fe" stroke="#a9c0ea" stroke-width="1.5"/>
 <text x="185" y="54" text-anchor="middle" class="b" font-size="13" fill="#1e3a8a">서버 · NetworkList&lt;WantedEntry&gt;</text>
 <g font-size="12">
  <rect x="40" y="68" width="290" height="30" rx="6" fill="#fff" stroke="#a9c0ea"/><text x="52" y="88" fill="#1e293b">서주아 · 8,000원 · 몽타주 {{머리,모자}}</text>
  <rect x="40" y="104" width="290" height="30" rx="6" fill="#fff" stroke="#a9c0ea"/><text x="52" y="124" fill="#1e293b">강이찬 · 8,400원 · 몽타주 {{수염,안경}}</text>
  <rect x="40" y="140" width="290" height="30" rx="6" fill="#fff" stroke="#cbd5e1" stroke-dasharray="5 4"/><text x="52" y="160" fill="#94a3b8">양결 · 11,700원 — 검거됨 → 리스트에서 내림</text>
 </g>

 <!-- events into list -->
 <g font-size="12">
  <rect x="400" y="30" width="200" height="44" rx="10" fill="#ecfdf5" stroke="#6ee7b7"/>
  <text x="500" y="49" text-anchor="middle" class="b" fill="#065f46">몽타주 발행</text>
  <text x="500" y="66" text-anchor="middle" font-size="11" fill="#065f46">범인마다 항목 추가</text>
  <line x1="398" y1="52" x2="356" y2="52" stroke="#0f766e" stroke-width="1.8" marker-end="url(#mg)"/>

  <rect x="400" y="102" width="200" height="44" rx="10" fill="#fef2f2" stroke="#fca5a5"/>
  <text x="500" y="121" text-anchor="middle" class="b" fill="#991b1b">검거</text>
  <text x="500" y="138" text-anchor="middle" font-size="11" fill="#991b1b">항목 내림 → 보관함에 보관</text>
  <line x1="398" y1="124" x2="356" y2="124" stroke="#b91c1c" stroke-width="1.8" marker-end="url(#mr)"/>

  <rect x="400" y="174" width="200" height="44" rx="10" fill="#fff6e6" stroke="#e7c48d"/>
  <text x="500" y="193" text-anchor="middle" class="b" fill="#7c3a00">탈출</text>
  <text x="500" y="210" text-anchor="middle" font-size="11" fill="#7c3a00">보관함 항목 그대로 복원</text>
  <line x1="398" y1="196" x2="356" y2="196" stroke="#b45309" stroke-width="1.8" marker-end="url(#m)"/>
 </g>

 <!-- archive -->
 <rect x="640" y="102" width="120" height="116" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-dasharray="5 4"/>
 <text x="700" y="124" text-anchor="middle" class="b" font-size="12" fill="#475569">서버 보관함</text>
 <rect x="652" y="136" width="96" height="26" rx="6" fill="#fff" stroke="#cbd5e1"/><text x="700" y="153" text-anchor="middle" font-size="11" fill="#64748b">양결 몽타주</text>
 <text x="700" y="200" text-anchor="middle" font-size="11" fill="#94a3b8">새로 만들지 않는다</text>
 <path d="M 600 124 L 638 124" stroke="#b91c1c" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#mr)"/>
 <path d="M 640 196 L 602 196" stroke="#b45309" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#m)"/>

 <!-- clients -->
 <rect x="790" y="30" width="90" height="190" rx="12" fill="#fff" stroke="#a9c0ea" stroke-width="1.5"/>
 <text x="835" y="54" text-anchor="middle" class="b" font-size="12" fill="#1e3a8a">본부 UI</text>
 <text x="835" y="74" text-anchor="middle" font-size="11" fill="#64748b">전 클라</text>
 <text x="835" y="120" text-anchor="middle" class="mono" font-size="10" fill="#475569">OnListChanged</text>
 <text x="835" y="136" text-anchor="middle" font-size="11" fill="#475569">→ 다시 그림</text>
 <path d="M 185 30 L 185 14 L 835 14 L 835 28" fill="none" stroke="#1d4ed8" stroke-width="1.5" marker-end="url(#mb)"/>
 <text x="510" y="10" text-anchor="middle" font-size="10" fill="#1d4ed8">리스트가 바뀔 때마다</text>
</svg></body></html>'''
pass  # C is hand-written now
print('ok')
