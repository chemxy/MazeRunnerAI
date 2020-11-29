from Object import Object

types = {"player":1, "wall":2, "exit":3, "food":4, "enemy":5}

class Player(Object): 
    def __init__(self,x ,y):
        # iniitial character x-y coordinates in pixels
        self.__index = (x,y)
        self.__location = (x*50, y*50)
        # character's idle animation count
        self.animationCount = 0
        #self.life = 100
        self.__type = "player"

    def getX(self):
        return self.__index[0]

    def getY(self):
        return self.__index[1]

    def setX(self, x):
        self.__index = (x, self.__index[1])
        self.__location = (x*50, self.__index[1]*50)

    def setY(self,y):
        self.__index = (self.__index[0], y)
        self.__location = (self.__index[0]*50, y*50)

    def getIndex(self):
        return self.__index
    
    def setIndex(self, index):
        x = index[0]
        y = index[1]
        self.__index = (x, y)
        self.__location = (x * 50, y * 50)
        
    def getLocation(self):
        return self.__location
    
    def setLocation(self, location):
        x = location[0]
        y = location[1]
        self.__location = (x,y)
        self.__index = (x/50, y/50)
        
    def move(self, direction):
        if direction == "UP":
            self.setY(self.__index[1] - 1)
        elif direction == "DOWN":
            self.setY(self.__index[1] + 1)
        elif direction == "LEFT":
            self.setX(self.__index[0] - 1)
        elif direction == "RIGHT":
           self.setX(self.__index[0] + 1)
