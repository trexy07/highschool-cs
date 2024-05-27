back=Image('https://media.istockphoto.com/vectors/rock-seamless-pattern-vector-design-illustration-vector-id1249992176?b=1&k=20&m=1249992176&s=170667a&w=0&h=YiF3wT-puPnKcY25RJd5RzyNBQbWMWKZpAlcsbfeU2E=',0,0)
app.lv=1
c='skyblue'
lv1=Group(Polygon(0,250,150,250,150,175,100,175,100,50,300,50,300,175,250,175,250,250,400,250,400,375,0,375,fill=c),Polygon(0,0,400,0,400,225,275,225,275,200,325,200,325,25,75,25,75,200,125,200,125,225,0,225,fill=c))
lv2=Polygon(150,0,150,225,0,225,0,250,175,250,175,0,400,0,400,375,325,375,325,200,300,200,300,375,0,375,0,0,fill=c,visible=False)


lv2gen=Image('https://cdn-icons-png.flaticon.com/512/3463/3463407.png',325,300+5,visible=False)
lv2gen.width=75
lv2gen.height=75
rods=Group()
lavatop=Rect(100,150,200,25,fill=gradient('orange','yellow',start='bottom'))
lavabot=Rect(150,175,100,70/2,fill=gradient('red','orange',start='bottom'))
watertop=Rect(100,75,200,35,fill='blue')
waterbot=Rect(150,175,100,1,fill='blue',visible=False)
enemy=Image('https://www.graphicpie.com/wp-content/uploads/2020/11/red-among-us-png.png',150,275)
enemy.width/=20
enemy.height/=20
app.totalstep=0
app.targetstep=-1
player=Image('https://static.wikia.nocookie.net/among-us-wiki/images/a/a2/Green_old_design.png/revision/latest/scale-to-width-down/250?cb=20201013061349',0,0)
player.width/=2
player.height/=2
player.left=-30
player.bottom=385
ash=Image('https://kadantgrantek.com/templates/yootheme/cache/gransorb_pile-b2075fa8.png',0,0,visible=False)
ash.width/=10
ash.height/=10
ash.centerX=20
ash.bottom=390
ash.opacity=100
flow=Polygon(60,353,60,375,15,375,fill=gradient('red','orange',start='bottom'),opacity=0)
dead=Image('https://static.wikia.nocookie.net/among-us-wiki/images/3/38/Fortegreen%27s_dead_body.png/revision/latest/scale-to-width-down/250?cb=20210628111711',0,325,visible=False)
dead.width/=3.5
dead.height/=3.5
def rod(x1,y1,x2,y2,hx,hy,dirx,diry):
    
    e=Group(Line(x1,y1,x2,y2,fill='goldenrod',lineWidth=5),Circle(hx,hy,12.5,fill='skyblue',border='goldenrod',borderWidth=5))
    
    e.dirY=diry
    e.dirX=dirx
    e.toFront()
    rods.add(e)
def lower_lava():
    if not lavatop.height-1<=0:
        lavatop.height-=1
        lavatop.bottom=175
        lavabot.height+=1
        lavabot.top=175
    elif not lavabot.bottom>=375:
        lavatop.visible=False
        lavabot.height+=1
        lavabot.top+=1
        
    else:
        #lavabot.visible=False
        if not lavabot.height-3<=20:
            lavabot.width+=5
            lavabot.height-=3
        lavabot.bottom=375
        lavabot.centerX=200
        if lavabot.visible:
            enemy.visible=False
            #ash.visible=True
def lower_water():
    
    if watertop.hitsShape(lavatop) and lavatop.visible:
        lavatop.visible=False
        lavabot.visible=False
        Rect(100,150,200,25)
        Rect(150,175,100,35)
        watertop.visible=False
    if not watertop.bottom>=175 and lavabot.visible:
        watertop.centerY+=2
    elif watertop.bottom>=175 and not watertop.height-1==0:
        waterbot.visible=True
        waterbot.height+=2
        waterbot.top=175
        watertop.height-=1
        watertop.bottom=175
    elif not waterbot.bottom>=353:
        watertop.visible=False
        waterbot.height+=1
        waterbot.top+=1
    elif not waterbot.height-2==0 and not enemy.visible:
        waterbot.height-=2
        waterbot.top+=2
        Rect(60,353,280,22)
        lavabot.visible=False
    else:
        waterbot.visible=False
def onStep():
    if player.centerX>=400 and app.lv==1 :
        wl('YOU WON!!!','lime')
    app.totalstep+=1
    for rod in rods:
        if rod.centerY==212.5:
            if rod.left>=250:
                lower_lava()
        if rod.centerY==112.5:
            if rod.left>=300:
                lower_water()
        if rod.centerX==62.5:
            if rod.bottom<=250 and lavabot.width==280 and flow.opacity !=100 and lavabot.visible:
                flow.opacity+=2.5
            if rod.bottom<=250 and not lavabot.visible and not waterbot.visible and not enemy.visible and app.lv==1:
                player.centerX+=5
                player.toFront()
            if flow.opacity ==100:
                ash.visible=True
                player.visible=False
                #ash.toFront()
                wl('You were burnt to ash!','firebrick')
            elif rod.bottom<=250 and enemy.visible:
                if not enemy.centerX<=50:
                    enemy.centerX-=5
                    enemy.toFront()
                else:
                    player.visible=False
                    dead.visible=True
                    #enemy.toFront()
                    wl('the susy baka got you','firebrick')
        if rod.contains(app.x,app.y):
            rod.centerX+=rod.dirX
            rod.centerY+=rod.dirY
            app.x=rod.centerX
            app.y=rod.centerY
            if rod.centerX>800 or rod.centerX<-800 or rod.centerY>800 or rod.centerY<-800:
                pass
                
app.x=0
app.y=0
def onMousePress(x,y):
    app.x=x
    app.y=y
    for rod in rods:
        if rod.contains(x,y):
            rod.centerX+=rod.dirX
            rod.centerY+=rod.dirY
rod(75,112.5,350,112.5,375-12.5,112.5,5,0)
rod(125,212.5,300,212.5,325-12.5,212.5,5,0)
rod(62.5,375,62.5,200,62.5,200-12.5,0,-5)
cover=Group()
mes=Group()
def wl(message,color):
    print('f')
    if app.totalstep>app.targetstep:
        app.targetstep=app.totalstep+45
        print('changed ')
    player.toBack()
    if len(cover)==0:
        dead.toFront()
        ash.toFront()
        cover.add(Rect(0,0,400,400,opacity=75))
        print('coveradded')
        mes.add(Label(message,200,200,fill=color,size=40))
        cover.toFront()
        mes.toFront()
        cover.visible=True
        mes.visible=True
    
    if app.targetstep==app.totalstep:
        if  color=='lime':
            app.lv+=1
            print(app.lv)
        cover.clear()
        mes.clear()
        app.targetstep=-1
        if app.lv==1:
            cover.visible=False
            mes.visible=False
            back.toFront()
            lv1.toFront()
            watertop.visible=True
            watertop.height=35
            watertop.top=75
            watertop.left=100
            watertop.toFront()
            waterbot.height=1
            waterbot.top=175
            waterbot.toFront()
            rods.clear()
            rod(75,112.5,350,112.5,375-12.5,112.5,5,0)
            rod(125,212.5,300,212.5,325-12.5,212.5,5,0)
            rod(62.5,375,62.5,200,62.5,200-12.5,0,-5)
            rods.toFront()
            lavatop.visible=True
            lavatop.toFront()
            lavatop.height=25
            lavatop.bottom=175
            lavabot.width=100
            lavabot.height=35
            lavabot.left=150
            lavabot.bottom=210
            lavabot.visible=True
            lavabot.toFront()
            enemy.visible=True
            enemy.toFront()
            enemy.centerX=200
            player.visible=True
            player.toFront()
            player.centerX=7
            flow.toFront()
            flow.opacity=0 
            dead.toFront()
            ash.visible=False
            dead.visible=False
            waterbot.visible=False
        if app.lv==2:
            player.centerX=7
            cover.visible=False
            mes.visible=False
            back.toFront()
            lv2.toFront()
            lv2.visible=True
            lv1.visible=False
            lv2gen.visible=True
            player.toFront()
            rods.clear()
            rod(150,75-12.5,150+175,75-12.5+175,142.5,55,-2.5,-2.5)
            rod(62.5,375,62.5,200,62.5,200-12.5,0,-5)
            rod(312.5,25,312.5,200,312.5,12.5,0,-5)
            rods.toFront()