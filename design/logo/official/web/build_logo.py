# Rebuild official MCKA logo as clean vector (trace of original + re-set small caption line)
from PIL import Image, ImageFilter; import numpy as np, re, subprocess
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
SRC='../mcka-logo-official.jpg'; S=8
im=np.array(Image.open(SRC).convert('RGB')).astype(float)
bg=np.median(im,axis=1,keepdims=True)
a=((im-bg)/(255-bg+1e-6)).clip(0,1); a=a[:,:,0]*.5+a[:,:,2]*.5
a[171:183,:]=0                      # caption line is re-set as type below
A=Image.fromarray((a*255).astype('uint8'))
B=A.resize((A.width*S,A.height*S),Image.LANCZOS).filter(ImageFilter.GaussianBlur(S*.6))
Image.fromarray(np.where(np.array(B)<128,255,0).astype('uint8')).convert('1').save('mask.pbm')
subprocess.run(['potrace','mask.pbm','-s','-o','trace.svg','--turdsize','40','--alphamax','1.1','--opttolerance','0.3'],check=True)
t=open('trace.svg').read()
g=re.search(r'<g transform="translate\(0.000000,(\d+)\.000000\) scale\(0.100000,-0.100000\)"\s*fill="#000000" stroke="none">(.*?)</g>',t,re.S)
H=int(g.group(1)); paths=g.group(2)
mark=f'<g transform="scale({1/S}) translate(0,{H}) scale(0.1,-0.1)">{paths}</g>'
# caption: Michroma, cap height 7px, spans x 45..368, baseline y 180
f=TTFont('/usr/share/fonts/truetype/sand-box/google/Michroma/Michroma-Regular.ttf')
gs=f.getGlyphSet(); cmap=f.getBestCmap(); cap=f['OS/2'].sCapHeight
k=7/cap; txt='KORFBALL ASSOCIATION'
adv=[gs[cmap[ord(c)]].width*k for c in txt]
nat=sum(adv[:-1])+ (gs[cmap[ord(txt[-1])]].width*k)
# measure last glyph ink right edge approx = advance; spread remaining width as tracking
TR=2.2; sx=(368-45-TR*(len(txt)-1))/nat; track=TR
x=45; cp=''
for c,w in zip(txt,adv):
    pen=SVGPathPen(gs); gs[cmap[ord(c)]].draw(TransformPen(pen,(k*sx,0,0,-k,x,180)))
    cp+=f'<path d="{pen.getCommands()}"/>'; x+=w*sx+track
VB='35 7 342 181'
def svg(fill): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB}" role="img" aria-label="Macau China Korfball Association"><g fill="{fill}">{mark}{cp}</g></svg>'
for name,fill in [('mcka-logo-white','#FFFFFF'),('mcka-logo-navy','#14213D'),('mcka-logo-green','#0B6A12')]:
    open(name+'.svg','w').write(svg(fill))
print('sx',round(sx,2))
