class Player:
    def __init__(self, name, points, figure, stop,x,y):
        self.name = name
        self.points = points
        self.figure = figure
        self.stop = stop
        self.x = x
        self.y = y
    def show(self):
        print(self.name, self.points, self.figure, self.stop)
    def showName(self):
        return(self.name)
    def showStop(self):
        return(self.stop)
    def updateStop(self, newstop):
        self.stop = newstop
    def showPosX(self):
        return(self.x)
    def showPosY(self):
        return(self.y)
    def updatePos(self,x,y):
        self.x = x
        self.y = y
    def showPoints(self):
        return self.points
    def updatePoints(self,points):
        self.points = points