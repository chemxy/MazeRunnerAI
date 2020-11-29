types = {"player":1, "wall":2, "exit":3, "food":4, "enemy":5}

class Object:
    def __init__(self, x, y, type): #type = "wall", "exit", "food", "player", "enemy"
        self.x = x
        self.y = y
        self.index = tuple(self.x, self.y)
        self.location = tuple(x * 50, y * 50)
        if(type in types.keys()):
            self.type = type
        else:
            print("ERROR: the input type is not valid!")

    def isEqual(self, another):
        if self.index == another.index and str(self.type) == str(another.type):
            return True
        else:
            return False

    def isSameLocation(self, another):
        if self.index == another.index:
            return True
        else:
            return False

    def getType(self):
        return str(self.type)

    def getIndex(self):
            return self.index

    def getLocation(self):
        return self.location

    def changeTypeTo(self, newType):
        self.type = newType

    def __str__(self):
        s = str(self.type) + " : " +str(self.index)
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