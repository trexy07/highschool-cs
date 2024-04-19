everything=Group()


### tehetrisse
everything.add(Rect(0,300,400,100))


for x in range(0,400,25):
    everything.add(Line(x,300,x,400,fill='white'))
for y in range(300,400,25):
    everything.add(Line(0,y,400,y,fill='white'))


d='gray'
bord=gradient('white',d,d,d,d,d,d,rgb(70,70,70),start='top')


piece1=Group(Rect(25,325,25,25,border=bord),Rect(25,350,25,25,border=bord),Rect(25,375,25,25,border=bord))
piece1.fill='cyan'


piece2=Group(Rect(0,300,25,25,border=bord),Rect(25,300,25,25,border=bord),Rect(50,300,25,25,border=bord))
piece2.fill='cyan'


lab=Label("EHTRISSE",237.5,350,fill='white',size=65,bold=True)


piece1.top=25
piece2.top=0
lab.bottom=47 
everything.add(piece1,piece2,lab)
app.count=0
def reStep():
    app.count+=1
    if app.count>15:
        if not piece1.bottom==bot.bottom and app.count%2==0:
            piece1.centerY+=25
        elif piece1.bottom==bot.bottom and not piece2.bottom==bot.bottom-75:
            if app.count%2==0:
                piece2.centerY+=25
        elif  lab.bottom <bot.bottom-25:
            if app.count%2==0:
                lab.bottom+=25
        
        if piece1.bottom>=bot.bottom:
            piece1.bottom=bot.bottom
        if piece2.bottom>=bot.bottom-75:
            piece2.bottom=bot.bottom-75
        
bot=Rect(0,300,400,100,border='gray',fill=None)
everything.add(bot)
### code clicker
everything.add(Rect(0,0,400,100))
b=rgb(55,118,171)
y=rgb(255,211,67)


im=Image("https://cdn.freebiesupply.com/logos/large/2x/python-5-logo-png-transparent.png",0,0)


size=52.5




everything.add(Label("C DE CLICKER",200,50,fill=gradient(b,b,y,y,y,y,y,y,y,y,y,y,start='left'),size=52.5,font='monospace',bold=True,border='Black',borderWidth=1.5))
im.width/=65
im.height/=65
im.centerX=60-2.5
im.centerY=50
everything.add(im)
everything.add(Rect(0,0,400,100,border='gray',fill=None))






### 12th bit 
pickColor={
    0:'gray',
    2:'red',
    4:'orange',
    8:'yellow',
    16:'green',
    32:'blue',
    64:'darkviolet',
    128:'pink',
    256:rgb(255, 195, 30),
    512:rgb(255, 255, 100),
    1024:'lightgreen', 
    2048:'cornflowerBlue'}


for x in range(0,400,25):
    for y in range(100,200,25):
        n=choice([2,4,8,16,32,64,128,256,512,1024,2048])
        everything.add(Rect(x,y,25,25,fill=pickColor[n]))
        off=25/2
        e=75/2
        everything.add(Label(n,x+off,y+off,size=e/len(str(n))))


everything.add(Label('12TH BIT',200,150,fill='black',size=85,border='White',bold=True))


everything.add(Rect(0,100,400,100,border='gray',fill=None))


### dvd


everything.add(Rect(0,200,400,100,fill='white'))


ball=Circle(256+100-5,244,5,fill='white',rotateAngle=45+180)
checker=Rect(ball.centerX,ball.centerY,60,28,align='center',fill=None)
everything.add(ball,checker)
color='mediumOrchid'
im1=Group(Oval(186,152.5,177.5*2,26*2),Oval(70,50-2,(153-69)*2,(108-52)*2),Polygon(60,104,60,103,56,103,56,104),Oval(70+221,104,90*2,48*2,align='bottom'),Oval(70+255,9,60*2,41*2,align='top'))
im1.fill=color


im2=Group(Oval(180,152.5,40*2,10*2),Oval(70-1,24,100-7,60-1,align='top'),Polygon(54,104,54,23,138,20,138,-10,-16,-10,-16,103),Oval(70-1+230,24+59,100-7,55,align='bottom'),Polygon(269,104,269+30,4,200,4,200,104))
im2.fill='white'


im3=Group(Polygon(35,38,71,38,56,104,20-1,104),Polygon(266,38,302,38,286,104,250.5,104),Polygon(37,30,41.5,9,180,9,200-1,70,247,9,320,9,320,30,269,30,185.5,127,152,30))
im3.fill=color


all=Group(im1,im2,im3)
all.width/=20/3
all.height/=20/3
everything.add(all)




app.hits=0
border=Group(Line(400,200,0,200,lineWidth=5,fill=None),
    Line(0,300,400,300,lineWidth=5,fill=None),
    Line(0,200,0,300,lineWidth=5,fill=None),
    Line(400,200,400,300,lineWidth=5,fill=None))
everything.add(border)


bot2=Rect(0,200,400,100,border='gray',fill=None)
app.counter=0
def onStep():
    reStep()
    onStep2()
    app.counter+=1
    if not (rounded(ball.centerX)==30 and (rounded(ball.centerY)==rounded(bot2.bottom-18)or rounded(ball.centerY)==rounded(bot2.bottom-17))):
        ball.centerX,ball.centerY=getPointInDir(ball.centerX,ball.centerY,ball.rotateAngle,2)
        for shape in border:
            if checker.hitsShape(shape) and app.counter>10 :
                app.counter=0
                angle=angleTo(shape.x1,   shape.y1,  shape.x2,   shape.y2)
                dif=ball.rotateAngle-angle
                num=angle+0-dif
                ball.rotateAngle=num
                app.hits+=1
                if app.hits%2==1:
                    all.fill='blue'
                    im2.fill='white'
                else:
                    all.fill=color
                    im2.fill='White'
        all.centerX=ball.centerX
        all.centerY=ball.centerY  
        checker.centerX=ball.centerX
        checker.centerY=ball.centerY


everything.add(bot2)


ev2=Group()




### labrinth of the undead


"""
t=25
b=75
l=3.5


ev2.add(Rect(0,0,400,100,fill=rgb(30,30,30)))
ud=Group()
ud.add(Line(25,t,25,b,lineWidth=l))
ud.add(Line(25,b,50,b,lineWidth=l))
ud.add(Line(50,b,50,t,lineWidth=l))


ud.add(Line(75,t,75,b,lineWidth=l))
ud.add(Line(75,t,100,b,lineWidth=l))
ud.add(Line(100,b,100,t,lineWidth=l))


d1=Arc(125,50,50,50,0,180,fill=None,border='black',borderWidth=l)
ud.add(d1)


ud.add(Line(175,t,175,b,lineWidth=l))
ud.add(Line(175,t,200,t,lineWidth=l))
ud.add(Line(175,b,200,b,lineWidth=l))
ud.add(Line(175,50,187.5,50,lineWidth=l))


ud.add(Line(225,50,237.5,t,lineWidth=l))
ud.add(Line(237.5,t,250,50,lineWidth=l))
ud.add(Line(250,50,250,b,lineWidth=l))
ud.add(Line(225,50,225,b,lineWidth=l))
ud.add(Line(225,50,250,50,lineWidth=l))
d2=Arc(275,50,50,50,0,180,fill=None,border='black',borderWidth=l)
ud.add(d2)


ud.add(Line(325,t,325,62.5,lineWidth=l))
ud.add(Circle(325,b,l))
ud.centerX+=25
ud.fill='gray'
d1.border=ud.fill
d2.border=ud.fill
d1.fill=None
d2.fill=None




m=Group(
    Line(50,75,50,100),
    Line(0,100,0,50),
    Line(0,50,25,50),
    Line(25,50,25,75),
    Line(50,25,25,25),
    Line(100,25,75,25),
    Line(125,75,150,75),
    Line(200,75,200,100),
    Line(250,75,250,100),
    Line(250,25,275,25),
    Line(300,25,300,0),
    Line(325,50,350,50),
    Line(350,25,375,25),
    Line(375,25,375,75))
m.fill='gray'


"""
ob=Group(Polygon(221,-5,315,29,179,405,85,371,fill=gradient('black','black','forestgreen',start='left')))
ob.rotateAngle=70
ob.top=000
ev2.add(ob)


ev2.add(Label('LABRINTH',200,100/3,fill='white',size=30,font='cinzel'))
ev2.add(Label('OF THE UNDEAD',200,100/3*2,fill='white',size=30,font='cinzel'))
ev2.add(Rect(0,0,400,100,border='gray',fill=None))
### max's quail code  
ev2.add(Rect(0,100,400,100)) 








quail=Label('Quail_',115,150,fill='lime',font='montserrat',size=52,align='left')
quail.counter=0
def onStep2():
    quail.counter+=1
    if quail.counter%15==10:
        if quail.value=='Quail_':
            quail.value='Quail'
        else:
            quail.value='Quail_'
        quail.left=115
    


ev2.add(quail)
ev2.add(Rect(0,100,400,100,border='gray',fill=None))






ev2.top=400
everything.add(ev2)








app.offy=0
app.oldy=0
def onMousePress(x,y):
    app.oldy=y
def onMouseDrag(x,y):
    if  x>350:
        dif=(app.oldy-y)*(everything.height/350-1)
        app.oldy=y
        everything.top-=dif
    if everything.bottom<400:
        everything.bottom=400
    elif everything.top>0:
        everything.top=0