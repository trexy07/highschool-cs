
import browser

# from base import * 
# from base import getTextInput, make_uno, public, private, join, names, rescroll, rgb, drawRect, drawCircle, drawLabel, gradient2
from base import getTextInput, make_uno, public, private, join, names, rescroll, rgb, drawRect, drawCircle, drawLabel, gradient2

from game import Game

# globalYOffset, globalXOffset = canvas.getBoundingClientRect().top, canvas.getBoundingClientRect().left # used for repositioning the mouse location



        
# function resizeCanvas() {
# def size:
# canvas.width = window.innerWidth
# canvas.height = window.innerHeight
# window.addEventListener('resize', size, false);


class Menu():
    def __init__ (self):
        # self.drawMainMenu()
        self.drawSplash()
        self.game = None
        self.paused = False
        self.splash=2



    def drawSplash(self):
        # drawRect(0, 0, 400, 400, fill='midnightblue')
        # drawLabel("splash", 200, 200, size=130, rotateAngle=45)
        
        drawRect(0, 0, 400, 400)
        
        x, y = 200, 200
        font = "comic sans Ms" if "unit4" == "unit3" else "arial"
        scale=6
        #         drawCircle(x-4,y+3,45/2,fill=rgb(65, 65, 65),border='black',borderWidth=1)
        drawCircle(x, y, 45 / 2 * scale, fill=rgb(215, 38, 0), border="black", borderWidth=1  * scale)

        drawLabel(
            "ONU",
            x - 2 * scale,
            y + 1.5 * scale,
            size=22.5 * 1.1 * scale,
            fill=gradient2(
                "midnightBlue", "lightCyan", "midnightBlue", "midnightBlue", start="top"
            ),
            border=None,
            borderWidth=0.5 * scale,
            bold=True,
            rotateAngle=-20,
            font=font,
        )

        drawLabel(
            "ONU",
            x,
            y,
            size=22.5 * 1.1 * scale,
            fill=gradient2(
                "gold", "gold", "lightgoldenrodyellow", "white", start="top"
            ),
            border="midnightBlue",
            borderWidth=0.5 * scale,
            bold=True,
            rotateAngle=-20,
            font=font,
        )
        # Call the function to load and draw the image
        # drawSvdbf("svdbf.png",10,10,500,300)

    
    def drawMainMenu (self):
        browser.document.body.style.backgroundColor = "black"

        # color defs
        _red    = rgb(0xd7, 0x26, 0x00)
        _yellow = rgb(0xec, 0xd4, 0x07)
        _green  = rgb(0x37, 0x97, 0x11)
        _blue   = rgb(0x09, 0x56, 0xbf)
        
        drawRect(0, 0, 400, 400, fill="black") # og dimgray
        # drawRect(0, 0, 4000, 4000, fill="white") # 4 scale testing

        drawLabel("new game", 200, 50, size=80, fill=_red)
        drawLabel("join game", 200, 150, size=80, fill=_green)
        drawLabel("re-join", 200, 250, size=80, fill=_blue)
        drawLabel("spectate", 200, 350, size=80, fill=_yellow)
        # for y in range(0,350+1,100):
        #     drawLine(0,y,400,y,fill='white')
    

        
        
    

    def drawPause(self):
                browser.document.body.style.backgroundColor = "rgb(202, 154, 178)"

                drawRect(0, 0, 400, 400, fill=rgb(202, 154, 178)) # origionaly "hotpink"
                y=0
                drawLabel("Pause Screen\u2122", 200, y:=y+40, size=50)

                drawLabel("Click `new game` to create a new game.", 200, y:=y+50, size=20)

                drawLabel("Click `join game` to join an existing game.", 200, y:=y+40, size=20)

                drawLabel("Click `re-join` to join game you were", 200, y:=y+40, size=20)
                drawLabel("previously in.", 200, y:=y+20, size=20)

                drawLabel("Click `spectate` to watch a game", 200, y:=y+40, size=20)

                drawLabel("Press `r` while on the pause screen (this", 200, y:=y+40, size=20)
                drawLabel("screen) to be prompted with the option to", 200, y:=y+20, size=20)
                drawLabel("restart the app.", 200, y:=y+20, size=20)

                drawLabel("The game rules can be found at this URL:", 200, y:=y+40, size=20)
                drawLabel("https://trevinspi.freeddns.org/games/rules", 200, y:=y+20, size=20)
                drawLabel("(press o to open the rules in a new tab)", 200, y:=y+20, size=20)

    
    def keyDown (self, key):
        if key == 'p':
            self.paused = not self.paused
            rescroll()
            if self.paused:
                self.drawPause()
            else:
                if self.game is None:
                    self.drawMainMenu()
                else:
                    browser.document.body.style.backgroundColor = "rgb(53,101,77)"
                    self.game.render()
                
                
        if key == 'r' and self.paused:
            prompt = "Do you really want to restart your game client?"
            if browser.confirm(prompt):
                browser.window.scrollTo(0,0)
                browser.window.location.reload()
        if key == 'o' and self.paused:
            URL = "https://trevinspi.freeddns.org/games/rules"
            browser.window.open(URL, "_blank")
    
    def mouseDown (self, x,y):
        print((x, y))
        if self.paused: return
#         globalYOffset=canvas.getBoundingClientRect().top
#         globalXOffset=canvas.getBoundingClientRect().left
        
#         x = math.floor(val.x - globalXOffset)
#         y = math.floor(val.y - globalYOffset)
        
        if self.game is not None:
            self.game.mouseDown(x, y)
        else:
            # process button pressing
            
            # if 20<x<380:# horozontal checking not needed
                if 00<y<100:
                    print('new game')
                    self.new_game()
                elif 100<y<200:
                    print('join game')
                    self.join_empty()
                elif 200<y<300:
                    print('re-connect')
                    self.rejoin()
                elif 300<y<400:
                    print('spectate')
                    self.spectate()
            
    def onStep(self):
        if self.paused: return
        if self.game!=None:
        
            self.game.onStep()
        else:
            self.splash-=1
            if self.splash==0:
                self.drawMainMenu()
            

    def sqlScan(self, s):
        # Q4 stuff -- sanitize it better
        if '`' in s or '%' in s or ',' in s:
            return False
        return True

    def new_game(self):
        #while True:
        #get game id
        name_list=names()['names']
        #index_list=names()['index']
        name=None
        #q="whats the new game's name?"
        #while type(name)!=str or len(name)>20:
        additive=''
#         for i in range(3):
        while True:
            print(additive)
            name=getTextInput(f"what's the new game's name? {additive}")#, can't be an int, unique # game_name
#             print(type(name_list))
            if type(name)==str and len(name)<=20 and name not in name_list and not name.isdigit() and self.sqlScan(name): 
                break
            elif type(name)!=str:
                return
            elif len(name)>20:
                additive="(max 20 chars)"
            elif name in name_list:
                additive="(that game name is already chosen, did you mean to join?)"
            elif name.isdigit():
                additive="(name can't be an int)"
            elif not self.sqlScan(name):
                additive='(disalowed chars: "`", "%", ",")'

#         else:
#             return None

#         while type(user_name)!=str or len(name)>20 or len(name)==0:

        user_name=None
#         for i in range(3):
        additive=''
        while True:
            user_name=getTextInput("what's your username? "+additive)
            if type(user_name)==str and len(user_name)<=20 and len(user_name)!=0 and self.sqlScan(user_name):
                break
            elif len(user_name)>20 or len(user_name)==0:
                additive='(max 20, min 1 chars)'
#             elif user_name==""
#             elif user_names in user_names:
            elif type(user_name)!=str:
                return
            elif not self.sqlScan(user_name):
                additive='(disalowed chars: "`", "%", ",")'

        user_pswd=getTextInput("what's your password for you account? (optional)")

        if type(user_pswd)!=str:
            return
        while not self.sqlScan(user_pswd):
            user_pswd=getTextInput('''what's your password for your account? (optional, disalowed chars: "`", "%", ",")''')
            if type(user_pswd)!=str:
                return





        ID=make_uno(name,user_name,user_pswd)
#         print(ID)
#         drawLabel(ID,200,200)
        self.game=Game(ID,0,user_pswd)


    def join_empty(self):
        result=names()
        nameList=result['names']
        indexList=result['index']
        
        while True:
            ID=getTextInput("whats the game's ID or name?") # also game_num
            
            if type(ID) is not str:
                return
            
            while not self.sqlScan(ID):
                ID=getTextInput('''whats the game's ID or name? (disalowed chars: "`", "%", ",")''')
                if type(ID) is not str:
                    return
            try:
                if not ID.isdigit():
                    index=nameList.index(ID)
                    ID=indexList[index]
                
                result=public(ID)
                break

            except Exception as e:
    #             drawLabel("no game found",200,200)
                prompt = "no game found"
                browser.confirm(prompt)
            
                print(e)
                return
        
#         drawLabel(result,200,200)
#         drawLabel(str(result),200,300)
        
        userNames=[]
        for i in range(1,5):
            userNames.append(result["name"+str(i)])

        if "None" not in userNames:
            prompt = "no room in game"
            browser.confirm(prompt)
            return
            
        userName=None
#         for i in range(3):
        additive=''
        while True:
            userName=getTextInput("whats your screen name? "+additive)
            print(ID, type(ID))
            if type(userName)==str and len(userName)<=20 and len(userName)!=0 and self.sqlScan(userName):
                break
            elif len(userName)>20 or len(userName)==0:
                additive='(max 20, min 1 chars)'
                
            elif userName in userNames:
                additive=f"(username already taken; taken names: {userNames})"
                
            elif type(userName)!=str:
                return
            
            elif not self.sqlScan(userName):
                additive='(disalowed chars: "`", "%", ",")'
                
    
        userPswd=getTextInput("whats your password for you account? (optional)")

        if type(userPswd)!=str:
            return
        while not self.sqlScan(userPswd):
            userPswd=getTextInput('''what's your password for your account? (optional, disalowed chars: "`", "%", ",")''')
            if type(userPswd)!=str:
                return
                # userPswd=''
        
#         if "None" in userNames:
        userNum=join(ID,userName,userPswd)
#         print(userNum)
        self.game=Game(ID,userNum,userPswd)
#         else:
#             drawLabel("no space in game!, would you like to spectate?",200,200)


    def rejoin(self):
        additive=''
        ID=None
#         while self.game==None:
        result=None
        # while True
#             for i in range(3):
        result=names()
        name_list=result['names']
        index_list=result['index']
            
            
            
        while True:
            ID=getTextInput("whats the game's ID or name?")# also game_num
#             try:
            while not self.sqlScan(ID):
                ID=getTextInput('''whats the game's ID or name? (disalowed chars: "`", "%", ",")''')
                if type(ID)!=str:
                    return
            if type(ID)!=str:
                return
            try:
                if not ID.isdigit():
                    index=name_list.index(ID)
                    ID=index_list[index]
                
            
                result=public(ID)
                break

            except Exception :
    #             drawLabel("no game found",200,200)
                prompt = "no game found"
                browser.confirm(prompt)
            
                return

        user_names=[]
        for i in range(4):
            user_names.append(result["name"+str(i+1)])
#             user_names=result[0:4]

        user_name=None
#         for i in range(3):
        while True:
            user_name=getTextInput("what's your username?"+str(user_names))
            
            if user_name in user_names :
                user_num=user_names.index(user_name)+1
                break
            elif type(user_name)!=str:
                return


#             print2(user_num)

        additive2=''
#             for i in range(3):
        while True:
            pswd=getTextInput("what's your password?"+additive2)

            if type(pswd)!=str:
                return
            
            # input validation
            while not self.sqlScan(pswd):
                pswd=getTextInput('''whats your password for your account? (optional, disalowed chars: "`", "%", ",")''')
                if type(pswd)!=str:
                    return
                    # user_pswd=''
            try:
                private(ID,user_num,pswd)
                break
            except:
                prompt = "password wrong"
                browser.confirm(prompt)
            additive=additive2=" (try again)"


        self.game=Game(ID,user_num,user_pswd=pswd)



    def spectate(self):
        
        ID=None
        result=names()
        name_list=result['names']
        index_list=result['index']

        while True:
            ID=getTextInput("whats the game's ID or name?")# also game_num
#             try:
            while not self.sqlScan(ID):
                ID=getTextInput('''whats the game's ID or name? (disalowed chars: "`", "%", ",")''')
                if type(ID)!=str:
                    return
            if type(ID)!=str:
                return
            try:
                if not ID.isdigit():
                    index=name_list.index(ID)
                    ID=index_list[index]
            
                result=public(ID)
                break

            except Exception :
    #             drawLabel("no game found",200,200)
                prompt = "no game found"
                browser.confirm(prompt)
            
                return
        self.game=Game(ID,spectate=True)
