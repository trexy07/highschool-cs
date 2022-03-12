app.health = 10
app.ammo = 100
app.bulletsShot = 0
app.kills = 0
app.Kills = 0
app.distanceMoved = 0
app.gun = 'RPG'
app.currentgun = (app.gun)
app.reload = 0
app.gunspeed = 15
app.time = 0
app.seconds = 0
app.minutes = 0
app.timePlayed = '00:00'
app.PlayerSpriteX = 200
app.PlayerSpriteY = 200
app.background = gradient ('black', 'black', 'forestgreen', start='top-left')
app.TitleScreen = 1
app.setMaxShapeCount (3000)
app.stepsPerSecond = 10
app.gamePaused = False
app.Restart = False
app.settings = False
app.secret = False
app.c = False
app.zR = True 
app.l = False
app.L = 'Score'
app.kY = True
app.p = False
app.xF = True
app.found = 0
TitleScreenBackground1 = Rect (0, 0, 400, 400, fill=gradient ('black', 'black', 'forestgreen', start='left-top'))
TitleScreenLabel1 = Label ('Labyrinth of the Undead', 198, 145, size=28, rotateAngle=-14, fill='white', font='monospace', bold=True, italic=True, visible=False)
TitleScreenLabel2 = Label ('click to start', 275, 330, size=25, rotateAngle=-20, font='monospace', fill='white', visible=False)
IntroductionLabel1 = Label ("created by:", 275, 100, rotateAngle=20, size=20, font='monospace', fill='white', visible=False, opacity=0)
IntroductionLabel2 = Label ('BirdFace Studios', 200, 200, rotateAngle=-5, size=35, font='monospace', fill='white', visible=False, opacity=0)
IntroductionLabel3 = Label ('Made with Python', 200, 140, size=30, font='monospace', fill='white', visible=False, opacity=0)
IntroductionLabel4 = Label ('And the CMU graphics module', 200, 170, size=20, font='monospace', fill='white', visible=False, opacity=0)
IntroductionLogo1 = Image ('https://www.freeiconspng.com/uploads/bird-silhouette-sitting-bird-png-22.png', 150, 250, visible=False, opacity=0)
IntroductionLogo1.width //= 8
IntroductionLogo1.height //= 8
IntroductionLogo2 = Image ('https://cdn.freebiesupply.com/logos/large/2x/python-5-logo-png-transparent.png', 133.5, 230, visible=False, opacity=0)
IntroductionLogo2.width //= 18
IntroductionLogo2.height //= 18
SkipButton1= Label ('skip', 45, 30, font='monospace', fill='white', size=20, rotateAngle=-15, visible=False)
SkipButtonClickDetector1 = Rect (0, 0, 80, 60, visible=False)
PlayerSprite = Group (Oval (200, 200, 30, 17, fill=rgb(50, 50, 50)), Circle (200, 200, 5, fill='lemonchiffon'), visible=False)
Gun = Group(Rect(200,200,10,20,fill='grey',border='black',align='left-bottom'),Rect(200,200,10,20,fill=None,align='right-top',), visible=False)
ZombieGroup = Group()
BulletGroup = Group()
AmmoGroup = Group ()
Light = Polygon(200, 200, 130, 70, 155, 35, 200, 20, 245, 35, 270, 70, 230, 172, 225, 185, 229, 194, 230, 205, 227, 217, 
    220, 225, 211, 229, 200, 231, 189, 229, 180, 225, 173, 217, 170, 205, 171, 194, 175, 185,
    170, 172, 130, 70, 200, 200, 800, 800, 800, -400, -400, -400, -400, 800, 800, 800,
    opacity=98, visible=False, fill=rgb(20,20,20))
mazewalls=Group()
xAngle = Label(200,200,200,visible=False)
yAngle = Label(0,200,200,visible=False)
HealthCounter = Label (app.health, 50, 22, size=13, fill='grey', font='monospace', visible=False)
HealthCounterSprite = Group (Oval (30, 22, 10, 6, fill='red', rotateAngle=-45), Oval (25, 22, 10, 6, fill='red', rotateAngle=45), visible=False)
AmmoCounter = Label (100, 110, 22, size=13, fill='white', font='monospace', visible=False)
AmmoCounterSprite = Rect (85, 15, 7, 14, fill='yellow', border='black', visible=False)
nx,ny=0,0
LoseScreen = Label (0, 200, 200, visible=False)
LoseScreenBackground1 = Rect (0, 0, 400, 400, fill=gradient('black', 'black', 'forestgreen', start='left-top'), visible=False)
LoseScreenLabel1YouLose = Label ('You Lose!', 200, 140, size=30, fill='white', font='monospace', bold=True, visible=False)
LoseScreenLabel2PlayAgain = Label ('Play Again?', 300, 330, size=25, fill='white', font='monospace', bold=True, italic=True, rotateAngle=-25, visible=False)
LoseScreenPlayAgainClickDetector1 = Rect (200, 270, 200, 130, visible=False)
LoseScreenLabel3Stats = Label ('Stats:', 200, 180, size=20, fill='white', font='monospace', visible=False)
LoseScreenLabel4Score = Label ('Score:', 130, 210, size=13, align='left', fill='white', font='monospace', visible=False)
LoseScreenLabel5Kills = Label ('Kills:', 130, 220, size=13, align='left', fill='white', font='monospace', visible=False)
LoseScreenLabel6ShotsFired = Label ('Shots Fired:', 130, 230, size=13, align='left', fill='white', font='monospace', visible=False)
LoseScreenLabel7Accuracy = Label ('Accuracy:', 130, 240, size=13, align='left', fill='white', font='monospace', visible=False)
LoseScreenLabel8DistanceMoved = Label (' Distance Moved: ', 130, 250, size=13, align='left', fill='white', font='monospace', visible=False)
LoseScreenLabel9KillsPerShot = Label ('Kills Per Shot: ', 130, 260, size=13, align='left', fill='white', font='monospace', visible=False)
LoseScreenLabel10TimePlayed = Label ('Time Played: ', 130, 270, size=13, align='left', fill='white', font='monospace', visible=False)
PauseScreenOverlay1 = Rect (0, 0, 400, 400, fill=rgb(10, 10, 10), opacity=35, visible=False)
PauseScreenLabel1Paused = Label ('Paused', 165, 100, size=45, fill='white', font='monospace', rotateAngle=-6, visible=False)
PauseScreenLabel2Restart = Label ('Restart', 125, 145, size=20, fill='white', font='monospace', visible=False)
PauseScreenClickDetector1 = Rect (75, 135, 100, 20, visible=False)
PauseScreenLabel3Settings = Label ('Settings', 125, 165, size=20, fill='white', font='monospace', visible=False)
PauseScreenClickDetector2 = Rect (75, 155, 100, 20, visible=False)
Found = Label ('nothing', 160, 20, fill='white', font='monospace', size=18, visible=False)
StCdDvs = Label (100, 200, 420, fill='ghostwhite', font='monospace', size=44, rotateAngle=-10, visible=False)
StCdDv1 = Label (100, 90, 500, fill='ghostwhite', font='monospace', size=25, visible=False)
StCdDv2 = Label (100, 290, 500, fill='ghostwhite', font='monospace', size=25, visible=False)
StLbTy1 = Label (100, 30, 45, fill='ghostwhite', font='monospace', size=15, visible=False)
StLbTy2 = Label (100, 30, 60, fill='ghostwhite', font='monospace', size=15, visible=False)
StLbTy3 = Label (100, 30, 75, fill='ghostwhite', font='monospace', size=15, visible=False)
StLbTy4 = Label (100, 30, 90, fill='ghostwhite', font='monospace', size=15, visible=False)
StLbTy5 = Label (100, 30, 105, fill='ghostwhite', font='monospace', size=15, visible=False)
StLbTy6 = Label (100, 30, 120, fill='ghostwhite', font='monospace', size=15, visible=False)
StLbHl1 = Rect (26, 38, 136, 16, fill=None, border='ghostwhite', borderWidth=2, visible=False)
StLbPlr = Label (100, 45, 155, fill='ghostwhite', font='monospace', size=20, visible=False)
StLbAmt = Label (100, 215, 155, fill='ghostwhite', font='monospace', size=20, visible=False)
StLbNm1 = Label ('1: ', 35, 185, fill='ghostwhite', font='monospace', size=20, visible=False)
StLbNm2 = Label ('2: ', 35, 215, fill='ghostwhite', font='monospace', size=20, visible=False)
StLbNm3 = Label ('3: ', 35, 245, fill='ghostwhite', font='monospace', size=20, visible=False)
StLbNm4 = Label ('4: ', 35, 275, fill='ghostwhite', font='monospace', size=20, visible=False)
StLbNm5 = Label ('5: ', 35, 305, fill='ghostwhite', font='monospace', size=20, visible=False)
def onStep ():
    Found.value='Easter Eggs found: '+str(app.found)+'/5'
    Found.left=150
    if app.found>0:
        Found.visible=True
    else:
        Found.visible=False
    if app.secret==False:
        if app.Restart==False:
            if app.gamePaused==False:
                PauseScreenOverlay1.visible=False
                PauseScreenLabel1Paused.visible=False
                PauseScreenLabel2Restart.visible=False
                PauseScreenLabel3Settings.visible=False
                if app.TitleScreen==0 and LoseScreen.value==0:
                    app.time+=1
                    app.seconds+=0.1
                    if app.seconds>=60:
                        app.seconds-=60
                        app.minutes+=1
                    if len(str(int(app.seconds)))==1:
                        app.timePlayed='0'+str(app.minutes)+':0'+str(int(app.seconds))
                    else:
                        app.timePlayed='0'+str(app.minutes)+':'+str(int(app.seconds))
                    AmmoCounter.value=rounded(app.ammo)
                    HealthCounter.value=rounded(app.health)
                    app.background = rgb(30, 30, 30)
                    TitleScreenBackground1.visible=False
                    TitleScreenLabel1.visible=False
                    TitleScreenLabel2.visible=False
                    IntroductionLabel1.visible=False
                    IntroductionLabel1.opacity=0
                    IntroductionLabel2.visible=False
                    IntroductionLabel2.opacity=0
                    IntroductionLabel3.visible=False
                    IntroductionLabel3.opacity=0
                    IntroductionLabel4.visible=False
                    IntroductionLabel4.opacity=0
                    IntroductionLogo1.visible=False
                    IntroductionLogo1.opacity=0
                    IntroductionLogo2.visible=False
                    IntroductionLogo2.opacity=0
                    SkipButton1.visible=False
                    PlayerSprite.visible=True
                    Gun.visible=True
                    Light.visible=True
                    mazewalls.visible=True
                    AmmoCounter.visible=True
                    AmmoCounterSprite.visible=True
                    HealthCounter.visible=True
                    HealthCounterSprite.visible=True
                    LoseScreenBackground1.visible=False
                    LoseScreenLabel1YouLose.visible=False
                    LoseScreenLabel2PlayAgain.visible=False
                    LoseScreenLabel3Stats.visible=False
                    LoseScreenLabel4Score.visible=False
                    LoseScreenLabel5Kills.visible=False
                    LoseScreenLabel6ShotsFired.visible=False
                    LoseScreenLabel7Accuracy.visible=False
                    LoseScreenLabel8DistanceMoved.visible=False
                    LoseScreenLabel9KillsPerShot.visible=False
                    LoseScreenLabel10TimePlayed.visible=False
                    HealthCounter.value=rounded(app.health)
                    if HealthCounter.value!=0 and LoseScreen.value==0:
                        if app.Kills>=1:
                            app.kills+=1
                            app.Kills-=1
                        for Ammo in AmmoGroup:
                            if Ammo.hitsShape (PlayerSprite):
                                AmmoGroup.remove (Ammo)
                                app.ammo += randrange (3,10)
                                AmmoCounter.value = app.ammo
                        for bullet in BulletGroup:
                            if (app.currentgun=='SMG' or app.currentgun=='RPG') and (not bullet.fill==gradient('red','orange')):
                                app.gunspeed=10
                            if not app.currentgun=='Sword':
                                if bullet.fill==gradient ('red','orange'):
                                    app.gunspeed=0
                            if app.currentgun=='Pistol':
                                app.gunspeed=20
                            if not app.currentgun=='Sword':
                                if bullet.fill=='lemonchiffon':
                                    app.gunspeed=0
                            if app.currentgun=='Sword':
                                app.gunspeed=-15
                                PlayerSprite.toFront()
                                Gun.toFront()
                            if app.currentgun=='Sniper':
                                app.gunspeed=15
                                bulletGoalX,bulletGoalY=getPointInDir(bullet.centerX,bullet.centerY,bullet.rotateAngle,app.gunspeed)
                                bullet.centerX=bulletGoalX
                                bullet.centerY=bulletGoalY
                            if app.currentgun =='Shotgun':
                                app.gunspeed=15
                            if app.currentgun=='AR':
                                app.gunspeed=20
                            if bullet.fill=='blue':
                                app.gunspeed=30
                            if not app.currentgun =='Sword':
                                if (bullet.centerX>400 or bullet.centerX<0 or bullet.centerY>400 or bullet.centerY<0 or (bullet.hitsShape (mazewalls)) and not bullet.fill==gradient('red','orange')):
                                    if (not app.currentgun=='Sniper' and not bullet.fill=='blue') and bullet.hitsShape (mazewalls):
                                        bullet.visible=False
                                        BulletGroup.remove(bullet)
                                    elif app.currentgun=='Sniper':
                                        bulletGoalX,bulletGoalY=getPointInDir(bullet.centerX,bullet.centerY,bullet.rotateAngle,app.gunspeed)
                                        bullet.centerX=bulletGoalX
                                        bullet.centerY=bulletGoalY
                            if not (app.currentgun=='Sword'):
                                if bullet.fill=='lemonchiffon' and distance(bullet.centerX, bullet.centerY, PlayerSprite.centerX, PlayerSprite.centerY)>=4:
                                    bullet.visible=False
                                    BulletGroup.remove(bullet)
                            elif app.currentgun=='SMG' and distance(bullet.centerX, bullet.centerY, PlayerSprite.centerX, PlayerSprite.centerY)>=100:
                                bullet.visible=False
                                BulletGroup.remove(bullet)
                            elif app.currentgun=='Shotgun' and distance(bullet.centerX, bullet.centerY, PlayerSprite.centerX, PlayerSprite.centerY)>=150:
                                bullet.visible=False
                                BulletGroup.remove(bullet)
                            elif (app.currentgun=='Sword' and distance(bullet.centerX, bullet.centerY, PlayerSprite.centerX, PlayerSprite.centerY)>=4):
                                bullet.visible=False
                                BulletGroup.remove(bullet)
                            for zombie in ZombieGroup:
                                if (bullet.hitsShape (zombie)):
                                    zombie.visible=False
                                    ZombieGroup.remove(zombie) 
                                    if( not app.currentgun =='Sword'):
                                        if not bullet.fill==gradient('red','orange') and not app.currentgun=='Sniper':
                                            bullet.visible=False 
                                            BulletGroup.remove(bullet)
                                    if app.currentgun=='Shotgun':
                                        app.Kills+=0.2
                                    else:
                                        app.kills+=1
                                    Ammo = Group (Rect (zombie.centerX-5, zombie.centerY, 5, 10, fill='yellow', border='black', borderWidth=1.5), 
                                        Rect (zombie.centerX, zombie.centerY, 5, 10, fill='yellow', border='black', borderWidth=1.5), 
                                        Rect (zombie.centerX+5, zombie.centerY, 5, 10, fill='yellow', border='black', borderWidth=1.5))
                                    AmmoGroup.add (Ammo)
                            if not app.currentgun=='Sword':
                                if bullet.fill=='blue':
                                    bullet.rotateAngle=angleTo(bullet.centerX,bullet.centerY,xAngle.value,yAngle.value)
                            bulletGoalX,bulletGoalY=getPointInDir(bullet.centerX,bullet.centerY,bullet.rotateAngle,app.gunspeed)
                            bullet.centerX=bulletGoalX
                            bullet.centerY=bulletGoalY
                            if not app.currentgun =='Sword':
                                if bullet.fill=='dimgray':
                                    for Line in mazewalls:
                                        if bullet.hitsShape(Line):
                                            bullet.visible==False
                                            Line.visible=False
                                            BulletGroup.remove(bullet)
                                            mazewalls.remove(Line)
                            if (not app.currentgun=='Sword'):
                                if (bullet.centerX>400 or bullet.centerX<0 or bullet.centerY>400 or bullet.centerY<0) and not bullet.fill==gradient('red','orange'):
                                    bullet.visible=False 
                                    BulletGroup.remove(bullet)
                                    if (app.currentgun=='RPG'):
                                        rpge(bullet.centerX,bullet.centerY)
                            if( not app.currentgun =='Sword'):
                                if bullet.hitsShape(mazewalls) and not app.currentgun=='Sniper'and not bullet.fill==gradient('red','orange') and not bullet.fill=='blue' :
                                    bullet.visible=False
                                    BulletGroup.remove(bullet)
                                    if (app.currentgun=='RPG'):
                                        rpge(bullet.centerX,bullet.centerY)
                            
                        for zombie in ZombieGroup:
                            if distance(zombie.centerX,zombie.centerY,app.PlayerSpriteX,app.PlayerSpriteY)<=100:
                                if( not zombie.hitsShape (mazewalls)):
                                    zombie.rotateAngle = angleTo(zombie.centerX,zombie.centerY,app.PlayerSpriteX,app.PlayerSpriteY,)
                                    zombieGoalX,zombieGoalY=getPointInDir(zombie.centerX,zombie.centerY,zombie.rotateAngle,2)
                                    zombie.centerX=zombieGoalX
                                    zombie.centerY=zombieGoalY
                                elif (app.time % 15 == 0):
                                    randomNumber=randrange(1,5)
                                    if randomNumber==1:
                                        zombie.centerY-=5
                                    if randomNumber==2:
                                        zombie.centerY+=5
                                    if randomNumber==3:
                                        zombie.centerX+=5
                                    if randomNumber==4:
                                        zombie.centerX-=5
                            else:
                                randomNumber=randrange(0,5)
                                if randomNumber==1:
                                    zombie.centerY-=5
                                    if zombie.hitsShape (mazewalls) or zombie.centerY<0:
                                        zombie.centerY+=5
                                if randomNumber==2:
                                    zombie.centerY+=5
                                    if zombie.hitsShape (mazewalls) or zombie.centerY>400:
                                        zombie.centerY-=5
                                if randomNumber==3:
                                    zombie.centerX+=5
                                    if zombie.hitsShape (mazewalls) or zombie.centerX>400:
                                        zombie.centerX-=5
                                if randomNumber==4:
                                    zombie.centerX-=5
                                    if zombie.hitsShape (mazewalls) or zombie.centerX<0:
                                        zombie.centerX+=5
                            for bullet in BulletGroup:
                                if bullet.hitsShape (zombie):
                                    zombie.visible=False
                                    ZombieGroup.remove(zombie) 
                                    if app.currentgun=='RPG':
                                        rpge(bullet.centerX,bullet.centerY)
                                    if not app.currentgun=='Sword':
                                        if not app.currentgun=='Sniper' and not bullet.fill==gradient('red','orange') and not bullet.fill=='blue':
                                            bullet.visible=False 
                                            BulletGroup.remove(bullet)
                                    app.kills+=1
                                    Ammo = Group (Rect (zombie.centerX-5, zombie.centerY, 5, 10, fill='yellow', border='black', borderWidth=1.5), 
                                        Rect (zombie.centerX, zombie.centerY, 5, 10, fill='yellow', border='black', borderWidth=1.5), 
                                        Rect (zombie.centerX+5, zombie.centerY, 5, 10, fill='yellow', border='black', borderWidth=1.5))
                                    AmmoGroup.add (Ammo)
                                if not app.currentgun =='Sword':
                                    if bullet.fill==gradient('red','orange') and app.reload+30<=app.time:
                                        bullet.visible=False
                                        BulletGroup.remove(bullet)
                                    if bullet.fill=='blue' and app.reload+110<=app.time:
                                        bullet.visible=False
                                        BulletGroup.remove(bullet)
                            if(zombie.hitsShape (PlayerSprite)):
                                app.health-=1/5
                        if rounded(20-(app.time/500))!=0:
                            if app.time%abs(rounded(20-(app.time/500)))==0:   
                                zombie=Group (Oval (200, 200, 30, 17, fill=rgb(40, 40, 40)), Circle (200, 200, 5, fill='darkgreen'), visible=False)
                                zombie.centerX=(randrange (0,nx))*(400/nx)-(400/ny/2)
                                zombie.centerY=(randrange (0,ny))*(400/ny)-(400/ny/2)
                                zombie.rotateAngle = angleTo(zombie.centerX,zombie.centerY,app.PlayerSpriteX,app.PlayerSpriteY,)
                                if distance (PlayerSprite.centerX, PlayerSprite.centerY, zombie.centerX, zombie.centerY)>=20 and zombie.hitsShape (Light):
                                    zombie.visible=True
                                    ZombieGroup.add(zombie)
                        else:
                            if app.time%1==0:   
                                zombie=Group (Oval (200, 200, 30, 17, fill=rgb(40, 40, 40)), Circle (200, 200, 5, fill='darkgreen'), visible=False)
                                zombie.centerX=randrange (0, 400)
                                zombie.centerY=randrange (0, 400)
                                zombie.rotateAngle = angleTo(zombie.centerX,zombie.centerY,app.PlayerSpriteX,app.PlayerSpriteY,)
                                if distance (PlayerSprite.centerX, PlayerSprite.centerY, zombie.centerX, zombie.centerY)>=20 and zombie.hitsShape (Light):
                                    zombie.visible=True
                                    ZombieGroup.add(zombie)
                    else:
                        LoseScreen.value=1
                if LoseScreen.value==1:
                    TitleScreenBackground1.visible=False
                    TitleScreenLabel1.visible=False
                    TitleScreenLabel2.visible=False
                    IntroductionLabel1.visible=False
                    IntroductionLabel2.visible=False
                    IntroductionLabel3.visible=False
                    IntroductionLabel4.visible=False
                    IntroductionLogo1.visible=False
                    IntroductionLogo2.visible=False
                    SkipButton1.visible=False
                    PlayerSprite.visible=False
                    Gun.visible=False
                    ZombieGroup.visible=False
                    BulletGroup.visible=False
                    AmmoGroup.visible=False
                    Light.visible=False
                    mazewalls.visible=False
                    HealthCounter.visible=False
                    HealthCounterSprite.visible=False
                    AmmoCounter.visible=False
                    AmmoCounterSprite.visible=False
                    LoseScreenBackground1.visible=True
                    LoseScreenLabel1YouLose.visible=True
                    LoseScreenLabel2PlayAgain.visible=True
                    if LoseScreenLabel2PlayAgain.size<32:
                        LoseScreenLabel2PlayAgain.size+=1.5
                    else:
                        LoseScreenLabel2PlayAgain.size=25
                    LoseScreenLabel3Stats.visible=True
                    LoseScreenLabel4Score.visible=True
                    LoseScreenLabel4Score.value=('Score:          '+(str((app.kills*150)+(app.ammo*2)+(app.time//5))))
                    LoseScreenLabel4Score.left=130
                    LoseScreenLabel5Kills.visible=True
                    LoseScreenLabel5Kills.value=('Kills:          '+(str(app.kills)))
                    LoseScreenLabel5Kills.left=130
                    LoseScreenLabel6ShotsFired.visible=True
                    LoseScreenLabel6ShotsFired.value=('Shots Fired:    '+(str(app.bulletsShot)))
                    LoseScreenLabel6ShotsFired.left=130
                    LoseScreenLabel7Accuracy.visible=True
                    if app.kills==0:
                        LoseScreenLabel7Accuracy.value= ('Accuracy:       0.00')
                    elif app.kills>=app.bulletsShot:
                        LoseScreenLabel7Accuracy.value= ('Accuracy:       100.00')
                    else:
                        LoseScreenLabel7Accuracy.value=('Accuracy:       '+(str(int(rounded(app.kills/app.bulletsShot*10000))/100))+'%')
                    LoseScreenLabel7Accuracy.left=130
                    LoseScreenLabel8DistanceMoved.visible=True
                    LoseScreenLabel8DistanceMoved.value=('Distance Moved: '+(str(app.distanceMoved)))
                    LoseScreenLabel8DistanceMoved.left=130
                    LoseScreenLabel9KillsPerShot.visible=True
                    
                    if app.kills==0 or app.bulletsShot==0:
                        LoseScreenLabel9KillsPerShot.value=('Kills Per Shot: '+str(0))
                    else:
                        LoseScreenLabel9KillsPerShot.value=('Kills Per Shot: '+(str((rounded((app.kills/app.bulletsShot)*1000))/1000)))
                    if app.bulletsShot==0:
                        LoseScreenLabel9KillsPerShot.value=('Kills Per Shot: '+(str((rounded((app.kills/1)*1000))/1000)))
                    LoseScreenLabel9KillsPerShot.left=130
                    LoseScreenLabel10TimePlayed.value=('Time Played:    '+app.timePlayed)
                    LoseScreenLabel10TimePlayed.left=130
                    LoseScreenLabel10TimePlayed.visible=True
                if app.TitleScreen==1 and LoseScreen.value==0:
                    app.background=gradient('black', 'black', 'forestgreen', start='top-left')
                    TitleScreenLabel1.visible=True
                    TitleScreenLabel2.visible=True
                    if TitleScreenLabel2.size<=30:
                        TitleScreenLabel2.size+=1
                    elif TitleScreenLabel2.size>30:
                        TitleScreenLabel2.size=25
                    LoseScreenBackground1.visible=False
                    LoseScreenLabel1YouLose.visible=False
                    LoseScreenLabel2PlayAgain.visible=False
                    LoseScreenLabel3Stats.visible=False
                    LoseScreenLabel4Score.visible=False
                    LoseScreenLabel5Kills.visible=False
                    LoseScreenLabel6ShotsFired.visible=False
                    LoseScreenLabel7Accuracy.visible=False
                    LoseScreenLabel8DistanceMoved.visible=False
                    LoseScreenLabel9KillsPerShot.visible=False
                    LoseScreenLabel10TimePlayed.visible=False
                if app.TitleScreen==2 and LoseScreen.value==0:
                    SkipButton1.visible=True
                    TitleScreenLabel1.visible=False
                    TitleScreenLabel2.visible=False
                    TitleScreenBackground1.visible=True
                    IntroductionLabel1.visible=True
                    if IntroductionLabel1.opacity<100:
                        IntroductionLabel1.opacity+=10
                    IntroductionLabel2.visible=True
                    if IntroductionLabel2.opacity<100:
                        IntroductionLabel2.opacity+=10
                    IntroductionLogo1.visible=True
                    if IntroductionLogo1.opacity<100:
                        IntroductionLogo1.opacity+=2.5
                        if IntroductionLogo1.opacity==100:
                            app.TitleScreen=3
                    LoseScreenBackground1.visible=False
                    LoseScreenLabel1YouLose.visible=False
                    LoseScreenLabel2PlayAgain.visible=False
                    LoseScreenLabel3Stats.visible=False
                    LoseScreenLabel4Score.visible=False
                    LoseScreenLabel5Kills.visible=False
                    LoseScreenLabel6ShotsFired.visible=False
                    LoseScreenLabel7Accuracy.visible=False
                    LoseScreenLabel8DistanceMoved.visible=False
                    LoseScreenLabel9KillsPerShot.visible=False
                    LoseScreenLabel10TimePlayed.visible=False
                if app.TitleScreen==3 and LoseScreen.value==0:
                    IntroductionLabel1.visible=False
                    IntroductionLabel1.opacity=0
                    IntroductionLabel2.visible=False
                    IntroductionLabel2.opacity=0
                    IntroductionLabel3.visible=True
                    if IntroductionLabel3.opacity<100:
                        IntroductionLabel3.opacity+=10
                    IntroductionLabel4.visible=True
                    if IntroductionLabel4.opacity<100:
                        IntroductionLabel4.opacity+=10
                    if IntroductionLogo1.opacity>0:
                        IntroductionLogo1.opacity-=5
                        if IntroductionLogo1.opacity==0:
                            IntroductionLogo1.visible=False
                    IntroductionLogo2.visible=True
                    if IntroductionLogo2.opacity<100:
                        IntroductionLogo2.opacity+=2.5
                        if IntroductionLogo2.opacity==100:
                            app.TitleScreen=4
                if app.TitleScreen==4 and LoseScreen.value==0:
                    IntroductionLabel3.visible=False
                    IntroductionLabel3.opacity=0
                    IntroductionLabel4.visible=False
                    IntroductionLabel4.opacity=0
                    if IntroductionLogo2.opacity>0:
                        IntroductionLogo2.opacity-=4
                        if IntroductionLogo2.opacity==0:
                            IntroductionLogo2.visible=False
                            TitleScreenBackground1.visible=False
                            app.TitleScreen=0
            elif app.gamePaused==True:
                PauseScreenOverlay1.visible=True
                PauseScreenLabel1Paused.visible=True
                if app.settings==False:
                    PauseScreenLabel2Restart.left=80
                    PauseScreenLabel2Restart.visible=True
                    PauseScreenLabel3Settings.left=80
                    PauseScreenLabel3Settings.visible=True
                elif app.settings==True:
                    PauseScreenLabel2Restart.visible=False
                    PauseScreenLabel3Settings.visible=False
        elif app.Restart==True:
            app.bulletsShot=0
            app.TitleScreen=1
            LoseScreen.value=0
            app.health=10
            app.ammo=100
            AmmoCounter.value=(app.ammo)
            app.kills=0
            app.bulletsFired=0
            app.distanceMoved=0
            app.time=0
            app.seconds=0
            app.minutes=0
            app.reload=0
            ZombieGroup.clear (all)
            ZombieGroup.visible=True
            BulletGroup.clear (all)
            BulletGroup.visible=True
            AmmoGroup.clear (all)
            AmmoGroup.visible=True
            app.PlayerSpriteX=200
            app.PlayerSpriteY=200
            PlayerSprite.centerX=200
            PlayerSprite.centerY=200
            Gun.centerX=PlayerSprite.centerX
            Gun.centerY=PlayerSprite.centerY
            Gun.visible=False
            Light.visible=False
            PlayerSprite.visible=False
            mazewalls.visible=False
            HealthCounter.visible=False
            HealthCounterSprite.visible=False
            AmmoCounter.visible=False
            AmmoCounterSprite.visible=False
            PauseScreenOverlay1.visible=False
            PauseScreenLabel1Paused.visible=False
            PauseScreenLabel2Restart.visible=False
            PauseScreenLabel3Settings.visible=False
            app.gamePaused=False
            app.c=False
            StCdDvs.visible=False
            StCdDv1.visible=False
            StCdDv2.visible=False
            app.l=False
            app.L='thing'
            StLbTy1.visible=False
            StLbTy2.visible=False
            StLbTy3.visible=False
            StLbTy4.visible=False
            StLbTy5.visible=False
            StLbTy6.visible=False
            StLbHl1.visible=False
            StLbPlr.visible=False
            StLbAmt.visible=False
            StLbNm1.visible=False
            StLbNm2.visible=False
            StLbNm3.visible=False
            StLbNm4.visible=False
            StLbNm5.visible=False
            app.settings=False
            app.Restart=False
    elif app.secret==True:
        print ('You found a secret!')
        TitleScreenBackground1.visible=False
        TitleScreenLabel1.visible=False
        TitleScreenLabel2.visible=False
        IntroductionLabel1.visible=False
        IntroductionLabel2.visible=False
        IntroductionLabel3.visible=False
        IntroductionLabel4.visible=False
        IntroductionLogo1.visible=False
        IntroductionLogo2.visible=False
        SkipButton1.visible=False
        PlayerSprite.visible=False
        Gun.visible=False
        ZombieGroup.visible=False
        BulletGroup.visible=False
        AmmoGroup.visible=False
        Light.visible=False
        mazewalls.visible=False
        HealthCounter.visible=False
        HealthCounterSprite.visible=False
        AmmoCounter.visible=False
        AmmoCounterSprite.visible=False
        LoseScreenLabel1YouLose.visible=False
        LoseScreenLabel2PlayAgain.visible=False
        LoseScreenLabel3Stats.visible=False
        LoseScreenLabel4Score.visible=False
        LoseScreenLabel5Kills.visible=False
        LoseScreenLabel6ShotsFired.visible=False
        LoseScreenLabel7Accuracy.visible=False
        LoseScreenLabel8DistanceMoved.visible=False
        LoseScreenLabel9KillsPerShot.visible=False
        LoseScreenLabel10TimePlayed.visible=False
        PauseScreenOverlay1.visible=False
        PauseScreenLabel1Paused.visible=False
        PauseScreenLabel2Restart.visible=False
        PauseScreenLabel3Settings.visible=False
        app.background=gradient ('black', 'black', 'forestgreen', start='left-top')
        if app.c==True:
            StCdDvs.value="Developers"
            StCdDvs.visible=True
            if StCdDvs.centerY>-50:
                StCdDvs.centerY-=2
            StCdDv1.value="Max Demar"
            StCdDv1.visible=True
            if StCdDv1.centerY>-50:
                StCdDv1.centerY-=2
            StCdDv2.value="Trevin Carter"
            StCdDv2.visible=True
            if StCdDv2.centerY>-50:
                StCdDv2.centerY-=2
        if app.l==True:
            StLbTy1.value='Score'
            StLbTy1.left=30
            StLbTy1.visible=True
            StLbTy2.value='Kills'
            StLbTy2.left=30
            StLbTy2.visible=True
            StLbTy3.value='Shots Fired'
            StLbTy3.left=30
            StLbTy3.visible=True
            StLbTy4.value='Accuracy'
            StLbTy4.left=30
            StLbTy4.visible=True
            StLbTy5.value='Distance Moved'
            StLbTy5.left=30
            StLbTy5.visible=True
            StLbTy6.value='Time Played'
            StLbTy6.left=30
            StLbTy6.visible=True
            StLbHl1.visible=True
            StLbPlr.value='Player Name'
            StLbPlr.left=45
            StLbPlr.visible=True
            StLbAmt.value=app.L
            StLbAmt.left=210
            StLbAmt.visible=True
            if app.L=='Score':
                StLbNm1.value='1:  Cthulhu     368250'
                StLbNm2.value='2:  Trevin      103478'
                StLbNm3.value='3:  Zayd        46171'
                StLbNm4.value='4:  Ethan       42290'
                StLbNm5.value='5:  Nathan      31061'
            if app.L=='Kills':
                StLbNm1.value='1:  Cthulhu     2294'
                StLbNm2.value='2:  Trevin      667'
                StLbNm3.value='3:  ProGamer    9'
                StLbNm4.value='4:  '
                StLbNm5.value='5:  '
            if app.L=='Shots Fired':
                StLbNm1.value='1:  Cthulhu     2201'
                StLbNm2.value='2:  Trevin      1379'
                StLbNm3.value='3:  ProGamer    109'
                StLbNm4.value='4:  '
                StLbNm5.value='5:  '
            if app.L=='Accuracy':
                StLbNm1.value='1:  Cthulhu     100.00%'
                StLbNm2.value='2:  Trevin      100.00%'
                StLbNm3.value='3:  ProGamer    008.41%'
                StLbNm4.value='4:  '
                StLbNm5.value='5:  '
            if app.L=='Distance Moved':
                StLbNm1.value='1:  Cthulhu     15023'
                StLbNm2.value='2:  Trevin      13368'
                StLbNm3.value='3:  ProGamer    132'
                StLbNm4.value='4:  '
                StLbNm5.value='5:  '
            if app.L=='Time Played':
                StLbNm1.value='1:  Cthulhu     19:46'
                StLbNm2.value='2:  Trevin      13:08'
                StLbNm3.value='3:  ProGamer    00:28'
                StLbNm4.value='4:  '
                StLbNm5.value='5:  '
            StLbNm1.left=17
            StLbNm1.visible=True
            StLbNm2.left=17
            StLbNm2.visible=True
            StLbNm3.left=17
            StLbNm3.visible=True
            StLbNm4.left=17
            StLbNm4.visible=True
            StLbNm5.left=17
            StLbNm5.visible=True
def onMousePress (x, y):
    if app.secret==False:
        if app.gamePaused==False:
            if app.TitleScreen==1 and LoseScreen.value==0:
                if TitleScreenBackground1.contains(x, y)==True:
                    app.TitleScreen=2
                    TitleScreenBackground1.visible=False
                    TitleScreenLabel1.visible=False
            elif app.TitleScreen==2 or app.TitleScreen==3 or app.TitleScreen==4 and LoseScreen.value==0:
                if SkipButtonClickDetector1.contains(x, y)==True:
                    app.TitleScreen=0
            elif LoseScreen.value==1:
                if LoseScreenPlayAgainClickDetector1.contains (x, y)==True:
                    app.Restart=True
        else:
            if PauseScreenClickDetector1.contains (x, y)==True and app.settings==False:
                app.Restart=True
            if PauseScreenClickDetector2.contains (x, y)==True:
                app.settings=True
    else:
        if app.l==True and x>=30 and x<=155 and y>=40 and y<=130:
            if y>=40 and y<=55:
                app.L='Score'
                StLbHl1.top=38
            if y>=55 and y<=70:
                app.L='Kills'
                StLbHl1.top=53
            if y>=70 and y<=85:
                app.L='Shots Fired'
                StLbHl1.top=68
            if y>=85 and y<=100:
                app.L='Accuracy'
                StLbHl1.top=83
            if y>=100 and y<=115:
                app.L='Distance Moved'
                StLbHl1.top=98
            if y>=115 and y<=130:
                app.L='Time Played'
                StLbHl1.top=113
        else:
            app.secret=False
            app.Restart=True
def onKeyHold (keys):
    if app.secret==False:
        if ('p' in keys or 'tab' in keys or 'escape' in keys):
            if app.gamePaused==False:
                app.gamePaused=True
            elif app.gamePaused==True:
                app.gamePaused=False
                app.settings=False
        if app.gamePaused==False:
            if app.TitleScreen==0 and LoseScreen.value==0:
                if('w' in keys or 'up' in keys) and PlayerSprite.centerY>10:
                    PlayerSprite.centerY-=5
                    if PlayerSprite.hitsShape (mazewalls):
                        PlayerSprite.centerY+=5
                    app.distanceMoved+=1
                if('s' in keys or 'down' in keys) and PlayerSprite.centerY<390:
                    PlayerSprite.centerY+=5
                    if PlayerSprite.hitsShape (mazewalls):
                        PlayerSprite.centerY-=5
                    app.distanceMoved+=1
                if('a' in keys or 'left' in keys) and PlayerSprite.centerX>10:
                    PlayerSprite.centerX-=5
                    if PlayerSprite.hitsShape (mazewalls):
                        PlayerSprite.centerX+=5
                    app.distanceMoved+=1
                if('d' in keys or 'right' in keys) and PlayerSprite.centerX<390:
                    PlayerSprite.centerX+=5
                    if PlayerSprite.hitsShape (mazewalls):
                        PlayerSprite.centerX-=5
                    app.distanceMoved+=1
                if('space' in keys):
                    if app.ammo>=1:
                        if (app.currentgun=='Pistol'):
                            if app.reload+4<=app.time:
                                app.reload=app.time
                                shoot(5,10,-2,2,1,1)
                                AmmoCounter.value=rounded(app.ammo)
                        if app.currentgun=='SMG':
                            if app.reload+1<=app.time:
                                app.reload=app.time
                                shoot(4,7,-30,30,2,1)
                                AmmoCounter.value=rounded(app.ammo)
                        if app.currentgun=='Sniper':
                            if app.reload+10<=app.time:
                                app.reload=app.time
                                shoot(5,16,0,1,5,1)
                                AmmoCounter.value=rounded(app.ammo)
                        if app.currentgun=='Tracker':
                            if app.reload+20<=app.time:
                                app.reload=app.time
                                shoot(10,20,0,1,20,1)
                                AmmoCounter.value=rounded(app.ammo)
                        if (app.currentgun=='RPG'):
                            if app.reload+60<=app.time:
                                app.reload=app.time
                                shoot(10,20,0,1,30,1)
                                AmmoCounter.value=rounded(app.ammo)
                        if (app.currentgun=='AR'):
                            if app.reload+randrange(2,4)<=app.time:
                                app.reload=app.time
                                shoot(5,12,-7,7,2,1)
                                AmmoCounter.value=rounded(app.ammo)
                        if (app.currentgun=='Shotgun'):
                            if app.reload+20<=app.time:
                                app.reload=app.time
                                shoot(5,10,-7,7,1,0.2)
                                shoot(5,10,0,14,1,0.2)
                                shoot(5,10,-14,0,1,0.2)
                                shoot(5,10,7,21,1,0.2)
                                shoot(5,10,-21,7,1,0.2)
                                AmmoCounter.value=rounded(app.ammo)
                        if (app.currentgun=='WallBreaker'):
                            if app.reload+10<=app.time:
                                app.reload=app.time
                                shoot(10,20,-3,3,50,0)
                                AmmoCounter.value=rounded(app.ammo)
                        if (app.currentgun=='Sword'):
                            if app.reload+4<=app.time:
                                app.reload=app.time
                                shoot(0,0,180-22,181-22,0.5,0)
                                AmmoCounter.value=rounded(app.ammo)
                        if app.ammo<0:
                            app.ammo=0
                    if app.currentgun=='Melee':
                        if app.reload+7<=app.time:
                            app.reload=app.time
                            shoot(6,12,0,1,0,0)
                elif 'q' in keys:
                    app.currentgun='Melee'
                    if app.reload+7<=app.time:
                        app.reload=app.time
                        shoot(6,24,0,1,0,0)
                    app.currentgun=app.gun
                app.PlayerSpriteX=PlayerSprite.centerX
                app.PlayerSpriteY=PlayerSprite.centerY
                Gun.centerX=PlayerSprite.centerX
                Gun.centerY=PlayerSprite.centerY
                Light.centerX=PlayerSprite.centerX
                Light.centerY=PlayerSprite.centerY
                rotate=angleTo(PlayerSprite.centerX,PlayerSprite.centerY,xAngle.value,yAngle.value)
                Gun.rotateAngle = rotate
                Light.rotateAngle=rotate
                if(not Light.centerX==PlayerSprite.centerX or not Light.centerY==PlayerSprite.centerY):
                    Light.centerX=PlayerSprite.centerX
                    Light.centerY=PlayerSprite.centerY
                PlayerSprite.rotateAngle=rotate
        elif app.gamePaused==True:
            if '|' in keys and '~' in keys:
                password = app.getTextInput('password')
                if password=='credits' and app.zR==True:
                    app.secret=True
                    app.c=True
                    app.found+=1
                    app.zR=False
                if password=='leaderboard' and app.kY==True:
                    app.secret=True
                    app.l=True
                    app.found+=1
                    app.kY=False
                if password=='password' and app.xF==True:
                    app.secret=True
                    app.p=True
                    app.found+=1
                    app.xF=False
def onMouseMove(x,y):
    if app.secret==False:
        if app.gamePaused==False:
            if LoseScreen.value==0:
                xAngle.value=x
                yAngle.value=y
                rotate=angleTo(PlayerSprite.centerX,PlayerSprite.centerY,x,y)
                Gun.rotateAngle = rotate
                Light.rotateAngle = rotate
                Light.centerX=PlayerSprite.centerX
                Light.centerY=PlayerSprite.centerY
                PlayerSprite.rotateAngle=rotate
def rpge(x,y):
    if app.secret==False:
        bullet = Circle(200,200,80,fill=gradient('red','orange'),border='black',align='left-bottom')
        app.reload=app.time
        bullet.centerX=x
        bullet.centerY=y
        bullet.rotateAngle = angleTo(PlayerSprite.centerX,PlayerSprite.centerY,xAngle.value,yAngle.value)
        bullet.visible=True
        bulletGoalX,bulletGoalY=getPointInDir(PlayerSprite.centerX,PlayerSprite.centerY,bullet.rotateAngle,3)
        BulletGroup.add(bullet)
def shoot(sizeX,sizeY,accuracyL,accuracyH,used,shot):
    if (app.currentgun=='RPG'):
        bullet = Oval(200,200,sizeX,sizeY,fill='yellow',border='black',align='left-bottom')
    elif (app.currentgun=='Sword'):
        bullet= Group (Line (175,200,185,210,fill='white'), Line (185,210,200,215,fill='white'), 
        Line (160,210,175,225,fill='white'), Line (175,225,200,230,fill='white'), 
    Rect (200,200,7,20,align='bottom',fill=gradient('darkgray','dimgray','darkgray',start='left')), 
    Polygon (197,200,200,170,203,200,200,230,fill=gradient('darkgray','dimgray','darkgray',start='left')), 
    Rect (200,180,4,10,align='bottom',fill='saddlebrown'), Line (-400,-400,-800,-840), Line (800,800,1200,1200))
        bullet.height//=1.5
        bullet.width//=1.5
    else:
        bullet = Rect(200,200,sizeX,sizeY,fill='yellow',border='black',align='left-bottom')
    bullet.centerX=Gun.centerX
    bullet.centerY=Gun.centerY
    bullet.rotateAngle = angleTo(PlayerSprite.centerX,PlayerSprite.centerY,xAngle.value,yAngle.value)
    bullet.rotateAngle+=randrange(accuracyL, accuracyH)
    if (app.currentgun=='Melee'):
        bullet.fill= 'lemonchiffon'
        bullet.rotateAngle+=180
        bullet.toFront()
    if (app.currentgun=='WallBreaker'):
        bullet.fill='dimgray'
    if (app.currentgun=='Tracker'):
        bullet.fill='blue'
    bullet.visible=True
    bulletGoalX,bulletGoalY=getPointInDir(PlayerSprite.centerX,PlayerSprite.centerY,bullet.rotateAngle,3)
    if( app.currentgun=='Sword' or app.currentgun=='Melee'):
        bullet.centerX=bulletGoalX
        bullet.centerY=bulletGoalY
    BulletGroup.add(bullet)
    app.ammo-=used
    app.bulletsShot+=shot
class Cell:
    wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    def __init__(self,x,y):
        self.x,self.y = x, y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}
    def has_all_walls(self):
        return all(self.walls.values())
    def knock_down_wall(self,other,wall):
        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False
class Maze:
    def __init__(self,nx,ny,ix=0,iy=0):
        self.nx,self.ny=nx,ny
        self.ix,self.iy=ix,iy
        self.maze_map=[[Cell(x,y) for y in range(ny)] for x in range(nx)]
    def cell_at(self,x,y):
        return self.maze_map[x][y]
    def __str__(self):
        maze_rows=['--+'* self.nx * 1]
        for y in range(self.ny):
            maze_row=['V']
            for x in range(self.nx):
                if self.maze_map[x][y].walls['E']:
                    maze_row.append('  |')
                else:
                    maze_row.append('   ')
            maze_rows.append(''.join(maze_row))
            maze_row=['dwn']
            for x in range(self.nx):
                if self.maze_map[x][y].walls['S']:
                    maze_row.append('--+')
                else:
                    maze_row.append('  +')
            maze_rows.append(''.join(maze_row))
        return '\n'.join(maze_rows)
    def find_valid_neighbours(self,cell):
        delta=[('W',(-1,0)),
            ('E',(1,0)),
            ('S',(0,1)),
            ('N',(0,-1))]
        neighbours=[]
        for direction, (dx,dy) in delta:
            x2,y2=cell.x+dx,cell.y+dy
            if(0<= x2 < self.nx) and (0 <= y2 < self.ny):
                neighbour=self.cell_at(x2,y2)
                if neighbour.has_all_walls():
                    neighbours.append((direction,neighbour))
        return neighbours
    def make_maze(self):
        n=self.nx*self.ny
        cell_stack=[]
        current_cell=self.cell_at(self.ix,self.iy)
        nv=1
        while nv<n:
            neighbours=self.find_valid_neighbours(current_cell)
            if not neighbours:
                current_cell=cell_stack.pop()
                continue
            direction,next_cell=choice(neighbours)
            current_cell.knock_down_wall(next_cell,direction)
            cell_stack.append(current_cell)
            current_cell=next_cell
            nv+=1
nx = ny = 5
ix=iy=0
maze=Maze(nx,ny,ix,iy)
maze.make_maze()
app.x1=0
app.y1=0
app.x2=-400/nx
app.y2=0
app.MT=0
for i in range(nx*ny*2+ny):
    if '--+'==str(maze)[app.MT*3:(app.MT+1)*3]:
        app.x1+=400/nx
        app.x2+=400/nx
        app.MT+=1
        mazewalls.add(Line(app.x1,app.y1,app.x2,app.y2,opacity=30,lineWidth=2))
    if'  +'==str(maze)[app.MT*3:(app.MT+1)*3]:
        app.x1+=400/nx
        app.x2+=400/nx
        app.MT+=1
    if'   '==str(maze)[app.MT*3-1:(app.MT+1)*3-1]:
        app.x1+=400/nx
        app.x2+=400/nx
        app.MT+=1
    if '  |'==str(maze)[app.MT*3-1:(app.MT+1)*3-1]:
        app.x1+=400/nx
        app.x2+=400/nx
        mazewalls.add(Line(app.x1,app.y1,app.x2,app.y2+400/ny,opacity=30,lineWidth=2))
        app.MT+=1
    if 'V' in str(maze)[app.MT*3-1:(app.MT+1)*3-1]:
        app.x1=0
        app.x2=0
        app.MT+=1
    if 'dwn'==str(maze)[app.MT*3:(app.MT+1)*3]:
        app.y1+=400/ny
        app.y2+=400/ny
        app.x1=0
        app.x2=-400/nx
        app.MT+=1
mazewalls.visible=False