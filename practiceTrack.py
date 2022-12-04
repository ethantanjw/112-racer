from main5 import *
class practiceTrack(object):
    def __init__(self,sectors,carX,carY,cx,cy,width,height):
        self.sectors = sectors
        self.cx = cx
        self.cy = cy
        self.carX = carX
        self.carY = carY
        self.width = width
        self.height = height

    def drawSectors(self,canvas, scrollX, scrollY):
        for sector in self.sectors:
            canvas.create_rectangle(self.sectors[sector][0]-scrollX,
                                    self.sectors[sector][1]-scrollY,
                                    self.sectors[sector][2]-scrollX,
                                    self.sectors[sector][3]-scrollY,
                                    outline='grey',fill='grey')

    def drawTurningPoints(self,canvas):
        canvas.create_rectangle(self.cx-self.width*(3/10),self.cy-self.height*(0.5/10),self.cx-self.width*(2.5/10),self.cy+self.height*(0.5/10),fill='red')
        canvas.create_rectangle(self.cx-self.width*(4/10),self.cy-self.height*(6/10),self.cx-self.width*(3/10),self.cy-self.height*(6.5/10),fill='red')
        canvas.create_rectangle(self.cx-self.width*(2.5/10),self.cy-self.height*(7.5/10),self.cx-self.width*(2/10),self.cy-self.height*(6.5/10),fill='red')
        canvas.create_rectangle(self.cx-self.width*(2/10),self.cy-self.height*(4/10),self.cx-self.width*(1/10),self.cy-self.height*(3.5/10),fill='red')
        canvas.create_rectangle(self.cx+self.width*(0.5/10),self.cy-self.height*(3.5/10),self.cx+self.width*(1/10),self.cy-self.height*(2.5/10),fill='red')        
        canvas.create_rectangle(self.cx+self.width*(1/10),self.cy-self.height*(6/10),self.cx+self.width*(2/10),self.cy-self.height*(6.5/10),fill='red')
        canvas.create_rectangle(self.cx+self.width*(2.5/10),self.cy-self.height*(7.5/10),self.cx+self.width*(3/10),self.cy-self.height*(6.5/10),fill='red')
        canvas.create_rectangle(self.cx+self.width*(3/10),self.cy-self.height*(1/10),self.cx+self.width*(4/10),self.cy-self.height*(0.5/10),fill='red')

    def getSector(self):
        for num in self.sectors:
            # print(self.cx,self.cy,num)
            if self.sectors[num][0]<self.carX<self.sectors[num][2] and self.sectors[num][1]<self.carY<=self.sectors[num][3]:
                return num 
            elif (num=='sector0') and self.sectors[num][0]>self.carX and self.sectors[num][1]<self.carY<self.sectors[num][3]:
                return (num,'collisionLeft')
            elif (num=='sector1'or num=='sector5')and self.sectors[num][0]<self.carX<self.sectors[num][2]and self.sectors[num][1]>=self.carY:
                return (num,'collisionTop')
            elif (num=='sector2' or num=='sector6' or num=='sector4')and (self.sectors[num][2]<=self.carX<self.sectors[num][2]+self.width*(1/10))and (self.sectors[num][1]<self.carY<self.sectors[num][3]):
                return (num,'collisionRight')
            elif (num=='sector3' or num=='sector7') and (self.sectors[num][0]<self.carX<self.sectors[num][2]) and (self.sectors[num][3]+self.width*(1/10)> self.carY >= self.sectors[num][3]):
                return (num,'collisionDown')
                
    def drawStartLine(self,canvas):
        canvas.create_rectangle(self.cx-10,self.cy-self.height*(0.5/10),self.cx+10,self.cy+self.height*(0.5/10),outline = 'white',fill='white')

    def playerT1(self):
        if self.cx - self.width*(4/10)<= self.carX <= self.cx - self.width*(3.5/10)and self.carY >= self.cy-self.height*(0.5/10):
            return True

    def playerT2(self):
        if self.cx - self.width*(4/10)<= self.carX <= self.cx - self.width*(3/10) and self.cy - self.height*(7.5/10)<= self.carY<= self.cy - self.height*(7/10):
            return True

    def playerT3(self):
        if self.cx - self.width*(1.5/10)<self.carX<self.cx-self.width*(1/10)and self.cy-self.height*(7.5/10)<self.carY<self.cy-self.height*(6.5/10):
            return True

    def playerT4(self):
        if self.cx-self.width*(2/10)<self.carX<self.cx-self.width*(1/10) and self.cy-self.height*(3/10)<self.carY<self.cy-self.height*(2.5/10):
            return True

    def playerT5(self):
        if self.cx+self.width*(1.5/10)<self.carX<self.cx+self.width*(2/10) and self.cy-self.height*(3.5/10)<self.carY<self.cy-self.height*(2.5/10):
            return True

    def playerT6(self):
        if self.cx+self.width*(1/10)<self.carX<self.cx+self.width*(2/10) and self.cy-self.height*(7.5/10)<self.carY<self.cy-self.height*(7/10):
            return True
    
    def playerT7(self):
        if self.cx+self.width*(3.5/10)<self.carX<self.cx+self.width*(4/10) and self.cy-self.height*(7.5/10)<self.carY<self.cy-self.height*(6.5/10):
            return True

    def playerT8(self):
        if self.cx+self.width*(3/10)<self.carX<self.cx+self.width*(4/10) and self.cy<self.carY<self.cy+self.height*(0.5/10):
            return True
########
    def T1TurningPoint(self):
        if self.cx-self.width*(3/10)<=self.carX<=self.cx-self.width*(2.5/10) and self.cy-self.height*(0.5/10)<=self.carY<=self.cy+self.height*(0.5/10):
            return True
    
    def T2TurningPoint(self):
        if self.cx-self.width*(4/10)<=self.carX<=self.cx-self.width*(3/10) and self.cy-self.height*(6.5/10)<=self.carY<=self.cy-self.height*(6/10):     
            return True   

    def T3TurningPoint(self):
        if self.cx-self.width*(2.5/10)<=self.carX<=self.cx-self.width*(2/10) and self.cy-self.height*(7.5/10)<=self.carY<=self.cy-self.height*(6.5/10):
            return True

    def T4TurningPoint(self):
        if self.cx-self.width*(2/10)<=self.carX<=self.cx-self.width*(1/10) and self.cy-self.height*(4/10)<=self.carY<=self.cy-self.height*(3.5/10):
            return True

    def T5TurningPoint (self):
        if self.cx+self.width*(0.5/10)<=self.carX<=self.cx+self.width*(1/10) and self.cy-self.height*(3.5/10)<=self.carY<=self.cy-self.height*(2.5/10):
            return True

    def T6TurningPoint(self):
        if self.cx+self.width*(1/10)<=self.carX<=self.cx+self.width*(2/10) and self.cy-self.height*(6.5/10)<=self.carY<=self.cy-self.height*(6/10):
            return True

    def T7TurningPoint(self):
        if self.cx+self.width*(2.5/10)<=self.carX<=self.cx+self.width*(3/10) and self.cy-self.height*(7.5/10)<=self.carY<=self.cy-self.height*(6.5/10):
            return True

    def T8TurningPoint(self):
        if self.cx+self.width*(3/10)<=self.carX<=self.cx+self.width*(4/10) and self.cy-self.height*(1/10)<=self.carY<=self.cy-self.height*(0.5/10):
            return True
    
    



    
