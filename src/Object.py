types = {"player":1, "wall":2, "exit":3, "food":4, "enemy":5}

class Object:
    def __init__(self, x, y, type): #objType = "innerWall", "wall", "exit", "food", "player", "enemy"
        self.x = x
        self.y = y
        self.location = (self.x, self.y)
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
    def __init__(self, x, y): #objType = "innerWall", "outterWall", "exit", "food"
        self.x = x
        self.y = y
        self.location = (self.x, self.y)
        self.type = "wall"

class Food(Object):
    def __init__(self, x, y): #objType = "innerWall", "outterWall", "exit", "food"
        self.x = x
        self.y = y
        self.location = (self.x, self.y)
        self.type = "food"