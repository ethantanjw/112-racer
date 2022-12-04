from main5 import *
class practiceCar(object):
    def __init__(self,carX,carY,width,height,images,index):
        self.carX = carX
        self.carY = carY
        self.width = width
        self.height = height
        self.images = images
        self.index = index

    def drawSector0(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[0][0])) 
    
    def drawT1(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[0][self.index])) 

    def drawSector1(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[1][0])) 
    
    def drawT2(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[1][self.index])) 

    def drawSector2(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[2][0])) 
    
    def drawT3(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[2][self.index])) 

    def drawSector3(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[3][0])) 

    def drawT4(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[2][self.index])) ######

    def drawSector4(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[2][0])) 
    
    def drawT5(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[1][self.index]))

    def drawSector5(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[1][0])) 

    def drawT6(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[1][self.index]))

    def drawSector6(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[2][0])) 

    def drawT7(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[2][self.index]))

    def drawSector7(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[3][0])) 
    
    def drawT8(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[3][self.index]))

    def drawSector8(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[0][0])) 

    def drawSector9(self,canvas):
        canvas.create_image(self.carX,self.carY,image=ImageTk.PhotoImage(self.images[0][0])) 