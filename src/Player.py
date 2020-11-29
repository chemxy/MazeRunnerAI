from Object import Object

types = {"player":1, "wall":2, "exit":3, "food":4, "enemy":5}

class Player(Object): 
    def __init__(self,x ,y):
        # iniitial character x-y coordinates in pixels
        self.__x = x
        self.__y = y
        self.__index = (x,y)
        self.__location = (x*50, y*50)
        # character's idle animation count
        self.animationCount = 0
        #self.life = 100
        self.__type = "player"

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x
        self.__index = (x, self.__y)
        self.__location = (x*50, self.__y*50)

    def setY(self,y):
        self.__y = y
        self.__index = (self.__x, y)
        self.__location = (self.__x*50, y*50)

    def getIndex(self):
        return self.__index
    
    def setIndex(self, index):
        self.__index = __index

    def getLocation(self):
        return self.__location
    
    def setLocation(self, location):
        self.__location = location

    def __updateLocation(self):
        self.__index = (self.__x,self.__y)
        self.__location = (self.__x*50, self.__y*50)

   
    def move(self, direction):
        if direction == "UP":
            self.setY(self.__y - 1)
        elif direction == "DOWN":
            self.setY(self.__y + 1)
        elif direction == "LEFT":
            self.setX(self.__x - 1)
        elif direction == "RIGHT":
           self.setX(self.__x + 1)
        self.__updateLocation()
