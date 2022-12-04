from cmu_112_graphics import *
from practiceCar import *
from practiceTrack import *
from raceCar import *
from raceTrack import *
import math
import random

def splashScreenMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2,app.height/2,image=ImageTk.PhotoImage(app.menuImage))
    drawStartBox(app,canvas)
    font = 'Arial 50 bold'
    canvas.create_text(app.width/2, app.height*(1/10), text='Welcome to 112 Motorsport!',
                       font=font, fill='black')

def drawStartBox(app,canvas):
    canvas.create_rectangle(app.width*(3/10),app.height*(2/10),app.width*(7/10),app.height*(3/10),fill='grey')
    canvas.create_text(app.width*(5/10),app.height*(2.5/10),text='How to play',font='Arial 20 bold',fill='black')
    canvas.create_rectangle(app.width*(3/10),app.height*(3.5/10),app.width*(7/10),app.height*(4.5/10),fill='grey')
    canvas.create_text(app.width*(5/10),app.height*(4/10),text='Practice!',font='Arial 20 bold',fill='black')
    canvas.create_rectangle(app.width*(3/10),app.height*(5/10),app.width*(7/10),app.height*(6/10),fill='grey')
    canvas.create_text(app.width*(5/10),app.height*(5.5/10),text='Race!',font='Arial 20 bold',fill='black')
    canvas.create_rectangle(app.width*(3/10),app.height*(6.5/10),app.width*(7/10),app.height*(7.5/10),fill='grey')
    canvas.create_text(app.width*(5/10),app.height*(7/10),text='Bonus Mode!',font='Arial 20 bold',fill='black')

def splashScreenMode_mousePressed(app, event):
    if app.width*(3/10)<event.x<app.width*(7/10)and app.height*(5/10)<event.y<app.height*(6/10):
        app.mode = 'raceMode'
    elif app.width*(3/10)<event.x<app.width*(7/10)and app.height*(3.5/10)<event.y<app.height*(4.5/10):
        app.mode = 'practiceMode'
    elif app.width*(3/10)<event.x<app.width*(7/10) and app.height*(2/10)<event.y<app.height*(3/10):
        app.mode = 'guideMode'
    elif app.width*(3/10)<event.x<app.width*(7/10)and app.height*(6.5/10)<event.y<app.height*(7.5/10):
        app.mode = 'bonusMode'

def appStarted(app):
####### bonus mode
    app.velocity = 0
    app.maxVelocity = 3
    app.accel2 = 0.5
    app.deccel2 = 0.2
    app.directions = []
    for i in range(24):
        angle = (i/24)*2*math.pi
        app.directions.append(angle)
    app.carMove = True
    app.scrollX = 0
    app.scrollY = 0
#######
    app.playerIndex = 0
    app.exampleImageTemp = app.loadImage('exampleImage.png') #from game play screenshot
    app.exampleImage = app.scaleImage(app.exampleImageTemp,2/10)
    app.menuImage = app.loadImage('trackImage.jpeg') #from https://s100.iracing.com/wp-content/uploads/2020/08/cota-5-1024x576.jpg
    app.victoryImage = app.loadImage('victory.jpg') #from https://www.bmw-motorsport.com/content/dam/bmw/marketBMWSPORTS/bmw-motorsport_com/news/BMW_Customer_Racing_Review_16_11_20/nls-orginal.jpg.asset.1605527285113.jpg
    app.trackWidth = app.width*(1/10)
    app.practiceCX = app.width*(5/10)
    app.practiceCY = app.height*(5/10)
    app.carX = app.width*(5/10) -10
    app.carY = app.height*(5/10)
    app.cx = app.width*(5/10) - 11
    app.cy = app.height*(8.5/10)
    app.enemyCX = app.width*(5/10) - 11
    app.enemyCY = app.height*(8.7/10)
    app.dx = 3
    app.dy = 3
    app.dxSlow = 1
    app.dySlow = 1
    app.enemyDX = 3
    app.enemyDY = 3
    app.enemyDXSlow = 1
    app.enemyDYSlow = 1
    app.carWidth = app.width*(0.1/10)
    app.enemyWin = False
    app.playerWin = False
    app.gameOver = False
    app.carList = ['player','enemy']
    app.timerDelay = 1
    app.playerTimerCount = 0
    app.enemyTimerCount = 0
    app.collisionTimer = 3000 
    app.enemyCollisionTimer = 3000 
    app.carCollisionTimer = 2000
    app.playerMinute = 0
    app.playerSecond = 0
    app.enemyMinute = 0
    app.enemySecond = 0
    app.turnAngle = math.pi/2
    app.r = 12 #12
    app.mode = 'splashScreenMode'
    app.collision = False
    app.enemyCollision = False
    app.carCollision = False
    app.accelTF = True
    app.enemyAccelTF = True 
    app.practiceTrackFinal = practiceTrack(practiceTrackSectors(app),app.carX,app.carY,app.practiceCX,app.practiceCY,app.width,app.height)
    app.raceTrackFinal = raceTrack(raceTrackSectors(app),app.cx,app.cy,app.enemyCX,app.enemyCY,app.width,app.height)
    app.enemyLapCount = 0
    app.playerLapCount = 0
    app.enemyTurns = []
    for turn in range(8):
        app.enemyTurns.append(bool(random.randint(0,1)))
    app.playerTurns = [False,False,False,False,False,False,False,False]
    app.enemySectorsTracker = set()
    app.playerSectorsTracker = set()
    app.accelSlow = 0.015  #0.015
    app.accel = 0.03  #0.03
    app.playerImage = app.loadImage('Player Car.png') #from http://clipart-library.com/clipart/clip-art-car-12.htm
    app.enemyImage = app.loadImage('Enemy Car.png') #from http://clipart-library.com/clipart/LTdojedMc.htm
    app.enemyCarImages = []
    app.playerRaceCarImages = []
    app.playerRaceCarImages2 = []
    for i in range(4):
        app.playerRaceCarImages += [[0]*6]
    for i in range(4):
        for j in range(6): ##############
            pos = app.playerImage.crop(((2500/24)*(i*6+j),0,(2500/24)*(i*6+j+1),104))
            app.playerRaceCarImages[i][j] = app.scaleImage(pos,1/3)
    for i in range(24):
        pos2 = app.playerImage.crop(((2500/24)*(i),0,(2500/24)*(i+1),104))
        tempImage = app.scaleImage(pos2,1/3)
        app.playerRaceCarImages2.append(tempImage)
    app.playerRaceCar = raceCar(app.cx,app.cy,app.width,app.height,app.playerRaceCarImages,app.playerIndex)
    app.practiceCar = practiceCar(app.carX,app.carY,app.width,app.height,app.playerRaceCarImages,app.playerIndex)
    for image in range(8):
        enemyPos = app.enemyImage.crop(((2500/8)*(image),0,(2500/8)*(image+1),312))
        enemyCarPos = app.scaleImage(enemyPos,1/10)
        app.enemyCarImages.append(enemyCarPos)
    app.enemyCar = enemyCar(app.enemyCX,app.enemyCY,app.width,app.height,app.enemyCarImages)
def guideMode_redrawAll(app,canvas):
    canvas.create_rectangle(app.width*(1/10),app.height*(2/10),app.width*(9/10),app.height*(9/10),fill='white',width=20)
    canvas.create_text(app.width*(5/10),app.height*(3/10),text='Press the space bar when the yellow player car is in \nthe center of each red rectangle on the track. \nThis will allow the car to turn in each corner.',font = 'Arial 18 bold')
    canvas.create_image(app.width*(5/10),app.height*(5.5/10),image=ImageTk.PhotoImage(app.exampleImage))
    canvas.create_text(app.width*(5/10),app.height*(8/10),text='Press key r to switch to the menu screen at any time',font='Arial 18 bold')

def guideMode_keyPressed(app,event):
    if event.key == 'r':
        app.mode = 'splashScreenMode'

def practiceTrackSectors(app):
    practiceTrack = dict()
    practiceTrack['sector0'] = (app.practiceCX-app.width*(4/10),app.practiceCY-app.height*(0.5/10),app.practiceCX,app.practiceCY+app.height*(0.5/10))
    practiceTrack['sector1'] = (app.practiceCX-app.width*(4/10),app.practiceCY-app.height*(7.5/10),app.practiceCX-app.width*(3/10),app.practiceCY-app.height*(0.5/10))
    practiceTrack['sector2'] = (app.practiceCX-app.width*(3/10),app.practiceCY-app.height*(7.5/10),app.practiceCX-app.width*(1/10),app.practiceCY-app.height*(6.5/10))
    practiceTrack['sector3'] = (app.practiceCX-app.width*(2/10),app.practiceCY-app.height*(6.5/10),app.practiceCX-app.width*(1/10),app.practiceCY-app.height*(2.5/10))
    practiceTrack['sector4'] = (app.practiceCX-app.width*(1/10),app.practiceCY-app.height*(3.5/10),app.practiceCX+app.width*(2/10),app.practiceCY-app.height*(2.5/10))
    practiceTrack['sector5'] = (app.practiceCX+app.width*(1/10),app.practiceCY-app.height*(7.5/10),app.practiceCX+app.width*(2/10),app.practiceCY-app.height*(3.5/10))
    practiceTrack['sector6'] = (app.practiceCX+app.width*(2/10),app.practiceCY-app.height*(7.5/10),app.practiceCX+app.width*(4/10),app.practiceCY-app.height*(6.5/10))
    practiceTrack['sector7'] = (app.practiceCX+app.width*(3/10),app.practiceCY-app.height*(6.5/10),app.practiceCX+app.width*(4/10),app.practiceCY+app.height*(0.5/10))
    practiceTrack['sector8'] = (app.practiceCX+10,app.practiceCY-app.height*(0.5/10),app.practiceCX+app.width*(3/10),app.practiceCY+app.height*(0.5/10))
    practiceTrack['sector9'] = (app.practiceCX,app.practiceCY-app.height*(0.5/10),app.practiceCX+10,app.practiceCY+app.height*(0.5/10))
    return practiceTrack

def getSeconds(app):
    if app.playerSecond % 60 == 0:
        app.playerMinute += 1

def practiceMode_timerFired(app):
    app.playerTimerCount += app.timerDelay 
    app.practiceTrackFinal = practiceTrack(practiceTrackSectors(app),app.carX,app.carY,app.practiceCX,app.practiceCY,app.width,app.height)
    app.practiceCar = practiceCar(app.carX,app.carY,app.width,app.height,app.playerRaceCarImages,app.playerIndex)
    movePraticePlayerCar(app)
    playerLapPassed(app)
    playerPracticeCarTurn(app)
    if app.collisionTimer > 0: 
        app.collisionTimer -= 50
    else:
        app.collision = False
    if app.accelTF == False: 
        if app.collision == False:
            app.dx = 3
            app.dy = 3
        else:
            app.dxSlow = 1
            app.dySlow = 1
    if app.playerTimerCount % 1000 == 0:
        app.playerSecond += 1

def playerLapPassed(app):
    if len(app.playerSectorsTracker)==10:
        app.playerLapCount += 1
        app.playerTurns = [False,False,False,False,False,False,False,False]
        app.playerSectorsTracker = set()
        app.playerTimerCount = 0
        app.playerMinute = 0
        app.playerSecond = 0

def movePraticePlayerCar(app):
    if app.practiceTrackFinal.getSector() == 'sector0': #front straight
        app.playerSectorsTracker = set()
        app.playerSectorsTracker.add(0)
        if app.playerTurns[0] == False:
            app.playerIndex = 0
        app.accelTF = True
        if app.collision == True:
            app.dxSlow += app.accelSlow
            app.practiceCX += app.dxSlow
        else:
            app.dx += app.accel
            app.practiceCX += app.dx
    elif app.practiceTrackFinal.getSector() == ('sector0','collisionLeft'): #miss turn 1
        app.collision = True
        app.collisionTimer = 3000
        if app.collision == True:
            app.practiceCX = app.practiceCX - app.trackWidth*(0.8)
            app.practiceCY = app.practiceCY + app.trackWidth*(0.8)
    elif app.practiceTrackFinal.getSector() == 'sector1': #short straight after turn 1
        app.playerSectorsTracker.add(1)
        app.accelTF = True
        if app.playerTurns[1] == False:
            app.playerIndex = 0
        if app.collision == True:
            app.dySlow += app.accelSlow
            app.practiceCY += app.dySlow
        else:
            app.dy += app.accel
            app.practiceCY += app.dy
    elif app.practiceTrackFinal.getSector() == ('sector1','collisionTop'): #miss turn 2
        app.collision = True
        app.collisionTimer = 3000
        if app.collision == True:
            app.practiceCY = app.practiceCY - app.trackWidth*(0.8)
            app.practiceCX = app.practiceCX - app.trackWidth*(0.8)
    elif app.practiceTrackFinal.getSector() == 'sector2': #short straight after turn 2
        app.playerSectorsTracker.add(2)
        if app.playerTurns[2] == False:
            app.playerIndex = 0
        app.accelTF = True
        if app.collision == True:
            app.dxSlow += app.accelSlow
            app.practiceCX -= app.dxSlow
        else:
            app.dx += app.accel
            app.practiceCX -= app.dx
    elif app.practiceTrackFinal.getSector() == ('sector2','collisionRight'): #miss turn 3
        app.collision = True
        app.collisionTimer = 3000
        if app.collision == True:
            app.practiceCX = app.practiceCX + app.trackWidth*(0.8)
            app.practiceCY = app.practiceCY - app.trackWidth*(0.8)
    elif app.practiceTrackFinal.getSector() == 'sector3':#short straight after turn 3
        app.playerSectorsTracker.add(3)
        app.accelTF = True
        if app.playerTurns[3] == False:
            app.playerIndex = -1
        if app.collision == True:
            app.dySlow += app.accelSlow
            app.practiceCY -= app.dySlow
        else:
            app.dy += app.accel
            app.practiceCY -= app.dy
    elif app.practiceTrackFinal.getSector() == ('sector3', 'collisionDown'): #miss turn 4
        app.collision = True
        app.collisionTimer = 3000
        if app.collision == True:
            app.practiceCY = app.practiceCY + app.trackWidth*(0.8)
            app.practiceCX = app.practiceCX - app.trackWidth*(0.8)
    elif app.practiceTrackFinal.getSector() == 'sector4': #short straight after turn 4
        app.playerSectorsTracker.add(4)
        app.accelTF = True
        if app.playerTurns[4] == False:
            app.playerIndex = -1
        if app.collision == True:
            app.dxSlow += app.accelSlow
            app.practiceCX -= app.dxSlow
        else:
            app.dx += app.accel
            app.practiceCX -= app.dx
    elif app.practiceTrackFinal.getSector() == ('sector4','collisionRight'): #miss turn 5
        app.collision = True
        app.collisionTimer = 3000
        if app.collision == True:
            app.practiceCX = app.practiceCX + app.trackWidth*(0.8)
            app.practiceCY = app.practiceCY + app.trackWidth*(0.8)
    elif app.practiceTrackFinal.getSector() == 'sector5': #short straight after turn 5
        app.playerSectorsTracker.add(5)
        app.accelTF = True
        if app.playerTurns[5] == False:
            app.playerIndex = 0
        if app.collision == True:
            app.dySlow += app.accelSlow
            app.practiceCY += app.dySlow
        else:
            app.dy += app.accel
            app.practiceCY += app.dy
    elif app.practiceTrackFinal.getSector() == ('sector5','collisionTop'): #miss turn 6
        app.collision = True
        app.collisionTimer = 3000
        if app.collision == True:
            app.practiceCY = app.practiceCY - app.trackWidth*(0.8)
            app.practiceCX = app.practiceCX - app.trackWidth*(0.8)
    elif app.practiceTrackFinal.getSector() == 'sector6': #short straight after turn 6
        app.playerSectorsTracker.add(6)
        app.accelTF = True
        if app.playerTurns[6] == False:
            app.playerIndex = 0
        if app.collision == True:
            app.dxSlow += app.accelSlow
            app.practiceCX -= app.dxSlow
        else:
            app.dx += app.accel
            app.practiceCX -= app.dx
    elif app.practiceTrackFinal.getSector() == ('sector6','collisionRight'):#miss turn 7
        app.collision = True
        app.collisionTimer = 3000
        if app.collision == True:        
            app.practiceCX = app.practiceCX + app.trackWidth*(0.8)
            app.practiceCY = app.practiceCY - app.trackWidth*(0.8)
    elif app.practiceTrackFinal.getSector() == 'sector7': #short straight after turn 7
        app.playerSectorsTracker.add(7)
        app.accelTF = True
        if app.playerTurns[7] == False:
            app.playerIndex = 0
        if app.collision == True:
            app.dySlow += app.accelSlow
            app.practiceCY -= app.dySlow
        else:
            app.dy += app.accel
            app.practiceCY -= app.dy
    elif app.practiceTrackFinal.getSector() == ('sector7','collisionDown'):#miss last turn
        app.collision = True
        app.collisionTimer = 3000
        if app.collision == True:
            app.practiceCY = app.practiceCY + app.trackWidth*(0.8)
            app.practiceCX = app.practiceCX + app.trackWidth*(0.8)
    elif app.practiceTrackFinal.getSector() == 'sector8': #front straight
        app.playerSectorsTracker.add(8)
        app.accelTF = True
        app.playerIndex = 0
        if app.collision == True:
            app.dxSlow += app.accelSlow
            app.practiceCX += app.dxSlow
        else:
            app.dx += app.accel
            app.practiceCX += app.dx
    elif app.practiceTrackFinal.getSector() == 'sector9': #front straight
        app.playerSectorsTracker.add(9)
        app.accelTF = True
        app.playerIndex = 0
        if app.collision == True:
            app.dxSlow += app.accelSlow
            app.practiceCX += app.dxSlow
        else:
            app.dx += app.accel
            app.practiceCX += app.dx

def practiceMode_keyPressed(app,event):
    if event.key == 'Space':
        if app.practiceTrackFinal.T1TurningPoint() == True:
            app.playerTurns[0] = True
        elif app.practiceTrackFinal.T2TurningPoint() == True:
            app.playerTurns[1] = True
        elif app.practiceTrackFinal.T3TurningPoint() == True:
            app.playerTurns[2] = True
        elif app.practiceTrackFinal.T4TurningPoint() == True:
            app.playerTurns[3] = True
        elif app.practiceTrackFinal.T5TurningPoint() == True:
            app.playerTurns[4] = True
        elif app.practiceTrackFinal.T6TurningPoint() == True:
            app.playerTurns[5] = True
        elif app.practiceTrackFinal.T7TurningPoint() == True:
            app.playerTurns[6] = True
        elif app.practiceTrackFinal.T8TurningPoint() == True:
            app.playerTurns[7] = True
    elif event.key == 'r':
        app.mode = 'splashScreenMode'
        appStarted(app)

def playerPracticeCarTurn(app):
    if app.practiceTrackFinal.playerT1() == True: #turn 1 (right up)
        app.accelTF = False 
        if app.playerTurns[0] == True:
            if app.playerIndex < 5:
                app.playerIndex += 1
            app.practiceCX -= app.r * math.cos(app.turnAngle)
            app.practiceCY += app.r * math.sin(app.turnAngle)
    elif app.practiceTrackFinal.playerT2() == True: #turn 2 (right across)
        app.accelTF = False 
        if app.playerTurns[1] == True:
            if app.playerIndex < 5:
                app.playerIndex += 1
            app.practiceCY -= app.r * math.cos(app.turnAngle)
            app.practiceCX -= app.r * math.sin(app.turnAngle)
    elif app.practiceTrackFinal.playerT3() == True: #turn 3 (right down)
        app.accelTF = False 
        if app.playerTurns[2] == True:
            if app.playerIndex < 5:
                app.playerIndex += 1
            app.practiceCY -= app.r * math.sin(app.turnAngle)
            app.practiceCX += app.r * math.cos(app.turnAngle)
    elif app.practiceTrackFinal.playerT4() == True: #turn 4 (left across)
        app.accelTF = False 
        if app.playerTurns[3] == True:
            if app.playerIndex > -6:
                app.playerIndex -= 1
            app.practiceCY += app.r * math.cos(app.turnAngle)
            app.practiceCX -= app.r * math.sin(app.turnAngle)
    elif app.practiceTrackFinal.playerT5() == True: #turn 5 (left up)
        app.accelTF = False 
        if app.playerTurns[4] == True:
            if app.playerIndex > -6:
                app.playerIndex -= 1
            app.practiceCX -= app.r * math.cos(app.turnAngle)
            app.practiceCY += app.r * math.sin(app.turnAngle)
    elif app.practiceTrackFinal.playerT6() == True: #turn 6 (right across)
        app.accelTF = False 
        if app.playerTurns[5] == True:
            if app.playerIndex < 5:
                app.playerIndex += 1
            app.practiceCY += app.r * math.cos(app.turnAngle)
            app.practiceCX -= app.r * math.sin(app.turnAngle)
    elif app.practiceTrackFinal.playerT7() == True: #turn 7 (right down)
        app.accelTF = False 
        if app.playerTurns[6] == True:
            if app.playerIndex < 5:
                app.playerIndex += 1
            app.practiceCX -= app.r * math.cos(app.turnAngle)
            app.practiceCY -= app.r * math.sin(app.turnAngle)
    elif app.practiceTrackFinal.playerT8() == True: # last turn (left across)
        app.accelTF = False 
        if app.playerTurns[7] == True:
            if app.playerIndex < 5:
                app.playerIndex += 1
            app.practiceCY -= app.r * math.cos(app.turnAngle)
            app.practiceCX += app.r * math.sin(app.turnAngle)

def drawPracticeTrack(app,canvas):
    app.practiceTrackFinal.drawSectors(canvas, app.scrollX, app.scrollY)
    app.practiceTrackFinal.drawStartLine(canvas)
    app.practiceTrackFinal.drawTurningPoints(canvas)

def practiceMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill='green')
    drawPracticeTrack(app,canvas)
    if app.collision == True:
        canvas.create_text(app.width*(5/10),app.height*(7.5/10),text = 'Collision!',font='Arial 20 bold')
    canvas.create_text(app.width/2,app.height*(9.2/10),text=f'laptime = {app.playerMinute} minute {app.playerSecond} seconds {app.playerTimerCount%1000//100} milliseconds',font='Arial 20 bold')
    canvas.create_text(app.width/2,app.height*(9.5/10),text=f'Player Laps Completed = {app.playerLapCount}',font='Arial 20 bold')
    canvas.create_text(app.width/2,app.height*(9.8/10),text=f'Player Speed = {int(((app.dx**2)+(app.dy**2))**0.5//1)}',font='Arial 20 bold')
    if app.practiceTrackFinal.getSector() == 'sector0':
        app.practiceCar.drawSector0(canvas)
    if app.practiceTrackFinal.playerT1() == True: ###
        if app.playerTurns[0] == True:
            app.practiceCar.drawT1(canvas)
    if app.practiceTrackFinal.getSector() == 'sector1':
        app.practiceCar.drawSector1(canvas)
    if app.practiceTrackFinal.playerT2() == True:
        if app.playerTurns[1] == True:
            app.practiceCar.drawT2(canvas) ###
    if app.practiceTrackFinal.getSector() == 'sector2':
        app.practiceCar.drawSector2(canvas)
    if app.practiceTrackFinal.playerT3() == True:
        if app.playerTurns[2] == True:
            app.practiceCar.drawT3(canvas) ###
    if app.practiceTrackFinal.getSector() == 'sector3':
        app.practiceCar.drawSector3(canvas)
    if app.practiceTrackFinal.playerT4() == True:
        if app.playerTurns[3] == True:
            app.practiceCar.drawT4(canvas) ###
    if app.practiceTrackFinal.getSector() == 'sector4':
        app.practiceCar.drawSector4(canvas)
    if app.practiceTrackFinal.playerT5() == True:
        if app.playerTurns[4] == True:
            app.practiceCar.drawT5(canvas) ###
    if app.practiceTrackFinal.getSector() == 'sector5':
        app.practiceCar.drawSector5(canvas)
    if app.practiceTrackFinal.playerT6() == True:
        if app.playerTurns[5] == True:
            app.practiceCar.drawT6(canvas) ###
    if app.practiceTrackFinal.getSector() == 'sector6':
        app.practiceCar.drawSector6(canvas)
    if app.practiceTrackFinal.playerT7() == True:
        if app.playerTurns[6] == True:
            app.practiceCar.drawT7(canvas) ###
    if app.practiceTrackFinal.getSector() == 'sector7':
        app.practiceCar.drawSector7(canvas)
    if app.practiceTrackFinal.playerT8() == True:
        if app.playerTurns[7] == True:
            app.practiceCar.drawT8(canvas) ###
    if app.practiceTrackFinal.getSector() == 'sector8':
        app.practiceCar.drawSector8(canvas)
    if app.practiceTrackFinal.getSector() == 'sector9':
        app.practiceCar.drawSector9(canvas)
####################
def bonusMode_timerFired(app):
    # print(app.velocity)
    print(app.playerSectorsTracker)
    if app.velocity > app.maxVelocity:
        app.velocity = app.maxVelocity
    app.scrollX = -app.velocity * math.cos(app.directions[app.playerIndex])
    app.scrollY = -app.velocity * math.sin(app.directions[app.playerIndex])
    moveBonusCar(app)
    app.practiceTrackFinal = practiceTrack(practiceTrackSectors(app),app.carX,app.carY,app.practiceCX,app.practiceCY,app.width,app.height)
    playerLapPassed(app)
    if app.playerIndex >= 23:
        app.playerIndex = 0
    if app.collisionTimer > 0: 
        app.collisionTimer -= 50
    else:
        app.collision = False

def moveBonusCar(app):
    app.practiceCX -= app.scrollX
    app.practiceCY -= app.scrollY
    if app.practiceTrackFinal.getSector() == 'sector0': #front straight
        app.playerSectorsTracker = set()
        app.playerSectorsTracker.add(0)
    elif app.practiceTrackFinal.getSector() == ('sector0','collisionLeft'): #miss turn 1
        app.collision = True
        app.collisionTimer = 3000
        app.playerIndex += 6
        if app.collision == True:
            app.practiceCX = app.practiceCX - app.trackWidth*(0.8)
            app.practiceCY = app.practiceCY + app.trackWidth*(0.8)
            app.velocity -= 3
    elif app.practiceTrackFinal.getSector() == 'sector1': 
        app.playerSectorsTracker.add(1)
    elif app.practiceTrackFinal.getSector() == ('sector1','collisionTop'): #miss turn 2
        app.collision = True
        app.collisionTimer = 3000
        app.playerIndex += 6
        if app.collision == True:
            app.practiceCY = app.practiceCY - app.trackWidth*(0.8)
            app.practiceCX = app.practiceCX - app.trackWidth*(0.8)
            app.velocity -= 3
    elif app.practiceTrackFinal.getSector() == 'sector2': 
        app.playerSectorsTracker.add(2)
    elif app.practiceTrackFinal.getSector() == ('sector2','collisionRight'): #miss turn 3
        app.collision = True
        app.collisionTimer = 3000
        app.playerIndex += 6
        if app.collision == True:
            app.practiceCX = app.practiceCX + app.trackWidth*(0.8)
            app.practiceCY = app.practiceCY - app.trackWidth*(0.8)
            app.velocity -= 3
    elif app.practiceTrackFinal.getSector() == 'sector3': 
        app.playerSectorsTracker.add(3)
    elif app.practiceTrackFinal.getSector() == ('sector3', 'collisionDown'): #miss turn 4
        app.collision = True
        app.collisionTimer = 3000
        app.playerIndex -= 6
        if app.collision == True:
            app.practiceCY = app.practiceCY + app.trackWidth*(0.8)
            app.practiceCX = app.practiceCX - app.trackWidth*(0.8)
            app.velocity -= 3
    elif app.practiceTrackFinal.getSector() == 'sector4': 
        app.playerSectorsTracker.add(4)
    elif app.practiceTrackFinal.getSector() == ('sector4','collisionRight'): #miss turn 5
        app.collision = True
        app.collisionTimer = 3000
        app.playerIndex -= 6
        if app.collision == True:
            app.practiceCX = app.practiceCX + app.trackWidth*(0.8)
            app.practiceCY = app.practiceCY + app.trackWidth*(0.8)
            app.velocity -= 3
    elif app.practiceTrackFinal.getSector() == 'sector5': 
        app.playerSectorsTracker.add(5)
    elif app.practiceTrackFinal.getSector() == ('sector5','collisionTop'): #miss turn 6
        app.collision = True
        app.collisionTimer = 3000
        app.playerIndex += 6
        if app.collision == True:
            app.practiceCY = app.practiceCY - app.trackWidth*(0.8)
            app.practiceCX = app.practiceCX - app.trackWidth*(0.8)
            app.velocity -= 3
    elif app.practiceTrackFinal.getSector() == 'sector6': 
        app.playerSectorsTracker.add(6)
    elif app.practiceTrackFinal.getSector() == ('sector6','collisionRight'):#miss turn 7
        app.collision = True
        app.collisionTimer = 3000
        app.playerIndex += 6
        if app.collision == True:        
            app.practiceCX = app.practiceCX + app.trackWidth*(0.8)
            app.practiceCY = app.practiceCY - app.trackWidth*(0.8)
            app.velocity -= 3
    elif app.practiceTrackFinal.getSector() == 'sector7': 
        app.playerSectorsTracker.add(7)
    elif app.practiceTrackFinal.getSector() == ('sector7','collisionDown'):#miss last turn
        app.collision = True
        app.collisionTimer = 3000
        app.playerIndex += 6
        if app.collision == True:
            app.practiceCY = app.practiceCY + app.trackWidth*(0.8)
            app.practiceCX = app.practiceCX + app.trackWidth*(0.8)
            app.velocity -= 3
    elif app.practiceTrackFinal.getSector() == 'sector8': 
        app.playerSectorsTracker.add(8)
    elif app.practiceTrackFinal.getSector() == 'sector9': 
        app.playerSectorsTracker.add(9)

def bonusMode_keyPressed(app,event):
    if event.key == 'w':
        app.velocity += app.accel2
    elif event.key == 'd':
        app.playerIndex += 1
    elif event.key == 'a':
        app.playerIndex -= 1
    elif event.key == 'r':
        appStarted(app)
        app.mode = 'splashScreenMode'
    elif event.key == 'Space':
        if app.velocity > 0:
            app.velocity -= app.deccel2
    
def bonusMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill='green')
    drawPracticeTrack(app,canvas)
    canvas.create_image(app.carX,app.carY,image=ImageTk.PhotoImage(app.playerRaceCarImages2[app.playerIndex]))
    if app.collision == True:
        canvas.create_text(app.width*(5/10),app.height*(7.5/10),text = 'Collision!',font='Arial 20 bold')
    canvas.create_text(app.width/2,app.height*(9.8/10),text=f'Player Speed = {app.velocity//1}',font='Arial 20 bold')
    canvas.create_text(app.width/2,app.height*(9.5/10),text=f'Player Laps Completed = {app.playerLapCount}',font='Arial 20 bold')
######################
def raceTrackSectors(app):
    raceTrack = dict()
    raceTrack['sector0'] = (app.width*(1/10),app.height*(8/10),(app.width/2)-10,app.height*(9/10))
    raceTrack['sector1'] = (app.width*(1/10),app.height*(1/10),app.width*(2/10),app.height*(8/10))
    raceTrack['sector2'] = (app.width*(2/10),app.height*(1/10),app.width*(4/10),app.height*(2/10))
    raceTrack['sector3'] = (app.width*(3/10),app.height*(2/10),app.width*(4/10),app.height*(6/10))
    raceTrack['sector4'] = (app.width*(4/10),app.height*(5/10),app.width*(7/10),app.height*(6/10))
    raceTrack['sector5'] = (app.width*(6/10),app.height*(1/10),app.width*(7/10),app.height*(5/10))
    raceTrack['sector6'] = (app.width*(7/10),app.height*(1/10),app.width*(9/10),app.height*(2/10))
    raceTrack['sector7'] = (app.width*(8/10),app.height*(2/10),app.width*(9/10),app.height*(9/10))
    raceTrack['sector8'] = ((app.width/2)+10,app.height*(8/10),app.width*(8/10),app.height*(9/10))
    raceTrack['sector9'] = ((app.width/2)-10,app.height*(8/10),(app.width/2)+10,app.height*(9/10))
    return raceTrack

def getSeconds(app):
    if app.playerSecond % 60 == 0:
        app.playerMinute += 1
    if app.enemySecond % 60 == 0:
        app.enemyMinute += 1

def raceMode_timerFired(app):
    # print(app.playerIndex)
    if app.gameOver == False:
        if app.playerLapCount == 10 and app.playerTimerCount < app.enemyTimerCount:
            app.playerWin = True
            app.gameOver = True
        elif app.enemyLapCount == 2 and app.playerTimerCount > app.enemyTimerCount:
            app.enemyWin = True
            app.gameOver = True
        app.enemyTimerCount += app.timerDelay
        app.playerTimerCount += app.timerDelay 
        app.raceTrackFinal = raceTrack(raceTrackSectors(app),app.cx,app.cy,app.enemyCX,app.enemyCY,app.width,app.height)
        app.playerRaceCar = raceCar(app.cx,app.cy,app.width,app.height,app.playerRaceCarImages,app.playerIndex)
        app.enemyCar = enemyCar(app.enemyCX,app.enemyCY,app.width,app.height,app.enemyCarImages)
        movePlayerRaceCar(app)
        moveEnemyCar(app)
        enemyLapPassed(app)
        playerLapPassed(app)
        enemyCarTurn(app)
        playerCarTurn(app)
        if app.collisionTimer > 0:
            app.collisionTimer -= 50
        else:
            app.collision = False
        if app.accelTF == False: ######
            if app.collision == False:
                app.dx = 3
                app.dy = 3
            else:
                app.dxSlow = 1
                app.dySlow = 1
        if app.enemyAccelTF == False: ######
            if app.enemyCollision == False:
                app.enemyDX = 3
                app.enemyDY = 3
            else:
                app.enemyDXSlow = 1
                app.enemyDYSlow = 1
        if app.playerTimerCount % 1000 == 0:
            app.playerSecond += 1
        if app.enemyTimerCount % 1000 == 0:
            app.enemySecond += 1
        if app.enemyCollisionTimer > 0:
            app.enemyCollisionTimer -= 50
        else:
            app.enemyCollision = False

def enemyLapPassed(app):###
    if len(app.enemySectorsTracker)==10:
        app.enemyLapCount += 1
        app.enemyTurns = []
        for turn in range(8):
            app.enemyTurns.append(bool(random.randint(0,1)))
        app.enemySectorsTracker = set()
        app.enemyTimerCount = 0
        app.enemyMinute = 0
        app.enemySecond = 0

def movePlayerRaceCar(app):
    if app.raceTrackFinal.getSector() == 'sector0': #front straight
        app.accelTF = True
        app.playerSectorsTracker = set()
        app.playerSectorsTracker.add(0)
        if app.playerTurns[0] == False:
            app.playerIndex = 0
        if app.collision == True:
            app.dxSlow += app.accelSlow
            app.cx -= app.dxSlow
        else:
            app.dx += app.accel
            app.cx -= app.dx
    elif app.raceTrackFinal.getSector() == ('sector0','collisionLeft'): #miss turn 1
        app.collision = True
        app.collisionTimer = 3000
        if app.collision == True:
            app.cx = raceTrackSectors(app)['sector1'][0]+(raceTrackSectors(app)['sector1'][2]-raceTrackSectors(app)['sector1'][0])/2
            app.cy = raceTrackSectors(app)['sector1'][3] - 1
    elif app.raceTrackFinal.getSector() == 'sector1': #short straight after turn 1
        app.accelTF = True
        app.playerSectorsTracker.add(1)
        if app.playerTurns[1] == False:
            app.playerIndex = 0
        if app.collision == True:
            app.dySlow += app.accelSlow
            app.cy -= app.dySlow
        else:
            app.dy += app.accel
            app.cy -= app.dy
    elif app.raceTrackFinal.getSector() == ('sector1','collisionTop'): #miss turn 2
        app.collision = True
        app.collisionTimer = 3000
        if app.collision == True:
            app.cy = raceTrackSectors(app)['sector2'][1]+(raceTrackSectors(app)['sector2'][3]-raceTrackSectors(app)['sector2'][1])/2
            app.cx = raceTrackSectors(app)['sector2'][0] + 1
    elif app.raceTrackFinal.getSector() == 'sector2': #short straight after turn 2
        app.accelTF = True
        app.playerSectorsTracker.add(2)
        if app.playerTurns[2] == False:
            app.playerIndex = 0
        if app.collision == True:
            app.dxSlow += app.accelSlow
            app.cx += app.dxSlow
        else:
            app.dx += app.accel
            app.cx += app.dx
    elif app.raceTrackFinal.getSector() == ('sector2','collisionRight'): #miss turn 3
        app.collision = True
        app.collisionTimer = 3000
        if app.collision == True:
            app.cx = raceTrackSectors(app)['sector3'][0]+(raceTrackSectors(app)['sector3'][2]-raceTrackSectors(app)['sector3'][0])/2
            app.cy = raceTrackSectors(app)['sector3'][1] + 1
    elif app.raceTrackFinal.getSector() == 'sector3':#short straight after turn 3
        app.accelTF = True
        app.playerSectorsTracker.add(3)
        if app.playerTurns[3] == False:
            app.playerIndex = -1
        if app.collision == True:
            app.dySlow += app.accelSlow
            app.cy += app.dySlow
        else:
            app.dy += app.accel
            app.cy += app.dy
    elif app.raceTrackFinal.getSector() == ('sector3', 'collisionDown'): #miss turn 4
        app.collision = True
        app.collisionTimer = 3000
        if app.collision == True:
            app.cy = raceTrackSectors(app)['sector4'][1]+(raceTrackSectors(app)['sector4'][3]-raceTrackSectors(app)['sector4'][1])/2
            app.cx = raceTrackSectors(app)['sector4'][0] + 1
    elif app.raceTrackFinal.getSector() == 'sector4': #short straight after turn 4
        app.accelTF = True
        app.playerSectorsTracker.add(4)
        if app.playerTurns[4] == False:
            app.playerIndex = -1
        if app.collision == True:
            app.dxSlow += app.accelSlow
            app.cx += app.dxSlow
        else:
            app.dx += app.accel
            app.cx += app.dx
    elif app.raceTrackFinal.getSector() == ('sector4','collisionRight'): #miss turn 5
        app.collision = True
        app.collisionTimer = 3000
        if app.collision == True:
            app.cx = raceTrackSectors(app)['sector5'][0]+(raceTrackSectors(app)['sector5'][2]-raceTrackSectors(app)['sector5'][0])/2
            app.cy = raceTrackSectors(app)['sector5'][3] -1
    elif app.raceTrackFinal.getSector() == 'sector5': #short straight after turn 5
        app.accelTF = True
        app.playerSectorsTracker.add(5)
        if app.playerTurns[5] == False:
            app.playerIndex = 0
        if app.collision == True:
            app.dySlow += app.accelSlow
            app.cy -= app.dySlow
        else:
            app.dy += app.accel
            app.cy -= app.dy
    elif app.raceTrackFinal.getSector() == ('sector5','collisionTop'): #miss turn 6
        app.collision = True
        app.collisionTimer = 3000
        if app.collision == True:
            app.cy = raceTrackSectors(app)['sector6'][1]+(raceTrackSectors(app)['sector6'][3]-raceTrackSectors(app)['sector6'][1])/2
            app.cx = raceTrackSectors(app)['sector6'][0] +1
    elif app.raceTrackFinal.getSector() == 'sector6': #short straight after turn 6
        app.accelTF = True
        app.playerSectorsTracker.add(6)
        if app.playerTurns[6] == False:
            app.playerIndex = 0
        if app.collision == True:
            app.dxSlow += app.accelSlow
            app.cx += app.dxSlow
        else:
            app.dx += app.accel
            app.cx += app.dx
    elif app.raceTrackFinal.getSector() == ('sector6','collisionRight'):#miss turn 7
        app.collision = True
        app.collisionTimer = 3000
        if app.collision == True:        
            app.cx = raceTrackSectors(app)['sector7'][0]+(raceTrackSectors(app)['sector7'][2]-raceTrackSectors(app)['sector7'][0])/2
            app.cy = raceTrackSectors(app)['sector7'][1] +1
    elif app.raceTrackFinal.getSector() == 'sector7': #short straight after turn 7
        app.accelTF = True
        app.playerSectorsTracker.add(7)
        if app.playerTurns[7] == False:
            app.playerIndex = 0
        if app.collision == True:
            app.dySlow += app.accelSlow
            app.cy += app.dySlow
        else:
            app.dy += app.accel
            app.cy += app.dy
    elif app.raceTrackFinal.getSector() == ('sector7','collisionDown'):#miss last turn
        app.collision = True
        app.collisionTimer = 3000
        if app.collision == True:
            app.cy = raceTrackSectors(app)['sector8'][1]+(raceTrackSectors(app)['sector0'][3]-raceTrackSectors(app)['sector0'][1])/2
            app.cx = raceTrackSectors(app)['sector8'][2] -1
    elif app.raceTrackFinal.getSector() == 'sector8': #front straight
        app.accelTF = True
        app.playerSectorsTracker.add(8)
        app.playerIndex = 0
        if app.collision == True:
            app.dxSlow += app.accelSlow
            app.cx -= app.dxSlow
        else:
            app.dx += app.accel
            app.cx -= app.dx
    elif app.raceTrackFinal.getSector() == 'sector9': #front straight
        app.accelTF = True
        app.playerSectorsTracker.add(9)
        app.playerIndex = 0
        if app.collision == True:
            app.dxSlow += app.accelSlow
            app.cx -= app.dxSlow
        else:
            app.dx += app.accel
            app.cx -= app.dx

def moveEnemyCar(app):
    if app.raceTrackFinal.getEnemySector() == 'sector0': #front straight
        app.enemyAccelTF = True
        app.enemySectorsTracker = set()
        app.enemySectorsTracker.add(0)
        if app.enemyCollision == True:
            app.enemyDXSlow += app.accelSlow
            app.enemyCX -= app.enemyDXSlow
        else:
            app.enemyDX += app.accel
            app.enemyCX -= app.enemyDX
    elif app.raceTrackFinal.getEnemySector() == ('sector0','collisionLeft'): #miss turn 1
        app.enemyCollision = True
        app.enemyCollisionTimer = 3000
        if app.enemyCollision == True:
            app.enemyCX = raceTrackSectors(app)['sector1'][0]+(raceTrackSectors(app)['sector1'][2]-raceTrackSectors(app)['sector1'][0])/3
            app.enemyCY = raceTrackSectors(app)['sector1'][3] - 1
    elif app.raceTrackFinal.getEnemySector() == 'sector1': #short straight after turn 1
        app.enemyAccelTF = True
        app.enemySectorsTracker.add(1)
        if app.enemyCollision == True:
            app.enemyDYSlow += app.accelSlow
            app.enemyCY -= app.enemyDYSlow
        else:
            app.enemyDY += app.accel
            app.enemyCY -= app.enemyDY
    elif app.raceTrackFinal.getEnemySector() == ('sector1','collisionTop'): #miss turn 2
        app.enemyCollision = True
        app.enemyCollisionTimer = 3000
        if app.enemyCollision == True:
            app.enemyCY = raceTrackSectors(app)['sector2'][1]+(raceTrackSectors(app)['sector2'][3]-raceTrackSectors(app)['sector2'][1])/3
            app.enemyCX = raceTrackSectors(app)['sector2'][0] + 1
    elif app.raceTrackFinal.getEnemySector() == 'sector2': #short straight after turn 2
        app.enemyAccelTF = True
        app.enemySectorsTracker.add(2)
        if app.enemyCollision == True:
            app.enemyDXSlow += app.accelSlow
            app.enemyCX += app.enemyDXSlow
        else:
            app.enemyDX += app.accel
            app.enemyCX += app.enemyDX
    elif app.raceTrackFinal.getEnemySector() == ('sector2','collisionRight'): #miss turn 3
        app.enemyCollision = True
        app.enemyCollisionTimer = 3000
        if app.enemyCollision == True:
            app.enemyCX = raceTrackSectors(app)['sector3'][0]+(raceTrackSectors(app)['sector3'][2]-raceTrackSectors(app)['sector3'][0])/3
            app.enemyCY = raceTrackSectors(app)['sector3'][1] + 1
    elif app.raceTrackFinal.getEnemySector() == 'sector3':#short straight after turn 3
        app.enemyAccelTF = True
        app.enemySectorsTracker.add(3)
        if app.enemyCollision == True:
            app.enemyDYSlow += app.accelSlow
            app.enemyCY += app.enemyDYSlow
        else:
            app.enemyDY += app.accel
            app.enemyCY += app.enemyDY
    elif app.raceTrackFinal.getEnemySector() == ('sector3', 'collisionDown'): #miss turn 4
        app.enemyCollision = True
        app.enemyCollisionTimer = 3000
        if app.enemyCollision == True:
            app.enemyCY = raceTrackSectors(app)['sector4'][1]+(raceTrackSectors(app)['sector4'][3]-raceTrackSectors(app)['sector4'][1])/3
            app.enemyCX = raceTrackSectors(app)['sector4'][0] + 1
    elif app.raceTrackFinal.getEnemySector() == 'sector4': #short straight after turn 4
        app.enemyAccelTF = True
        app.enemySectorsTracker.add(4)
        if app.enemyCollision == True:
            app.enemyDXSlow += app.accelSlow
            app.enemyCX += app.enemyDXSlow
        else:
            app.enemyDX += app.accel
            app.enemyCX += app.enemyDX
    elif app.raceTrackFinal.getEnemySector() == ('sector4','collisionRight'): #miss turn 5
        app.enemyCollision = True
        app.enemyCollisionTimer = 3000
        if app.enemyCollision == True:
            app.enemyCX = raceTrackSectors(app)['sector5'][0]+(raceTrackSectors(app)['sector5'][2]-raceTrackSectors(app)['sector5'][0])/3
            app.enemyCY = raceTrackSectors(app)['sector5'][3] -1
    elif app.raceTrackFinal.getEnemySector() == 'sector5': #short straight after turn 5
        app.enemyAccelTF = True
        app.enemySectorsTracker.add(5)
        if app.enemyCollision == True:
            app.enemyDYSlow += app.accelSlow
            app.enemyCY -= app.enemyDYSlow
        else:
            app.enemyDY += app.accel
            app.enemyCY -= app.enemyDY
    elif app.raceTrackFinal.getEnemySector() == ('sector5','collisionTop'): #miss turn 6
        app.enemyCollision = True
        app.enemyCollisionTimer = 3000
        if app.enemyCollision == True:
            app.enemyCY = raceTrackSectors(app)['sector6'][1]+(raceTrackSectors(app)['sector6'][3]-raceTrackSectors(app)['sector6'][1])/3
            app.enemyCX = raceTrackSectors(app)['sector6'][0] +1
    elif app.raceTrackFinal.getEnemySector() == 'sector6': #short straight after turn 6
        app.enemyAccelTF = True
        app.enemySectorsTracker.add(6)
        if app.enemyCollision == True:
            app.enemyDXSlow += app.accelSlow
            app.enemyCX += app.enemyDXSlow
        else:
            app.enemyDX += app.accel
            app.enemyCX += app.enemyDX
    elif app.raceTrackFinal.getEnemySector() == ('sector6','collisionRight'):#miss turn 7
        app.enemyCollision = True
        app.enemyCollisionTimer = 3000
        if app.enemyCollision == True:        
            app.enemyCX = raceTrackSectors(app)['sector7'][0]+(raceTrackSectors(app)['sector7'][2]-raceTrackSectors(app)['sector7'][0])/3
            app.enemyCY = raceTrackSectors(app)['sector7'][1] +1
    elif app.raceTrackFinal.getEnemySector() == 'sector7': #short straight after turn 7
        app.enemyAccelTF = True
        app.enemySectorsTracker.add(7)
        if app.enemyCollision == True:
            app.enemyDYSlow += app.accelSlow
            app.enemyCY += app.enemyDYSlow
        else:
            app.enemyDY += app.accel
            app.enemyCY += app.enemyDY
    elif app.raceTrackFinal.getEnemySector() == ('sector7','collisionDown'):#miss last turn
        app.enemyCollision = True
        app.enemyCollisionTimer = 3000
        if app.enemyCollision == True:
            app.enemyCY = raceTrackSectors(app)['sector8'][1]+(raceTrackSectors(app)['sector8'][3]-raceTrackSectors(app)['sector8'][1])/3
            app.enemyCX = raceTrackSectors(app)['sector8'][2] -1
    elif app.raceTrackFinal.getEnemySector() == 'sector8': #front straight
        app.enemyAccelTF = True
        app.enemySectorsTracker.add(8)
        if app.enemyCollision == True:
            app.enemyDXSlow += app.accelSlow
            app.enemyCX -= app.enemyDXSlow
        else:
            app.enemyDX += app.accel
            app.enemyCX -= app.enemyDX
    elif app.raceTrackFinal.getEnemySector() == 'sector9': #front straight
        app.enemyAccelTF = True
        app.enemySectorsTracker.add(9)
        if app.enemyCollision == True:
            app.enemyDXSlow += app.accelSlow
            app.enemyCX -= app.enemyDXSlow
        else:
            app.enemyDX += app.accel
            app.enemyCX -= app.enemyDX

def raceMode_keyPressed(app,event):
    if event.key == 'Space':
        if app.raceTrackFinal.T1TurningPoint() == True:
            app.playerTurns[0] = True
        elif app.raceTrackFinal.T2TurningPoint() == True:
            app.playerTurns[1] = True
        elif app.raceTrackFinal.T3TurningPoint() == True:
            app.playerTurns[2] = True
        elif app.raceTrackFinal.T4TurningPoint() == True:
            app.playerTurns[3] = True
        elif app.raceTrackFinal.T5TurningPoint() == True:
            app.playerTurns[4] = True
        elif app.raceTrackFinal.T6TurningPoint() == True:
            app.playerTurns[5] = True
        elif app.raceTrackFinal.T7TurningPoint() == True:
            app.playerTurns[6] = True
        elif app.raceTrackFinal.T8TurningPoint() == True:
            app.playerTurns[7] = True
    elif event.key == 'r':
        app.mode = 'splashScreenMode'
        appStarted(app)

def playerCarTurn(app):
    if app.raceTrackFinal.playerT1() == True: #turn 1 (right up)
        app.accelTF = False 
        if app.playerTurns[0] == True:
            if app.playerIndex < 5:
                app.playerIndex += 1
            app.cx += app.r * math.cos(app.turnAngle)
            app.cy -= app.r * math.sin(app.turnAngle)
    elif app.raceTrackFinal.playerT2() == True: #turn 2 (right across)
        app.accelTF = False 
        if app.playerTurns[1] == True:
            if app.playerIndex < 5:
                app.playerIndex += 1
            app.cy -= app.r * math.cos(app.turnAngle)
            app.cx += app.r * math.sin(app.turnAngle)
    elif app.raceTrackFinal.playerT3() == True: #turn 3 (right down)
        app.accelTF = False 
        if app.playerTurns[2] == True:
            if app.playerIndex < 5:
                app.playerIndex += 1
            app.cx -= app.r * math.cos(app.turnAngle)
            app.cy += app.r * math.sin(app.turnAngle)
    elif app.raceTrackFinal.playerT4() == True: #turn 4 (left across)
        app.accelTF = False 
        if app.playerTurns[3] == True:
            if app.playerIndex > -6:
                app.playerIndex -= 1
            app.cy += app.r * math.cos(app.turnAngle)
            app.cx += app.r * math.sin(app.turnAngle)
    elif app.raceTrackFinal.playerT5() == True: #turn 5 (left up)
        app.accelTF = False 
        if app.playerTurns[4] == True:
            if app.playerIndex > -6:
                app.playerIndex -= 1
            app.cx -= app.r * math.cos(app.turnAngle)
            app.cy -= app.r * math.sin(app.turnAngle)
    elif app.raceTrackFinal.playerT6() == True: #turn 6 (right across)
        app.accelTF = False 
        if app.playerTurns[5] == True:
            if app.playerIndex < 5:
                app.playerIndex += 1
            app.cy -= app.r * math.cos(app.turnAngle)
            app.cx += app.r * math.sin(app.turnAngle)
    elif app.raceTrackFinal.playerT7() == True: #turn 7 (right down)
        app.accelTF = False 
        if app.playerTurns[6] == True:
            if app.playerIndex < 5:
                app.playerIndex += 1
            app.cx -= app.r * math.cos(app.turnAngle)
            app.cy += app.r * math.sin(app.turnAngle)
    elif app.raceTrackFinal.playerT8() == True: # last turn (left across)
        app.accelTF = False 
        if app.playerTurns[7] == True:
            if app.playerIndex < 5:
                app.playerIndex += 1
            app.cy -= app.r * math.cos(app.turnAngle)
            app.cx -= app.r * math.sin(app.turnAngle)

def enemyCarTurn(app):
    if app.raceTrackFinal.enemyT1() == True: #turn 1 (right up)
        app.enemyAccelTF = False 
        if app.enemyTurns[0] == True:
            app.enemyCX += app.r * math.cos(app.turnAngle)
            app.enemyCY -= app.r * math.sin(app.turnAngle)
    elif app.raceTrackFinal.enemyT2() == True: #turn 2 (right across)
        app.enemyAccelTF = False 
        if app.enemyTurns[1] == True:
            app.enemyCY -= app.r * math.cos(app.turnAngle)
            app.enemyCX += app.r * math.sin(app.turnAngle)
    elif app.raceTrackFinal.enemyT3() == True: #turn 3 (right down)
        app.enemyAccelTF = False 
        if app.enemyTurns[2] == True:
            app.enemyCX -= app.r * math.cos(app.turnAngle)
            app.enemyCY += app.r * math.sin(app.turnAngle)
    elif app.raceTrackFinal.enemyT4() == True: #turn 4 (left across)
        app.enemyAccelTF = False 
        if app.enemyTurns[3] == True:
            app.enemyCY += app.r * math.cos(app.turnAngle)
            app.enemyCX += app.r * math.sin(app.turnAngle)
    elif app.raceTrackFinal.enemyT5() == True: #turn 5 (left up)
        app.enemyAccelTF = False 
        if app.enemyTurns[4] == True:
            app.enemyCX -= app.r * math.cos(app.turnAngle)
            app.enemyCY -= app.r * math.sin(app.turnAngle)
    elif app.raceTrackFinal.enemyT6() == True: #turn 6 (right across)
        app.enemyAccelTF = False 
        if app.enemyTurns[5] == True:
            app.enemyCY -= app.r * math.cos(app.turnAngle)
            app.enemyCX += app.r * math.sin(app.turnAngle)
    elif app.raceTrackFinal.enemyT7() == True: #turn 7 (right down)
        app.enemyAccelTF = False 
        if app.enemyTurns[6] == True:
            app.enemyCX -= app.r * math.cos(app.turnAngle)
            app.enemyCY += app.r * math.sin(app.turnAngle)
    elif app.raceTrackFinal.enemyT8() == True: # last turn (left across)
        app.enemyAccelTF = False 
        if app.enemyTurns[7] == True:
            app.enemyCY -= app.r * math.cos(app.turnAngle)
            app.enemyCX -= app.r * math.sin(app.turnAngle)

def drawRaceTrack(app,canvas):
    app.raceTrackFinal.drawSectors(canvas)
    app.raceTrackFinal.drawStartLine(canvas)
    app.raceTrackFinal.drawTurningPoints(canvas)

def raceMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill='green')
    canvas.create_text(app.width*(5/10),app.height*(9.6/10),text=f'Player Laptime = {app.playerMinute} minute {app.playerSecond} seconds {app.playerTimerCount%1000//100} milliseconds',font='Arial 15 bold')
    canvas.create_text(app.width*(5/10),app.height*(9.8/10),text=f'Enemy Laptime = {app.enemyMinute} minute {app.enemySecond} seconds {app.enemyTimerCount%1000//100} milliseconds',font='Arial 15 bold')
    drawRaceTrack(app,canvas)
    canvas.create_text(app.width*(5/10),app.height*(6.5/10),text=f'Player Speed = {int(((app.dx**2)+(app.dy**2))**0.5//1)}',font='Arial 15 bold')
    canvas.create_text(app.width*(5/10),app.height*(6.2/10),text=f'Enemy Speed = {int(((app.enemyDX**2)+(app.enemyDY**2))**0.5//1)}',font='Arial 15 bold')
    if app.collision == True:
        canvas.create_text(app.width*(5/10),app.height*(7.5/10),text = 'Player Collision!',font='Arial 20 bold')
    if app.enemyCollision == True:
        canvas.create_text(app.width*(5/10),app.height*(7.2/10),text = 'Enemy Collision!',font='Arial 20 bold')
    canvas.create_text(app.width*(5/10),app.height*(9.2/10),text=f'Enemy Laps Completed = {app.enemyLapCount}',font='Arial 15 bold')
    canvas.create_text(app.width*(5/10),app.height*(9.4/10),text=f'Player Laps Completed = {app.playerLapCount}',font='Arial 15 bold')
    if app.raceTrackFinal.getSector() == 'sector0':
        app.playerRaceCar.drawSector0(canvas)
    if app.raceTrackFinal.playerT1() == True: ###
        if app.playerTurns[0] == True:
            app.playerRaceCar.drawT1(canvas)
    if app.raceTrackFinal.getSector() == 'sector1':
        app.playerRaceCar.drawSector1(canvas)
    if app.raceTrackFinal.playerT2() == True: ###
        if app.playerTurns[1] == True:
            app.playerRaceCar.drawT2(canvas)
    if app.raceTrackFinal.getSector() == 'sector2':
        app.playerRaceCar.drawSector2(canvas)
    if app.raceTrackFinal.playerT3() == True: ###
        if app.playerTurns[2] == True:
            app.playerRaceCar.drawT3(canvas)
    if app.raceTrackFinal.getSector() == 'sector3':
        app.playerRaceCar.drawSector3(canvas)
    if app.raceTrackFinal.playerT4() == True: ###
        if app.playerTurns[3] == True:
            app.playerRaceCar.drawT4(canvas)
    if app.raceTrackFinal.getSector() == 'sector4':
        app.playerRaceCar.drawSector4(canvas)
    if app.raceTrackFinal.playerT5() == True: ###
        if app.playerTurns[4] == True:
            app.playerRaceCar.drawT5(canvas)
    if app.raceTrackFinal.getSector() == 'sector5':
        app.playerRaceCar.drawSector5(canvas)
    if app.raceTrackFinal.playerT6() == True: ###
        if app.playerTurns[5] == True:
            app.playerRaceCar.drawT6(canvas)
    if app.raceTrackFinal.getSector() == 'sector6':
        app.playerRaceCar.drawSector6(canvas)
    if app.raceTrackFinal.playerT7() == True: ###
        if app.playerTurns[6] == True:
            app.playerRaceCar.drawT7(canvas)
    if app.raceTrackFinal.getSector() == 'sector7':
        app.playerRaceCar.drawSector7(canvas)
    if app.raceTrackFinal.playerT8() == True: ###
        if app.playerTurns[7] == True:
            app.playerRaceCar.drawT8(canvas)
    if app.raceTrackFinal.getSector() == 'sector8':
        app.playerRaceCar.drawSector8(canvas)
    if app.raceTrackFinal.getSector() == 'sector9':
        app.playerRaceCar.drawSector9(canvas)
    ########
    if app.raceTrackFinal.getEnemySector() == 'sector0':
        app.enemyCar.drawEnemySector0(canvas)
    elif app.raceTrackFinal.getEnemySector() == 'sector1':
        app.enemyCar.drawEnemySector1(canvas)
    elif app.raceTrackFinal.getEnemySector() == 'sector2':
        app.enemyCar.drawEnemySector2(canvas)
    elif app.raceTrackFinal.getEnemySector() == 'sector3':
        app.enemyCar.drawEnemySector3(canvas)
    elif app.raceTrackFinal.getEnemySector() == 'sector4':
        app.enemyCar.drawEnemySector4(canvas)
    elif app.raceTrackFinal.getEnemySector() == 'sector5':
        app.enemyCar.drawEnemySector5(canvas)
    elif app.raceTrackFinal.getEnemySector() == 'sector6':
        app.enemyCar.drawEnemySector6(canvas)
    elif app.raceTrackFinal.getEnemySector() == 'sector7':
        app.enemyCar.drawEnemySector7(canvas)
    elif app.raceTrackFinal.getEnemySector() == 'sector8':
        app.enemyCar.drawEnemySector8(canvas)
    elif app.raceTrackFinal.getEnemySector() == 'sector9':
        app.enemyCar.drawEnemySector9(canvas)
    
    if app.playerWin == True:
        canvas.create_image(app.width*(5/10),app.height*(5/10),image=ImageTk.PhotoImage(app.victoryImage))
        canvas.create_rectangle(app.width*(3/10),app.height*(4.5/10),app.width*(7/10),app.height*(5.5/10),fill='white')
        canvas.create_text(app.width*(5/10),app.height*(5/10),text='Player Wins!',font='Arial 50 bold')
    elif app.enemyWin == True:
        canvas.create_image(app.width*(5/10),app.height*(5/10),image=ImageTk.PhotoImage(app.victoryImage))
        canvas.create_rectangle(app.width*(3/10),app.height*(4.5/10),app.width*(7/10),app.height*(5.5/10),fill='white')
        canvas.create_text(app.width*(5/10),app.height*(5/10),text='Enemy Wins!',font='Arial 50 bold')
    
def playGame():
    runApp(width=800,height=800)
def main():
    playGame()
if __name__ == '__main__':
    main()





                                   
