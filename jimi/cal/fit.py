import numpy as np, json, sys
from PIL import Image, ImageDraw
def fit(pts):
    A=np.array([[1,lo,la,lo*la,lo*lo,la*la] for (lo,la),_ in pts]); X=np.array([p for _,p in pts],float)
    cx,*_=np.linalg.lstsq(A,X[:,0],rcond=None); cy,*_=np.linalg.lstsq(A,X[:,1],rcond=None)
    res=A@cx-X[:,0], A@cy-X[:,1]
    return cx.tolist(),cy.tolist(),float(np.max(np.hypot(*res)))
def proj(c,lo,la):
    cx,cy=c; v=[1,lo,la,lo*la,lo*lo,la*la]; return sum(a*b for a,b in zip(cx,v)), sum(a*b for a,b in zip(cy,v))
if __name__=='__main__':
    name,img=sys.argv[1],sys.argv[2]; pts=json.load(open(f'cal/{name}_pts.json'))
    cx,cy,err=fit(pts); json.dump([cx,cy],open(f'cal/{name}_coef.json','w')); print('max residual px',round(err,1))
    test=json.load(open(f'cal/{name}_test.json'))
    im=Image.open(img).convert('RGB'); d=ImageDraw.Draw(im)
    for n,(lo,la) in test.items():
        x,y=proj((cx,cy),lo,la); d.ellipse([x-5,y-5,x+5,y+5],outline=(220,0,0),width=2); d.text((x+7,y-6),n,fill=(220,0,0))
    im.save(f'cal/{name}_check.png')
