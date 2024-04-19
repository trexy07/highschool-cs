### credits for arcade 
### pause menu in quail
### games can open on mouse relese so you can scroll without opening a game 


import time
list_of_shortenings=[
Q:="",
c0:="​",c1:="­",c2:="﻿",
c00:="​​",c11:="­­",c22:="﻿﻿",
c012:="​­﻿",
h1:=100,o1:=110,o2:=120,o3:=130,o4:=140,o5:=150,o6:=160,o7:=170,o8:=180,o9:=190,
h2:=200,t1:=210,t2:=220,t3:=230,t4:=240,t5:=250,t6:=260,t7:=270,t8:=280,t9:=290,
h3:=300,T1:=310,T2:=320,T3:=330,T4:=340,T5:=350,T6:=360,T7:=370,T8:=380,T9:=390,
h4:=400,
h5:=500,
h6:=600,
h8:=800,
h10:=1000,
h12:=1200,


arcdgm:="arcade.game.",


esc:="escape",ent:="enter",tab:="tab",spc:="space",
lf:="left",rt:="right",up:="up",dw:="down",
cn:="center",tp:="top",bt:="bottom",
tf:=tp+"-"+lf,tr:=tp+"-"+rt,bf:=bt+"-"+lf,br:=bt+"-"+rt,


wh:="white",bk:="black",
dk:="dark",lt:="light",md:="medium",
gy:="gray",dy:=dk+gy,
bw:="brown",sb:="saddle"+bw,yb:="sandy"+bw,tn:="tan",
rd:="red",dr:=dk+rd,
on:="orange",do:=dk+on,
yl:="yellow",
gr:="green",dg:=dk+gr,lg:=lt+gr,fg:="forest"+gr,lw:="lawn"+gr,lm:="lime",
bl:="blue",db:="dodger"+bl,cb:="cornflower"+bl,mb:=md+"slate"+bl,cy:="cyan",
pr:="purple",vi:="violet",dv:=dk+vi,mo:=md+"orchid",
cz:="cinzel",ms:="monospace",mt:="montserrat",ot:="orbitron",
grd:=gradient,grd6gy:=lambda a:grd(wh,*[gy]*6,rgb(*[70]*3),start=a),


bc:="back",rst:="restart",RST:="RESTART",rstINST:=f"press this or hit r to {rst}",


T:=True,
F:=False,
N:=None,
i:=int,
f:=float,
s:=str,
l:=len,
r:=range,
a:=abs,
enum:=enumerate,


ez:=lambda a:a==0,
nz:=lambda a:a!=0,
evn:=lambda a:a%2==0,
odd:=lambda a:a%2==1,
rnd:=lambda a:i(a)if a-i(a)<0.5else i(a)+1,
rndu:=lambda a:1+i(a)if a-i(a)>0else i(a),


rr:=randrange,
chc:=choice,


tme:=time.time,


ap:=app,


gti:=ap.getTextInput,
rstrt:=lambda: gti(f'type "{RST}" to confirm')==RST,
gpd:=getPointInDir,
a2:=angleTo,
ds:=distance,
Grp:=Group,
Ply:=Polygon,
RPy:=RegularPolygon,
Str:=Star,
Crc:=Circle,
Ovl:=Oval,
Rct:=Rect,
Lbl:=Label,
Lne:=Line,
tF:=lambda a:a.toFront(),
tB:=lambda a:a.toBack(),
hT:=lambda a,b,c:a.hits(b,c),
hS:=lambda a,b:a.hitsShape(b),
cT:=lambda a,b,c:a.contains(b,c),
cS:=lambda a,b:a.containsShape(b),
cX:=lambda a:a.centerX,
cY:=lambda a:a.centerY,
lF:=lambda a:a.left,
rT:=lambda a:a.right,
tP:=lambda a:a.top,
bT:=lambda a:a.bottom,
wD:=lambda a:a.width,
hG:=lambda a:a.height,
rA:=lambda a:a.rotateAngle,
fL:=lambda a:a.fill,
bR:=lambda a:a.border,
bW:=lambda a:a.borderWidth,
oP:=lambda a:a.opacity,
vS:=lambda a:a.visible,
rD:=lambda a:a.radius,
lW:=lambda a:a.lineWidth,
dS:=lambda a:a.dashes,
aS:=lambda a:a.arrowStart,
aE:=lambda a:a.arrowEnd,
vL:=lambda a:a.value,
fN:=lambda a:a.font,
sZ:=lambda a:a.size,
bL:=lambda a:a.bold,
iL:=lambda a:a.italic,
pN:=lambda a:a.points,
rN:=lambda a:a.roundness,
pL:=lambda a:a.pointList,
aP:=lambda a,b,c:a.addPoint(b,c),
sA:=lambda a:a.startAngle,
sW:=lambda a:a.sweepAngle,
cH:=lambda a:a.children,
aD:=lambda a,*b:a.add(*b),
cL:=lambda a:a.clear(),
rM:=lambda a,b:a.remove(b),
hE:=lambda a,b,c:a.hitTest(b,c),


brd:=lambda a:a.board,
]
ap.setMaxShapeCount(3000)
ap.restart=Grp(Rct(90,10,t2,50,fill=dv),Lbl(f"hit this to {rst} arcade",h2,35,fill=wh,size=20),visible=F)
class Arcade:
  class LoadingScreen:
    def __init__(t):t.active=T;ap.background=bk;t.bar=Rct(45,295,0.1,40,fill=grd(rgb(0,0,205),rgb(0,0,205),bk,start=br),border=N,borderWidth=0);t.grp=Grp(Lbl("BirdFace",o9,83,font=mt,size=43,bold=T,fill=wh),Lbl("Arcade",h2,o2,font=mt,size=90,bold=T,fill=wh),Lbl("Loading...",135,265,fill=wh,font=mt,size=30,bold=T),Rct(40,t9,T2,50,fill=N,border=grd(rgb(0,0,205),rgb(0,0,205),bk,start=br),borderWidth=5),t.bar,visible=T)
    def oS(t):
      if(wD(t.bar)<=T1)&t.active:
        t.bar.width+=rr(8)
        if wD(t.bar)>T1:t.grp.visible=t.active=F;arcade.menu.active=arcade.menu.aS.visible=T
    def restart(t):t.bar.width=0.1;t.active=t.grp.visible=T
  class Menu:
    class Codeclicker:
      def __init__(t,p):y=rgb(255,211,67);p*=h1;t.pl=Image("https://cdn.freebiesupply.com/logos/large/2x/python-5-logo-png-transparent.png",38.5,p+37);t.pl.width=t.pl.height=37;t.border=Rct(0,p,h4,h1,border=gy,fill=N);t.hitbox=Rct(0,p,h4,h1,fill=N);t.hitbox.type="codeclicker";t.grp=Grp(Rct(0,p,h4,h1),t.pl,Lbl("C DE CLICKER",h2,p+55,size=52.5,font=ms,bold=T,border=bk,borderWidth=1.5,fill=grd(rgb(55,118,171),rgb(55,118,171),y,y,y,y,y,y,y,y,y,y,start=lf)),bR(t),t.hitbox,visible=F)
    class Twelfthbit:
      def __init__(t,p):
        p*=h1;t.grp=Grp(visible=F);t.pC={2:rd,4:on,8:yl,16:gr,32:bl,64:dv,128:"pink",256:rgb(255,195,30),512:rgb(255,255,h1),1024:lg,2048:cb}
        for x in r(0,h4,25):
          for y in r(p,p+h1,25):number=chc([2,4,8,16,32,64,128,256,512,1024,2048]);aD(t.grp,Rct(x,y,25,25,fill=t.pC[number]),Lbl(number,x+12.5,y+12.5,size=35/l(s(number))))
        t.border=Rct(0,p,h4,h1,border=gy,fill=N);t.hitbox=Rct(0,p,h4,h1,fill=N);t.hitbox.type="twelfthbit";aD(t.grp,bR(t),Lbl("12TH BIT",h2,p+50,fill=bk,size=85,border=wh,bold=T),t.hitbox)
    class Dvd:
      def __init__(t,p):p*=h1;t.grp=Grp(Rct(0,p,h4,h1,fill=wh),visible=F);t.ball=Crc(351,p+44,5,fill=wh,rotateAngle=225);t.checker=Rct(351,p+44,60,28,align=cn,fill=N);t.logo=Grp(Ovl(186,152.2,355,52,fill=mo),Ovl(186,152.2,80,20,fill=wh),Ovl(65,48,178,112,fill=mo),Ovl(69,53.5,93,59,fill=wh),Ply(54,104,54,23,138,20,138,-9,-24,-9,-24,103,fill=wh),Ovl(292,58,182,95,fill=mo),Ovl(325,50,o2,82,fill=mo),Ovl(299,55.5,93,55,fill=wh),Ply(269,104,299,4,h2,4,h2,104,fill=wh),Ply(35,38,71,38,56,104,19,104,35,38,37,30,41.5,9,o8,9,199,70,247,9,T2,9,T2,30,269,30,266,38,302,38,286,104,250.5,104,266,38,269,30,185.5,127,152,30,37,30,fill=mo));t.logo.width,t.logo.height=60.1,28.2;t.logo.centerX,t.logo.centerY=351,p+44;t.hits=t.c=0;t.boundingbox=Grp(Lne(h4,p,0,p,lineWidth=5,fill=N),Lne(0,p+h1,h4,p+h1,lineWidth=5,fill=N),Lne(0,p,0,p+h1,lineWidth=5,fill=N),Lne(h4,p,h4,p+h1,lineWidth=5,fill=N));t.border=Rct(0,p,h4,h1,border=gy,fill=N);t.hitbox=Rct(0,p,h4,h1,fill=N);t.hitbox.type="dvd";aD(t.grp,t.ball,t.checker,t.logo,t.boundingbox,bR(t),t.hitbox)
      def oS(t):
        t.c+=1
        if(rnd(cX(t.ball))!=30)&(i(cY(t.ball)not in(i(bT(bR(t))-17),i(bT(bR(t))-18)))):
          t.ball.centerX,t.ball.centerY=gpd(cX(t.ball),cY(t.ball),rA(t.ball),2)
          for J in t.boundingbox:
            if(t.c>10)&hS(t.checker,J):
              t.c=0;t.ball.rotateAngle=2*a2(J.x1,J.y1,J.x2,J.y2)-rA(t.ball);t.hits+=1
              if odd(t.hits):
                for j in t.logo:j.fill=bl if fL(j)!=wh else fL(j)
              else:
                for j in t.logo:j.fill=mo if fL(j)!=wh else fL(j)
          t.logo.centerX,t.logo.centerY=t.checker.centerX,t.checker.centerY=cX(t.ball),cY(t.ball)
    class Tehtrisse:
      def __init__(t,p):
        p*=h1;t.grp=Grp(Rct(0,p,h4,h1),visible=F)
        for x in r(0,h4,25):aD(t.grp,Lne(x,p,x,p+h1,fill=wh))
        for y in r(p,p+h1,25):aD(t.grp,Lne(0,y+1,h4,y+1,fill=wh))
        border=grd6gy(tp);t.piece1=Grp(Rct(25,p-75,25,25,fill=cy,border=border),Rct(25,p-50,25,25,fill=cy,border=border),Rct(25,p-25,25,25,fill=cy,border=border));t.piece2=Grp(Rct(0,p-h1,25,25,fill=cy,border=border),Rct(25,p-h1,25,25,fill=cy,border=border),Rct(50,p-h1,25,25,fill=cy,border=border));t.Lbl=Lbl("EHTRISSE",237.5,p-75.5,fill=wh,size=65,bold=T);t.border=Rct(0,p,h4,h1,border=gy,fill=N);t.count=0;t.hitbox=Rct(0,p,h4,h1,fill=N);t.hitbox.type="tehtrisse";aD(t.grp,t.piece1,t.piece2,t.Lbl,bR(t),t.hitbox)
      def oS(t):
        t.count+=1
        if t.count>30:
          if(bT(t.piece1)!=bT(bR(t)))&evn(t.count):t.piece1.centerY+=25
          elif(bT(t.piece1)==bT(bR(t)))&(bT(t.piece2)!=bT(bR(t))-75)&evn(t.count):t.piece2.centerY+=25
          elif(bT(t.Lbl)<bT(bR(t))-25)&evn(t.count):t.Lbl.bottom+=25
          if bT(t.piece1)>=bT(bR(t)):t.piece1.bottom=bT(bR(t))
          if bT(t.piece2)>=bT(bR(t))-75:t.piece2.bottom=bT(bR(t))-75
    class Quail:
      def __init__(t,p):p*=h1;t.quail=Lbl("Quail_",115,p+50,fill=lm,font=mt,size=52,align=lf);t.quail.counter=0;t.border=Rct(0,p,h4,h1,border=gy,fill=N);t.hitbox=Rct(0,p,h4,h1,fill=N);t.hitbox.type="quail";t.grp=Grp(Rct(0,p,h4,h1),bR(t),t.quail,t.hitbox,visible=F)
      def oS(t):
        t.quail.counter+=1
        if t.quail.counter%15==10:
          if vL(t.quail)=="Quail_":t.quail.value="Quail"
          else:t.quail.value="Quail_"
          t.quail.left=115
    class Undead:
      def __init__(t,p):p*=h1;t.grp=Grp(Ply(221,-5,315,29,179,405,85,371,fill=grd(bk,bk,fg,start=lf)),visible=F);t.grp.rotateAngle=70;t.grp.top=p-0.7611;t.border=Rct(0,p,h4,h1,border=gy,fill=N);t.hitbox=Rct(0,p,h4,h1,fill=N);t.hitbox.type="undead";aD(t.grp,Lbl("LABYRINTH",h2,h1/3+p,fill=wh,size=30,font=cz),Lbl("OF THE UNDEAD",h2,h1/3*2+p,fill=wh,size=30,font=cz),bR(t),t.hitbox)
    class Toader:
      def __init__(t,p):p*=h1;t.b=Grp(Rct(0,p,h4,25,fill=db),Rct(0,p+25,h4,25,fill=lw),Rct(0,p+50,h4,25,fill=dy),Rct(0,p+75,h4,25,fill=lw));y=12.5+p;t.cr=Grp(Crc(0,y,12.5,fill=bw),Rct(0,y,75,25,align=lf,fill=bw),Crc(75,y,12.5,fill=tn,border=bw));t.cr.left=25;t.cr2=Grp(Crc(0,y,12.5,fill=bw),Rct(0,y,75,25,align=lf,fill=bw),Crc(75,y,12.5,fill=tn,border=bw));t.cr3=Grp(Ply(80,h1,o5,h1,o5,90,o2,90,115,80,h1,80,95,89,90,90),Arc(90,h1,20,20,-90,90));t.cr3.fill=chc([rd,on,yl,gr,bl,vi]);t.cr3.centerY,t.cr3.left=y+50,60;t.cr4=Grp(Ply(80,h1,125,h1,125,90,115,90,o1,80,h1,80,95,89,90,90),Arc(90,h1,20,20,-90,90));t.cr4.fill=chc([rd,on,yl,gr,bl,vi]);t.cr4.centerY,t.cr4.centerX=y+50,225;t.cr5=Grp(Ply(80,h1,140,h1,140,90,130,89,125,80,h1,80,95,89,90,90),Arc(90,h1,20,20,-90,90));t.cr5.fill=chc([rd,on,yl,gr,bl,vi]);t.cr5.centerY=y+50;t.cr5.centerX=t.cr2.right=T5;t.Lbl=Lbl("TOADER",h2,25+y,fill=bk,size=25);t.player=Rct(h2,y+75,25,25,fill=dg,align=cn);t.border=Rct(0,p,h4,h1,border=gy,fill=N);t.hitbox=Rct(0,p,h4,h1,fill=N);t.hitbox.type="toader";t.grp=Grp(t.b,t.cr,t.cr2,t.cr3,t.cr4,t.cr5,t.Lbl,t.player,bR(t),t.hitbox)
    class Bugreporting:
      def __init__(t,p):p*=h1;t.grp=Grp(Rct(0,p,h4,h1),Lbl("BUG REPORTING",h2,p+50,size=40,fill=lm,font=ot));t.border=Rct(0,p,h4,h1,border=gy,fill=N);t.hitbox=Rct(0,p,h4,h1,fill=N);t.hitbox.type="bugreporting";aD(t.grp,bR(t),t.hitbox)
    def __init__(t):
      t.active=F;t.grp=[];t.tehtrisse=t.Tehtrisse(3);t.dvd=t.Dvd(2);t.twelfthbit=t.Twelfthbit(4);t.codeclicker=t.Codeclicker(1);t.quail=t.Quail(6);t.undead=t.Undead(5);t.toader=t.Toader(0);t.bugreporting=t.Bugreporting(7);t.grp+=[t.tehtrisse,t.dvd,t.twelfthbit,t.codeclicker,t.quail,t.undead,t.toader,t.bugreporting];tF(bR(t.codeclicker));tF(bR(t.tehtrisse));tF(bR(t.twelfthbit));tF(bR(t.dvd));tF(bR(t.quail));tF(bR(t.undead));tF(bR(t.toader));tF(bR(t.bugreporting));t.aS=Grp(visible=F)
      for m in t.grp:
        for J in m.grp:aD(t.aS,J)
      t.hitboxes=Grp()
      for m in t.grp:aD(t.hitboxes,m.hitbox)
      aD(t.aS,t.hitboxes)
    def oS(t):
      if t.active:
        for m in t.grp:
          m.grp.visible=T
          try:m.oS()
          except:F
  class Game:
    class Codeclicker:
      def __init__(t):
        t.count=t.mini=t.money=t.cps=0;ap.background=bk;t.stepsPerSecond=20;t.wait=-1;t.hit=Image("https://cdn.freebiesupply.com/logos/large/2x/python-5-logo-png-transparent.png",0,0);t.hit.width/=20;t.hit.height/=20;t.hit.centerX=t.hit.centerY=h2
        t.outDict={0:c0+c0+c0,1:c0+c0+c1,2:c0+c0+c2,3:c0+c1+c0,4:c0+c1+c1,5:c0+c1+c2,6:c0+c2+c0,7:c0+c2+c1,8:c0+c22,9:c1+c0+c0,"c":c1+c0+c1,"p":c1+c0+c2,"d":c1+c1+c0,"m":c1+c1+c1,"t":c1+c1+c2}
        t.inDict={c0+c0+c0:0,c0+c0+c1:1,c0+c0+c2:2,c0+c1+c0:3,c0+c1+c1:4,c0+c1+c2:5,c0+c2+c0:6,c0+c2+c1:7,c0+c22:8,c1+c0+c0:9,c1+c0+c1:"c",c1+c0+c2:"p",c1+c1+c0:"d",c1+c1+c1:"m",c1+c1+c2:"t"}
        t.code=Grp();t.back1=Rct(0,0,h4,62.5,fill=wh);t.back2=Rct(0,337.5,h4,62.5,fill=wh);t.pointsUp=Grp(Rct(0,0,h2,62.5,fill=bl,opacity=60),Lbl("upgrade money per click",h1,12.5));t.n1=Lbl("1 $",h1,27.5);t.n2=Lbl(1,h1,42);t.pasiveUp=Grp(Rct(h2,0,h2,62.5,fill=rd,opacity=60),Lbl("upgrade pasive clicks",h3,12.5));t.n3=Lbl("1 $",h3,27.5);t.n4=Lbl(0,h3,42);t.boost=Grp(Rct(h2,337.5,h2,62.5,fill=lm,opacity=60));t.boost.alpha=Lbl("double profit for 20s",h3,362.5);t.n5=Lbl("500 $",h3,377.5);t.doubler=t.clickPoint=t.boost.price=1;t.e=Rct(0,338,h2,62,fill=yl,opacity=60);t.mL=Lbl("0  $",h1,366,size=69);t.sizeCheck=Rct(0,T3,h2,8,fill=N);t.doc={0:Q};t.string=[]
        for a in(Q,"c"):
          for b in(Q,"d","Vg","Tg","Qag","Qig","Sxg","Spg","Ocg","Nog"):
            for c in(Q,"U","D","T","Qa","Qi","Sx","Sp","Oc","No"):
              if c+b+a=="U":t.string+=["M"]
              elif c+b+a=="D":t.string+=["B"]
              elif c+b+a==Q:t.string+=["K"]
              else:t.string+=[a+b+c]
          for J in r(l(t.string)):t.doc[J+1]=t.string[J]
        t.grp=Grp(t.hit,t.back1,t.back2,t.pointsUp,t.n1,t.n2,t.pasiveUp,t.n3,t.n4,t.boost,t.boost.alpha,t.n5,t.e,t.mL,t.sizeCheck,visible=F);t.restartButton=Grp(Rct(h2,h3,372.5,50,align=cn,fill=gr),Lbl(rstINST,h2,h3,size=32));t.pM=Grp(Rct(0,0,h4,h4,fill=wh),Lbl("paused!",h2,h1,size=75),Lbl("click the python logo to earn money",h2,o8,size=20),Lbl("click the upgrades to buy them",h2,h2,size=20),t.restartButton,visible=F)
      def codes2(t):
        c="'"+chc([rd,on,yl,gr,lm,cy,bl,vi,pr,"None",wh,bl,gy])+"'";w,x,y,z,o,R=s(rr(h4)),s(rr(h4)),s(rr(10,51)),s(rr(10,51)),rr(8),rr(10)
        if o==0:S=f"Rct({w},{x},{y},{z},fill={c})"
        elif o==1:S=f"Ovl({w},{x},{y},{z},fill={c})"
        elif o==2:S=f"Crc({w},{x},{y},fill={c})"
        elif o==3:S=f"Lne({w},{x},{i(w)+i(y)},{i(x)+i(z)},fill={c})"
        elif o==4:S=f"RPy({w},{x},{y},{R},fill={c})"
        elif o==5:S=f"Str({w},{x},{y},{R},fill={c})"
        elif o==6:S=f"Arc({w},{x},{y},{z},{rr(T6)},{rr(T6)},fill={c})"
        elif o==7:
          v=Q
          for J in r(5):v+=chc([chr(j)for j in r(65,91)]+[chr(j)for j in r(97,123)])
          S=f"Lbl('{v}',{w},{x},fill={c})"
        return S
      def no(t,o):
        for J in r(l(s(o))//3+1):
          if o<=10**(3*(J+1))-1:
            if o<=h10:return f"{o//(10**(3*J))} {t.doc[J]}"
            else:
              n=s(o/(10**(3*J)))
              while(l(n)>4)|(n[-1]==".")|(n[-1]=="0"):n=n[0:-1]
              return f"{n} {t.doc[J]}"
      def oMP(t,x,y):
        if ap.paused==F:
          if hT(t.hit,x,y):
            t.mini+=1;t.money+=t.clickPoint*t.doubler
            if t.mini==5:
              t.mini=0;b=Lbl(t.codes2(),rr(h1,h3),h4,fill=lm,size=15)
              if lF(b)<=0:b.left=5
              elif rT(b)>=h4:b.right=395
              tB(b);aD(t.code,b)
          elif hT(t.pointsUp,x,y)&(t.money>=t.clickPoint**3):t.money-=t.clickPoint**3;t.clickPoint+=1;t.n1.value=t.no(t.clickPoint**3)+" $";t.n2.value=t.clickPoint
          elif hT(t.pasiveUp,x,y)&(t.money>=(t.cps+1)**3):t.money-=(t.cps+1)**3;t.cps+=1;t.n3.value=t.no((t.cps+1)**3)+" $";t.n4.value=t.cps
          elif hT(t.boost,x,y)&(t.money>=t.boost.price**2*h5)&(fL(t.boost)==lm):t.money-=t.boost.price**2*h5;t.boost.price+=1;t.n5.value=t.no(t.boost.price**2*h5)+" $";t.doubler=2;t.wait=t.count+h4;t.boost.fill=gy
        elif cT(t.restartButton,x,y):
          if rstrt():ap.restart.visible=F;t.count=t.mini=t.money=t.cps=t.n4.value=ap.paused=t.pM.visible=F;t.clickPoint=t.doubler=t.n2.value=t.boost.price=1;t.wait=-1;t.n1.value=t.n3.value="1 $";t.n5.value,t.mL.value="500 $","0  $";t.mL.size=69;cL(t.code)
      def oS(t):
        for J in t.code:
          J.centerY-=5
          if bT(J)<=0:rM(t.code,J)
        t.mL.value=t.no(t.money)+" $"
        for J in r(70):
          t.mL.size=70-J
          if(hS(t.mL,t.sizeCheck)|hS(t.mL,t.boost))==F:break
        t.count+=1
        if t.count%20==0:t.money+=t.cps*t.doubler
        if t.wait==t.count:t.doubler=1;t.boost.fill=lm
      def oKP(t,k):
        if k=="e":
          e=Q
          for J in r(rr(4,8)):e+=chc(arcade.allchars)
          for J in s(t.clickPoint):e+=t.outDict[i(J)]
          e+=t.outDict["c"]
          for J in s(t.cps):e+=t.outDict[i(J)]
          e+=t.outDict["p"]
          for J in s(t.boost.price):e+=t.outDict[i(J)]
          e+=t.outDict["d"]
          for J in s(t.money):e+=t.outDict[i(J)]
          e+=t.outDict["m"]
          for J in s(i(tme())):e+=t.outDict[i(J)]
          e+=t.outDict["t"]
          for J in r(rr(4,8)):e+=chc(arcade.allchars)
          gti(f'copy the text between the quotes "{e}". to load; press i & paste it in to load it.')
        elif"i"==k:
          z=gti("paste in the save and press ok.");t2=Q
          for J in z:
            if J in c0+c1+c2:t2+=s(J)
          z=Q
          for J in r(l(t2)//3):z+=s(t.inDict[t2[J*3:J*3+3]])
          t2=Q
          for J in z:
            if J not in"cpdmt":t2+=J
            elif J=="c":t.clickPoint=i(t2);t2=Q;t.n1.value=t.no(t.clickPoint**3)+" $";t.n2.value=t.clickPoint
            elif J=="p":t.cps=i(t2);t2=Q;t.n3.value=t.no((t.cps+1)**3)+" $";t.n4.value=t.cps
            elif J=="d":t.boost.price=i(t2);t2=Q;t.n5.value=t.no(t.boost.price**2*h5)+"$"
            elif J=="m":
              t.money=i(t2);t2=Q
              for j in r(70):
                t.mL.size=70-j
                if(hS(t.mL,t.sizeCheck)|hS(t.mL,t.boost))==F:break
            elif"t"==J:eT=i(tme())-i(t2);t2=Q;t.money+=eT*t.cps
        elif(k==esc)&ap.paused:ap.paused=t.pM.visible=F
        elif k==esc:ap.paused=t.pM.visible=T
        elif"r"==k:t.oMP(h2,h3)
    class Twelfthbit:
      def __init__(t):
        t.board=[0]*16+[0.5];t.youLost=Lbl(Q,h2,h2,size=75,fill=wh,border=bk,bold=T);t.youLost2=Lbl(Q,h2,275,size=75,fill=wh,border=bk,bold=T);t.message=Grp(Rct(0,o7,h4,o2,fill=wh),Lbl("use W.A.S.D or arrow keys.",h2,185,size=25),Lbl("Same number squares merge,",h2,215,size=25),Lbl(" and try to get to the highest number.",h2,245,size=25),Lbl("Use e to save and i to load.",h2,275,size=25));t.squareGrp=Grp();t.zeros=[];t.stepsPerSecond=0.5;t.ksn=0;t.pickColor={0:gy,2:rd,4:on,8:yl,16:gr,32:bl,64:dv,128:"pink",256:rgb(255,195,30),512:rgb(255,255,h1),1024:lg,2048:cb,4096:mb,8192:dr,16384:do,32768:"gold",65536:dg,131072:wh,62144:pr}
        for J in r(2):
          for j in r(16):
            if t.board[j]==0:t.zeros+=[j]
          t.board[chc(t.zeros)]=4if rr(10)>8else 2
        t.drawboard();tF(t.message);t.outD={0:c0*3,2:c00+c1,4:c00+c2,8:c0+c1+c0,16:c0+c11,32:c012,64:c0+c2+c0,128:c0+c2+c1,256:c0+c22,512:c1+c00,1024:c1+c0+c1,2048:c1+c0+c2,4096:c11+c0,8192:c1*3,16384:c11+c2,32768:c1+c2+c0,65536:c1+c2+c1,2**17:c1+c22,2**18:c2+c00," ":c2*3};t.inD={c0*3:0,c00+c1:2,c00+c2:4,c0+c1+c0:8,c0+c11:16,c012:32,c0+c2+c0:64,c0+c2+c1:128,c0+c22:256,c1+c00:512,c1+c0+c1:1024,c1+c0+c2:2048,c11+c0:4096,c1*3:8192,c11+c2:16384,c1+c2+c0:32768,c1+c2+c1:65536,c1+c22:2**17,c2+c00:2**18,c2*3:" "};t.restartButton=Grp(Rct(h2,315,372.5,50,align=cn,fill=gr),Lbl(rstINST,h2,315,size=32));t.pM=Grp(Rct(0,0,h4,h4,fill=wh),Lbl("paused!",h2,h1,size=75),visible=F);tF(t.message);t.grp=Grp(t.youLost,t.youLost2,t.squareGrp,t.message,visible=F);tF(t.pM)
      def __getitem__(t,f):return t.board[f]
      def check(t):
        a=0
        for J,v in enum(t.board):
          if J not in(3,7,11,15,16):a+=t[J+1]==v
          if J not in(12,13,14,15,16):a+=t[J+4]==v
          if J not in(0,4,8,12,16):a+=t[J-1]==v
          if J not in(0,1,2,3,16):a+=t[J-4]==v
        return(0in t.board)|a
      def drawboard(t):
        cL(t.squareGrp);tY=sX=0
        for J in r(16):
          b=c=bk
          if t[J]in(2.1,4.1):t.board[J]=i(t[J]);b=wh
          elif t[J]==131072:c=bk
          aD(t.squareGrp,Rct(sX,tY,h1,h1,fill=t.pickColor[t[J]],border=b))
          if t[J]!=0:aD(t.squareGrp,Lbl(t[J],sX+50,tY+50,size=o5/l(s(t[J]))-1,bold=T,fill=c))
          sX+=h1
          if sX==h4:sX=0;tY+=h1
        if sum(t[:16])>=262140:t.youLost.value="You Win!";tF(t.youLost)
        elif t.check()==F:t.youLost.value="You Lost!";t.youLost2.value=sum(t[:16]);tF(t.youLost);tF(t.youLost2);t.youLost.visible=t.youLost2.visible=T
      def oKP(t,k):
        if vS(t.pM):
          if k==esc:
            t.pM.visible=t.message.visible=F;tB(t.restartButton)
          elif"r"==k:
            if rstrt():
              t.board=[0]*16+[0.5];t.zeros=[];ap.restart.visible=F
              for J in r(2):
                for j in r(16):
                  if t[j]==0:t.zeros+=[j]
                t.board[chc(t.zeros)]=4if rr(10)>8else 2
              t.drawboard();t.youLost.visible=t.youLost2.visible=t.pM.visible=t.message.visible=t.restartButton.visible=F
        else:
          t.message.visible=action=F
          if"d"==k:t.oKP(rt)
          elif"a"==k:t.oKP(lf)
          elif"s"==k:t.oKP(dw)
          elif"w"==k:t.oKP(up)
          elif rt in k:
            for J in r(4):
              for j in r(15):
                if ez(t[j+1])&nz(t[j])&(j not in(3,7,11,15)):t.board[j+1]=t[j];t.board[j]=0;action=T
            for J in r(15,-1,-1):
              if(t[J+1]==t[J])&nz(t[j])&(j not in(3,7,11,15)):t.board[J+1]=t[J]*2;t.board[J]=0;action=T
            for J in r(4):
              for j in r(15):
                if ez(t[j+1])&nz(t[j])&(j not in(3,7,11,15)):t.board[j+1]=t[j];t.board[j]=0;action=T
          elif lf in k:
            for J in r(4):
              for j in r(15,-1,-1):
                if ez(t[j-1])&nz(t[j])&(j not in(0,4,8,12)):t.board[j-1]=t[j];t.board[j]=0;action=T
            for j in r(16):
              if(t[j-1]==t[j])&nz(t[j])&(j not in(0,4,8,12)):t.board[j-1]=t[j]*2;t.board[j]=0;action=T
            for J in r(4):
              for j in r(15,-1,-1):
                if ez(t[j-1])&nz(t[j])&(j not in(0,4,8,12)):t.board[j-1]=t[j];t.board[j]=0;action=T
          elif dw in k:
            for J in r(4):
              for j in r(12):
                if ez(t[j+4])&nz(t[j])&(j!=12):t.board[j+4]=t[j];t.board[j]=0;action=T
            for j in r(11,-1,-1):
              if(t[j]==t[j+4])&nz(t[j]):t.board[j+4]=t[j]*2;t.board[j]=0;action=T
            for J in r(4):
              for j in r(12):
                if ez(t[j+4])&nz(t[j])&(j!=12):t.board[j+4]=t[j];t.board[j]=0;action=T
          elif up in k:
            for J in r(4):
              for j in r(15,3,-1):
                if ez(t[j-4])&nz(t[j]):t.board[j-4]=t[j];t.board[j]=0;action=T
            for j in r(12):
              if(t[j]==t[j+4])&nz(t[j]):t.board[j+4]=t[j]*2;t.board[j]=0;action=T
            for J in r(4):
              for j in r(15,3,-1):
                if ez(t[j-4])&nz(t[j]):t.board[j-4]=t[j];t.board[j]=0;action=T
          t.zeros=[]
          for j in r(16):
            if t[j]==0:t.zeros+=[j]
          if action&nz(l(t.zeros)):t.board[chc(t.zeros)]=chc([2.1]*9+[4.1])
          t.drawboard()
          if"e"==k:
            t=Q
            for J in r(rr(4,8)):t+=chc(arcade.allchars)
            for J in r(16):t+=t.outD[t[J]]+t.outD[" "]
            for J in r(rr(4,8)):t+=chc(arcade.allchars)
            gti(f'copy the text betwen the quotes "{t}"then press ok.')
          elif"i"==k:
            st=gti("paste in the save and press ok.");t2=Q
            for J in st:
              if J in c012:t2+=J
            t=Q
            for J in r(l(t2)//3):t+=s(t.inD[t2[J*3:J*3+3]])
            p=Q;c=0
            for n in r(l(st)+1):
              if s(t)[n:n+1]!=" ":p+=t[n:n+1]
              else:t.board[c]=i(p);p=Q;c+=1
            t.drawboard()
          elif k==esc:t.pM.visible=t.message.visible=t.restartButton.visible=T;tF(t.message);tF(t.restartButton)
      def oMP(t,x,y):
        if cT(t.restartButton,x,y):t.oKP("r")
    class Dvd:
      def __init__(t):
        t.stepsPerSecond=60;t.ball=Crc(rr(h1,h3),rr(h1,h3),30,fill=N,rotateAngle=rr(0,T6,5));t.im1=Grp(Ovl(186,152.5,355,52),Ovl(70,48,168,112),Ply(60,104,60,103,56,103,56,104),Ovl(291,104,o8,96,align=bt),Ovl(325,9,o2,82,align=tp));t.im2=Grp(Ovl(o8,152.5,80,20),Ovl(69,24,93,59,align=tp),Ply(54,104,54,23,138,20,138,-10,-16,-10,-16,103),Ovl(299,83,93,55,align=bt),Ply(269,104,299,4,h2,4,h2,104));t.im2.fill=wh;t.im3=Grp(Ply(35,38,71,38,56,104,20-1,104),Ply(266,38,302,38,286,104,250.5,104),Ply(37,30,41.5,9,o8,9,199,70,247,9,T2,9,T2,30,269,30,185.5,127,152,30));t.im3.fill=t.im1.fill=mo;t.all=Grp(t.im1,t.im2,t.im3);t.all.width/=10/3;t.all.height/=10/3;aD(t.all,Lbl("TM",237,106,size=10,italic=T,bold=T,fill=mo));t.hits=t.c=t.target=0;t.check=Rct(cX(t.ball),cY(t.ball),wD(t.all),hG(t.all),align=cn,fill=N);t.border=Grp(Lne(h4,-6,0,-6,lineWidth=5),Lne(h4,0,h4,h4,lineWidth=5),Lne(h4,h4,0,h4,lineWidth=5),Lne(0,h4,0,0,lineWidth=5));t.back=Rct(0,0,h4,h4,fill=N,opacity=50);t.colors=[cy,rd,on,yl,bl,"hotPink",mo];t.order=[]
        for J in r(l(t.colors)):t.order+=[t.colors.pop(rr(l(t.colors)))]
        t.all.fill=t.order[6];t.im2.fill=ap.background=bk;t.grp=Grp(t.ball,t.all,bR(t),t.back,visible=F);t.restartButton=Grp(Rct(h2,h3,372.5,50,align=cn,fill=gr),Lbl(rstINST,h2,h3,size=32));t.pM=Grp(Rct(0,0,h4,h4,fill=wh),Lbl("paused!",h2,h1,size=75),Lbl("press right arrow to rotate the DVD clockwise",h2,o9,size=17),Lbl("press left arrow to rotate the DVD counterclockwise",h2,t1,size=17),t.restartButton,visible=F)
      def oS(t):
        t.c+=1;t.ball.centerX,t.ball.centerY=gpd(cX(t.ball),cY(t.ball),rA(t.ball),2)
        for J in bR(t):
          if hS(t.check,J)&(t.c>10):
            t.c=0;n=2*a2(J.x1,J.y1,J.x2,J.y2)-rA(t.ball);t.ball.rotateAngle=n;t.hits+=1;t.all.fill=t.order[t.hits];t.im2.fill=bk
            if t.hits==6:t.hits=0
        t.all.centerX,t.all.centerY=t.check.centerX,t.check.centerY=cX(t.ball),cY(t.ball)
        if(rnd(rT(t.check))>394)&(rnd(tP(t.check))<0):t.back.fill=grd(fg,bk,bk,start=tr);t.target=t.c+30
        elif(rnd(rT(t.check))>394)&(rnd(bT(t.check))>394):t.back.fill=grd(fg,bk,bk,start=br);t.target=t.c+30
        elif(rnd(lF(t.check))<6)&(rnd(tP(t.check))<0):t.back.fill=grd(fg,bk,bk,start=tf);t.target=t.c+30
        elif(rnd(lF(t.check))<6)&(rnd(bT(t.check))>394):t.back.fill=grd(fg,bk,bk,start=bf);t.target=t.c+30
        if t.target==t.c:t.back.fill=N
      def oKP(t,k):
        if ap.stepsPerSecond!=0:
          if k==rt or"d"==k:t.ball.rotateAngle+=5
          elif k==lf or"a"==k:t.ball.rotateAngle-=5
          elif k==esc:t.pM.visible=T;ap.stepsPerSecond=0
        elif k==esc:t.pM.visible=F;ap.stepsPerSecond=60
        elif"r"==k:t.oMP(h2,h3)
      def oMP(t,x,y):
        if cT(t.restartButton,x,y)&vS(t.restartButton):
          if rstrt():ap.restart.visible=F;t.pM.visible=F;ap.stepsPerSecond=60;t.ball.centerX,t.ball.centerY=rr(h1,h3),rr(h1,h3);t.oS();t.ball.rotateAngle=rr(72)*5
    class Toader:
      def __init__(t):
        t.player=Rct(h2,h4,25,25,fill=dg,align=bt);t.playing=T;t.wl=db;t.wr=rgb(30,144,255);t.rl=dy;t.rr=rgb(*[169]*3);t.g=lw;t.roads=[];t.sL=Grp()
        for J in r(16):aD(t.sL,Rct(0,375-(J*25),h4,25))
        for J in r(20):
          m=chc([t.rr]*4+[t.wl,t.wr]);t.roads+=[t.g]
          if m==t.rr:
            for J in r(4):t.roads+=[chc([t.rr,t.rl])]
          elif m==t.wl:t.roads+=[t.wl,t.wr]*2
          elif m==t.wr:t.roads+=[t.wr,t.wl]*2
        t.score=t.steps=t.count=t.index=t.stepsPerSecond=0;t.render();t.crs=Grp();tF(t.crs);t.youLostCover=Rct(0,0,h4,h4,fill=wh,opacity=77,visible=F);t.youLost=Lbl("You Lost",h2,h2,size=50);t.youLost2=Lbl(f"Press R To {rst}",h2,t5,size=25);t.youLost3=Lbl("Score:",h2,275,size=25);t.losing=Grp(t.youLostCover,t.youLost,t.youLost2,t.youLost3);tB(t.losing);t.firstPress=T;t.menu=Grp(Rct(0,0,h4,h4,fill=wh,opacity=77),Lbl("TOADER",h2,75,size=75),Lbl("Press Enter To Start",h2,o5,size=25),Rct(h2,275,125,125,align=cn,fill=N,border=bk,borderWidth=5));t.leftButton=Ply(t7,213,t7,338,315,275);t.rightButton=Ply(131,213,131,338,86,275);aD(t.menu,t.leftButton,t.rightButton);t.chimken=Grp()
        for J in r(o7,t4,15):aD(t.chimken,Rct(J,244,13,13,align=cn,rotateAngle=45,fill=sb))
        aD(t.chimken,Rct(o6,245,80,80,fill=wh),Rct(o6,245,16,50,fill=rd),Rct(192,245,16,50,fill=rd),Rct(224,245,16,50,fill=rd),Rct(o6,245,80,80,fill=N,border=bk,borderWidth=1),Rct(o5,225,h1,h1,fill=N));t.chicken=Grp(Rct(o7,225,80,70,fill=rgb(*[235]*3),border=bk,borderWidth=1),Rct(206,295,4,30,align=tp,fill=yl),Rct(226,295,4,30,align=tp,fill=yl),Rct(208,325,15,4,align=br,fill=yl),Rct(228,325,15,4,align=br,fill=yl),Crc(185,t5,5),Ply(o7,t5,o7,265,155,258.5,fill=on),Lne(205,253,t2,285),Lne(235,253,t2,285),Rct(o5,225,h1,h1,fill=N));t.chicken.visible=t.chimken.visible=F;t.egg=Grp(Rct(o5,225,h1,h1,fill=N),Arc(h2,285,50,60,90,o8,fill=yb),Arc(h2,285,50,80,-90,o8,fill=yb),visible=F);t.frog=Rct(0,0,h1,h1,fill=dg);t.pI=["t.frog","t.chicken","t.egg","t.chimken"];t.shownIcon=exec(t.pI[0]);t.shownIcon.centerX,t.shownIcon.centerY=h2,275;aD(t.menu,t.shownIcon)
        for i in range(80):t.oS()
        t.restartButton=Grp(Rct(h2,h3,372.5,50,align=cn,fill=gr),Lbl(rstINST,h2,h3,size=32));t.pM=Grp(Rct(0,0,h4,h4,fill=wh),Lbl("Paused",h2,h2,size=50),t.restartButton,Lbl("Press the arrow keys or W.A.S.D. to hop around",h2,t5,size=15),Lbl("try not to get hit by a cr or fall into the water",h2,265,size=15));tB(t.pM);t.grp=Grp(t.player,t.sL,t.crs,t.losing,t.menu,t.chimken,t.chicken,t.frog,t.shownIcon,t.pM,visible=F)
      def cr0(t,y,d):
        if d==-1:cr=Grp(Ply(80,h1,o4,h1,o4,90,o3,89,125,80,h1,80,95,89,90,90),Arc(90,h1,20,20,-90,90));cr.left=h4
        else:cr=Grp(Ply(o4,h1,80,h1,80,90,90,89,95,80,o2,80,125,89,o3,90),Arc(o3,h1,20,20,0,90));cr.right=0
        cr.fill=chc([rd,on,yl,gr,bl,vi]);cr.move=d;cr.bottom=y;return cr
      def cr1(t,y,d):
        if d==-1:cr=Grp(Ply(80,h1,o5,h1,o5,90,o2,90,115,80,h1,80,95,89,90,90),Arc(90,h1,20,20,-90,90));cr.left=h4
        else:cr=Grp(Ply(o4,h1,70,h1,70,90,h1,90,105,80,o2,80,125,89,o3,90),Arc(o3,h1,20,20,0,90));cr.right=0
        cr.fill=chc([rd,on,yl,gr,bl,vi]);cr.move=d;cr.bottom=y;return cr
      def cr2(t,y,d):
        if d==-1:cr=Grp(Ply(80,h1,125,h1,125,90,115,90,110,80,h1,80,95,89,90,90),Arc(90,h1,20,20,-90,90));cr.left=h4
        else:cr=Grp(Ply(125,h1,80,h1,80,*[90]*3,95,80,105,80,o1,89,115,90),Arc(115,h1,20,20,0,90));cr.right=0
        cr.fill=chc([rd,on,yl,gr,bl,vi]);cr.move=d;cr.bottom=y;return cr
      def log(t,y,d):
        l=rr(2,6)
        if d==-1:end=Crc(l*25,y,12);cr=Grp(Crc(0,y,12),Rct(0,y,l*25,24,align=lf),end);cr.left=h4
        else:end=Crc(l*25,y,12);cr=Grp(Crc(0,y,12),Rct(0,y,l*25,24,align=lf),end);cr.right=0
        cr.fill=bw;end.fill=tn;end.border=bw;cr.opacity=99;end.borderWidth=3;cr.move=d;cr.bottom=y;return cr
      def GR(t,y,d):
        if d==-1:cr=Grp(Crc(0,y,10));cr.left=h4
        else:cr=Grp(Crc(0,y,10));cr.right=0
        cr.fill=t.g;cr.move=d;cr.bottom=y;return cr
      def render(t):
        for J in r(16):cH(t.sL)[J].fill=t.roads[J]
      def oS(t):
        if t.count<2:
          t.count+=1
          for J in t.sL:
            if fL(J)==t.rr:
              crx=exec(f"t.cr{rr(3)}({bT(J)},1)");crx.centerX=rr(60,T4,80)
              while hS(crx,t.crs):crx.centerX=rr(60,T4,80)
              aD(t.crs,crx)
            elif fL(J)==t.rl:
              crx=exec(f"t.cr{rr(3)}({bT(J)},-1)");crx.centerX=rr(60,T4,80)
              while hS(crx,t.crs):crx.centerX=rr(60,T4,80)
              aD(t.crs,crx)
            elif fL(J)==t.wl:crx=exec(f"t.log({bT(J)},-1)");crx.centerX=rr(60,T4,80);aD(t.crs,crx)
            elif fL(J)==t.wr:crx=exec(f"t.log({bT(J)},1)");crx.centerX=rr(60,T4,80);aD(t.crs,crx)
            elif fL(J)==t.g:
              crx=exec(f"t.GR({bT(J)},-1)");crx.centerX=rr(60,T4,80)
              while hS(crx,t.crs):crx.centerX=rr(60,T4,80)
              aD(t.crs,crx)
        if t.playing:
          t.steps+=1
          for c in t.crs:
            if c.move<0:c.centerX-=5
            else:c.centerX+=5
            if lF(c)>h4:
              y=s(bT(c))
              if oP(c)!=99:
                if fL(c)!=t.g:rM(t.crs,c);c=exec(f"t.cr{rr(3)}({y},1)")
                else:rM(t.crs,c);c=exec("t.GR("+y+",1)")
                if hS(c,t.crs):c.left=405
                aD(t.crs,c)
              else:rM(t.crs,c);c=exec("t.log("+y+",1)");aD(t.crs,c)
            elif rT(c)<0:
              y=s(bT(c))
              if oP(c)!=99:
                if fL(c)!=t.g:rM(t.crs,c);c=exec("t.cr"+s(rr(3))+"("+y+",-1)")
                else:rM(t.crs,c);c=exec("t.GR("+y+",-1)")
                if hS(c,t.crs):c.right=-5
                aD(t.crs,c)
              else:rM(t.crs,c);c=exec("t.log("+y+",-1)");aD(t.crs,c)
          if hS(t.player,t.crs):
            if hE(t.crs,cX(t.player),cY(t.player))!=N:
              if oP(hE(t.crs,cX(t.player),cY(t.player)))==99:
                if hE(t.crs,cX(t.player),cY(t.player)).move<0:t.player.centerX-=5
                else:t.player.centerX+=5
              elif fL(hE(t.crs,cX(t.player),cY(t.player)))!=t.g:tF(t.losing);t.youLost3.value="Score: "+s(t.score);t.playing=F
          else:
            if(cY(t.player)==362.5)&((fL(cH(t.sL)[1])==t.wr)|(fL(cH(t.sL)[1])==t.wl)):tF(t.losing);t.youLost3.value="Score: "+s(t.score);t.playing=F
            elif(cY(t.player)==387.5)&((fL(cH(t.sL)[0])==t.wr)|(fL(cH(t.sL)[0])==t.wl)):tF(t.losing);t.youLost3.value="Score: "+s(t.score);t.playing=F
          if rT(t.player)>h4:t.player.right=h4
          elif lF(t.player)<0:t.player.left=0
      def oKP(t,k):
        k=k.lower()
        if(k=="r")&(t.playing==F):
          if vL(t.youLost3)=="Score:":
            if rstrt():t.youLost3.value="null";t.oKP("r")
          else:
            ap.restart.visible=F;t.youLost3.value="Score:";tB(t.losing);t.playing=T;t.roads=[]
            for J in r(20):
              m=chc([t.rr,t.rr,t.rr,t.rr,t.wl,t.wr])
              t.roads+=[t.g]
              if m==t.rr:
                for j in r(4):t.roads+=[chc([t.rr,t.rl])]
              elif m==t.wl:t.roads+=[t.wl,t.wr,t.wl,t.wr]
              elif m==t.wr:t.roads+=(t.wr,t.wl,t.wr,t.wl)
            t.render();t.menu.visible=T;t.player.width=t.player.height=h1;t.shownIcon=exec(t.pI[0]);t.shownIcon.centerX,t.shownIcon.centerY=h2,275;t.player=Rct(h2,h4,25,25,fill=dg,align=bt);t.player.visible=F;cL(t.crs);ap.stepsPerSecond=t.steps=t.count=t.score=0;t.firstPress=T
            for i in range(80):t.oS()
            for i in range(4):t.index-=1;t.shownIcon.visible=F;t.shownIcon=exec(t.pI[t.index%l(t.pI)]);t.shownIcon.centerX,t.shownIcon.centerY=h2,275;aD(t.menu,t.shownIcon)
            t.oKP(esc);t.oKP(esc);tB(t.player)
            ap.restart.visible=F
        if t.playing:
          if ap.stepsPerSecond!=0:
            if k=="w":t.oKP(up)
            elif k=="s":t.oKP(dw)
            elif k=="a":t.oKP(lf)
            elif k=="d":t.oKP(rt)
            elif k==up:
              if t.firstPress:t.firstPress=F;t.player.centerY-=25
              else:t.roads+=[t.roads.pop(0)];t.crs.centerY+=25;t.score+=1
              t.render()
              for cr in t.crs:
                if tP(cr)>=h4:
                  cx=cX(cr)
                  if cx>h4 or cx<0:cx=rr(60,T4,80)
                  rM(t.crs,cr);p15=cH(t.sL)[15]
                  if fL(p15)==t.rr:cr=exec("t.cr"+s(rr(3))+"("+s(bT(p15))+",1)");cr.centerX=cx;aD(t.crs,cr)
                  elif fL(p15)==t.rl:cr=exec("t.cr"+s(rr(3))+"("+s(bT(p15))+",-1)");cr.centerX=cx;aD(t.crs,cr)
                  elif fL(p15)==t.wl:cr=exec("t.log("+s(bT(p15))+",-1)");cr.centerX=cx;aD(t.crs,cr)
                  elif fL(p15)==t.wr:cr=exec("t.log("+s(bT(p15))+",1)");cr.centerX=cx;aD(t.crs,cr)
                  elif fL(p15)==t.g:cr=exec("t.GR("+s(bT(p15))+",-1)");cr.centerX=cx;aD(t.crs,cr)
            elif(k==dw)&(t.firstPress==F):t.firstPress=T;t.player.centerY+=25
            elif k==rt:t.player.centerX+=25
            elif k==lf:t.player.centerX-=25
          elif(k==ent or tab==k)&(bT(t.player)==h4):t.menu.visible=t.player.visible=F;t.player=exec(t.pI[t.index%l(t.pI)]);t.player.visible=t.player.visible=T;t.player.width,t.player.height,t.player.centerX,t.player.centerY=25,25,h2,387.5;tF(t.player);ap.stepsPerSecond=30  
          if(k==esc)&(vL(t.youLost3)=="Score:"):tF(t.pM);t.player.visible=t.playing=t.shownIcon.visible=F;ap.restart.visible=F
        elif(k==esc)&(vL(t.youLost3)=="Score:"):tB(t.pM);t.player.visible=t.playing=t.shownIcon.visible=T;ap.restart.visible=T
        if("Score: "in vL(t.youLost3))&(k==esc):
            if ap.restart.visible:tB(t.pM);t.player.visible=t.shownIcon.visible=T;ap.restart.visible=T
            else:tF(t.pM);t.player.visible=t.shownIcon.visible=F;ap.restart.visible=F


      def oMP(t,x,y):
        if ap.stepsPerSecond==0:
          if hT(t.leftButton,x,y):t.index+=1;t.shownIcon.visible=F;t.shownIcon=exec(t.pI[t.index%l(t.pI)]);t.shownIcon.centerX,t.shownIcon.centerY=h2,275;aD(t.menu,t.shownIcon)
          elif hT(t.rightButton,x,y):t.index-=1;t.shownIcon.visible=F;t.shownIcon=exec(t.pI[t.index%l(t.pI)]);t.shownIcon.centerX,t.shownIcon.centerY=h2,275;aD(t.menu,t.shownIcon)
        elif cT(t.restartButton,x,y):t.oKP("r")
    class Undead:
      def __init__(t):
        t.bG=Rct(0,0,h4,h4,fill=grd(bk,bk,fg,start=tf));t.cG=t.gun="AR";t.gT=N;t.gS=15;t.R=t.bS=t.kills=t.Kills=t.dM=t.time=t.secs=t.mins=t.yAngle=t.restart=t.S=t.LS=t.paused=t.MT=F;t.timePlayed="00:00";t.stepsPerSecond=10;t.TS=1;t.tSL=Lbl("click to start",275,T3,size=25,rotateAngle=-20,font=ms,fill=wh);t.tSG=Grp(Lbl("Labyrinth of the Undead",198,145,size=28,rotateAngle=-14,fill=wh,font=ms,bold=T,italic=T),t.tSL,visible=F);t.il1=Lbl("created by:",275,h1,rotateAngle=20,size=20,font=ms,fill=wh,visible=F,opacity=0);t.il2=Lbl("BirdFace Studios",h2,h2,rotateAngle=-5,size=35,font=ms,fill=wh,visible=F,opacity=0);t.il3=Lbl("Made with Python",h2,o4,size=30,font=ms,fill=wh,visible=F,opacity=0);t.il4=Lbl("And the CMU graphics module",h2,o7,size=20,font=ms,fill=wh,visible=F,opacity=0);t.ilo1=Image("https://www.freeiconspng.com/uploads/bird-silhouette-sitting-bird-png-22.png",o5,250,visible=F,opacity=0);t.ilo1.width//=8;t.ilo1.height//=8;t.ilo2=Image("https://cdn.freebiesupply.com/logos/large/2x/python-5-logo-png-transparent.png",133.5,t3,visible=F,opacity=0);t.ilo2.width//=18;t.ilo2.height//=18;t.sB2=Lbl("skip",45,30,font=ms,fill=wh,size=20,rotateAngle=-15,visible=F);t.sBCD=Rct(0,0,80,60,visible=F);t.zG=Grp();t.bgr=Grp();t.aG=Grp();t.player=Grp(Ovl(h2,h2,30,17,fill=rgb(*[50]*3)),Crc(h2,h2,5,fill="lemonchiffon"));t.Gun=Grp(Rct(h2,h2,10,20,fill=gy,border=bk,align=bf),Rct(h2,h2,10,20,fill=N,align=tr));t.Light=Ply(h2,h2,o3,70,155,35,h2,20,245,35,270,70,t3,172,225,185,229,194,t3,205,227,217,t2,225,211,229,h2,231,189,229,o8,225,173,217,o7,205,171,194,175,185,o7,172,o3,70,h2,h2,*[h8]*3+[-h4]*4+[h8]*3,opacity=100,fill=rgb(*[20]*3));t.pG=Grp(t.player,t.Gun,t.Light,visible=F);t.mazeW=Grp();t.xAngle=h2;t.ammo=h1;t.health=10;t.hC=Lbl(t.health,50,22,size=13,fill=gy,font=ms);t.ammoC=Lbl(t.ammo,110,22,size=13,fill=wh,font=ms);t.CounterGrp=Grp(Ovl(30,22,10,6,fill=rd,rotateAngle=-45),Ovl(25,22,10,6,fill=rd,rotateAngle=45),Rct(85,15,7,14,fill=yl,border=bk),t.hC,t.ammoC,visible=F);t.ls1=Lbl("You Lose!",h2,o4,size=30,fill=wh,font=ms,bold=T,visible=F);t.ls2=Lbl("Play Again?",h3,T3,size=25,fill=wh,font=ms,bold=T,italic=T,rotateAngle=-25,visible=F);t.pA=Rct(h2,270,h2,o3,visible=F);t.ls3=Lbl("Stats:",h2,o8,size=20,fill=wh,font=ms,visible=F);t.ls4=Lbl("Score:",o3,t1,size=13,align=lf,fill=wh,font=ms);t.ls5=Lbl("Kilt.ls:",o3,t2,size=13,align=lf,fill=wh,font=ms);t.ls6=Lbl("Shots Fired:",o3,t3,size=13,align=lf,fill=wh,font=ms);t.ls7=Lbl("Accuracy:",o3,240,size=13,align=lf,fill=wh,font=ms);t.ls8=Lbl(" Distance Moved: ",o3,250,size=13,align=lf,fill=wh,font=ms);t.ls9=Lbl("Kilt.ls Per Shot: ",o3,260,size=13,align=lf,fill=wh,font=ms);t.ls0=Lbl("Time Played: ",o3,270,size=13,align=lf,fill=wh,font=ms);t.lsg=Grp(t.ls4,t.ls5,t.ls6,t.ls7,t.ls8,t.ls9,t.ls0,visible=F);t.pSR=Lbl(rst,125,145,size=20,fill=wh,font=ms);t.pSCD1=Rct(75,135,h1,20,visible=F);
        
        t.pSS=Lbl("Settings",125,165,size=20,fill=wh,font=ms);t.pSCD2=Rct(75,155,h1,20,visible=F);t.pSG=Grp(Rct(0,0,h4,h4,fill=rgb(*[10]*3),opacity=35),Lbl("Paused",165,h1,size=45,fill=wh,font=ms,rotateAngle=-6),t.pSR,t.pSS,Label("use W.A.S.D or arrows to move arround",200,190,size=15,fill=wh,font=ms,bold=T),Label("look around using your mouse",200,205,size=15,fill=wh,font=ms,bold=T),Label("press lmb or space to shoot",200,220,size=15,fill=wh,font=ms,bold=T),visible=F);t.nx=t.ny=5;t.ix=t.iy=t.x1=t.y1=t.y2=0;t.maze=t.Maze(t.nx,t.ny,t);t.Maze.make(t.maze,t);t.x2=-h4/t.nx
        
        for J in r(t.nx*t.ny*2+t.ny):
          if"--+"==s(t.maze)[t.MT*3:(t.MT+1)*3]:t.x1+=h4/t.nx;t.x2+=h4/t.nx;t.MT+=1;aD(t.mazeW,Lne(t.x1,t.y1,t.x2,t.y2,opacity=90,lineWidth=3))
          if"  +"==s(t.maze)[t.MT*3:(t.MT+1)*3]:t.x1+=h4/t.nx;t.x2+=h4/t.nx;t.MT+=1
          if"   "==s(t.maze)[t.MT*3-1:t.MT*3+2]:t.x1+=h4/t.nx;t.x2+=h4/t.nx;t.MT+=1
          if"  |"==s(t.maze)[t.MT*3-1:t.MT*3+2]:t.x1+=h4/t.nx;t.x2+=h4/t.nx;aD(t.mazeW,Lne(t.x1,t.y1,t.x2,t.y2+h4/t.ny,opacity=90,lineWidth=3));t.MT+=1
          if"V" in s(t.maze)[t.MT*3-1:t.MT*3+2]:t.x1=0;t.x2=0;t.MT+=1
          if"dwn"==s(t.maze)[t.MT*3:t.MT*3+3]:t.y1+=h4/t.ny;t.y2+=h4/t.ny;t.x1=0;t.x2=-h4/t.nx;t.MT+=1
        t.mazeW.visible=F
        
      def oS(t):
        if t.restart==F:
          if t.paused==F:
            t.pSG.visible=F
            if(t.TS==0)&(t.LS==0):
              t.time+=1;t.secs+=0.1
              if t.secs>=60:t.secs-=60;t.mins+=1
              t.sB2.visible=F
              t.bG.fill=rgb(*[60]*3);t.timePlayed=f"{s(t.mins).zfill(2)}:{s(i(t.secs)).zfill(2)}";t.ammoC.value=rnd(t.ammo);t.hC.value=rnd(t.health);
              t.pG.visible=t.mazeW.visible=t.CounterGrp.visible=T
              t.tSG.visible=t.il1.visible=t.il2.visible=t.il3.visible=t.il4.visible=t.ilo1.visible=t.ilo2.visible=t.lsg.visible=t.ls1.visible=t.ls2.visible=t.ls3.visible=F;
              t.il1.opacity=t.il2.opacity=t.il3.opacity=t.il4.opacity=t.ilo1.opacity=t.ilo2.opacity=0;
              if vL(t.hC)!=0:
                if t.Kills>=1:t.kills+=1;t.Kills-=1
                for J in t.aG:
                  if hS(J,t.player):rM(t.aG,J);del J;t.ammo+=rr(3,10)
                if t.cG=="Melee":t.gS=10;t.gT=10
                elif t.cG=="Sword":t.gS=-15;t.gT=4;tF(t.player);tF(t.Gun)
                elif t.cG=="Pistol":t.gS=20;t.gT=4
                elif t.cG=="SMG":t.gS=10;t.gT=1
                elif t.cG=="Sniper":t.gS=15;t.gT=10
                elif t.cG=="AR":t.gS=20;t.gT=rr(2,5)
                elif t.cG=="Shotgun":t.gS=15;t.gT=20
                elif t.cG=="RPG":t.gS=10;t.gT=60
                elif t.cG=="Tracker":t.gS=24;t.gT=20
                elif t.cG=="WallBreaker":t.gS=22;t.gT=10
                for b in t.bgr:
                  if b.type=="rpge":t.gS=0
                  if b.type=="sniper":
                    b.centerX,b.centerY=gpd(cX(b),cY(b),rA(b),t.gS)
                    if(hS(b,t.bg)==F)&(b.type!="sword"):rM(t.bgr,b);del b;continue
                    if hS(b,t.mazeW):
                      if b.type not in"sniperswordrpgetrackerwallbreaker":
                        rM(t.bgr,b)
                        if b.type=="rpg":t.rpge(cX(b),cY(b))
                        del b;continue
                  if ds(cX(b),cY(b),cX(t.Gun),cY(t.Gun))>=b.ds:rM(t.bgr,b);del b;continue
                  for z in t.zG:
                    if hS(b,z):
                      rM(t.zG,z) 
                      if b.type not in"swordrpgesniper":rM(t.bgr,b);b.des=T
                      if t.cG=="Shotgun":t.Kills+=0.2
                      else:t.kills+=1
                      xoff,yoff=rr(-5,5),rr(-5,5);aD(t.aG,Grp(Rct(cX(z)-5+xoff,cY(z)+yoff,5,10,fill=yl,border=bk,borderWidth=1.5),Rct(cX(z)+xoff,cY(z)+yoff,5,10,fill=yl,border=bk,borderWidth=1.5),Rct(cX(z)+5+xoff,cY(z)+yoff,5,10,fill=yl,border=bk,borderWidth=1.5)));del xoff,yoff,z
                  if b.des:del b;continue
                  if b.type=="tracker":b.rotateAngle=a2(cX(b),cY(b),t.xAngle,t.yAngle)
                  b.centerX,b.centerY=gpd(cX(b),cY(b),rA(b),t.gS)
                  if b.type=="wallbreaker":
                    for w in t.mazeW:
                      if hS(b,w):rM(t.bgr,b);b.des=T;rM(t.mazeW,w);del w
                    if b.des:del b
                  if(hS(b,t.bG)==F)&(b.type!="sword"):
                    rM(t.bgr,b)
                    del b;continue
                  if hS(b,t.mazeW):
                    if b.type not in("sniper","sword","rpge","tracker","wallbreaker"):
                      rM(t.bgr,b)
                      if b.type=="rpg":t.rpge(cX(b),cY(b))
                      del b;continue
                  if(b.type=="rpge")&(t.R+30<=t.time):rM(t.bgr,b);del b;continue
                  if(b.type=="tracker")&(t.R+110<=t.time):rM(t.bgr,b);del b;continue
                for z in t.zG:
                  if ds(cX(z),cY(z),cX(t.player),cY(t.player))<=o5:
                    if hS(z,t.mazeW)==F:z.rotateAngle=a2(cX(z),cY(z),cX(t.player),cY(t.player));z.centerX,z.centerY=gpd(cX(z),cY(z),rA(z),2)
                    elif t.time%15==0:
                      rand=rr(4)
                      if rand==0:z.centerY-=5
                      elif rand==1:z.centerY+=5
                      elif rand==2:z.centerX+=5
                      elif rand==3:z.centerX-=5
                  else:
                    rand=rr(5)
                    if rand==1:
                      z.centerY-=5
                      if hS(z,t.mazeW)|(cY(z)<0):z.centerY+=5
                    if rand==2:
                      z.centerY+=5
                      if hS(z,t.mazeW)|(cY(z)>h4):z.centerY-=5
                    if rand==3:
                      z.centerX+=5
                      if hS(z,t.mazeW)|(cX(z)>h4):z.centerX-=5
                    if rand==4:
                      z.centerX-=5
                      if hS(z,t.mazeW)|(cX(z)<0):z.centerX+=5
                  for b in t.bgr:
                    if hS(b,z):
                      rM(t.zG,z);z.des=T
                      if b.type=="rpg":t.rpge(cX(b),cY(b))
                      t.kills+=1;xoff,yoff=rr(-5,5),rr(-5,5);aD(t.aG,Grp(Rct(cX(z)-5+xoff,cY(z)+yoff,5,10,fill=yl,border=bk,borderWidth=1.5),Rct(cX(z)+xoff,cY(z)+yoff,5,10,fill=yl,border=bk,borderWidth=1.5),Rct(cX(z)+5+xoff,cY(z)+yoff,5,10,fill=yl,border=bk,borderWidth=1.5)));del xoff,yoff
                      if b.type not in ["sniper","sword","rpge","tracker"]:rM(t.bgr,b);del b
                  if z.des:del z;continue
                  if hS(z,t.player):t.health-=0.2
                if rnd(20-(t.time/h5))!=0:
                  if t.time%a(rnd(20-(t.time/h5)))==0:
                    z=Grp(Ovl(h2,h2,30,17,fill=rgb(*[40]*3)),Crc(h2,h2,5,fill=dg),visible=F);z.des=F;z.centerX,z.centerY=rr(40,h4,80),rr(40,h4,80);z.rotateAngle=a2(cX(z),cY(z),cX(t.player),cY(t.player))
                    if(ds(cX(t.player),cY(t.player),cX(z),cY(z))>=20)&hS(z,t.Light):z.visible=T;aD(t.zG,z)
                elif t.time%1==0:
                  z=Grp(Ovl(h2,h2,30,17,fill=rgb(*[40]*3)),Crc(h2,h2,5,fill=dg),visible=F);z.des=F;z.centerX,z.centerY=rr(0,h4),rr(0,h4);z.rotateAngle=a2(cX(z),cY(z),cX(t.player),cY(t.player))
                  if(ds(cX(t.player),cY(t.player),cX(z),cY(z))>=20)&hS(z,t.Light):z.visible=T;aD(t.zG,z)
              else:t.LS=1
            if t.LS==1:
              t.bG.fill=grd(bk,bk,fg,start=tf);t.tSG.visible=t.il1.visible=t.il2.visible=t.il3.visible=t.il4.visible=t.ilo1.visible=t.ilo2.visible=t.sB2.visible=t.pG.visible=t.zG.visible=t.bgr.visible=t.aG.visible=t.mazeW.visible=t.CounterGrp.visible=F;t.lsg.visible=t.ls1.visible=t.ls2.visible=t.ls3.visible=T
              if t.ls2.size<32:t.ls2.size+=1.5
              else:t.ls2.size=25
              t.ls4.value=f"Score:      {(t.kills*o5)+(t.ammo*2)+(t.time // 5)}";t.ls5.value=f"Kills:      {t.kills}";t.ls6.value=f"Shots Fired:  {t.bS}"
              if t.kills==0:t.ls7.value="Accuracy:     0.00"
              elif t.kills>=t.bS:t.ls7.value="Accuracy:     100.00"
              else:t.ls7.value=f"Accuracy:     {i(rnd((t.kills/t.bS)*10000))/h1}%"
              t.ls8.value=f"Distance Moved:{t.dM}"
              if t.kills==0:t.ls9.value="Kills Per Shot: 0"
              elif t.bS==0:t.ls9.value=f"Kills Per Shot: {t.kills}"
              else:t.ls9.value=f"Kills Per Shot: {rnd((t.kills/t.bS)*h10)/h1}"
              t.ls0.value=f"Time Played:  {t.timePlayed}"
              for J in t.lsg:J.left=o3
            if(t.TS==1)&(t.LS==0):
              t.bG.fill=grd(bk,bk,fg,start=tf);t.tSG.visible=T
              if t.tSL.size<=30:t.tSL.size+=1
              elif t.tSL.size>30:t.tSL.size=25
              t.lsg.visible=t.ls1.visible=t.ls2.visible=t.ls3.visible=F
            if(t.TS==2)&(t.LS==0):
              t.sB2.visible=t.il1.visible=t.il2.visible=t.ilo1.visible=T;t.tSG.visible=t.lsg.visible=t.ls1.visible=t.ls2.visible=t.ls3.visible=F
              if t.il1.opacity<h1:t.il1.opacity+=10
              if t.il2.opacity<h1:t.il2.opacity+=10
              if t.ilo1.opacity<h1:
                t.ilo1.opacity+=2.5
                if t.ilo1.opacity==h1:t.TS=3
            if(t.TS==3)&(t.LS==0):
              t.il1.visible=t.il2.visible=F;t.il1.opacity=t.il2.opacity=0;t.il3.visible=t.il4.visible=T
              if t.il3.opacity<h1:t.il3.opacity+=10
              if t.il4.opacity<h1:t.il4.opacity+=10
              if t.ilo1.opacity>0:
                t.ilo1.opacity-=5
                if t.ilo1.opacity==0:t.ilo1.visible=F
              t.ilo2.visible=T
              if t.ilo2.opacity<h1:
                t.ilo2.opacity+=2.5
                if t.ilo2.opacity==h1:t.TS=4
            if(t.TS==4)&(t.LS==0):
              t.il3.visible=t.il4.visible=F;t.il3.opacity=t.il4.opacity=0
              if t.ilo2.opacity>0:
                t.ilo2.opacity-=4
                if t.ilo2.opacity==0:t.ilo2.visible=F;t.TS=0
          elif t.paused:
            t.pSG.visible=T
            if t.S==F:t.pSR.left=t.pSS.left=80;t.pSR.visible=t.pSS.visible=T
            elif t.S:t.pSR.visible=t.pSS.visible=F
        elif t.restart:t.health=10;t.ammo=h1;cL(t.zG);cL(t.bgr);cL(t.aG);t.TS=t.aG.visible=t.bgr.visible=t.zG.visible=T;t.player.centerX=t.player.centerY=t.Gun.centerX=t.Gun.centerY=h2;t.bS=t.LS=t.kls=t.bulletsFired=t.dM=t.time=t.secs=t.mins=t.R=t.pG.visible=t.mazeW.visible=t.CounterGrp.visible=t.pSG.visible=t.paused=t.S=t.restart=F
      def oMM(t,x,y):
        if(t.paused==F)&(t.LS==0):t.xAngle,t.yAngle=x,y;t.Gun.rotateAngle=t.Light.rotateAngle=t.player.rotateAngle=a2(cX(t.pG),cY(t.pG),x,y);t.Light.centerX,t.Light.centerY=t.Gun.centerX,t.Gun.centerY=cX(t.player),cY(t.player)
      def oMP(t,x,y):
        if t.paused==F:
          if t.TS&(t.LS==0)&cT(t.bG,x,y):t.TS=2;t.tSG.visible=F
          elif(t.TS in(2,3,4))&(t.LS==0)&cT(t.sBCD,x,y):t.TS=0
          elif t.LS==0:t.oMM(x,y);t.oKH([spc])
          elif t.LS&cT(t.pA,x,y):t.restart=T
        else:
          if cT(t.pSCD1,x,y)&(t.S==F):
              if rstrt():t.restart=T;ap.restart.visible=F
          if cT(t.pSCD2,x,y):t.S=T
      def oKP(t,k):
        k=k.lower()
        if(t.LS==0)&(t.TS==0)&(t.restart==F):
          if k=="q":
            if t.cG=="Melee":t.cG=t.gun;t.Gun.visible=T
            else:t.cG="Melee";t.Gun.visible=F
          elif k in(esc,tab):
            if t.paused:
              if t.S:
                  t.S=F
                  ap.restart.visible=False
              else:t.paused=F
            else:t.paused=T
          elif k=="p":
            if t.paused:t.paused=t.S
            else:t.paused=T
          elif(k=="s")&t.paused:t.S=t.S==F
      def oKH(t,k):
        for K in k:K=K.lower()
        if t.paused==F:
          if(t.TS==0)&(t.LS==0):
            if("w"in k or up in k)&(cY(t.pG)>10):
              t.pG.centerY-=5;t.dM+=1
              if hS(t.player,t.mazeW):t.pG.centerY+=5
            if("s"in k or dw in k)&(cY(t.pG)<T9):
              t.pG.centerY+=5;t.dM+=1
              if hS(t.player,t.mazeW):t.pG.centerY-= 5
            if("a"in k or lf in k)&(cX(t.pG)>10):
              t.pG.centerX-=5;t.dM+=1
              if hS(t.player,t.mazeW):t.pG.centerX+=5
            if("d"in k or rt in k)&(cX(t.pG)<T9):
              t.pG.centerX+=5;t.dM+=1
              if hS(t.player,t.mazeW):t.pG.centerX-=5
            if spc in k:
              if t.R+t.gT<=t.time:
                if t.cG=="Melee":t.shoot(7,14,0,1,0,0);t.R=t.time
                elif t.ammo>=1:
                  if t.cG=="Sword":t.shoot(0,0,158,159,0.5,0)
                  elif t.cG=="Pistol":t.shoot(5,10,-2,2,1,1)
                  elif t.cG=="SMG":t.shoot(4,7,-30,30,2,1)
                  elif t.cG=="Sniper":t.shoot(5,16,0,1,5,1)
                  elif t.cG=="AR":t.shoot(5,12,-7,7,2,1)
                  elif t.cG=="Shotgun":t.shoot(5,10,-7,7,1,0.2);t.shoot(5,10,0,14,1,0.2);t.shoot(5,10,-14,0,1,0.2);t.shoot(5,10,7,21,1,0.2);t.shoot(5,10,-21,7,1,0.2)
                  elif t.cG=="RPG":t.shoot(10,20,0,1,30,1)
                  elif t.cG=="Tracker":t.shoot(10,20,0,1,20,1)
                  elif t.cG=="WallBreaker":t.shoot(10,20,-3,3,50,0)
                  t.ammoC.value=rnd(t.ammo)
                  if t.ammo<0:t.ammo=0
                  t.R=t.time
            t.Gun.rotateAngle=t.Light.rotateAngle=t.player.rotateAngle=a2(cX(t.player),cY(t.player),t.xAngle,t.yAngle)
            if cX(t.Light)!=cX(t.player)or cY(t.Light)!=cY(t.player):t.Light.centerX,t.Light.centerY=cX(t.player),cY(t.player)
      def rpge(t,x,y):b=Crc(x,y,80,fill=grd(rd,on),border=bk);b.type="rpge";b.ds=h6;b.des=F;t.R=t.time;aD(t.bgr,b)
      def shoot(t,sX,sY,acL,acH,use,sh):
        if t.cG=="RPG":b=Ovl(cX(t.Gun),cY(t.Gun),sX,sY,fill=yl,border=bk,align=bf)
        elif t.cG=="Sword":b=Grp(Lne(175,h2,185,t1,fill=wh),Lne(185,t1,h2,215,fill=wh),Lne(o6,t1,175,225,fill=wh),Lne(175,225,h2,t3,fill=wh),Rct(h2,h2,7,20,align=bt,fill=grd(dy,"dimgrey",dy,start=lf)),Ply(197,h2,h2,o7,203,h2,h2,t3,fill=grd(dy,"dimgrey",dy,start=lf)),Rct(h2,o8,4,10,align=bt,fill="saddlebrown"),Lne(-h4,-h4,-h8,-840),Lne(h8,h8,h12,h12));b.moved=F;b.height//=1.5;b.width//=1.5
        else:b=Rct(h2,h2,sX,sY,fill=yl,border=bk,borderWidth=1.5,align=bf)
        b.rotateAngle=a2(cX(t.Gun),cY(t.Gun),t.xAngle,t.yAngle)+rr(acL,acH);b.centerX,b.centerY=cX(t.Gun),cY(t.Gun)
        if t.cG=="Melee":b.fill="lemonchiffon";b.type="melee";tF(b);posX,posY=gpd(cX(t.Gun),cY(t.Gun),rA(t.player)+40,10);b.centerX,b.centerY,b.ds=posX,posY,20
        elif t.cG=="Sword":b.type="sword";b.ds=4
        elif t.cG=="Pistol":b.type="bullet";b.ds=o9
        elif t.cG=="SMG":b.type="bullet";b.ds=h1
        elif t.cG=="Sniper":b.type="sniper";b.ds=h6
        elif t.cG=="AR":b.type="bullet";b.ds=o9
        elif t.cG=="Shotgun":b.type="bullet";b.ds=o5
        elif t.cG=="RPG":b.type="rpg";b.ds=h6
        elif t.cG=="WallBreaker":b.fill="dimgrey";b.type="wallbreaker";b.ds=h6
        elif t.cG=="Tracker":b.fill=bl;b.type="tracker";b.ds=h6
        if t.cG=="Sword":b.centerX,b.centerY=gpd(cX(t.Gun),cY(t.Gun),rA(b),3)
        b.visible=T;b.des=F;aD(t.bgr,b);t.ammo-=use;t.bS+=sh
      class Cell:
        wp={"N":"S","S":"N","E":"W","W":"E"}
        def __init__(t,x,y): t.x,t.y=x,y;t.walls={"N":T,"S":T,"E":T,"W":T}
      class Maze:
        def __init__(t,nx,ny,S,ix=0,iy=0):t.nx,t.ny=nx,ny;t.ix,t.iy=ix,iy;t.mzmp=[[S.Cell(x,y)for y in r(ny)]for x in r(nx)]
        def __str__(t):
            mR=["--+"*t.nx*1]
            for y in r(t.ny):
                mrow=["V"]
                for x in r(t.nx):
                    if t.mzmp[x][y].walls["E"]:mrow+=["  |"]
                    else:mrow+=["   "]
                mR+=[Q.join(mrow)];mrow=["dwn"]
                for x in r(t.nx):
                    if t.mzmp[x][y].walls["S"]:mrow+=["--+"]
                    else:mrow+=["  +"]
                mR+=[Q.join(mrow)]
            return"\n".join(mR)
        def make(t,S):
            n=t.nx*t.ny;cs=[];curr=t.mzmp[t.ix][t.iy];nv=1
            while nv<n:
                delta=[("W",(-1,0)),("E",(1,0)),("S",(0,1)),("N",(0,-1))];nghbrs=[]
                for dr,(dx,dy)in delta:
                    x2,y2=curr.x+dx,curr.y+dy
                    if(0<=x2<t.nx)&(0<=y2<t.ny):
                        nghbr=t.mzmp[x2][y2]
                        if all(nghbr.walls.values()):nghbrs+=[(dr,nghbr)]
                if not nghbrs:curr=cs.pop();continue
                d,nc=choice(nghbrs);curr.walls[d]=F;nc.walls[S.Cell.wp[d]]=F;cs.append(curr);curr=nc;nv+=1
    class Bugreporting:
      def __init__(t):gti("link to report a bug https://forms.gle/YD7gjPLAeAVFcGcA7");t.stepsPerSecond=0
    class Tehtrisse:
      def __init__(t):
        try:t.track=Sound("http://docs.google.com/uc?export=open&id=1Z88_byi8WaIpxVeLqnLuhmy-kXokGatq");t.track.play(restart=T,loop=T)
        except:F
        try:t.bSo=Sound("https://docs.google.com/uc?export=open&id=1JM0CQaIiCsPwWShayKdhYkPIkXhn99At")
        except:F
        t.lLbl=Lbl(Q,h2,h2,size=40,fill=rd,bold=T,border=wh);t.timeStarted=t.tTi=t.lnsC=F;t.gameRct=Rct(50,-5,h2,410,border=wh,fill=N);t.NextPieceRct=Rct(325,70,90,90,border=wh,align=cn);t.TimePlayed=Lbl("00:00",325,265,size=24,font=ot,bold=T,fill=wh);t.upArrow=Ply(325,331,308,314,308,281,342,281,342,314,fill=N,border=wh);t.leftArrow=Ply(326,T3,309,347,276,347,276,313,309,313,fill=N,border=wh);t.downArrow=Ply(325,329,342,346,342,379,308,379,308,346,fill=N,border=wh);t.rightArrow=Ply(324,T3,341,313,374,313,374,347,341,347,fill=N,border=wh);t.bts=Grp(t.upArrow,t.leftArrow,t.downArrow,t.rightArrow);t.sGS=Grp(t.gameRct,t.NextPieceRct,t.TimePlayed,t.bts,visible=F);t.vL=[];t.hoL=[]
        for x in r(9):L=Lne(70+x*20,0,70+x*20,-(x*14),fill=wh,visible=F);L.lN=x;L.done=F;t.vL+=[L]
        for x in r(19):L=Lne(50,20+(x*20),50-(x*10),20+(x*20),fill=wh,visible=F);L.lN=x;L.done=F;t.hoL+=[L]
        t.gL=Lbl("teHtRiSSe",h2,80,size=60,font=cz,bold=T,fill=wh,opacity=0);t.gL.fade=t.bCM=T;tF(t.gL);t.bFL=Grp(Lbl("by",h2,155,size=30,font=cz,bold=T,fill=wh,opacity=0),Lbl("BiRdfACe",h2,o9,size=40,font=cz,bold=T,fill=wh,opacity=0));t.pB=Grp(Rct(50,135,t7,50,fill=N),Lbl("play",o1,o6,size=40,font=cz,bold=T,fill=wh));t.helpB=Grp(Rct(50,185,t7,50,fill=N),Lbl("h",73,t1,size=40,font=cz,bold=T,fill=wh),Lbl("elp",127,t1,size=40,font=cz,bold=T,fill=wh));t.sB=Grp(Rct(50,235,t7,50,fill=N),Lbl("settings",161,t6,size=40,font=cz,bold=T,fill=wh));t.cB=Grp(Rct(50,285,t7,50,fill=N),Lbl("credits",148,T1,size=40,font=cz,bold=T,fill=wh));t.mOG=Grp(t.pB,t.helpB,t.sB,t.cB,visible=F);t.moh=Rct(50,135,t7,50,fill=N,border=wh,borderWidth=3);t.bL=Lbl(bc,115,T1,size=40,font=cz,bold=T,fill=wh);t.bB=Grp(Rct(50,285,t7,50,fill=N));t.uMG=Grp(t.moh,t.bB,t.bL,visible=F);t.helpText=[".controls: ","   move piece left by pressing left,","   a, or clicking the d-pad on the left","   move piece right by pressing right,","   d, or clicking the d-pad on the right","   rotate piece by pressing up or w","   move piece down by pressing down or s"," ",".scoring:","   make a line of blocks to score","   clear more lines at the same time","   to be awarded more points."," ",".losing:","   you lose when a piece touches the","   top of the board"," ",".saving:","   pause game by pressing p, then","   e tab to create a save, and","   i to load a save",];t.hL=Grp(visible=F);t.hB=Grp(Rct(265,365,135,35,fill=N),Lbl("Back",332.5,382.5,fill=wh,size=20,font=cz,bold=T),visible=F);t.sM=Lbl("Settings",h2,80,size=60,font=cz,bold=T,fill=wh);t.difficultyMenu=Grp(Rct(50,135,t7,50,fill=N),Lbl("difficulty",183,o6,size=40,font=cz,bold=T,fill=wh));t.kybndsMenu=Grp(Rct(50,185,t7,50,fill=N),Lbl("keybinds",164,t1,size=40,font=cz,bold=T,fill=wh));t.cML=Lbl(lt,60,t6,align=lf,size=40,font=cz,bold=T,fill=wh);t.colorMenu=Grp(Rct(50,235,t7,50,fill=N),t.cML);t.sMOG=Grp(t.sM,t.difficultyMenu,t.kybndsMenu,t.colorMenu,visible=F);t.pBKeybinds=["p","P"];t.eBK=[ent,tab,];t.bBKeybinds=["backspace",esc,"b","B"];t.pBK=[tab,esc,"p","P"];t.iK=["i","I"];t.eK=["e","E"];t.upArrow.kybnds=[up,"w","W"];t.leftArrow.kybnds=[lf,"a","A"];t.downArrow.kybnds=[dw,"s","S"];t.rightArrow.kybnds=[rt,"d","D"];t.lns=[" ","$Tehtrisse"," ","made by:","~BirdFace Studios"," ","with:","python by python software organization","cmu graphics module by CMU"," ","/"," "," ","time original (bad) - m","time revised (good) - t","end result time - t & m","lose screen - t","score - t","logos - m","play area and animation - m","keybinds - t","touch control sprites & functionality - t","touch control sprites revision & VFX - m","touch control end result - t & m","color scheme - t","inspiration - Peter 'Mr. E' Erickson","name of game - m","menus - m","settings - t & m","help text - t","credits text - t & m","credits scroll & render -t","original game saving - t","'compressed' game saving - m","end result game saving - t & m","block creation functionality & sprites - t","added block functionality - m","end result blocks - t & m","playtester - jared","music & sound efects - t","some sound efects from zapsplat.com"];t.cT=Grp()
        for J,v in enum(t.helpText):
          if v[0]==".":b=T;v=v[1:l(v)];si=20
          else:b=T;si=16
          aD(t.hL,Lbl(v,7,(J*17)+18,size=si,fill=wh,bold=b,visible=F,font=ms,align=lf))
        for J in r(l(t.lns)):
          if t.lns[J][0]==".":b=T;y=12;si=40;n=Q;t.lns[J]=t.lns[J][1:l(t.lns[J])]
          elif t.lns[J][0]=="~":b=T;y=12;si=30;n=Q;t.lns[J]=t.lns[J][1:l(t.lns[J])]
          elif t.lns[J][0]=="$":b=T;y=0;si=60;n=cz;t.lns[J]=t.lns[J][1:l(t.lns[J])]
          elif t.lns[J][0]=="/":t.lns[J]=t.lns[J][1:l(t.lns[J])];hit=Image("https://cdn.freebiesupply.com/logos/large/2x/python-5-logo-png-transparent.png",0,0);hit.width/=2390/96;hit.height/=2390/96;hit.centerX=h4/3;hit.centerY=h4+(J*24)+12;aD(t.cT,hit);stencil=Image("https://academy.cs.cmu.edu/favicons/android-chrome-384x384.png",0,0);stencil.width/=397/96;stencil.height/=397/96;stencil.centerX=h4/3*2;stencil.centerY=h4+(J*24)+12;aD(t.cT,stencil)
          else:b=F;y=0;si=22;n=Q
          aD(t.cT,Lbl(t.lns[J],h2,h4+(J*24)+y,size=si,fill=wh,bold=b,visible=F,font=n))
        ap.background=bk;t.stepsPerSecond=20;t.sL=t.menu=t.hM=t.sM=t.sDM=t.sKM=t.sCM=t.credits=t.nBS=t.sLA=t.pG=t.tT=t.aT=t.bOX=t.bOY=F;t.score=Lbl(0,325,h2,fill=wh,size=75,opacity=0,font=ot);t.bS=t.difficulty=25;t.nextBlock=t.cb=N;t.sqs=[];t.rS=Grp();t.bar=Rct(0,385,h4,10,fill=wh,visible=F);t.newGrp=Grp();t.scoreDic={0:0,1:40,2:h1,3:h3,4:h12};t.convert={0:"A",20:"B",40:"C",60:"D",80:"E",h1:"F",o2:"G",o4:"H",o6:"I",o8:"J",h2:"K",t2:"L",t4:"M",t6:"N",t8:"O",h3:"P",T2:"Q",T4:"R",T6:"S",T8:"T",325:"U",50:"a",70:"b",90:"c",o1:"d",o3:"e",o5:"f",o7:"g",o9:"h",t1:"i",t3:"j",t5:"k",yl:"0",cy:"1",rd:"2",lm:"3",dv:"4",bl:"5",on:"6"};t.n2w={0:"v",1:"m",2:"n",3:"o",4:"p",5:"q",6:"r",7:"s",8:"t",9:"u",};t.w2n={"v":"0","m":"1","n":"2","o":"3","p":"4","q":"5","r":"6","s":"7","t":"8","u":"9"};t.noWidth=c0+c1+c2;t.currentKeybind=Lbl(" ",h2,265,size=18,fill=wh,font=ot,bold=T);t.currentKeybind.index=-1;t.kG=Grp(Rct(0,0,h4,285),Lbl("press a number to edit",h2,20,size=18,fill=wh,font=ot,bold=T),Lbl("the matching keybind",h2,40,size=18,fill=wh,font=ot,bold=T),Lbl("then press a new key",h2,60,size=18,fill=wh,font=ot,bold=T),t.currentKeybind,visible=F);listOfKeybinds=[ent,bc,"pause","import","export",up,dw,lf,rt];t.dict={"0":c0+c0+c0+c0+c0,"1":c0+c0+c0+c0+c1,"2":c0+c0+c0+c0+c2,"3":c0+c0+c0+c1+c0,"4":c0+c0+c0+c1+c1,"5":c0+c0+c0+c1+c2,"6":c0+c0+c0+c2+c0,"7":c0+c0+c0+c2+c1,"8":c0+c0+c0+c22,"9":c0+c0+c1+c0+c0,"0":c0+c0+c1+c0+c1,"A":c0+c0+c1+c0+c2,"B":c0+c0+c1+c1+c0,"C":c0+c0+c1+c1+c1,"D":c0+c0+c1+c1+c2,"E":c0+c0+c1+c2+c0,"F":c0+c0+c1+c2+c1,"G":c0+c0+c1+c22,"H":c0+c0+c2+c0+c0,"I":c0+c0+c2+c0+c1,"J":c0+c0+c2+c0+c2,"K":c0+c0+c2+c1+c0,"L":c0+c0+c2+c1+c1,"M":c0+c0+c2+c1+c2,"N":c0+c0+c22+c0,"O":c0+c0+c22+c1,"P":c0+c0+c22+c2,"Q":c0+c1+c0+c0+c0,"R":c0+c1+c0+c0+c1,"S":c0+c1+c0+c0+c2,"T":c0+c1+c0+c1+c0,"U":c0+c1+c0+c1+c1,"a":c0+c1+c0+c1+c2,"b":c0+c1+c0+c2+c0,"c":c0+c1+c0+c2+c1,"d":c0+c1+c0+c22,"e":c0+c1+c1+c0+c0,"f":c0+c1+c1+c0+c1,"g":c0+c1+c1+c0+c2,"h":c0+c1+c1+c1+c0,"i":c0+c1+c1+c1+c1,"j":c0+c1+c1+c1+c2,"k":c0+c2+c0+c0+c0,"l":c0+c2+c0+c0+c1,"m":c0+c2+c0+c0+c2,"n":c0+c2+c0+c1+c0,"o":c0+c2+c0+c1+c1,"p":c0+c2+c0+c1+c2,"q":c0+c2+c0+c2+c0,"r":c0+c2+c0+c2+c1,"s":c0+c2+c0+c22,"t":c0+c2+c1+c0+c0,"u":c0+c2+c1+c0+c1,"v":c0+c2+c1+c0+c2,"w":c0+c2+c1+c1+c0,"x":c0+c2+c1+c1+c1,c0+c0+c0+c0+c0:"0",c0+c0+c0+c0+c1:"1",c0+c0+c0+c0+c2:"2",c0+c0+c0+c1+c0:"3",c0+c0+c0+c1+c1:"4",c0+c0+c0+c1+c2:"5",c0+c0+c0+c2+c0:"6",c0+c0+c0+c2+c1:"7",c0+c0+c0+c22:"8",c0+c0+c1+c0+c0:"9",c0+c0+c1+c0+c1:"0",c0+c0+c1+c0+c2:"A",c0+c0+c1+c1+c0:"B",c0+c0+c1+c1+c1:"C",c0+c0+c1+c1+c2:"D",c0+c0+c1+c2+c0:"E",c0+c0+c1+c2+c1:"F",c0+c0+c1+c22:"G",c0+c0+c2+c0+c0:"H",c0+c0+c2+c0+c1:"I",c0+c0+c2+c0+c2:"J",c0+c0+c2+c1+c0:"K",c0+c0+c2+c1+c1:"L",c0+c0+c2+c1+c2:"M",c0+c0+c22+c0:"N",c0+c0+c22+c1:"O",c0+c0+c22+c2:"P",c0+c1+c0+c0+c0:"Q",c0+c1+c0+c0+c1:"R",c0+c1+c0+c0+c2:"S",c0+c1+c0+c1+c0:"T",c0+c1+c0+c1+c1:"U",c0+c1+c0+c1+c2:"a",c0+c1+c0+c2+c0:"b",c0+c1+c0+c2+c1:"c",c0+c1+c0+c22:"d",c0+c1+c1+c0+c0:"e",c0+c1+c1+c0+c1:"f",c0+c1+c1+c0+c2:"g",c0+c1+c1+c1+c0:"h",c0+c1+c1+c1+c1:"i",c0+c1+c1+c1+c2:"j",c0+c2+c0+c0+c0:"k",c0+c2+c0+c0+c1:"l",c0+c2+c0+c0+c2:"m",c0+c2+c0+c1+c0:"m",c0+c2+c0+c1+c1:"o",c0+c2+c0+c1+c2:"p",c0+c2+c0+c2+c0:"q",c0+c2+c0+c2+c1:"r",c0+c2+c0+c22:"s",c0+c2+c1+c0+c0:"t",c0+c2+c1+c0+c1:"u",c0+c2+c1+c0+c2:"v",c0+c2+c1+c1+c0:"w",c0+c2+c1+c1+c1:"x",}
        for J,v in enum(listOfKeybinds):aD(t.kG,Lbl(f"{v} {J+1}",h1,J*20+80,size=18,fill=wh,align=rt,font=ot,bold=T))
        t.theKeysGrp=Grp();aD(t.kG,t.theKeysGrp);t.kL=[t.eBK,t.bBKeybinds,t.pBK,t.iK,t.eK,t.upArrow.kybnds,t.downArrow.kybnds,t.leftArrow.kybnds,t.rightArrow.kybnds];t.sKB();t.iL=[t.score,t.gL]
        for J in t.kG:t.iL+=[J]
        for J in t.cT:t.iL+=[J]
        for J in t.sMOG:t.iL+=[J]
        for J in t.hB:t.iL+=[J]
        for J in t.hL:t.iL+=[J]
        for J in t.uMG:t.iL+=[J]
        for J in t.mOG:t.iL+=[J]
        for J in t.hoL:t.iL+=[J]
        for J in t.vL:t.iL+=[J]
        for J in t.sGS:t.iL+=[J]
        for J in r(5):
          for j in t.iL:
            if type(j)==Grp:
              for k in j:t.iL+=[k]
              rM(t.iL,j)
        t.rB=Grp(Rct(h2,h3,372.5,50,align=cn,fill=gr),Lbl(rstINST,h2,h3,size=32));t.pM=Grp(Rct(0,0,h4,h4,fill=wh),Lbl("paused!",h2,h1,size=75,font=cz),Lbl("use wasd or arrows to move the block.",h2,o6,size=20),Lbl("w or up rotates the block",h2,h2-12.5,size=20),Lbl("get ten blocks in a row to score.",h2,215,size=20),Lbl("tip: score multiple lines a once for a bonus",h2,t4,size=20),t.rB,visible=F)
      def iC(t):
        for J in t.iL:
          if fL(J)==bk:J.fill=wh
          elif fL(J)==wh:J.fill=bk
          if bR(J)==bk:J.border=wh
          elif bR(J)==wh:J.border=bk
        if ap.background==bk:ap.background=wh
        else:ap.background=bk
        if t.cML.value==lt:t.cML.value=dk
        else:t.cML.value=lt
        t.cML.left=60
      def sKB(t):
        cL(t.theKeysGrp)
        for J,v in enum(t.kL):
          k=Q
          for j in v:
            k+=j
            if j!=v[-1]:k+=","
          if ap.background==wh:c=bk
          else:c=wh
          aD(t.theKeysGrp,Lbl(k,125,J*20+80,size=18,fill=c,align=lf,font=ot,bold=T))
      def pS(t):t.pG=t.sGS.visible=T;t.gL.visible=t.mOG.visible=t.uMG.visible=t.sMOG.visible=t.menu=F;t.gameRct.opacity=h1
      def mS(t):t.menu=t.sL=t.mOG.visible=t.uMG.visible=t.gL.visible=T;t.hM=t.sM=t.credits=t.tT=t.bL.visible=t.bB.visible=t.sMOG.visible=t.sGS.visible=t.bts.visible=t.cT.visible=t.hL.visible=t.hB.visible=t.bFL.visible=F;t.moh.top=135;t.sPS("end")
      def hS(t):t.hM=t.hL.visible=t.hB.visible=T;t.menu=t.gL.visible=t.bFL.visible=t.mOG.visible=t.uMG.visible=F;t.hB.centerY=372.5;t.moh.top=135
      def sS(t):t.sL=t.sM=t.uMG.visible=t.bL.visible=t.sMOG.visible=T;t.hM=t.sDM=t.sKM=t.sCM=t.credits=t.menu=t.tT=t.gL.visible=t.bFL.visible=t.mOG.visible=t.sGS.visible=t.bts.visible=t.kG.visible=F;t.moh.top=135;t.bL.value=bc;t.bL.left=57.62
      def sKS(t):t.sM=t.sMOG.visible=F;t.sKM=t.uMG.visible=t.bL.visible=t.kG.visible=T;t.moh.top=285;t.bL.value="save";t.bL.left=57.62
      def cS(t):t.menu=t.gL.visible=t.bFL.visible=t.mOG.visible=t.uMG.visible=F;t.moh.top=135;t.bL.value=bc;t.bL.left=57.62;t.bB.width,t.bB.height=135,25;t.bB.right=t.bB.bottom=t.cT.top=h4;t.bL.visible=t.cT.visible=t.hB.visible=t.credits=T;t.hB.centerY=27.5
      def sPS(t,c):
        for J in t.sGS:
          if oP(J)<h1:J.opacity+=1.25
        if c=="end":
          for L in t.vL:L.y2=F-(L.lN*14);L.visible=F
          for L in t.hoL:L.x2=50-(L.lN*10);L.visible=F
        else:
          for L in t.vL:
            if L.done==F:
              L.y2+=7
              if L.y2>0:
                L.visible=T
                if L.y2>h4:L.y2=h4;L.done=T
          for L in t.hoL:
            if L.done==F:
              L.x2+=5
              if L.x2>50:
                L.visible=T
                if L.x2>t5:L.x2=t5;L.done=T
          v=w=h=I=F
          for L in t.vL:
            if L.done:v+=1
          if(v)==9:w=T
          for L in t.hoL:
            if L.done:h+=1
          if h==19:I=T
          if w&I&(t.nBS==F):t.nextBlock=t.mB(325,70);t.nBS=T
      def mMU(t):t.moh.top={135:285,185:135,235:185,285:235}[tP(t.moh)]
      def mMD(t):t.moh.top={135:185,185:235,235:285,285:135}[tP(t.moh)]
      def oS(t):
        if t.sL==F:
          if(oP(t.gL)<h1)&t.gL.fade:
            t.gL.opacity+=2.5;t.bFL.opacity+=2.5
            if t.gL.opacity==h1:t.gL.fade=F
          elif t.gL.fade==F:
            t.tT+=1
            if t.tT>40:
              t.bFL.opacity-=2.5
              if t.bFL.opacity==F:t.mS()
        elif t.credits:t.cT.centerY-=1
        elif(t.menu==F)&(t.sLA==F)&(vS(t.hB)==F)&(vS(t.sMOG)==F)&(vS(t.theKeysGrp)==F):
          t.sPS(t.tT);t.tT+=1
          if t.tT==97:t.tT=F;t.sLA=t.pG=t.timeStarted=T;t.nB()
        elif t.pG:
          if l(t.newGrp)>0:
            t.aT+=1
            if t.bCM:t.bOX,t.bOY=cX(t.cb),cY(t.cb);t.cb.centerX,t.cb.centerY=325,70;t.nextBlock.visible=F
            t.bCM=F
          if t.aT%20==10:t.newGrp.visible=F
          elif t.aT%20==F:t.newGrp.visible=T
          if t.aT>30:
            t.aT=F;g=Grp();t.bCM=T;t.cb.centerX,t.cb.centerY=t.bOX,t.bOY;t.cb.visible=t.nextBlock.visible=T
            for b in t.rS:
              if bT(b)<bT(t.newGrp)-0.25:aD(g,b)
            g.bottom=bT(t.newGrp)
            for b in g:aD(t.rS,b)
            cL(t.newGrp);t.bar.top=5
            for J in r(20):
              c=F
              for b in t.rS:
                if hS(b,t.bar):c+=1
              if c==F:
                for b in t.rS:
                  if tP(b)<tP(t.bar)-10:b.centerY+=20
              t.bar.centerY+=20
          if t.timeStarted:
            t.tTi+=1;m=i(t.tTi/h12%60);se=i(t.tTi/20%60);h=i(t.tTi/72000)
            if h==F:
                t.TimePlayed.value=s(h1+m)[1:3]+":"+s(h1+se)[1:3]
            else:t.TimePlayed.value=s(h)+":"+s(h1+m)[1:3]+":"+s(h1+se)[1:3]
          t.tT+=1
          if t.tT%t.bS==F:
            if t.bCM:
              if bT(t.cb)<h4:
                t.cb.centerY+=20
                if hS(t.cb,t.rS):
                  t.cb.centerY-=20
                  for J in t.cb:t.sqs+=[lF(J),tP(J),fL(J)]
                  t.renderS();t.cb.visible=F;t.nB();t.bSo.play()
              elif bT(t.cb)==h4:
                for J in t.cb:t.sqs+=[lF(J),tP(J),fL(J)]
                t.renderS();t.cb.visible=F;t.nB();t.bSo.play()
      def oMP(t,x,y):
        if t.menu:
          if cT(t.pB,x,y):t.pS()
          elif cT(t.helpB,x,y):t.hS()
          elif cT(t.sB,x,y):t.sS()
          elif cT(t.cB,x,y):t.cS()
        elif t.hM or t.credits:
          if cT(t.hB,x,y):t.mS()
        elif t.sM:
          if cT(t.difficultyMenu,x,y):
            string="input any number >= 1 for your diffuculty (the base is 25,no decimals, and higher numbers are easier)";difficulty=gti(string)
            while T:
              if difficulty.isdigit():exec("break"if f(difficulty)>0 else"difficulty=gti(string)")
            t.difficulty=f(difficulty);t.bS=t.difficulty*10//((t.lnsC/2)+10)
            if t.bS<1:t.bS=1
          elif cT(t.kybndsMenu,x,y):t.sKS()
          elif cT(t.colorMenu,x,y):t.iC()
          elif cT(t.bB,x,y):t.mS()
        elif t.sKM&cT(t.bB,x,y):t.sS()
        elif t.pG:
          if cT(t.rB,x,y)&t.pM.visible:
            if rstrt():
              t.lLbl.value=Q;ap.restart.visible=F;t.pM.visible=F;t.bCM=1;cL(t.rS)
              try:
                for J in r(2):t.cb.visible=F;t.nB()
              except:F
              t.score.size=75;t.score.value=t.lnsC=F;ap.stepsPerSecond=20;t.score.opacity=0
          for b in t.bts:
            if cT(b,x,y):t.oKP(b.kybnds[0]);t.oKH([b.kybnds[0]])
      def oMR(t,x,y):
        if t.pG:
          for b in t.bts:b.fill=N if b.fill==wh else b.fill
      def oMM(t,x,y):
        if t.menu|t.sM|t.sKM:
          if cT(t.pB,x,y):t.moh.top=135
          elif cT(t.helpB,x,y):t.moh.top=185
          elif cT(t.sB,x,y):t.moh.top=235
          elif cT(t.cB,x,y):t.moh.top=285
      def oMD(t,x,y):
        if t.pG:
          for b in t.bts:
            if cT(b,x,y)&(b.fill==N):t.oKP(b.kybnds[0]);t.oKH([b.kybnds[0]])
            elif cT(b,x,y)==F:t.oKR(b.kybnds[0])
      def oKP(t,k):
        if t.menu:
          if k in t.pBKeybinds:t.pS()
          elif k in t.eBK:
            if tP(t.moh)==tP(t.pB):t.pS()
            elif tP(t.moh)==tP(t.helpB):t.hS()
            elif tP(t.moh)==tP(t.sB):t.sS()
            elif tP(t.moh)==tP(t.cB):t.cS()
        elif t.sKM:
          if k in t.eBK:t.oMP(cX(t.moh),cY(t.moh))
          if k.isdigit():
            if i(k)>0:
              k=i(k);lv=Q;v=t.kL[k-1]
              for c in v:
                lv+=c
                if c!=v[-1]:lv+=", "
              t.currentKeybind.value=lv;t.currentKeybind.index=k-1;t.moh.top=235
          elif t.currentKeybind.value!=" ":
            if k in t.kL[t.currentKeybind.index]:rM(t.kL[t.currentKeybind.index],k);t.sKB()
            else:t.kL[t.currentKeybind.index]+=[k];t.sKB()
            lv=Q;v=t.kL[t.currentKeybind.index]
            for T in v:
              lv+=T
              if T!=v[-1]:lv+=", "
            t.currentKeybind.value=lv
        elif(t.hM|t.credits)&(ent==k):t.mS()
        elif t.sM:
          if k in t.eBK:
            if tP(t.moh)==135:
              string="input any number >= 1 for your difficulty (the base is 25, no decimals, and higher numbers are easier)";difficulty=gti(string)
              while T:exec("break"if difficulty.isdigit()&(f(difficulty)>0)else"difficulty=gti(string)")
              t.difficulty=f(difficulty)
              t.bS=t.difficulty*10//((t.lnsC/2)+10)
              if t.bS<1:t.bS=1
            elif tP(t.moh)==185:t.sKS()
            elif tP(t.moh)==235:t.iC()
            elif tP(t.moh)==285:
              if t.sDM:t.sDM=F
              elif t.sKM:t.sKM=F
              elif t.sCM:t.sCM=F
              else:t.mS()
          if k in t.bBKeybinds:
            if t.sDM:t.sDM=F
            elif t.sKM:t.sKM=F
            elif t.sCM:t.sCM=F
            else:t.mS()
        if t.menu or t.sM or t.sKM:
          if k in t.upArrow.kybnds or k in t.leftArrow.kybnds:t.mMU()
          elif k in t.downArrow.kybnds or k in t.rightArrow.kybnds:t.mMD()
        elif t.pG:
          if t.cb!=N:
            if t.bCM:
              if k in t.upArrow.kybnds:
                for b in t.cb:
                  if tp in s(bR(b)):b.border=grd6gy(lf)
                  elif lf in s(bR(b)):b.border=grd6gy(bt)
                  elif bt in s(bR(b)):b.border=grd6gy(rt)
                  elif rt in s(bR(b)):b.border=grd6gy(tp)
                x,y=cX(t.cb),cY(t.cb)
                t.cb.rotateAngle+=90
                t.cb.top=rnd(tP(t.cb)/20)*20
                if wD(t.cb)in(40,80):t.cb.left=rnd(lF(t.cb)/20)*20-10
                else:t.cb.left=rnd(lF(t.cb)/20)*20+10
                if rT(t.cb)>t5:t.cb.right=t5
                elif lF(t.cb)<50:t.cb.left=50
                elif tP(t.cb)<0:t.cb.top=0
                elif bT(t.cb)>h4:t.cb.bottom=h4
                if hS(t.cb,t.rS):t.cb.rotateAngle-=90;t.cb.centerX,t.cb.centerY=x,y
              elif(k in t.leftArrow.kybnds)&(lF(t.cb)>50):
                t.cb.centerX-=20
                if hS(t.cb,t.rS):t.cb.centerX+=20
              elif k in t.downArrow.kybnds:
                if bT(t.cb)!=h4:
                  t.cb.centerY+=20
                  if hS(t.cb,t.rS):
                    t.cb.centerY-=20
                    for J in t.cb:t.sqs+=[lF(J),tP(J),fL(J)]
                    t.renderS();t.cb.visible=F;t.nB();t.bSo.play()
                  t.tT=F
                  if bT(t.cb)==h4:
                    for J in t.cb:t.sqs+=[lF(J),tP(J),fL(J)]
                    t.renderS();t.cb.visible=F;t.nB();t.bSo.play()
              elif(k in t.rightArrow.kybnds)&(rT(t.cb)<t5):
                t.cb.centerX+=20
                if hS(t.cb,t.rS):t.cb.centerX-=20
            if t.pM.visible&(k=="r"):t.oMP(h2,h3)
            if k in t.eK:t.makeSave()
            if k in t.iK:
              j=Q
              while l(j)==0:
                  j=gti("paste in your save (type escape to stop importing)")
              if j!=esc:t.zWtri(j,F)
        if k in t.pBK:
          if vS(t.pM):t.pM.visible=F;t.bCM=True;ap.stepsPerSecond=20
          else:t.pM.visible=True;tF(t.pM);ap.stepsPerSecond=t.bCM=F
      def oKH(t,k):
        if t.pG:
          for K in k:
            if K in t.upArrow.kybnds:
              if ap.background==bk:t.upArrow.fill=wh
              else:t.upArrow.fill=bk
            if K in t.leftArrow.kybnds:
              if ap.background==bk:t.leftArrow.fill=wh
              else:t.leftArrow.fill=bk
            if K in t.downArrow.kybnds:
              if ap.background==bk:t.downArrow.fill=wh
              else:t.downArrow.fill=bk
              t.oKP(t.downArrow.kybnds[0])
            if K in t.rightArrow.kybnds:
              if ap.background==bk:t.rightArrow.fill=wh
              else:t.rightArrow.fill=bk
      def oKR(t,k):
        if t.pG:
          if k in t.upArrow.kybnds:t.upArrow.fill=N
          if k in t.leftArrow.kybnds:t.leftArrow.fill=N
          if k in t.downArrow.kybnds:t.downArrow.fill=N
          if k in t.rightArrow.kybnds:t.rightArrow.fill=N
      def mB(t,x,y):
        B=rr(7);b=grd6gy(tp)
        if B==0:g=Grp(Rct(h2,h2,20,20,fill=yl,border=b),Rct(t2,h2,20,20,fill=yl,border=b),Rct(h2,t2,20,20,fill=yl,border=b),Rct(t2,t2,20,20,fill=yl,border=b))
        elif B==1:g=Grp(Rct(h2,h2,20,20,fill=cy,border=b),Rct(h2,t2,20,20,fill=cy,border=b),Rct(h2,t4,20,20,fill=cy,border=b),Rct(h2,t6,20,20,fill=cy,border=b))
        elif B==2:g=Grp(Rct(h2,h2,20,20,fill=rd,border=b),Rct(t2,h2,20,20,fill=rd,border=b),Rct(t2,t2,20,20,fill=rd,border=b),Rct(t4,t2,20,20,fill=rd,border=b))
        elif B==3:g=Grp(Rct(h2,t2,20,20,fill=lm,border=b),Rct(t2,t2,20,20,fill=lm,border=b),Rct(t2,h2,20,20,fill=lm,border=b),Rct(t4,h2,20,20,fill=lm,border=b))
        elif B==4:g=Grp(Rct(h2,t2,20,20,fill=dv,border=b),Rct(t2,t2,20,20,fill=dv,border=b),Rct(t4,t2,20,20,fill=dv,border=b),Rct(t2,h2,20,20,fill=dv,border=b))
        elif B==5:g=Grp(Rct(h2,t2,20,20,fill=bl,border=b),Rct(t2,t2,20,20,fill=bl,border=b),Rct(t4,t2,20,20,fill=bl,border=b),Rct(h2,h2,20,20,fill=bl,border=b))
        elif B==6:g=Grp(Rct(h2,t2,20,20,fill=on,border=b),Rct(t2,t2,20,20,fill=on,border=b),Rct(t4,t2,20,20,fill=on,border=b),Rct(t4,h2,20,20,fill=on,border=b))
        g.centerX,g.centerY=x,y;tF(g);return g
      def nB(t):
        if t.pG:
          t.cb=t.nextBlock;t.cb.left=o1;t.cb.top=0
          if t.cb.width==20:t.cb.centerX+=40
          elif t.cb.width==40:t.cb.centerX+=20
          if hS(t.cb,t.rS):
            if vL(t.score)<h2:v="u very bad at game"
            elif vL(t.score)<h8:v="u bad at game"
            elif vL(t.score)<2000:v="u okay at game"
            elif vL(t.score)<5000:v="u decent at game"
            elif vL(t.score)<50000:v="u good at game"
            else:v="u excellent at game"
            t.lLbl.value=v;ap.stepsPerSecond=0;t.bCM=F;tF(t.lLbl)
        t.nextBlock=t.mB(325,70)
      def renderS(t):
        for x in r(i(l(t.sqs)/3)):aD(t.rS,Rct(f(t.sqs[x*3])+0.25,f(t.sqs[x*3+1])+0.25,19.5,19.5,fill=t.sqs[x*3+2],border=grd6gy(tp)))
        cL(t.sqs);t.check()
      def check(t):
        t.bar.top=5;k=0
        for J in r(23):
          c=0
          for b in t.rS:
            if hS(b,t.bar):
              c+=1
              if c==10:
                k+=1
                for b in t.rS:
                  if hS(b,t.bar):b.visible=F;rM(t.rS,b);b.fill=wh;b.border=bk;aD(t.newGrp,b)
                t.bar.centerY-=20
          t.bar.centerY+=20
        t.score.value+=t.scoreDic[k]
        if vL(t.score)>0:t.score.opacity=h1
        t.score.size=h1/(l(s(vL(t.score)))/2)-3;t.lnsC=i(k);t.bS=t.difficulty*10//((t.lnsC/2)+10)
        if t.bS<1:t.bS=1
      def get(t,o):
        for J,v in t.convert.items():
          if J==o:return v
          elif v==o:return J
      def makeSave(t):
        n=[]
        for b in t.rS:n+=[t.get(lF(b)-0.25),t.get(tP(b)-0.25),t.get(s(fL(b)))]
        n+=["7",t.get(lF(t.cb)),t.get(tP(t.cb)),t.get(fL(t.cb)),t.get(rA(t.cb)%T6),t.get(cX(t.nextBlock)),t.get(cY(t.nextBlock)),t.get(fL(t.nextBlock)),t.get(0),"l"]
        for J in s(vL(t.score)):n+=[t.n2w[i(J)]]
        n+=["w"]
        for J in s(t.lnsC):n+=[t.n2w[i(J)]]
        n+=["x"]
        for J in s(t.tTi):n+=[t.n2w[i(J)]]
        t.zWtri(n,T)
      def importSave(t,v):
        k=L=o=Q;n=[];cL(t.rS);n1=n2=n3=n4=F
        for J in v:
          if(J in"ABCDEFGHIJKLMNOPQRSTUabcdefghijk0123456")&(n1==F):t.sqs+=[t.get(J)]
          elif n1&(J in"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghij0123456klmnopqrstuvwxyz"):
            if n2:
              if J=="w":n3=T
              elif n3==F:k+=t.w2n[J]
              elif n3:
                if J=="x":n4=T
                elif n4==F:L+=t.w2n[J]
                elif n4:o+=t.w2n[J]
            if J=="l":n2=T
            elif n2==F:n+=[t.get(J)]
          if J=="7":n1=T
        t.lnsC=L;t.bS=t.difficulty*10//((i(t.lnsC)/2)+10)
        if t.bS<1:t.bS=1
        t.renderS();t.mBB(n);t.score.value=i(k)
        if vL(t.score)>0:t.score.opacity=h1
        t.score.size=h1/(l(s(t.score.value))/2)-3;t.tTi=i(o);h=s(i(t.tTi/72000));m=s(i(t.tTi/h12%60)+h1)[1:3];z=s(i(t.tTi/20%60)+h1)[1:3]
        if h==0:t.TimePlayed.value=m+":"+z
        else:t.TimePlayed.value=h+":"+m+":"+z
        t.pS()
      def mBB(t,v):
        if t.cb!=N:
          t.cb.fill=N
          for x in t.cb:x.border=N
        if t.nextBlock!=N:
          t.nextBlock.fill=N
          for x in t.nextBlock:x.border=N
        for x in r(2):
          L=v[x*4];o=v[x*4+1];b=v[x*4+2];r=v[x*4+3];g=Grp();bd=grd6gy(tp)
          if b==yl:aD(g,Rct(h2,h2,20,20,fill=yl,border=bd),Rct(t2,h2,20,20,fill=yl,border=bd),Rct(h2,t2,20,20,fill=yl,border=bd),Rct(t2,t2,20,20,fill=yl,border=bd))
          elif b==cy:aD(g,Rct(h2,h2,20,20,fill=cy,border=bd),Rct(h2,t2,20,20,fill=cy,border=bd),Rct(h2,t4,20,20,fill=cy,border=bd),Rct(h2,t6,20,20,fill=cy,border=bd))
          elif b==rd:aD(g,Rct(h2,h2,20,20,fill=rd,border=bd),Rct(t2,h2,20,20,fill=rd,border=bd),Rct(t2,t2,20,20,fill=rd,border=bd),Rct(t4,t2,20,20,fill=rd,border=bd))
          elif b==lm:aD(g,Rct(h2,t2,20,20,fill=lm,border=bd),Rct(t2,t2,20,20,fill=lm,border=bd),Rct(t2,h2,20,20,fill=lm,border=bd),Rct(t4,h2,20,20,fill=lm,border=bd))
          elif b==dv:aD(g,Rct(h2,t2,20,20,fill=dv,border=bd),Rct(t2,t2,20,20,fill=dv,border=bd),Rct(t4,t2,20,20,fill=dv,border=bd),Rct(t2,h2,20,20,fill=dv,border=bd))
          elif b==bl:aD(g,Rct(h2,t2,20,20,fill=bl,border=bd),Rct(t2,t2,20,20,fill=bl,border=bd),Rct(t4,t2,20,20,fill=bl,border=bd),Rct(h2,h2,20,20,fill=bl,border=bd))
          elif b==on:aD(g,Rct(h2,t2,20,20,fill=on,border=bd),Rct(t2,t2,20,20,fill=on,border=bd),Rct(t4,t2,20,20,fill=on,border=bd),Rct(t4,h2,20,20,fill=on,border=bd))
          g.rotateAngle=r;tF(g)
          if x==0:g.left,g.top=L,t;t.cb=g
          else:g.centerX,g.centerY=L,o;t.nextBlock=g
      def zWtri(t,S,io):
        if io:
          aBet=Q.join([chr(j)for j in r(33,127)]);st=A=e=Q;bL=rr(4,8);eL=rr(4,8)
          while l(st)<bL:st+=choice(aBet)
          while l(e)<eL:e+=choice(aBet)
          for c in S:
            for J,v in t.dict.items():
              if c==J:A+=v;break
          F=st+A+e;gti(F);return F,l(f)
        else:
          n=Q;F=[]
          for J in S:
            if J in t.noWidth:n+=s(J)
          for x in r(i(l(n)/5)):F+=[t.dict[n[x*5:x*5+5]]]
          t.importSave(F)
          for J in t.hoL:J.visible=T
          for J in t.vL:J.visible=T
    class Quail:
      def __init__(t):gti("Quail is under construction. Please come back later.");t.stepsPerSecond=0
    def __init__(t):t.active=F;t.cG=t.toader=t.codeclicker=t.dvd=t.tehtrisse=t.twelfthbit=t.undead=t.quail=t.bugreporting=N
    def oS(t):
      if t.cG!=N:t.cG.oS()
  def __init__(t):t.currentBackground=bk;t.loadingScreen=t.LoadingScreen();t.menu=t.Menu();t.game=t.Game();t.allchars=Q.join([chr(j)for j in r(33,127)])
  def oS(t):t.loadingScreen.oS();t.menu.oS();t.game.oS()
  def oMP(t,x,y):
    if(t.menu.active)&(x<T5):
      for S in t.menu.hitboxes:
        if cT(S,x,y)&(t.game.cG==N):
          t.menu.aS.visible=t.loadingScreen.active=t.menu.active=t.game.active=F
          if eval(f"t.game.{S.type}")==N:exec(f"t.game.{S.type}=t.game.{S.type[0].upper()+S.type[1:]}()")
          t.game.cG=eval(f"t.game.{S.type}")
          ap.stepsPerSecond=t.game.cG.stepsPerSecond
          t.game.active=T
          try:t.game.cG.grp.visible=T
          except:F
          if S.type=="toader":
            tB(t.game.cG.losing);tB(t.game.cG.pM)
            for J in r(l(t.game.cG.pI)):t.game.cG.oMP(t8,275)
          break
    elif t.game.cG!=N:
        try:t.game.cG.oMP(x,y)
        except:F
arcade=Arcade()
def onStep():
  try:arcade.oS()
  except:F
ap.oldy=0
def onMousePress(x,y):
  ap.oldy=y
  arcade.oMP(x,y)
  if hT(ap.restart,x,y)&vS(ap.restart):
    if rstrt():restart()
def onMouseDrag(x,y):
  if x>T5:arcade.menu.aS.top-=(ap.oldy-y)*(h8/T5);ap.oldy=y
  if bT(arcade.menu.aS)<h4:arcade.menu.aS.bottom=h4
  elif tP(arcade.menu.aS)>0:arcade.menu.aS.top=0
  if arcade.game.cG!=N:
    try:arcade.game.cG.oMD(x,y)
    except:F
def onMouseRelease(x,y):
  if arcade.game.cG!=N:
    try:arcade.game.cG.oMR(x,y)
    except:F
def onMouseMove(x,y):
  if arcade.game.cG!=N:
    try:arcade.game.cG.oMM(x,y)
    except:F
def onKeyRelease(k):
  if arcade.game.cG!=N:
    try:arcade.game.cG.oKR(k)
    except:F
def onKeyPress(k):
  if arcade.game.cG!=N:
    try:arcade.game.cG.oKP(k)
    except:F
  if(k==esc)&(arcade.game.cG!=None):
      ap.restart.visible=vS(ap.restart)==F;tF(ap.restart)
      if type(arcade.game.cG)!=arcade.game.Toader:
        try:ap.restart.visible=vS(arcade.game.cG.pM)
        except Exception as f:print(f)
def onKeyHold(k):
  if k==[up]:
    arcade.menu.aS.top-=-5*((h8/T5)-1)
    if bT(arcade.menu.aS)<h4:arcade.menu.aS.bottom=h4
    elif tP(arcade.menu.aS)>0:arcade.menu.aS.top=0
  if k==[dw]:
    arcade.menu.aS.top-=5*((h8/T5)-1)
    if bT(arcade.menu.aS)<h4:arcade.menu.aS.bottom=h4
    elif tP(arcade.menu.aS)>0:arcade.menu.aS.top=0
  if arcade.game.cG!=N:
    try:arcade.game.cG.oKH(k)
    except:F
def restart():
  arcade.loadingScreen.restart();ap.background=bk;ap.oldy=ap.paused=ap.restart.visible=F;ap.stepsPerSecond=30;l=[arcdgm+"cG",arcdgm+"toader",arcdgm+"codeclicker",arcdgm+"dvd",arcdgm+"tethtrisse",arcdgm+"twelfthbit",arcdgm+"undead",arcdgm+"quail",arcdgm+"bugreporting"]
  try:arcade.game.cG.track.pause()
  except:F
  for v in l:
    try:exec(v+".grp.visible=F")
    except:F
    exec(v+"=N")
  for S in ap.group:
    try:
      if("Loading"in s(cH(S)))==F:cL(S)
    except Exception as f:S.visible=F;print(f)
try:
 c=l(__BRYTHON__.imported.cmu_graphics.CURRENT_APP_STATE.code);print(c,"is a palindrome"*(s(c)==s(c)[::-1]),"\nleft 2 remove:",(c+8826)-100000)
except:F