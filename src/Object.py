types = {"player":1, "wall":2, "exit":3, "food":4, "enemy":5}

class Object:
    def __init__(self, x, y, type): #type = "wall", "exit", "food", "player", "enemy"
        self.__x = x
        self.__y = y
        self.__index = (x,y)
        self.__location = (x*50, y*50)
        if(type in types.keys()):
            self.__type = type
        else:
            print("ERROR: the input type is not valid!")

    def isEqual(self, another):
        if self.__index == another.index and str(self.__type) == str(another.type):
            return True
        else:
            return False

    def isSameLocation(self, another):
        if self.__index == another.index:
            return True
        else:
            return False

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
        self.__index = index

    def getLocation(self):
        return self.__location
    
    def setLocation(self, location):
        self.__location = location

    def changeTypeTo(self, newType):
        self.__type = newType

    def __str__(self):
        s = str(self.__type) + " : " +str(self.__index)
        print(s)


class Wall(Object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__index = (x,y)
        self.__location = (x*50, y*50)
        self.__type = "wall"
        

class Food(Object):
    def __init__(self, x, y): 
        self.__x = x
        self.__y = y
        self.__index = (x,y)
        self.__location = (x*50, y*50)
        self.__type = "food"

class ExitPoint(Object):
    def __init__(self, x, y): 
        self.__x = x
        self.__y = y
        self.__index = (x,y)
        self.__location = (x*50, y*50)
        self.__type = "exit"