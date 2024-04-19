ball=Circle(randrange(100,300),randrange(100,300),30,fill='white',rotateAngle=45)#randrange(360))


color='mediumOrchid'
im1=Group(Oval(186,152.5,177.5*2,26*2),Oval(70,50-2,(153-69)*2,(108-52)*2),Polygon(60,104,60,103,56,103,56,104),Oval(70+221,104,90*2,48*2,align='bottom'),Oval(70+255,9,60*2,41*2,align='top'))
im1.fill=color


im2=Group(Oval(180,152.5,40*2,10*2),Oval(70-1,24,100-7,60-1,align='top'),Polygon(54,104,54,23,138,20,138,-10,-16,-10,-16,103),Oval(70-1+230,24+59,100-7,55,align='bottom'),Polygon(269,104,269+30,4,200,4,200,104))
im2.fill='white'


im3=Group(Polygon(35,38,71,38,56,104,20-1,104),Polygon(266,38,302,38,286,104,250.5,104),Polygon(37,30,41.5,9,180,9,200-1,70,247,9,320,9,320,30,269,30,185.5,127,152,30))
im3.fill=color


all=Group(im1,im2,im3)
all.width/=10/3
all.height/=10/3
all.add(Label('TM',237,106,size=10,italic=True,bold=True,fill=color))
app.hits=0
border=Group(Line(400,0,0,0,lineWidth=5),
    Line(400,0,400,400,lineWidth=5),
    Line(400,400,0,400,lineWidth=5),
    Line(0,400,0,0,lineWidth=5))
app.stepsPerSecond=60
app.counter=0
app.x1,app.y1=ball.centerX,ball.centerY
def onStep():
    app.counter+=1
    ball.centerX,ball.centerY=getPointInDir(ball.centerX,ball.centerY,ball.rotateAngle,2)
    for shape in border:
        if all.hitsShape(shape) and app.counter>10:
            app.counter=0
            angle=angleTo(shape.x1,   shape.y1,  shape.x2,   shape.y2)
            dif=ball.rotateAngle-angle
            num=angle-dif
            ball.rotateAngle=num
            app.hits+=1
            Line(app.x1,app.y1,ball.centerX,ball.centerY)
            app.x1,app.y1=ball.centerX,ball.centerY
            if app.hits%2==0:
                
                all.fill='blue'
                im2.fill='white'
            else:
                
                all.fill=color
                im2.fill='White'
    all.centerX=ball.centerX
    all.centerY=ball.centerY  
### give player slight "control" of the logo
### move it so it dosen't hit corner