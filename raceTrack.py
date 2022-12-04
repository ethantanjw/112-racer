from main5 import *
class raceTrack(object):
    def __init__(self,sectors,cx,cy,enemyCX,enemyCY,width,height):
        self.sectors = sectors
        self.cx = cx
        self.cy = cy
        self.enemyCX = enemyCX
        self.enemyCY = enemyCY
        self.width = width
        self.height = height

    def drawSectors(self,canvas):
        for sector in self.sectors:
            canvas.create_rectangle(self.sectors[sector][0],self.sectors[sector][1],self.sectors[sector][2],self.sectors[sector][3],outline='grey',fill='grey')

    def drawTurningPoints(self,canvas):
        canvas.create_rectangle(self.width*(2/10),self.height*(8/10),self.width*(2.5/10),self.height*(9/10),fill='red')
        canvas.create_rectangle(self.width*(1/10),self.height*(2/10),self.width*(2/10),self.height*(2.5/10),fill='red')
        canvas.create_rectangle(self.width*(2.5/10),self.height*(1/10),self.width*(3/10),self.height*(2/10),fill='red')
        canvas.create_rectangle(self.width*(3/10),self.height*(4.5/10),self.width*(4/10),self.height*(5/10),fill='red')
        canvas.create_rectangle(self.width*(5.5/10),self.height*(5/10),self.width*(6/10),self.height*(6/10),fill='red')        
        canvas.create_rectangle(self.width*(6/10),self.height*(2/10),self.width*(7/10),self.height*(2.5/10),fill='red')
        canvas.create_rectangle(self.width*(7.5/10),self.height*(1/10),self.width*(8/10),self.height*(2/10),fill='red')
        canvas.create_rectangle(self.width*(8/10),self.height*(7.5/10),self.width*(9/10),self.height*(8/10),fill='red')

    def getSector(self):
        for num in self.sectors:
            if self.sectors[num][0]<=self.cx<=self.sectors[num][2] and self.sectors[num][1]<=self.cy<=self.sectors[num][3]:
                return num 
            elif (num=='sector0') and self.sectors[num][0]>=self.cx and self.sectors[num][1]<self.cy<self.sectors[num][3]:
                return (num,'collisionLeft')
            elif (num=='sector1'or num=='sector5')and self.sectors[num][0]<self.cx<self.sectors[num][2]and self.sectors[num][1]>=self.cy:
                return (num,'collisionTop')
            elif (num=='sector2' or num=='sector6' or num=='sector4')and (self.sectors[num][2]<=self.cx<self.sectors[num][2]+self.width*(1/10))and (self.sectors[num][1]<self.cy<self.sectors[num][3]):
                return (num,'collisionRight')
            elif (num=='sector3' or num=='sector7') and (self.sectors[num][0]<self.cx<self.sectors[num][2]) and (self.sectors[num][3]+self.width*(1/10)> self.cy >= self.sectors[num][3]):
                return (num,'collisionDown')

    def getEnemySector(self):
        for num in self.sectors:
            if self.sectors[num][0]<=self.enemyCX<=self.sectors[num][2] and self.sectors[num][1]<=self.enemyCY<=self.sectors[num][3]:
                return num 
            elif (num=='sector0') and self.sectors[num][0]>=self.enemyCX and self.sectors[num][1]<self.enemyCY<self.sectors[num][3]:
                return (num,'collisionLeft')
            elif (num=='sector1'or num=='sector5')and self.sectors[num][0]<self.enemyCX<self.sectors[num][2]and self.sectors[num][1]>=self.enemyCY:
                return (num,'collisionTop')
            elif (num=='sector2' or num=='sector6' or num=='sector4')and (self.sectors[num][2]<=self.enemyCX<self.sectors[num][2]+self.width*(1/10))and (self.sectors[num][1]<self.enemyCY<self.sectors[num][3]):
                return (num,'collisionRight')
            elif (num=='sector3' or num=='sector7') and (self.sectors[num][0]<self.enemyCX<self.sectors[num][2]) and (self.sectors[num][3]+self.width*(1/10)> self.enemyCY >= self.sectors[num][3]):
                return (num,'collisionDown')
                
    def drawStartLine(self,canvas):
        canvas.create_rectangle((self.width/2)-10,self.sectors['sector0'][1],((self.width/2)+10,self.sectors['sector0'][3]),outline = 'white',fill='white')

    def T1TurningPoint(self):
        if self.width*(2/10)<= self.cx <= self.width*(2.5/10) and self.cy>=self.height*(8/10):
            return True

    def T2TurningPoint(self):
        if self.width*(1/10)<=self.cx<=self.width*(2/10) and self.height*(2/10)<=self.cy <= self.height*(2.5/10):
            return True

    def T3TurningPoint(self):
        if self.width*(2.5/10)<=self.cx<=self.width*(3/10) and self.height*(1/10)<=self.cy<=self.height*(2/10):
            return True

    def T4TurningPoint(self):
        if self.width*(3/10)<=self.cx<=self.width*(4/10) and self.height*(4.5/10)<=self.cy<=self.height*(5/10):
            return True

    def T5TurningPoint(self):
        if self.width*(5.5/10)<=self.cx<=self.width*(6/10) and self.height*(5/10)<=self.cy<=self.height*(6/10):
            return True

    def T6TurningPoint(self):
        if self.width*(6/10)<=self.cx<=self.width*(7/10) and self.height*(2/10)<=self.cy <= self.height*(2.5/10):
            return True
    
    def T7TurningPoint(self):
        if self.width*(7.5/10)<=self.cx<=self.width*(8/10) and self.height*(1/10)<=self.cy<=self.height*(2/10):
            return True

    def T8TurningPoint(self):
        if self.width*(8/10)<=self.cx<=self.width*(9/10) and self.height*(7.5/10)<=self.cy<=self.height*(8/10):
            return True

    def playerT1(self):
        if self.cx <= self.width*(1.5/10)and self.cy>self.height*(8/10):
            return True
    
    def playerT2(self):
        if self.cx <= self.width*(2/10) and self.cy<self.height*(1.5/10):     
            return True   

    def playerT3(self):
        if self.width*(3.5/10)<self.cx<self.width*(4/10)and self.cy<self.height*(2/10):
            return True

    def playerT4(self):
        if self.width*(3/10)<self.cx<=self.width*(4/10)and self.height*(5.5/10)<self.cy<self.height*(6/10):
            return True

    def playerT5 (self):
        if self.width*(6.5/10)<self.cx<self.width*(7/10)and self.height*(5/10)<self.cy<self.height*(6/10):
            return True

    def playerT6(self):
        if self.width*(6/10)<self.cx<self.width*(7/10)and self.height*(1/10)<self.cy<=self.height*(1.5/10):
            return True

    def playerT7(self):
        if self.width*(8.5/10)<self.cx<self.width*(9/10)and self.height*(1/10)<self.cy<=self.height*(2/10):
            return True

    def playerT8(self):
        if self.width*(8/10)<self.cx<self.width*(9/10)and self.height*(8.5/10)<=self.cy<=self.height*(9/10):
            return True
    
    def enemyT1(self):
        if self.enemyCX <= self.width*(1.5/10)and self.enemyCY>self.height*(8/10):
            return True
    
    def enemyT2(self):
        if self.enemyCX <= self.width*(2/10) and self.enemyCY<self.height*(1.5/10):     
            return True   

    def enemyT3(self):
        if self.width*(3.5/10)<self.enemyCX<self.width*(4/10)and self.enemyCY<self.height*(2/10):
            return True

    def enemyT4(self):
        if self.width*(3/10)<self.enemyCX<=self.width*(4/10)and self.height*(5.5/10)<self.enemyCY<self.height*(6/10):
            return True

    def enemyT5 (self):
        if self.width*(6.5/10)<self.enemyCX<self.width*(7/10)and self.height*(5/10)<self.enemyCY<self.height*(6/10):
            return True

    def enemyT6(self):
        if self.width*(6/10)<self.enemyCX<self.width*(7/10)and self.height*(1/10)<self.enemyCY<=self.height*(1.5/10):
            return True

    def enemyT7(self):
        if self.width*(8.5/10)<self.enemyCX<self.width*(9/10)and self.height*(1/10)<self.enemyCY<=self.height*(2/10):
            return True

    def enemyT8(self):
        if self.width*(8/10)<self.enemyCX<self.width*(9/10)and self.height*(8.5/10)<=self.enemyCY<=self.height*(9/10):
            return True
    



    
