from Object import Object

types = {"player":1, "wall":2, "exit":3, "food":4, "enemy":5}

class Player(Object): 
    def __init__(self,x ,y):
        # character's width and height in pixels
        #self.player_size = 50
        # iniitial character x-y coordinates in pixels
        self.x = x
        self.y = y
        #print("player initial location: " + str(self.x) + " " +str(self.y))
        self.index = (x,y)
        self.location = (x*50, y*50)
        # character's idle animation count
        self.animationCount = 0
        #self.life = 100
        self.type = "player"

    def setX(self, x):
        self.x = x

    def setY(self,y):
        self.y = y

    def updateLocation(self):
        self.index = (self.x,self.y)
        self.location = (self.x*50, self.y*50)

    def move(self, direction):
        if direction == "UP":
            self.setY(self.y - 1)
        elif direction == "DOWN":
            self.setY(self.y + 1)
        elif direction == "LEFT":
            self.setX(self.x - 1)

        elif direction == "RIGHT":
           self.setX(self.x + 1)

        self.updateLocation()
