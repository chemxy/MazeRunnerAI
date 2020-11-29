from Object import Object

types = {"player":1, "wall":2, "exit":3, "food":4, "enemy":5}

class Enemy(Object):
    def __init__(self, x, y): #enemytype = "A" or "B"
        # character's width and height in pixels
        #self.player_size = 50
        # iniitial character x-y coordinates in pixels
        self.__x = x
        self.__y = y
        self.__index = (x,y)
        self.__location = (x*50, y*50)
        # character's idle animation count
        self.animationCount = 0
        #self.life = 100
        #self.type = enemyType
        self.__type = "enemy"
    
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self,y):
        self.__y = y

    def getIndex(self):
        return self.__index
    
    def setIndex(self, index):
        self.__index = index

    def getLocation(self):
        return self.__location
    
    def setLocation(self, location):
        self.__location = location

    def __updateLocation(self):
        self.__index = (self.__x, self.__y)
        self.__location = (self.__x * 50, self.__y * 50)

    def move(self, direction):
        if direction == "UP":
            self.setY(self.y - 1)
        elif direction == "DOWN":
            self.setY(self.y + 1)
        elif direction == "LEFT":
            self.setX(self.x - 1)
        elif direction == "RIGHT":
           self.setX(self.x + 1)
        self.__updateLocation()