app.money=0


app.clickPoint=1
app.background='black'


app.stepsPerSecond=20
app.cps=0
app.quantity=0
app.doubler=1
app.wait=-1


hit=Image('https://cdn.freebiesupply.com/logos/large/2x/python-5-logo-png-transparent.png',0,0)
hit.width/=20
hit.height/=20
hit.centerX=200
hit.centerY=200


##### make python pop when clicked
## idle game in zwtri






code=Group()


pointsUp=Group(Rect(200-200,0,200,75-25/2,fill='blue'),Label('upgrade money per click',300-200,25/2))
num1=Label('1 $',300-200,15+25/2)
num2=Label(1,300-200,30+25/2)


pasiveUp=Group(Rect(0+200,0,200,75-25/2,fill='red'),Label('upgrade pasive clicks',100+200,25/2))
num3=Label('1 $',100+200,15+25/2)
num4=Label(0,100+200,30+25/2)


bost=Group(Rect(200,350-25/2,200,75-25/2,fill='lime'))
bost.alpha=Label('doubleClicks',300,350+25/2)
num5=Label('500 $',300,15+25/2+350)
bost.price=1


Rect(0,338,200,400-338,fill='yellow')
money=Label("0 $",100,366,size=69)
sizeCheck=Rect(0,330,200,8,fill=None)


def codes2 ():
    f=", "
    colors=['red','orange','yellow','green','lime','cyan','blue','violet','purple','None','white','black','gray']
    color=choice(colors)
    a=str(randrange(0,400))
    b=str(randrange(0,400))
    c=str(randrange(10,51))
    d=str(randrange(10,51))
    kind=randrange(8)
    if kind==0:
        return("Rect("+a+f+b+f+c+f+d+f+'fill = "'+color+'")')
    elif kind==1:
        return("Oval("+a+f+b+f+c+f+d+f+'fill = "'+color+'")')
    elif kind==2:
        return("Circle("+a+f+b+f+c+f+'fill = "'+color+'")')
    elif kind==3:
        return("Line("+a+f+b+f+ str(int(c)+int(a))+f+ str(int(d)+int(b))+f+'fill = "'+color+'")')
    elif kind==4:
        return("RegularPolygon("+a+f+b+f+c+f+str(randrange(10))+f+'fill = "'+color+'")')
    elif kind==5:
        return("Star("+a+f+b+f+c+f+str(randrange(10))+f+'fill = "'+color+'")')
    if kind==6:
        return("Arc("+a+f+b+f+c+f+d+f+str(randrange(360))+f+str(randrange(360))+f+'fill= "'+color+'")')
    if kind==7:
        e=""
        for i in range(5):
            e+=choice("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        return('Label("'+e+'"'+f+a+f+b+f+'fill = "'+color+'")')
    


doc={
    0:"",
    
}
string=[]
for y in ['','c']:
    for x in ['','d','vg','tg','qag','qig','sxg','spg','ocg','nog']:
        for i in ['','U','D','T','Qa','Qi','Sx','Sp','Oc','No']:
            if i+x+y=='U':
                string.append("M")
            elif i+x+y=='D':
                string.append("B")
            elif i+x+y=='':
                string.append('K')
            else:
                string.append(i+x+y)
#print(string)


for i in range(len(string)):
    #print(i+1,string[i])    
    doc.update({i+1:string[i]})
print(doc)
def no(t):
    for i in range(0,len(str(t))//3+1):
         
        if t<=10**(3*(i+1))-1:
            return(str(t//(10**(3*i)))+" "+doc[i])


app.mini=0
def onMousePress(x,y):
    
    if hit.hits(x,y):
        app.mini+=1
        app.money+=app.clickPoint*app.doubler
        if app.mini==5:
            app.mini=0
            bravo=Label(codes2(),randrange(100,300),400,fill='lime',size=15)
            if bravo.left<=0:
                bravo.left=5
            elif bravo.right>=400:
                bravo.right=395
            bravo.toBack()
            code.add(bravo)
            
    elif pointsUp.hits(x,y):
        if app.money>=app.clickPoint**3+1:
            app.money-=app.clickPoint**3+1
            app.clickPoint+=1
            num1.value=no(app.clickPoint**3)+" $"
            num2.value=app.clickPoint
    elif pasiveUp.hits(x,y) :
        if app.money>=app.cps**3+1:
            app.money-=app.cps**3+1
            app.cps+=1
            app.quantity+=1
            num3.value=no(app.cps**3)+" $"
            num4.value=app.cps
    elif bost.hits(x,y):
        if app.money>=bost.price**2*500 and bost.fill=='lime':
            app.money-=bost.price**2*500
            bost.price+=1
            num5.value=no(bost.price**2*500)+' $'
            app.doubler=2
            app.wait=app.count+400
            bost.fill='gray'
app.count=0
def onStep():
    for item in code:
        item.centerY-=5
        if item.bottom<=0:
            code.remove(item)
    money.value=no(app.money)+" $"
    
    
    for i in range(0,70):
        money.size=70-i
        if money.hitsShape(sizeCheck) or money.hitsShape(bost):
            pass
        else:
            money.size=70-i
            break
    app.count+=1
    if app.count%20==0:
        
        app.money+=app.quantity*app.doubler
        print(app.money,app.clickPoint,app.quantity)
        
    if app.wait==app.count:
        app.doubler=1
        bost.fill='lime'