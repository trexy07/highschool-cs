app.linesCleared=0
##### steps per 1 row drop =256//((app.linescleard/2)+10)




### song 4
track=Sound('http://docs.google.com/uc?export=open&id=1Z88_byi8WaIpxVeLqnLuhmy-kXokGatq')
track.play(restart=True)


#84 seconds 
### song 4


##### importing stuff


import random


##### importing stuff










##### actual game stuff


## Creates the background that the lines are on
TehtrisseRect = Rect(50, -5, 200, 410, border = "white")


## Creates the rectangle where the next piece goes
NextPieceRect = Rect(325, 70, 90, 90, border = "white",align='center')


## Creates a label to display time played
TimePlayed = Label("00:00", 325, 265, size = 24, font = "orbitron", bold = True, fill = "white")


## up arrow
upArrow = Polygon(325, 331,   308, 314,   308, 281,   342, 281,   342, 314,   fill = None, border = "white")


## left arrow
leftArrow = Polygon(326, 330,   309, 347,   276, 347,   276, 313,   309, 313,   fill = None, border = "white")


## down arrow
downArrow = Polygon(325, 329,   342, 346,   342, 379,   308, 379,   308, 346,   fill = None, border = "white")


## right arrow
rightArrow = Polygon(324, 330,   341, 313,   374, 313,   374, 347,   341, 347,   fill = None, border = "white")
# ok lets check there first
# its pobably on step
buttons = Group(upArrow, leftArrow, downArrow, rightArrow)


## Creates a group to store the static actual game shapes
StaticGameShapes = Group(TehtrisseRect, NextPieceRect, TimePlayed, buttons, visible = False)




## Creates the vertical lines on the screen
VerticalLines = []
for x in range(9):
    VerticalLine = Line(70 + (x * 20), 0, 70 + (x * 20), 0 - (x * 14), fill = "white", visible = False)
    VerticalLine.lineNum = x
    VerticalLine.done = False
    VerticalLines.append(VerticalLine)


## Creates the horizontal lines on the screen
HorizontalLines = []
for x in range(19):
    HorizontalLine = Line(50, 20 + (x * 20), 50 - (x * 10), 20 + (x * 20), fill = "white", visible = False)
    HorizontalLine.lineNum = x
    HorizontalLine.done = False
    HorizontalLines.append(HorizontalLine)


##### actual game stuff










##### opening sequence && main menu stuff


## Tehtrisse logo
TehtrisseLogo = Label("teHtRiSSe", 200, 80, size = 60, font = "cinzel", bold = True, fill = "white", opacity = 0)
TehtrisseLogo.fade = True
TehtrisseLogo.toFront()


## BirdFace logo
BirdFaceLogo = Group(Label("by", 200, 155, size = 30, font = "cinzel", bold = True, fill = "white", opacity = 0),   Label("BiRdfACe", 200, 190, size = 40, font = "cinzel", bold = True, fill = "white", opacity = 0))


## Play button
playButton = Group(Rect(50, 135, 270, 50, fill = None),   Label("play", 110, 160, size = 40, font = "cinzel", bold = True, fill = "white"))


## Help button
helpButton = Group(Rect(50, 185, 270, 50, fill = None),   Label("h", 73, 210, size = 40, font = "cinzel", bold = True, fill = "white"),   Label("elp", 127, 210, size = 40, font = "cinzel", bold = True, fill = "white"))


## Settings button
settingsButton = Group(Rect(50, 235, 270, 50, fill = None),   Label("settings", 161, 260, size = 40, font = "cinzel",  bold = True, fill = "white"))


## Credits button
creditsButton = Group(Rect(50, 285, 270, 50, fill = None),   Label("credits", 148, 310, size = 40, font = "cinzel", bold = True, fill = "white"))


## Menu options group to make stuff visible or not visible easier
menuOptionsGroup = Group(playButton, helpButton, settingsButton, creditsButton, visible = False)


##### opening sequence and main menu stuff










##### all menus have these


## menu option highlighter
menuOptionHighlighter = Rect(50, 135, 270, 50, fill = None, border = "white", borderWidth = 3)


## back button
backButton = Group(Rect(50, 285, 270, 50, fill = None),   Label("back", 115, 310, size = 40, font = "cinzel", bold = True, fill = "white"))


universalMenuGroup = Group(menuOptionHighlighter, backButton, visible = False)


##### all menus have these










##### settings menu


## settings menu
settingsMenu = Label("Settings", 200, 80, size = 60, font = "cinzel", bold = True, fill = "white")


## difficulty menu button
difficultyMenu = Group(Rect(50, 135, 270, 50, fill = None),   Label("difficulty", 183, 160, size = 40, font = "cinzel", bold = True, fill = "white"))


## keybinds menu button
keybindsMenu = Group(Rect(50, 185, 270, 50, fill = None),   Label("keybinds", 164, 210, size = 40, font = "cinzel", bold = True, fill = "white"))


## color menu button
colorMenu = Group(Rect(50, 235, 270, 50, fill = None),   Label("colors", 145, 260, size = 40, font = "cinzel",  bold = True, fill = "white"))


## Menu options group to make stuff visible or not visible easier
settingsMenuOptionsGroup = Group(settingsMenu, difficultyMenu, keybindsMenu, colorMenu, visible = False)




app.playButtonKeybinds = ["p", "P"]
app.enterButtonKeybinds = ["enter", "e", "E"]
app.backButtonKeybinds = ["backspace", "escape", "b", "B"]
app.pauseButtonKeybinds = ["tab", "escape", "p", "P"]
app.importExportKeybinds = ["i", "I"]
upArrow.keybinds = ["up", "w", "W"]
leftArrow.keybinds = ["left", "a", "A"]
downArrow.keybinds = ["down", "s", "S"]
rightArrow.keybinds = ["right", "d", "D"]


##### settings menu










##### variables that need to be tracked


app.background = "black"
app.stepsPerSecond = 20




app.timeStarted = False
app.startTime = None




app.timeTracker = 0
app.shownLogo = False
app.menu = False
app.helpMenu = False


app.settingsMenu = False
app.settingsDifficultyMenu = False
app.settingsKeybindsMenu = False
app.settingsColorMenu = False


app.credits = False
app.nextBlockShown = False
app.shownLineAnimation = False
app.playingGame = False




app.score=Label(0,325,200,fill='white',size=  (75) /len(str(0)),   opacity=0   )
##### variables that need to be tracked










##### game state variables


app.blockSpeed = 25
app.nextBlock = None
app.currentBlock = None


##### game state variables










##### helper functions
def playScreen():
    app.playingGame = True
    app.menu = False
    TehtrisseLogo.visible = False
    menuOptionsGroup.visible = False
    universalMenuGroup.visible = False
    menuOptionHighlighter.visible = False
    settingsMenuOptionsGroup.visible = False
    StaticGameShapes.opacity = 0
    StaticGameShapes.visible = True
    TehtrisseRect.opacity = 100
def menuScreen():
    app.shownLogo = True
    app.helpMenu = False
    app.settingsMenu = False
    app.credits = False
    app.menu = True
    app.timeTracker = 0
    TehtrisseLogo.visible = True
    BirdFaceLogo.visible = False
    menuOptionHighlighter.top = playButton.top
    menuOptionsGroup.visible = True
    universalMenuGroup.visible = False
    menuOptionHighlighter.visible = True
    settingsMenuOptionsGroup.visible = False
    StaticGameShapes.visible = False
    showPlayScreen("end")
    buttons.visible = False
def helpScreen():
    app.shownLogo = True
    app.helpMenu = True
    app.settingsMenu = False
    app.credits = False
    app.menu = False
    app.timeTracker = 0
    TehtrisseLogo.visible = False
    BirdFaceLogo.visible = False
    menuOptionHighlighter.top = playButton.top
    menuOptionsGroup.visible = False
    universalMenuGroup.visible = True
    settingsMenuOptionsGroup.visible = False
    StaticGameShapes.visible = False
    showPlayScreen("end")
    buttons.visible = False
def settingsScreen():
    app.shownLogo = True
    app.helpMenu = False
    app.settingsMenu = True
    app.credits = False
    app.menu = False
    app.timeTracker = 0
    TehtrisseLogo.visible = False
    BirdFaceLogo.visible = False
    menuOptionHighlighter.top = difficultyMenu.top
    menuOptionsGroup.visible = False
    universalMenuGroup.visible = True
    settingsMenuOptionsGroup.visible = True
    StaticGameShapes.visible = False
    showPlayScreen("end")
    buttons.visible = False
def creditsScreen():
    app.shownLogo = True
    app.helpMenu = False
    app.settingsMenu = False
    app.credits = True
    app.menu = False
    app.timeTracker = 0
    TehtrisseLogo.visible = False
    BirdFaceLogo.visible = False
    menuOptionHighlighter.top = playButton.top
    menuOptionsGroup.visible = False
    universalMenuGroup.visible = False
    settingsMenuOptionsGroup.visible = False
    StaticGameShapes.visible = False
    showPlayScreen("end")
    buttons.visible = False
def showPlayScreen(lineCounter):
    for StaticShape in StaticGameShapes:
        if StaticShape.opacity < 100:
            StaticShape.opacity += 1.25
    if lineCounter == "end":
        for line in VerticalLines:
            line.y2 = 0 - (line.lineNum * 14)
            line.visible = False
        for line in HorizontalLines:
            line.x2 = 50 - (line.lineNum * 10)
            line.visible = False
    else:
        for line in VerticalLines:
            if not line.done:
                line.y2 += 7
                if line.y2 > 0:
                    line.visible = True
                    if line.y2 > 400:
                        line.y2 = 400
                        line.done = True
        for line in HorizontalLines:
            if not line.done:
                line.x2 += 5
                if line.x2 > 50:
                    line.visible = True
                    if line.x2 > 250:
                        line.x2 = 250
                        line.done = True
        vAmountDone = 0
        vDone = False
        for line in VerticalLines:
            if line.done:
                vAmountDone += 1
        if vAmountDone == len(VerticalLines):
            vDone = True
        hAmountDone = 0
        hDone = False
        for line in HorizontalLines:
            if line.done:
                hAmountDone += 1
        if hAmountDone == len(HorizontalLines):
            hDone = True
        if vDone and hDone and not app.nextBlockShown:
            app.nextBlock = makeBlock(325, 70)
            app.nextBlockShown = True
def menuMoveUp():
    if menuOptionHighlighter.top == 135:
        menuOptionHighlighter.top = 285
    elif menuOptionHighlighter.top == 185:
        menuOptionHighlighter.top = 135
    elif menuOptionHighlighter.top == 235:
        menuOptionHighlighter.top = 185
    elif menuOptionHighlighter.top == 285:
        menuOptionHighlighter.top = 235
def menuMoveDown():
    if menuOptionHighlighter.top == 135:
        menuOptionHighlighter.top = 185
    elif menuOptionHighlighter.top == 185:
        menuOptionHighlighter.top = 235
    elif menuOptionHighlighter.top == 235:
        menuOptionHighlighter.top = 285
    elif menuOptionHighlighter.top == 285:
        menuOptionHighlighter.top = 135
##### helper functions










##### event functions (things like onMouseMove or onKeyPress)


def onStep():
    if not app.shownLogo:
        
        if TehtrisseLogo.opacity < 100 and TehtrisseLogo.fade:
            TehtrisseLogo.opacity += 2.5
            BirdFaceLogo.opacity += 2.5
            
            if TehtrisseLogo.opacity == 100:
                TehtrisseLogo.fade = False
        
        elif not TehtrisseLogo.fade:
            app.timeTracker += 1
            
            if app.timeTracker > 40:
                BirdFaceLogo.opacity -= 2.5
                
                if BirdFaceLogo.opacity == 0:
                    menuScreen()
    
    elif app.menu:
        pass
    
    elif app.helpMenu:
        pass
    
    elif app.settingsMenu:
        pass
    
    elif app.credits:
        pass
        
    elif not app.menu and not app.shownLineAnimation:
        showPlayScreen(app.timeTracker)
        app.timeTracker += 1
        if app.timeTracker == 97:
            app.timeTracker = 0
            app.shownLineAnimation = True
            app.playingGame = True
            app.timeStarted = True
            app.startTime = 5
            newBlock()
    
    elif app.playingGame:
        
        if app.timeStarted:
            pass
        app.timeTracker += 1
        if app.timeTracker % app.blockSpeed == 0:
            if app.currentBlock.bottom < 400:
                app.currentBlock.centerY += 20
                if app.currentBlock.hitsShape(renderedSquares):
                    app.currentBlock.centerY-= 20
                    for sh in app.currentBlock:
                        squares.append(sh.left)
                        squares.append(sh.top)
                        squares.append(sh.fill)
                    renderSquares()
                    app.currentBlock.visible=False
                    newBlock()
                    
            elif app.currentBlock.bottom == 400:
                
                for sh in app.currentBlock:
                    squares.append(sh.left)
                    squares.append(sh.top)
                    squares.append(sh.fill)
                renderSquares()
                app.currentBlock.visible=False
                newBlock()










def onMousePress(x, y):
    
    if app.menu:
        
        if playButton.contains(x, y):
            playScreen()
        elif helpButton.contains(x, y):
            helpScreen()
        elif settingsButton.contains(x, y):
            settingsScreen()
        elif creditsButton.contains(x, y):
            creditsScreen()
    
    
    elif app.settingsMenu:
        
        if difficultyMenu.contains(x, y):
            pass
        elif keybindsMenu.contains(x, y):
            pass
        elif colorMenu.contains(x, y):
            pass
        elif backButton.contains(x, y):
            menuScreen()
    
    elif app.playingGame:
        
        for button in buttons:
            if button.contains(x, y):
                onKeyPress(button.keybinds[0])
                onKeyHold([button.keybinds[0]])










def onMouseRelease(x, y):
    
    if app.playingGame:
        
        for button in buttons:
            if button.fill == "white":
                button.fill = None










def onMouseMove(x, y):
    
    if app.menu or app.settingsMenu:
        
        if playButton.contains(x, y):
            menuOptionHighlighter.top = 135
        
        elif helpButton.contains(x, y):
            menuOptionHighlighter.top = 185
            
        elif settingsButton.contains(x, y):
            menuOptionHighlighter.top = 235
        
        elif creditsButton.contains(x, y):
            menuOptionHighlighter.top = 285










def onMouseDrag(x, y):
    
    if app.playingGame:
        for button in buttons:
            
            if button.contains(x, y) and button.fill == None:
                onKeyPress(button.keybinds[0])
                onKeyHold([button.keybinds[0]])
            
            elif not button.contains(x, y):
                onKeyRelease(button.keybinds[0])










def onKeyPress(key):
    
    if app.menu:
        
        if key in app.playButtonKeybinds:
            playScreen()
        
        elif key in app.enterButtonKeybinds:
            if menuOptionHighlighter.top == playButton.top:
                playScreen()
            elif menuOptionHighlighter.top == helpButton.top:
                helpScreen()
            elif menuOptionHighlighter.top == settingsButton.top:
                settingsScreen()
            elif menuOptionHighlighter.top == creditsButton.top:
                creditsScreen()
    
    
    elif app.settingsMenu:
        if key in app.enterButtonKeybinds:
            
            if menuOptionHighlighter.top == 135:
                pass
            
            elif menuOptionHighlighter.top == 185:
                pass
            
            elif menuOptionHighlighter.top == 235:
                pass
            
            elif menuOptionHighlighter.top == 285:
                if app.settingsDifficultyMenu:
                    app.settingsDifficultyMenu = False
                elif app.settingsKeybindsMenu:
                    app.settingsKeybindsMenu = False
                elif app.settingsColorMenu:
                    app.settingsColorMenu = False
                else:
                    menuScreen()
        
        if key in app.backButtonKeybinds:
            
            if app.settingsDifficultyMenu:
                app.settingsDifficultyMenu = False
            elif app.settingsKeybindsMenu:
                app.settingsKeybindsMenu = False
            elif app.settingsColorMenu:
                app.settingsColorMenu = False
            else:
                menuScreen()
        
    
    
    if app.menu or app.helpMenu or app.settingsMenu or app.credits:
        
        if key in upArrow.keybinds or key in leftArrow.keybinds:
            menuMoveUp()
        elif key in downArrow.keybinds or key in rightArrow.keybinds:
            menuMoveDown()
    
    
    elif app.playingGame:
        
        if key in upArrow.keybinds:
            pass
        elif key in leftArrow.keybinds:
            pass
        elif key in downArrow.keybinds:
            pass
        elif key in rightArrow.keybinds:
            pass
        if "tab" in key:
            makeSave()
        elif 'escape'in key:
            zWtri(app.getTextInput(),False)
        
    if app.playingGame:
        if not app.currentBlock == None:
            if key in upArrow.keybinds:
                for block in app.currentBlock:
                    
                    if 'top' in str(block.border):
                        block.border=gradient('white','gray','gray','grey','gray','gray','grey',rgb(70,70,70),start='left')
                    elif 'left' in str(block.border):
                        block.border=gradient('white','gray','gray','grey','gray','gray','grey',rgb(70,70,70),start='bottom')
                    elif 'right' in str(block.border):
                        block.border=gradient('white','gray','gray','grey','gray','gray','grey',rgb(70,70,70),start='top')
                    elif 'bottom' in str(block.border):
                        block.border=gradient('white','gray','gray','grey','gray','gray','grey',rgb(70,70,70),start='right')
                xval,yval=app.currentBlock.centerX,app.currentBlock.centerY
                app.currentBlock.rotateAngle += 90
                app.currentBlock.top=rounded(app.currentBlock.top/20)*20
                if app.currentBlock.width==40 or app.currentBlock.width==80:
                    app.currentBlock.left=rounded(app.currentBlock.left/20)*20-10
                else:
                    app.currentBlock.left=rounded(app.currentBlock.left/20)*20+10
                if app.currentBlock.right>250:
                    app.currentBlock.right=250
                elif app.currentBlock.left<50:
                    app.currentBlock.left=50
                elif app.currentBlock.top<0:
                    app.currentBlock.top=0
                elif app.currentBlock.bottom>400:
                    app.currentBlock.bottom=400
                if app.currentBlock.hitsShape(renderedSquares):
                    app.currentBlock.rotateAngle-=90
                    app.currentBlock.centerX,app.currentBlock.centerY=xval,yval
            
            elif key in leftArrow.keybinds and app.currentBlock.left > 50:
                app.currentBlock.centerX -= 20
                
                if app.currentBlock.hitsShape(renderedSquares):
                    app.currentBlock.centerX+= 20
                    
            elif key in downArrow.keybinds:
                if not app.currentBlock.bottom == 400:
                    app.currentBlock.centerY += 20
                    if app.currentBlock.hitsShape(renderedSquares):
                        
                        app.currentBlock.centerY-= 20
                        for sh in app.currentBlock:
                            squares.append(sh.left)
                            squares.append(sh.top)
                            squares.append(sh.fill)
                        renderSquares()
                        app.currentBlock.visible=False
                        newBlock()
                    app.timeTracker = 0
                    if app.currentBlock.bottom == 400 :
                        
                        for sh in app.currentBlock:
                            squares.append(sh.left)
                            squares.append(sh.top)
                            squares.append(sh.fill)
                        renderSquares()
                        app.currentBlock.visible=False
                        
                        newBlock()
            
            elif key in rightArrow.keybinds and app.currentBlock.right < 250:
                app.currentBlock.centerX += 20
                if app.currentBlock.hitsShape(renderedSquares):
                    app.currentBlock.centerX-= 20










def onKeyHold(keys):
    
    if app.playingGame:
    
        for key in keys:
            if key in upArrow.keybinds:
                upArrow.fill = "white"
            if key in leftArrow.keybinds:
                leftArrow.fill = "white"
            if key in downArrow.keybinds:
                downArrow.fill = "white"
            if key in rightArrow.keybinds:
                rightArrow.fill = "white"










def onKeyRelease(key):
    
    if app.playingGame:
        if key in upArrow.keybinds:
            upArrow.fill = None
        if key in leftArrow.keybinds:
            leftArrow.fill = None
        if key in downArrow.keybinds:
            downArrow.fill = None
        if key in rightArrow.keybinds:
            rightArrow.fill = None


##### event functions (things like onMouseMove or onKeyPress)












def makeBlock(cx,cy):
    block=randrange(7)
    #block=0
    bord=gradient('white','gray','gray','grey','gray','gray','grey',rgb(70,70,70),start='top')
    if block==0:
        a=Rect(200,200,20,20,fill='yellow',border= bord)
        b=Rect(220,200,20,20,fill='yellow',border= bord)
        c=Rect(200,220,20,20,fill='yellow',border=bord)
        d=Rect(220,220,20,20,fill='yellow',border=bord)
        shape=Group(a,b,c,d)
    elif block==1:
        a=Rect(200,200,20,20,fill='cyan',border=bord)
        b=Rect(200,220,20,20,fill='cyan',border=bord)
        c=Rect(200,240,20,20,fill='cyan',border=bord)
        d=Rect(200,260,20,20,fill='cyan',border=bord)
        shape=Group(a,b,c,d)
    elif block==2:
        a=Rect(200,200,20,20,fill='red',border=bord)
        b=Rect(220,200,20,20,fill='red',border=bord)
        c=Rect(220,220,20,20,fill='red',border=bord)
        d=Rect(240,220,20,20,fill='red',border=bord)
        shape=Group(a,b,c,d)
    elif block==3:
        a=Rect(200,220,20,20,fill='lime',border=bord)
        b=Rect(220,220,20,20,fill='lime',border=bord)
        c=Rect(220,200,20,20,fill='lime',border=bord)
        d=Rect(240,200,20,20,fill='lime',border=bord)
        shape=Group(a,b,c,d)
    elif block==4:
        a=Rect(200,220,20,20,fill='darkviolet',border=bord)
        b=Rect(220,220,20,20,fill='darkviolet',border=bord)
        c=Rect(240,220,20,20,fill='darkviolet',border=bord)
        d=Rect(220,200,20,20,fill='darkviolet',border=bord)
        shape=Group(a,b,c,d)
    elif block==5:
        a=Rect(200,220,20,20,fill='blue',border=bord)
        b=Rect(220,220,20,20,fill='blue',border=bord)
        c=Rect(240,220,20,20,fill='blue',border=bord)
        d=Rect(200,200,20,20,fill='blue',border=bord)
        shape=Group(a,b,c,d)
    elif block==6:
        a=Rect(200,220,20,20,fill='orange',border=bord)
        b=Rect(220,220,20,20,fill='orange',border=bord)
        c=Rect(240,220,20,20,fill='orange',border=bord)
        d=Rect(240,200,20,20,fill='orange',border=bord)
        shape=Group(a,b,c,d)
    shape.centerX,shape.centerY=cx,cy
    shape.toFront()
    return shape
    






def newBlock():
    if app.playingGame:
        app.currentBlock = app.nextBlock
        app.currentBlock.left = 110
        app.currentBlock.top = 0
        if app.currentBlock.width == 20:
            app.currentBlock.centerX += 40
        elif app.currentBlock == 40:
            app.currentBlock.centerX += 20
        if app.currentBlock.hitsShape(renderedSquares):
            
            if score<200:
                Label("u very bad at game",200,200,size=58,fill='red',bold=True,border='white')
            elif score<800:
                Label("u bad at game",200,200,size=58,fill='red',bold=True,border='white')
            elif score<2000:
                Label("u okay at game",200,200,size=58,fill='red',bold=True,border='white')
            elif score<5000:
                Label("u decent at game",200,200,size=58,fill='red',bold=True,border='white')
            elif score<10000:
                Label("u good at game",200,200,size=58,fill='red',bold=True,border='white')
            elif score>50000:
                Label("u excellent at game",200,200,size=58,fill='red',bold=True,border='white')
            app.stop()


    app.nextBlock = makeBlock(250+75,70)
    
squares=[]
renderedSquares=Group()






def renderSquares():
    #renderedSquares.clear()
    for x in range(int(len(squares)/3)):
        left=squares[x*3]
        top=squares[x*3+1]
        color=squares[x*3+2]
        renderedSquares.add(Rect(float(left)+0.25,float(top)+0.25,19.5,19.5,fill=color,border=gradient('white','gray','gray','grey','gray','gray','grey',rgb(70,70,70),start='top')))
    squares.clear()
    check()    
bar=Rect(0,385,400,10,fill='white',visible=False)




scoreDic={
    0:0,
    1:40,
    2:100,
    3:300,
    4:1200,
}
def check():
    #'''
    bar.top=5
    linesRemoved=0
    for i in range(23):
        count=0
        for block in renderedSquares:
            if block.hitsShape(bar):
                count+=1
                if count==10:
                    #print('hit 10')
                    linesRemoved+=1
                    for block in renderedSquares:
                        if block.hitsShape(bar):
                            block.visible=False
                            renderedSquares.remove(block)
                        elif block.centerY<bar.centerY:
                            block.centerY+=20
                    bar.centerY-=20
        bar.centerY+=20
    app.score.value+=scoreDic[linesRemoved]
    if app.score.value>0:
        app.score.opacity=100
    app.score.size=  (100) /(len(str(app.score.value))/2)
    app.linesCleared=int(linesRemoved)
    app.blockSpeed=256//((app.linesCleared/2)+10)


app.convert={
    0            : 'A',
    20           : 'B',
    40           : 'C',
    60           : 'D',
    80           : 'E',
    100          : 'F',
    120          : 'G',
    140          : 'H',
    160          : 'I',
    180          : 'J',
    200          : 'K',
    220          : 'L',
    240          : 'M',
    260          : 'N',
    280          : 'O',
    300          : 'P',
    320          : 'Q',
    340          : 'R',
    360          : 'S',
    380          : 'T',
    325          : 'U',
    50           : 'a',
    70           : 'b',
    90           : 'c',
    110          : 'd',
    130          : 'e',
    150          : 'f',
    170          : 'g',
    190          : 'h',
    210          : 'i',
    230          : 'j',
    250          : 'k',
    'yellow'     : '0',
    'cyan'       : '1',
    'red'        : '2',
    'lime'       : '3',
    'darkviolet' : '4',
    'blue'       : '5',
    'orange'     : '6',
    
  
    
    
}


app.numToWords={
    0:'v',
    1:'m',
    2:'n',
    3:'o',
    4:'p',
    5:'q',
    6:'r',
    7:'s',
    8:'t',
    9:'u',
}


app.wordsToNum={
    'v':'0',
    'm':'1',
    'n':'2',
    'o':'3',
    'p':'4',
    'q':'5',
    'r':'6',
    's':'7',
    't':'8',
    'u':'9',
}


def getter(thing):
    for item, value in app.convert.items():
    
        if item == thing:
            return value
        elif value == thing:
            return item


def makeSave():
    name=[]
    for block in renderedSquares:
        left=(block.left-0.25)
        left=getter(left)
        name.append(left)
        
        top=(block.top-0.25)
        top=getter(top)
        name.append(top)
        
        color=str(block.fill)
        color=getter(color)
        name.append(color)
        
        
    name.append('7')
    name.append(getter(app.currentBlock.left))
    name.append(getter(app.currentBlock.top))
    name.append(getter(app.currentBlock.fill))
    name.append(getter(app.currentBlock.rotateAngle))
    name.append(getter(app.nextBlock.centerX))
    name.append(getter(app.nextBlock.centerY))
    name.append(getter(app.nextBlock.fill))
    name.append(getter(0))
    name.append('l')
    for item in str(app.score.value):
        name.append(app.numToWords[int(item)])
    name.append('w')
    for item in str(app.linesCleared):
        name.append(app.numToWords[int(item)])
    #app.getTextInput(name)
    #print(name)
    zWtri(name,True)
    


def importSave(value):
    #import value
    score=''
    lines=''
    nacb=[]
    renderedSquares.clear()
    next=False
    next2=False
    next3=False
    for item in value:
        if item in 'ABCDEFGHIJKLMNOPQRSTUabcdefghijk0123456' and not next:
            squares.append(getter(item))
        elif next and item in 'ABCDEFGHIJKLMNOPQRSTUabcdefghijk0123456lmnopqrstuvw':
            if next2:
                if item=='w':
                    next3=True
                elif not next3:
                    score+=app.wordsToNum[item]
                elif next3:
                    lines+=app.wordsToNum[item]
            if item=="l":
                next2=True
            elif not next2:
                nacb.append(getter(item))
            
        if item=="7":
            next=True
    #### set app.linesCleared
    app.linesCleared=lines
    app.blockSpeed=256//((int(app.linesCleared)/2)+10)
            
    #print(value)
    #print(squares,nacb)
    renderSquares()
    makeBigBlocks(nacb)
    #print(score)
    app.score.value=int(score)
    if app.score.value>0:
        app.score.opacity=100
    app.score.size=  (100) /(len(str(app.score.value))/2)
def makeBigBlocks(val):
    #app.currentBlock=None
    #app.nextBlock=None
    
    
    if not app.currentBlock ==None:
        app.currentBlock.fill=None
        for x in app.currentBlock:
            x.border=None
    if not app.nextBlock ==None:
        app.nextBlock.fill=None
        for x in app.nextBlock:
            x.border=None
    
    
    
    
    for x in range(2):
        left=val[x*4]
        top=val[x*4+1]
        block=val[x*4+2]
        rotate=val[x*4+3]
    # left=val[0:1]
    # top=val[1:2]
    # color=val[2:3]
        shape=Group()
        bord=gradient('white','grey','grey','grey','grey','grey','grey',rgb(70,70,70),start='top')
        if block=='yellow':
            a=Rect(200,200,20,20,fill='yellow',border= bord)
            b=Rect(220,200,20,20,fill='yellow',border= bord)
            c=Rect(200,220,20,20,fill='yellow',border=bord)
            d=Rect(220,220,20,20,fill='yellow',border=bord)
            shape.add(a,b,c,d)
        elif block=='cyan':
            a=Rect(200,200,20,20,fill='cyan',border=bord)
            b=Rect(200,220,20,20,fill='cyan',border=bord)
            c=Rect(200,240,20,20,fill='cyan',border=bord)
            d=Rect(200,260,20,20,fill='cyan',border=bord)
            shape.add(a,b,c,d)
        elif block=='red':
            a=Rect(200,200,20,20,fill='red',border=bord)
            b=Rect(220,200,20,20,fill='red',border=bord)
            c=Rect(220,220,20,20,fill='red',border=bord)
            d=Rect(240,220,20,20,fill='red',border=bord)
            shape.add(a,b,c,d)
        elif block=='lime':
            a=Rect(200,220,20,20,fill='lime',border=bord)
            b=Rect(220,220,20,20,fill='lime',border=bord)
            c=Rect(220,200,20,20,fill='lime',border=bord)
            d=Rect(240,200,20,20,fill='lime',border=bord)
            shape.add(a,b,c,d)
        elif block=='darkviolet':
            a=Rect(200,220,20,20,fill='darkviolet',border=bord)
            b=Rect(220,220,20,20,fill='darkviolet',border=bord)
            c=Rect(240,220,20,20,fill='darkviolet',border=bord)
            d=Rect(220,200,20,20,fill='darkviolet',border=bord)
            shape.add(a,b,c,d)
        elif block=='blue':
            a=Rect(200,220,20,20,fill='blue',border=bord)
            b=Rect(220,220,20,20,fill='blue',border=bord)
            c=Rect(240,220,20,20,fill='blue',border=bord)
            d=Rect(200,200,20,20,fill='blue',border=bord)
            shape.add(a,b,c,d)
        elif block=='orange':
            a=Rect(200,220,20,20,fill='orange',border=bord)
            b=Rect(220,220,20,20,fill='orange',border=bord)
            c=Rect(240,220,20,20,fill='orange',border=bord)
            d=Rect(240,200,20,20,fill='orange',border=bord)
            shape.add(a,b,c,d)
        shape.rotateAngle=rotate
        
        shape.toFront()
        
        if x==0:
            shape.left,shape.top=left,top
            app.currentBlock=shape
        else:
            shape.centerX,shape.centerY=left,top
            app.nextBlock=shape


renderSquares()






c0 = "​"
c1 = "­"
c2 = "﻿"
noWidth = c0 + c1 + c2
dictionary = {
    "0" : (c0+c0+c0+c0+c0), #00000
    "1" : (c0+c0+c0+c0+c1), #00001
    "2" : (c0+c0+c0+c0+c2), #00002
    "3" : (c0+c0+c0+c1+c0), #00010
    "4" : (c0+c0+c0+c1+c1), #00011
    "5" : (c0+c0+c0+c1+c2), #00012
    "6" : (c0+c0+c0+c2+c0), #00020
    "7" : (c0+c0+c0+c2+c1), #00021
    "8" : (c0+c0+c0+c2+c2), #00022
    "9" : (c0+c0+c1+c0+c0), #00100
    "0" : (c0+c0+c1+c0+c1), #00101
    "A" : (c0+c0+c1+c0+c2), #00102
    "B" : c0+c0+c1+c1+c0, #00110
    "C" : c0+c0+c1+c1+c1, #00111
    "D" : c0+c0+c1+c1+c2, #00112
    "E" : c0+c0+c1+c2+c0, #00120
    "F" : c0+c0+c1+c2+c1, #00121
    "G" : c0+c0+c1+c2+c2, #00122
    "H" : c0+c0+c2+c0+c0, #00200
    "I" : c0+c0+c2+c0+c1, #00201
    "J" : c0+c0+c2+c0+c2, #00202
    "K" : c0+c0+c2+c1+c0, #00210
    "L" : c0+c0+c2+c1+c1, #00211
    "M" : c0+c0+c2+c1+c2, #00212
    "N" : c0+c0+c2+c2+c0, #00220
    "O" : c0+c0+c2+c2+c1, #00221
    "P" : c0+c0+c2+c2+c2, #00222
    "Q" : c0+c1+c0+c0+c0, #01000
    "R" : c0+c1+c0+c0+c1, #01001
    "S" : c0+c1+c0+c0+c2, #01002
    "T" : c0+c1+c0+c1+c0, #01010
    "U" : c0+c1+c0+c1+c1, #01011
    "a" : c0+c1+c0+c1+c2, #01012
    "b" : c0+c1+c0+c2+c0, #01020
    "c" : c0+c1+c0+c2+c1, #01021
    "d" : c0+c1+c0+c2+c2, #01022
    "e" : c0+c1+c1+c0+c0, #01100
    "f" : c0+c1+c1+c0+c1, #01101
    "g" : c0+c1+c1+c0+c2, #01102
    "h" : c0+c1+c1+c1+c0, #01110
    "i" : c0+c1+c1+c1+c1, #01111
    "j" : c0+c1+c1+c1+c2, #01112
    "k" : c0+c2+c0+c0+c0, #02000
    "l": c0+c2+c0+c0+c1, #flag
    "m": c0+c2+c0+c0+c2,
    'n': c0+c2+c0+c1+c0,
    'o': c0+c2+c0+c1+c1,
    'p': c0+c2+c0+c1+c2,
    'q': c0+c2+c0+c2+c0,
    'r': c0+c2+c0+c2+c1,
    's': c0+c2+c0+c2+c2,
    't': c0+c2+c1+c0+c0,
    'u': c0+c2+c1+c0+c1,
    'v': c0+c2+c1+c0+c2,
    'w': c0+c2+c1+c1+c0,#flag 2 
                
                
    c0+c0+c0+c0+c0 : "0", #00000
    c0+c0+c0+c0+c1 : "1", #00001
    c0+c0+c0+c0+c2 : "2", #00002
    c0+c0+c0+c1+c0 : "3", #00010
    c0+c0+c0+c1+c1 : "4", #00011
    c0+c0+c0+c1+c2 : "5", #00012
    c0+c0+c0+c2+c0 : "6", #00020
    c0+c0+c0+c2+c1 : "7", #00021
    c0+c0+c0+c2+c2 : "8", #00022
    c0+c0+c1+c0+c0 : "9", #00100
    c0+c0+c1+c0+c1 : "0", #00101
    c0+c0+c1+c0+c2 : "A", #00102
    c0+c0+c1+c1+c0 : "B", #00110
    c0+c0+c1+c1+c1 : "C", #00111
    c0+c0+c1+c1+c2 : "D", #00112
    c0+c0+c1+c2+c0 : "E", #00120
    c0+c0+c1+c2+c1 : "F", #00121
    c0+c0+c1+c2+c2 : "G", #00122
    c0+c0+c2+c0+c0 : "H", #00200
    c0+c0+c2+c0+c1 : "I", #00201
    c0+c0+c2+c0+c2 : "J", #00202
    c0+c0+c2+c1+c0 : "K", #00210
    c0+c0+c2+c1+c1 : "L", #00211
    c0+c0+c2+c1+c2 : "M", #00212
    c0+c0+c2+c2+c0 : "N", #00220
    c0+c0+c2+c2+c1 : "O", #00221
    c0+c0+c2+c2+c2 : "P", #00222
    c0+c1+c0+c0+c0 : "Q", #01000
    c0+c1+c0+c0+c1 : "R", #01001
    c0+c1+c0+c0+c2 : "S", #01002
    c0+c1+c0+c1+c0 : "T", #01010
    c0+c1+c0+c1+c1 : "U", #01011
    c0+c1+c0+c1+c2 : "a", #01012
    c0+c1+c0+c2+c0 : "b", #01020
    c0+c1+c0+c2+c1 : "c", #01021
    c0+c1+c0+c2+c2 : "d", #01022
    c0+c1+c1+c0+c0 : "e", #01100
    c0+c1+c1+c0+c1 : "f", #01101
    c0+c1+c1+c0+c2 : "g", #01102
    c0+c1+c1+c1+c0 : "h", #01110
    c0+c1+c1+c1+c1 : "i", #01111
    c0+c1+c1+c1+c2 : "j", #01112
    c0+c2+c0+c0+c0 : "k", #02000
    c0+c2+c0+c0+c1 : "l", #flag
    c0+c2+c0+c0+c2 : "m",
    c0+c2+c0+c1+c0 : 'm',
    c0+c2+c0+c1+c1 : 'o',
    c0+c2+c0+c1+c2 : 'p',
    c0+c2+c0+c2+c0 : 'q',
    c0+c2+c0+c2+c1 : 'r',
    c0+c2+c0+c2+c2 : 's',
    c0+c2+c1+c0+c0 : 't',
    c0+c2+c1+c0+c1 : 'u',
    c0+c2+c1+c0+c2 : 'v',
    c0+c2+c1+c1+c0 : 'w',#flag2 
}


def zWtri(string, io):
    if io:
        aBet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/?"
        start = ""
        actual = ""
        end = ""
        bLen = random.randrange(4, 8)
        eLen = random.randrange(4, 8)
        while len(start) < bLen:
            start += random.choice(aBet)
        while len(end) < eLen:
            end += random.choice(aBet)
        for char in string:
            for item, value in dictionary.items():
                if char == item:
                    actual += value
                    break
        final = start+actual+end
        app.getTextInput(final)
        return final, len(final)
        
    else:
        
        string2=''
        for letter in string:
            if  letter in noWidth:
                string2+=str(letter)
        final=[]
        for x in range(int(len(string2)/5)):
            
            val=string2[x*5:x*5+5]
            val=dictionary[val]
            final.append(val)
        importSave(final)