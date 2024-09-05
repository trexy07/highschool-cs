import hashlib
import math

from base import *
from newbase import docio
docio.enable()

import browser


# configuration variable, NOT a permanent part of the code
Q__ = 4


globalYOffset=canvas.getBoundingClientRect().top
globalXOffset=canvas.getBoundingClientRect().left


class Menu():
    def __init__ (self):
        # self.drawMainMenu()
        self.drawSplash()
        self.game = None
        self.paused = False
        self.splash=2

    def drawMainMenu (self):
        drawRect(0, 0, 400, 400, fill="dimgray")
        drawLabel("new game", 200, 100, size=80)
        drawLabel("join game", 200, 200, size=80)
        drawLabel("re-join", 200, 300, size=80)
        for y in range(50,350+1,100):
            drawLine(0,y,400,y)
        
    def drawSplash(self):
        drawRect(0, 0, 400, 400, fill='midnightblue')
        drawLabel("splash", 200, 200, size=130, rotateAngle=45)

    def keyPress (self, key):
        if key == 'p':
            self.paused = not self.paused
            if self.paused:
                drawRect(0, 0, 400, 400, fill="hotpink")
                y=0
                drawLabel("Pause Screen\u2122", 200, y:=y+40, size=50)

                drawLabel("Click `new game` to create a new game.", 200, y:=y+50, size=20)

                drawLabel("Click `join game` to join an existing game.", 200, y:=y+40, size=20)

                drawLabel("Click `re-join` to join game you were", 200, y:=y+40, size=20)
                drawLabel("previously in.", 200, y:=y+20, size=20)

                drawLabel("Press `r` while on the pause screen (this", 200, y:=y+40, size=20)
                drawLabel("screen) to be prompted with the option to", 200, y:=y+20, size=20)
                drawLabel("restart the app.", 200, y:=y+20, size=20)

                drawLabel("The game rules can be found at this URL:", 200, y:=y+40, size=20)
                drawLabel("https://trevinspi.freeddns.org/games/rules", 200, y:=y+20, size=20)
                drawLabel("(press o to open the rules in a new tab)", 200, y:=y+20, size=20)
            else:
                if self.game is None:
                    self.drawMainMenu()
                else:
                    self.game.render()
                
        if key == 'r' and self.paused:
            prompt = "Do you really want to restart your game client?"
            if browser.confirm(prompt):
                browser.window.location.reload()
        if key == 'o' and self.paused:
            URL = "https://trevinspi.freeddns.org/games/rules"
            browser.window.open(URL, "_blank")
    
    def mouseDown (self, val):
        if self.paused: return
#         globalYOffset=canvas.getBoundingClientRect().top
#         globalXOffset=canvas.getBoundingClientRect().left
        
        x = math.floor(val.x - globalXOffset)
        y = math.floor(val.y - globalYOffset)
        print((x, y))
        
        if self.game is not None:
            self.game.mouseDown(x, y)
        else:
            # process button pressing
            
            # if 20<x<380:# horozontal checking not needed
                if 50<y<150:
                    print('new game')
                    self.new_game()
                elif 150<y<250:
                    print('join game')
                    self.join_empty()
                elif 250<y<350:
                    print('re-connect')
                    self.rejoin()
            
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
                # user_pswd=''
#         password = "password123".encode()
#         salt = b'salt'
#         hash_object = hashlib.sha256(salt + user_pswd.encode())
#         hex_dig = hash_object.hexdigest()




        ID=make_uno(name,user_name,user_pswd)
#         print(ID)
#         drawLabel(ID,200,200)
        self.game=Game(ID,1,user_pswd)


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
                additive=f"(username already taken; taken names: {user_names})"
                
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

            except Exception as e:
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

            
        
        
        
        
        
class Game():
    def __init__ (self,ID,user_num=1,user_pswd=''):
        
        self.ID=ID
        self.user_num=user_num
        self.user_pswd=user_pswd
        
        self.hand=[]
        self.user_names=[]
        self.user_card_count=[]
        self.card=None
        
        self.top_card='u '
        self.direction=1
        
        self.rate=0
        self.time=0
        self.winner=0
        self.onu=0
        
        self.refresh()
        
        print("game inited")
        
        # 19 Red cards – 0 to 9. (1 zero)
        # 19 Blue cards – 0 to 9.
        # 19 Green cards – 0 to 9.
        # 19 Yellow cards – 0 to 9.
        # 8 Skip cards – two cards of each color.
        # 8 Reverse cards – two cards of each color.
        # 8 Draw cards – two cards of each color.
        # 8 Black cards – 4 wild cards and 4 Wild Draw 4 cards.
#         self.posible_cards=[]
# #         values=[str(i) for range(9+1)]+[str(i) for i in range(1,9+1)]+['s','r','+2']*2
#         for color in 'rgby':
#             for i in [i for i in range(9+1)]+[i for i in range(1,9+1)]:
#                 self.posible_cards.append(color+str(i))
#             for special in ['s','r','+2','s','r','+2']:
#                 self.posible_cards.append(color+special)
#         for i in range(4):
#             self.posible_cards.append("B ")
#             self.posible_cards.append("B+4")
# #         drawLabel(self.posible_cards,200,250)
#         new_str=''
#         for item in self.posible_cards:
#             new_str+=item+','

#         print(new_str)
#         print(self.posible_cards)
        
        
        
        
    def mouseDown(self,mx,my):
        if self.card==None:
            self.refresh()
            
        self.time=0
#         rdm_card=choice(self.posible_cards)
#         # when drawing card replace s with u+21bb↻ or u+21ba↺
#         value=rdm_card[1:]
#         for card in self.hand:
#         self.render()
        if self.winner!=0 or self.player_count==1:
            return
        position=(50,375,1,0,0)
        
        x,y=position[0],position[1] # starting pos
        mod=300/(len(self.hand)) # how much the card position changes

        x+=position[2]*mod/2 # move the card in half a step to center
        y+=position[3]*mod/2
        
        if self.card is not None:
            #if a color was selected then place the card with the new color added
            x=200
            y=200
            c=''
            if x-16<mx<x+16 and  y-44.5-44.5<my<y-44.5:
                c='b'
            elif x-16<mx<x+16 and  y+44.5+44.5>my>y+44.5:
                c='y'
            elif x+32+16<mx<x+64 and  y-22.25<my<y+22.25:
                c='g'
            elif x-32>mx>x-64  and  y-22.25<my<y+22.25:
                c='r'
            else:
                print('no color',mx,my)
#             print(c)
            if c!='':
                place(self.ID,self.user_num,self.card,self.user_pswd,color=c)
            self.refresh()
            self.card=None
        elif 268<mx<268+32 and 177.75<my<177.75+44.5:
#             if self.turn!=self.user_num:
#             for card in self.hand:
#                 if (card[0]=='B' # if the card is wild
#                  or card[0]==self.top_card[0] # if the color matches
#                  or card[1:]==self.top_card[1:] # if the value matches
#                  or (self.top_card[0]=='B' and card[0]==self.top_card[-1]) # if the top card is wild && the color matches
#                 ):
#                     print('bro you still have cards to play' )
#                     return
#                     raise HTTPException(status_code=428, detail="bruh, you have cards you can play")
            print('drawing')
            print(draw(self.ID,self.user_num,self.user_pswd))
            self.refresh()
#             print('end drawing')
            pass
        elif distance(300,300,mx,my)<=30: # onu button
            press=False
        
            onu_bin=bin(self.onu+16)[2:]
    #         print(onu_bin)
            for user in range(4):

                # onu=sonu//(user+1)==1
                count=self.user_card_count[user]
    #             print(user+1,count,onu_bin[user])
    #             print(onu_bin[user] , count)
                if onu_bin[-user-1]=='0' and count==1:
                    press=True
                
            if press or (
                (self.turn==self.user_num and len(self.hand) == 2 # 2 cards your turn
                 or len(self.hand) ==1) # 1 card, any turn
                and onu_bin[-self.user_num] == '0'):# press is needed
                
                print("ONU button")
                onu(self.ID,self.user_num)
                self.refresh()
        else:
            print(' attempt place')
            for j in range(len(self.hand)):

    #             Card(card[0],value,angle=position[i][4]).draw(x-16,y-22.25)#-32/2,-44.5 /2
#                 drawCircle(x,y,5) # helpfull for debuging positions
    #             cx,cy=x-16,y-22.25
    #             print(x,y)
                if x-16<mx<x+16 and  y-22.25<my<y+22.25:
    #                 print(self.hand[j])
                    print('placing')
                    card=self.hand[j]
                    if (self.user_num==self.turn # if it's your turn
                        and (# and the card can be played
                             card[0]=='B' # if the card is wild
                             or card[0]==self.top_card[0] # if the color matches
                             or card[1:]==self.top_card[1:] # if the value matches
                             or (self.top_card[0]=='B' and card[0]==self.top_card[-1]) # if the top card is wild && the color matches
                            )
                       ):
                        if card[0]=='B':
                            
                            # selecting a color if its a wild
                            self.card=card
                            unoRed=rgb(215, 38,0)
                            unoYellow=rgb(236,212,7)
                            unoGreen=rgb(55,151,17)
                            unoBlue=rgb(9,86,191)
                            print('wild color select')
                            
#                             x=y=200
                            x=200-16
                            y=200-22.5
                            drawRect(x, y-66.75, 32, 44.5, fill=unoBlue, 
                                     border='black', borderWidth=1 )
                            drawRect(x, y+66.75, 32, 44.5, fill=unoYellow, 
                                     border='black', borderWidth=1 )
                            drawRect(x-48, y, 32, 44.5, fill=unoRed, 
                                     border='black', borderWidth=1 )
                            drawRect(x+48, y, 32, 44.5, fill=unoGreen, 
                                     border='black', borderWidth=1 )
#                             x=200-19.5-5-16
#                             y=200-29.5-5-22.5
#                             drawRect(x+12, y+47, 32, 44.5, fill=unoGreen, 
#                                      border='black', borderWidth=1 )
#                             drawRect(x+37, y+22, 32, 44.5, fill=unoYellow, 
#                                      border='black', borderWidth=1 )
#                             drawRect(x+19.5, y+29.5, 32,44.5, fill=unoBlue, 
#                                      border='black', borderWidth=1 )
#                             drawRect(x+29.5, y+39.5, 32,44.5, fill=unoRed, 
#                                      border='black', borderWidth=1 )
                        else:
                            print("before place")
                            place(self.ID,self.user_num,card,self.user_pswd)
                            print("before place")
                            self.refresh()
                            print("before place")
                    else:
                        print("id10t error - bruh, you cant play that card",self.top_card,card)
#                         self.refresh()
                    # self.refresh()
                    return None


                x+=position[2]*mod
                y+=position[3]*mod


    def render(self):
        
        # this part should be replaced with shape clear, then add rect
        drawRect(0,0,400,400,fill='dimgray')
        
        
        drawLabel(f"game id: {self.ID}",100,300)
        drawLabel(f"game name: {self.game_name}",100,320)
        
#         drawLine(200,0,200,400) # used to center hands
#         drawLine(0,200,400,200)
        
        # render hands
        hands=[]
        for user_num in range(4):
#             if user_num!=self.user_num-1:
#                 hands.append(["ba " for i in range(self.user_card_count[user_num%4])] )
#             hands.append(self.user_card_count[user_num])
            hands.append(["u " for i in range(self.user_card_count[user_num]) ])
        hands[self.user_num-1]=self.hand
        
        
        # rotate cards
        for i in range(self.user_num+5):
            hands.append(hands.pop(0))
            
        # render cards
        
        position=((50,25,1,0,180),(375,50,0,1,270),(50,375,1,0,0),(25,50,0,1,90))
        
        for i in range(4):
            if len(hands[i])==0:
                continue
            
            x,y=position[i][0],position[i][1] # starting pos
            mod=300/(len(hands[i])) # how much the card position changes
        
            x+=position[i][2]*mod/2 # move the card in half a step to center
            y+=position[i][3]*mod/2
            
            for j in range(len(hands[i])):
                card=hands[i][j]
                if card=='':
                    continue
                value=card[1:]
                if value=='r':
                    if self.direction==0:
                         value='↻'
                    else:
                        value='↺'
                elif value=='s':
                    value='🛇'
                
                opac=50 if (self.user_num==self.turn # if it's your turn
                    and (# and the card can be played
                         card[0]=='B' # if the card is wild
                         or card[0]==self.top_card[0] # if the color matches
                         or card[1:]==self.top_card[1:] # if the value matches
                         or (self.top_card[0]=='B' and card[0]==self.top_card[-1]) # if the top card is wild && the color matches
                        )
                   ) else 100
                
                Card(card[0],value,angle=position[i][4]).draw(x-16,y-22.25)#-32/2,-44.5 /2 # opacity= opac
                #drawCircle(x,y,10) # helpfull for debuging positions
                x+=position[i][2]*mod
                y+=position[i][3]*mod
        
            #drawLine(x,y,position[i][0],position[i][1]) # helped align card lines
            
        # direction label
        if self.direction==1:
             value='↻'
        else:
            value='↺'
        drawLabel(value,200,200,size=100)#=100
        
        # render top card and "draw pile"
#         print(self.top_card)
        value=self.top_card[1:]
        if value=='r':
            if self.direction==1:
                 value='↻'
            else:
                value='↺'
        elif value=='s':
            value='🛇'
            
        Card(self.top_card[0],value).draw(200-16,200-44.5 /2)#-32/2,-44.5 /2
        Card('back','ONU').draw(200-16+64+20,200-44.5 /2)#-32/2,-44.5 /2
        
        # render user_names
        position=((200,60,0),(340,200,270),(200,340,0),(60,200,90))
#         print(self.user_names)
        # rotate to account for player at bottom
#         print(self.user_names)
        target=self.turn
        winner=self.winner
        user_names=[self.user_names[i] for i in range(4)]
#         print('here',user_names)

        for i in range(self.user_num+1):
            user_names.append(user_names.pop(0))
            target-=1
            winner-=1
            
#         print(self.user_names)
        name=None
        for i in range(4):
            if self.winner != 0 and i == (winner - 1) % 4:
                fill = rgb(9, 86, 191)
                name = user_names[i] # set the thingy
            else:
                fill = "black"
            bold = i == (target - 1) % 4
            size = 18 if bold else 16
            drawLabel(user_names[i], *position[i][0:2],
                      rotateAngle=position[i][2], bold=bold, size=size)
        if name is not None:
            drawRect(0, 160, 400, 80, fill='white')
            drawLabel(f"{name} won!", 200, 200, size=20)
        
        
        # ONU button 
        # when onu can't be called, then decrese the opacity/ cover with trasparent gray circle
        
        x,y=300,300
        font='comic sans Ms' if 'unit3'=='unit3' else 'arial'
#         drawCircle(x-4,y+3,45/2,fill=rgb(65, 65, 65),border='black',borderWidth=1)
        drawCircle(x,y,45/2,fill=rgb(215, 38,0),border='black',borderWidth=1)

        drawLabel("ONU",x-2,y+1.5,size=22.5*1.1,
            fill=gradient2('midnightBlue', 'lightCyan', 'midnightBlue', 'midnightBlue', start="top"),
            border=None,borderWidth=.5,
            bold=True,rotateAngle=-20, font=font)

        drawLabel("ONU",x,y,size=22.5*1.1,
            fill=gradient2("gold","gold",'lightgoldenrodyellow',"white",start="top"),
            border="midnightBlue",borderWidth=.5,
            bold=True,rotateAngle=-20, font=font)
        
        press=False
        
        onu_bin=bin(self.onu+16)[2:]
#         print(onu_bin)
        for user in range(4):

            # onu=sonu//(user+1)==1
            count=self.user_card_count[user]
#             print(user+1,count,onu_bin[user])
#             print(onu_bin[user] , count)
            if onu_bin[-user-1]=='0' and count==1:
                press=True
#         print(press,self.turn==self.user_num , len(self.hand)==2 , onu_bin[-self.user_num]) # debug
        if press or (
            (self.turn==self.user_num and len(self.hand) ==2 # 2 cards your turn
             or len(self.hand) ==1) # 1 card, any turn
            and onu_bin[-self.user_num] == '0'): # press is needed
            pass
        else:
            drawCircle(x,y,30,fill='dimgray',opacity=50)
        
        if self.player_count==1:
            drawRect(0,160,400,80,fill='white')
            drawLabel("> 1 player needed for game",200,200,size=20)
            drawLabel("(get some friends)",200,235,size=10)
            
            drawRect(180,45,40,25,fill='dimgray')
        
        
        
    def refresh(self):
        result=public(self.ID)
        
#         drawLabel(str(result),200,300)
        
        if result['age']>0 and result['winner']==0:
            fountain(self.ID)
        
#         self.hand=result["cards"+str(self.user_num)].split(",")
        
        self.direction=2*result['direction']  -1
        
#         self.user_names=result[0:4]
        self.user_names=[]
        for i in range(4):
            self.user_names.append(result["name"+str(i+1)])

#         self.user_names=[]
        self.user_card_count=[]
        for i in range(4):
            self.user_card_count.append(result["len"+str(i+1)]  )
        
        self.top_card=result['top_card']
        self.turn=result['turn']
        self.game_name=result['game_name']
        self.winner=result['winner']
        self.onu=result['onu']
        self.player_count=result['player_count']
        
        self.hand=private(self.ID,self.user_num,self.user_pswd)['cards']
#         print(self.hand)
        self.hand=self.hand.split(',')
        self.hand.remove("")


#         for i in range(4):
# #             self.user_names.append(result["name"+str((self.user_num+i)%4)])
#             self.user_card_count.append(len( result["cards"+str((self.user_num+i)%4)]  ))
        
        
        
        self.render()
    def onStep(self):
        if self.winner!=0:
            return
        self.time+=1
        
        # log method
#         if self.time>1.3**self.rate:
#             self.rate+=1
# #             print(self.time)
            
#             self.time=0
#             if self.card==None:
#                 self.refresh()

        # boring linear method
    
        # manual exponential method
        if (self.time<10 and self.time%2==1) or (10<self.time <61  and self.time%5==1) or (self.time>61 and self.time%10==1) :
            if self.card==None:
                self.refresh()
            
        
#         self.render()
        
        pass
class Card():
    # example Cards
    # Card("b",'+2').draw(0,200)
    # card('black'," ").draw(80,200)
    # card('black',"+4").draw(160,200)
    # card('back'," ").draw(240,200)
    # card("green","5").draw(320,200)

    _black  = rgb(0x00, 0x00, 0x00)
    _red    = rgb(0xd7, 0x26, 0x00)
    _yellow = rgb(0xec, 0xd4, 0x07)
    _green  = rgb(0x37, 0x97, 0x11)
    _blue   = rgb(0x09, 0x56, 0xbf)
    _white  = rgb(0xff, 0xff, 0xff)
    _colors = {
        "u":      _black,
        "back":   _black,
        "B":      _black,
        "black":  _black,
        "r":      _red,
        "red":    _red,
        "y":      _yellow,
        "yellow": _yellow,
        "g":      _green,
        "green":  _green,
        "b":      _blue,
        "blue":   _blue,
    }
    _ovalFills = {
        "u":     _red,
        "back":  _red,
        "B":     _white,
        "black": _white,
    }
    _ovalBorders = {
        "u":     _red,
        "back":  _red,
    }
    _values = {
        
    }


    def __init__(self, color, symbol='-', scale=.5, angle=0):
        #print(color,value)
        self.color = self._colors[color]

        if color == "back":
            self.value = "ONU"
        elif symbol == "-":
            self.value = " "
        else:
            self.value = symbol

        self.ovalFill = self._ovalFills.get(color, self.color)
        self.ovalBorder = self._ovalBorders.get(color, self._white)
        
        self.size=1
        self.scale=scale
        
        if self.value[0] in '+🛇':
            self.size=.8
        if color=='black':
            self.size=1
        
        self.size*=scale
        
        # simpler cards for unit 3
        self.unit3=False
        
        
    def draw(self,x,y):
        if self.unit3:
            
            drawRect(x,y,64*self.scale,89*self.scale,fill= self.color,border="white",borderWidth=6*self.scale)
            
            if self.value!='ONU':
                self.size*=2
            
            drawLabel(self.value,x+32*self.scale,y+44.5*self.scale,size=22.5* self.size,
                fill=gradient2("gold","gold",'lightgoldenrodyellow',"white",start="top"),
                border="black",borderWidth=.5*self.scale,
                bold=True,rotateAngle=-20, font='comic sans Ms')
            
            
            
            return
        ## with base groups, throw all these shape in a group, then apply rotate

        drawRect(x,y,64*self.scale,89*self.scale,fill= self.color,border="white",borderWidth=6*self.scale)

        drawOval(x+32*self.scale,y+44.5*self.scale,45*self.scale,75*self.scale,rotateAngle=30, fill=self.ovalFill, border=self.ovalBorder, borderWidth=4 * self.scale)
        if self.value=='ONU':
            # Label(number,232-4,344.5+1.5,size=20*size,fill='black',bold=True,rotateAngle=-45)

            drawLabel(self.value,x+30*self.scale,y+46*self.scale,size=22.5* self.size,
                fill=gradient2('midnightBlue', 'lightCyan', 'midnightBlue', 'midnightBlue', start="top"),
                border=None,borderWidth=.5*self.scale,
                bold=True,rotateAngle=-20)

            drawLabel(self.value,x+32*self.scale,y+44.5*self.scale,size=22.5* self.size,
                fill=gradient2("gold","gold",'lightgoldenrodyellow',"white",start="top"),
                border="black",borderWidth=.5*self.scale,
                bold=True,rotateAngle=-20)

            #©, 
            #u+00AE above onu on back, black, 3*size
            drawLabel("© BirdFace",x+47.5*self.scale,y+80*self.scale,size=3* self.size,fill='white',bold=True)



        if self.color=='black' and self.value !="ONU":


            drawRect(x+12*self.scale, y+47*self.scale, 15*self.scale,20*self.scale, fill=self.unoGreen, border='black', borderWidth=1*self.scale)
            drawRect(x+37*self.scale, y+22*self.scale, 15*self.scale,20*self.scale, fill=self.unoYellow, border='black', borderWidth=1*self.scale)
            drawRect(x+19.5*self.scale, y+29.5*self.scale,       15*self.scale,20*self.scale, fill=self.unoBlue, border='black', borderWidth=1*self.scale)
            drawRect(x+29.5*self.scale, y+39.5*self.scale,       15*self.scale,20*self.scale, fill=self.unoRed, border='black', borderWidth=1*self.scale)


        if not (self.color=='black' or self.value=='ONU'):

            drawLabel(self.value,x+28*self.scale,y+46*self.scale,size=50* self.size,fill='black',bold=True)
            drawLabel(self.value,x+32*self.scale,y+44.5*self.scale,size=50* self.size, fill='white', border='black', borderWidth=2*self.scale, bold=True)
            
        # elif value[0]=='+':

        if not (self.value=='wild' or self.value=='ONU'):
            drawLabel(self.value, x+15.5*self.scale, y+15.375*self.scale,size=15* self.size,fill='black',bold=True,)
            drawLabel(self.value, x+17*self.scale, y+15*self.scale,size=15* self.size, fill='white', border='black', borderWidth=.5*self.scale, bold=True)

            drawLabel(self.value, x+49.5*self.scale, y+72.125*self.scale, size=15* self.size, fill='black', bold=True, rotateAngle=180)
            drawLabel(self.value, x+47.5*self.scale, y+72.5*self.scale, size=15* self.size, fill='white', border='black', borderWidth=.5*self.scale, bold=True, rotateAngle=180)


        drawRect(x,y,64*self.scale,89*self.scale,fill="transparent",border="white",borderWidth=6*self.scale)

    
    
# init the menu
menu=Menu()


# mouse press event
# def mouseDown(ev):
#     menu.mouseDown(ev)
# document["myCanvas"].bind("mousedown", menu.mouseDown)
canvas.bind("mousedown", menu.mouseDown)

# key press event
def keyPress (event):
    menu.keyPress(event.key)
document.bind("keydown", keyPress)

####### onstep
def onStep():
    menu.onStep()
    
    #required option a or b, dynamic step interval
    # window.setTimeout(handleOnStep, 1000)

# option b, set step iterval
window.setInterval(onStep, 1000)   

