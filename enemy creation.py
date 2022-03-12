app.background='White'
# gorblin


gorblin=Group()
gorblin.add(Oval(200,200,100,150,border='black',borderWidth=1))
gorblin.add(Rect(175,269,101,8,align='center',rotateAngle=120,border='black',borderWidth=1))
gorblin.add(Rect(225,269,101,8,align='center',rotateAngle=60,border='black',borderWidth=1))
gorblin.add(Rect(237.5,137.5,101,8,align='center',rotateAngle=-18.5,border='black',borderWidth=1))
gorblin.add(Rect(162.5,137.5,101,8,align='center',rotateAngle=198,border='black',borderWidth=1))
gorblin.add(Oval(200,200,97,147))
gorblin.add(Circle(200,105,30,border='black',borderWidth=1))
gorblin.fill='green'
gorblin.add(Circle(185,100,5,fill='gold'))
gorblin.add(Circle(215,100,5,fill='gold'))
gorblin.add(Line(190,110,210,110,rotateAngle=10)) 






# jelly cube




jellyCube=Group()
jellyCube.add(Polygon(125,150,200,100,200,200,125,250,fill='green'))
jellyCube.add(Polygon(200,100,275,150,275,250,200,200,fill='lightgreen'))
jellyCube.add(Polygon(200,200,275,250,200,300,125,250,fill='darkgreen'))
jellyCube.add(Polygon(200,200,275,150,275,250,200,300,fill='lightgreen',opacity=50))
jellyCube.add(Polygon(200,200,200,300,125,250,125,150,fill='darkgreen',opacity=50))
jellyCube.add(Polygon(125,150,200,200,275,150,200,100,fill='green',opacity=50))
jellyCube.add(Polygon(200,100,275,150,275,250,200,300,125,250,125,150,fill=None,border='black',borderWidth=2))
jellyCube.add(Line(200,200,125,250,lineWidth=1,fill='dimgray'))
jellyCube.add(Line(200,200,275,250,lineWidth=1,fill='dimgray'))
jellyCube.add(Line(200,200,200,100,lineWidth=1,fill='dimgray'))
jellyCube.add(Line(275,150,200,200,lineWidth=2))
jellyCube.add(Line(200,200,125,150,lineWidth=2))
jellyCube.add(Line(200,200,200,300,lineWidth=2))








# skelybones


skel=Group()
skel.add(Rect(200,90,16,104,align='top',fill=rgb(235, 235, 235),border='black',borderWidth=1))
skel.add(Rect(200,100,110,10,fill=rgb(235, 235, 235),border='black',borderWidth=1,align='center'))
skel.add(Rect(200,120,90,10,fill=rgb(235, 235, 235),border='black',borderWidth=1,align='top'))
skel.add(Rect(200,140,90,10,fill=rgb(235, 235, 235),border='black',borderWidth=1,align='top'))
skel.add(Rect(200,165,60,10,fill=rgb(235, 235, 235),border='black',borderWidth=1,align='center'))
skel.add(Oval(200,65,50,65,fill=rgb(235, 235, 235),border='black',borderWidth=1))
skel.add(Rect(205,250,111,10,fill=rgb(235, 235, 235),border='black',borderWidth=1,rotateAngle=75,align='left'))
skel.add(Rect(195,250,111,10,fill=rgb(235, 235, 235),border='black',borderWidth=1,rotateAngle=-75,align='right'))
skel.add(Rect(255,155,101,10,fill=rgb(235, 235, 235),border='black',borderWidth=1,rotateAngle=75,align='left'))
skel.add(Rect(145,155,101,10,fill=rgb(235, 235, 235),border='black',borderWidth=1,rotateAngle=-75,align='right'))
skel.add(Circle(185,65,5))
skel.add(Circle(215,65,5))
### face 1
skel.add(Line(190,80,210,80,rotateAngle=0))
### face 2
skel.add(Label('ww',200,80,rotateAngle=0))






# zomboi


zobi=Group()
zobi.add(Oval(200,148,100,120,border='black',borderWidth=1))
zobi.add(Rect(205,250,111,15,border='black',borderWidth=1,rotateAngle=75,align='left'))
zobi.add(Rect(195,250,111,15,border='black',borderWidth=1,rotateAngle=-75,align='right'))
zobi.add(Rect(215,136,121,15,border='black',borderWidth=1,rotateAngle=35,align='left'))
zobi.add(Rect(185,136,121,15,border='black',borderWidth=1,rotateAngle=-35,align='right'))
zobi.add(Oval(200,148,98,118))
zobi.add(Oval(200,65,50,65,border='black',borderWidth=1))
zobi.fill='green'
zobi.add(Circle(185,65,5))
zobi.add(Circle(215,65,5))
zobi.add(Oval(250,180,80,62,rotateAngle=60,fill=app.background))
zobi.add(Polygon(219,160,217,170,245,170,245,160,fill=rgb(235, 235, 235),border='black',borderWidth=1))
zobi.add(Polygon(224,150,245,150,245,142,235,143,228,147,fill=rgb(235, 235, 235),border='black',borderWidth=1))
zobi.add(Polygon(218,180,221,190,230,190,230,180,fill=rgb(235, 235, 235),border='black',borderWidth=1))
wound=Group(Line(250,142,235,143),Line(235,143,228,147),Line(228,147,224,150),Line(224,150,219,160),Line(219,160,217,170),Line(217,170,218,180),Line(218,180,221,190),Line(221,190,225,200))
wound.fill='red'
zobi.add(wound)
zobi.add(Label('0',200,80,rotateAngle=90))








#sprite mimic color inverted
sprite=Group()
sprite.add(Oval(200,300,150,80,fill='green',border='black',borderWidth=1))
sprite.add(Rect(125,100,150,200,fill='green',border='black',borderWidth=1))
sprite.add(Rect(200,100,146,200,fill='green',align='top'))
sprite.add(Oval(200,100,150,80,fill='silver',border='black',borderWidth=1))
sprite.add(Oval(240,100,30,40))
sprite.add(Label('sprite',205,220,rotateAngle=-20,size=35,fill='white'))
sprite.add(Star(202.5,225,75,7,fill=None,border='white',borderWidth=5,rotateAngle=15))






# sprite mimic


spritem=Group()
spritem.add(Oval(200,300,150,80,fill=rgb(255,127,255),border='black',borderWidth=1))
spritem.add(Rect(125,100,150,200,fill=rgb(255,127,255),border='black',borderWidth=1))
spritem.add(Rect(200,100,146,200,fill=rgb(255,127,255),align='top'))
spritem.add(Oval(200,100,150,80,fill=rgb(63,63,63),border='black',borderWidth=1))
spritem.add(Oval(240,100,30,40,fill='white'))
spritem.add(Label('sprite',205,220,rotateAngle=-20,size=35,fill='black'))
spritem.add(Star(202.5,225,75,7,fill=None,border='black',borderWidth=5,rotateAngle=15))






# rate


rate=Group()
rate.add(Oval(215,200,150,80,fill='gray',border='black',borderWidth=1))
rate.add(Rect(160,230,50.5,8,rotateAngle=-45,align='center',fill='pink',border='black',borderWidth=1))
rate.add(Rect(170,230,50.5,8,rotateAngle=45,align='center',fill='pink',border='black',borderWidth=1))
rate.add(Rect(270,230,50.5,8,rotateAngle=45,align='center',fill='pink',border='black',borderWidth=1))
rate.add(Rect(260,230,50.5,8,rotateAngle=-45,align='center',fill='pink',border='black',borderWidth=1))
rate.add(Rect(150,197,101,8,align='right',fill='pink',rotateAngle=7,border='black',borderWidth=1))
rate.add(Oval(215,200,147,76,fill='gray'))
rate.add(Oval(277,175,20,30,fill='dimgray',border='black',borderWidth=1,rotateAngle=-35))
rate.add(Oval(290,195,60,45,fill='gray',border='black',borderWidth=1))
rate.add(Circle(300,190,5,fill='black'))
rate.add(Circle(320,195,5,fill='black'))




#rat kong  mini boss


kingRat=Group()
kingRat.add(Oval(215,200,150,80,fill='dimgray',border='black',borderWidth=1))
kingRat.add(Rect(160,230,50.5,8,rotateAngle=-45,align='center',fill='palevioletred',border='black',borderWidth=1))
kingRat.add(Rect(170,230,50.5,8,rotateAngle=45,align='center',fill='palevioletred',border='black',borderWidth=1))
kingRat.add(Rect(270,230,50.5,8,rotateAngle=45,align='center',fill='palevioletred',border='black',borderWidth=1))
kingRat.add(Rect(260,230,50.5,8,rotateAngle=-45,align='center',fill='palevioletred',border='black',borderWidth=1))
kingRat.add(Rect(150,197,101,8,align='right',fill='palevioletred',rotateAngle=7,border='black',borderWidth=1))
kingRat.add(Oval(215,200,147,76,fill='dimgray'))
#kingRat.add(Oval(277,175,20,30,fill=rgb(90,90,90),border='black',borderWidth=1,rotateAngle=-35))#extra dim gray
kingRat.add(Oval(290,195,60,45,fill='dimgray',border='black',borderWidth=1))
kingRat.add(Circle(300,190,5,fill='black'))
kingRat.add(Circle(320,195,5,fill='black'))
crown=Polygon(274,158,274,178,317.2,178,317.2,158,310,168,302.8,158,295.6,168,288.4,158,281.2,168,fill='gold',border='goldenrod')
crown.centerX=291
crown.bottom=180
kingRat.add(crown)






# llama


llama=Group()
#llama.add(Polygon(150,230,250,230,315,240,315,250,85,250,85,240,fill='red'))#10 out 
llama.add(Polygon(255,230,250,310,235,310,235,250,165,250,165,310,150,310,145,230))
llama.add(Oval(225,250,100,100,align='bottom'))
llama.add(Oval(175,250,100,100,align='bottom'))
llama.add(Rect(175,150,50,50))
llama.add(Rect(275,200,35,120,align='right-bottom'))
llama.add(Rect(257.5,53.5,18,4,align='center',rotateAngle=-70))
llama.fill='lime'
llama.add(Polygon(275,95,300,85,300,75,260,65,fill=rgb(0,230,0)))
llama.add(Circle(240,80,20,align='left',fill='lime'))
llama.add(Circle(255,75,5,fill=rgb(0,170,0)))


# i like to kermit war crimes 
kermit=Group()


kermit.add(Oval(200,148,100,120,border='black',borderWidth=1,fill='olivedrab'))
kermit.add(Rect(205,250,111,15,border='black',borderWidth=1,rotateAngle=75,align='left',fill='olivedrab'))
kermit.add(Rect(195,250,111,15,border='black',borderWidth=1,rotateAngle=-75,align='right',fill='olivedrab'))
kermit.add(Rect(215,136,121,15,border='black',borderWidth=1,rotateAngle=35,align='left',fill='olivedrab'))
kermit.add(Rect(185,136,121,15,border='black',borderWidth=1,rotateAngle=-35,align='right',fill='olivedrab'))
kermit.add(Oval(200,148,98,118,fill='olivedrab'))
kermit.add(Star(200,90,50,8,fill=rgb(190,164,62)))
kermit.add(Oval(200,65,50,65,border='black',borderWidth=1,fill='olivedrab'))
kermit.add(Circle(185,62.5,5))
kermit.add(Circle(215,62.5,5))




# cmu dragon


stencil=Image('https://academy.cs.cmu.edu/static/media/darkDragon.aefa2ad0.png',0,0)
stencil.width*=80/67
stencil.height*=80/67
stencil.centerX=200
stencil.centerY=200
'''
Oval(200,210,200,90,rotateAngle=-30,fill='teal')
Polygon(120,215,80,235,45,267.5,30,305,37.5,345,70,370,107.5,370,155,355,190,345,210,322.5,
        190,330,155,342.5,120,355,70,350,55,330,55,305,60,290,75,275,95,267.5,116,264.5,fill='red')
Oval(220,352.5,70,60,fill=None,border='green',borderWidth=15)
a='hotpink'
Line(225,325,250,325,fill=a)
Line(250,325,265,330,fill=a)
Line(265,330,277.5,342.5,fill=a)
Line(277.5,342.5,285,370,fill=a)
Line(285,370,290,385,fill=a)
'''












# gorblin               done
# jelly cube            done
# skelybones            done
# zomboi                done
# sprite                done
# sprite evil           done
# rate                  done
# wharewolfs            
# kormit                
# cheems/doge           
# wiserd                
##### bosses
# king rat              done 
# the majik boi (boss)  
# cmu draggon           done
# llama                 done






gorblin.visible=False
jellyCube.visible=False
skel.visible=False
zobi.visible=False
sprite.visible=False
spritem.visible=False
rate.visible=False
kingRat.visible=False
llama.visible=False
kermit.visible=False
stencil.visible=False