types = {"player":1, "wall":2, "exit":3, "food":4, "enemy":5}

class Object:
    def __init__(self, x, y, type): #objType = "wall", "exit", "food", "player", "enemy"
        self.x = x
        self.y = y
        self.index = (self.x, self.y)
        self.location = (x * 50, y * 50)
        if(type in types.keys()):
            self.type = type

    def isEqual(self, another):
        if int(self.x) == int(another.x) and int(self.y) == int(another.y) and str(self.type) == str(another.type):
            return True
        else:
            return False
    def isSameLocation(self, another):
        if int(self.x) == int(another.x) and int(self.y) == int(another.y):
            return True
        else:
            return False

    def getType(self):
        return self.type

    def getLocation(self):
        return self.location

    def changeTypeTo(self, newType):
        self.type = newType

    def toString(self):
        s = str(self.type) + " : " +str(self.location)
        print(s)


class Wall(Object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.index = (self.x, self.y)
        self.location = (x * 50, y * 50)
        self.type = "wall"
        

class Food(Object):
    def __init__(self, x, y): 
        self.x = x
        self.y = y
        self.index = (self.x, self.y)
        self.location = (x * 50, y * 50)
        self.type = "food"

class ExitPoint(Object):
    def __init__(self, x, y): 
        self.x = x
        self.y = y
        self.index = (self.x, self.y)
        self.location = (x * 50, y * 50)
        self.type = "exit"