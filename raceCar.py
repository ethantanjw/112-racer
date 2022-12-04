from main5 import *
class raceCar(object):
    def __init__(self,cx,cy,width,height,images,playerIndex):
        self.cx = cx
        self.cy = cy
        self.width = width
        self.height = height
        self.images = images
        self.playerIndex = playerIndex

    def drawSector0(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[0][0])) 

    def drawT1(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[0][self.playerIndex])) 

    def drawSector1(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[1][0])) 

    def drawT2(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[1][self.playerIndex])) 

    def drawSector2(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[2][0])) 

    def drawT3(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[2][self.playerIndex])) 

    def drawSector3(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[3][0])) 

    def drawT4(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[2][self.playerIndex]))

    def drawSector4(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[2][0])) 
    
    def drawT5(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[1][self.playerIndex]))

    def drawSector5(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[1][0])) 
    
    def drawT6(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[1][self.playerIndex]))

    def drawSector6(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[2][0])) 
    
    def drawT7(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[2][self.playerIndex]))

    def drawSector7(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[3][0])) 

    def drawT8(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[3][self.playerIndex]))

    def drawSector8(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[0][0])) 

    def drawSector9(self,canvas):
        canvas.create_image(self.cx,self.cy,image=ImageTk.PhotoImage(self.images[0][0])) 

class enemyCar(object):
    def __init__(self,enemyCX,enemyCY,width,height,enemyImages):
        self.enemyCX = enemyCX
        self.enemyCY = enemyCY
        self.width = width
        self.height = height
        self.enemyImages = enemyImages

    def drawEnemySector0(self,canvas):
        canvas.create_image(self.enemyCX,self.enemyCY,image=ImageTk.PhotoImage(self.enemyImages[0])) 

    def drawEnemySector1(self,canvas):
        canvas.create_image(self.enemyCX,self.enemyCY,image=ImageTk.PhotoImage(self.enemyImages[2])) 

    def drawEnemySector2(self,canvas):
        canvas.create_image(self.enemyCX,self.enemyCY,image=ImageTk.PhotoImage(self.enemyImages[4])) 

    def drawEnemySector3(self,canvas):
        canvas.create_image(self.enemyCX,self.enemyCY,image=ImageTk.PhotoImage(self.enemyImages[6])) 

    def drawEnemySector4(self,canvas):
        canvas.create_image(self.enemyCX,self.enemyCY,image=ImageTk.PhotoImage(self.enemyImages[4])) 

    def drawEnemySector5(self,canvas):
        canvas.create_image(self.enemyCX,self.enemyCY,image=ImageTk.PhotoImage(self.enemyImages[2])) 

    def drawEnemySector6(self,canvas):
        canvas.create_image(self.enemyCX,self.enemyCY,image=ImageTk.PhotoImage(self.enemyImages[4])) 

    def drawEnemySector7(self,canvas):
        canvas.create_image(self.enemyCX,self.enemyCY,image=ImageTk.PhotoImage(self.enemyImages[6])) 

    def drawEnemySector8(self,canvas):
        canvas.create_image(self.enemyCX,self.enemyCY,image=ImageTk.PhotoImage(self.enemyImages[0])) 

    def drawEnemySector9(self,canvas):
        canvas.create_image(self.enemyCX,self.enemyCY,image=ImageTk.PhotoImage(self.enemyImages[0])) 