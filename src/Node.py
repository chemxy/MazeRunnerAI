from Object import Object, Wall, Food

types = {"player":1, "wall":2, "exit":3, "food":4, "enemy":5}

class Node: 
    """
        * this method initializes the Node class.
        * parameter(s): 
            - index: a tuple that contains a pair of points i.e. (x,y).
            - isWall: a boolean flag that idicates whether this node is a Wall object. i.e. true/False
            - isExit: a boolean flag that idicates whether this node is a Exit object. i.e. true/False
            - containsFood: a boolean flag that idicates whether this node contains a food object. i.e. true/False
    """
    def __init__(self, index, isWall=False, isExit=False, containsFood=False):
        x = index[0]
        y = index[1]
        self.__index = (x, y)
        self.__location = (x * 50, y * 50)
        
        self.__neighbors = []
        
        self.isWall = isWall
        self.isExit = isExit
        self.containsFood = containsFood

    def isEqual(self, another):
        if self.__index == another.index and self.isWall == another.isWall and self.isExit == another.isExit and self.containsFood == another.containsFood:
            return True
        else:
            return False

    def isSameLocation(self, another):
        if self.__index == another.__index:
            return True
        else:
            return False

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

    """
        * this method gets the index of the node, and return it as a tuple.
        * parameter(s): none.
    """
    def getIndex(self):
        return self.__index
    
    """
        * this method sets the index of the node.
        * parameter(s): 
            - index: the new index you want to set.
    """
    def setIndex(self, index):
        x = index[0]
        y = index[1]
        self.__index = (x, y)
        self.__location = (x * 50, y * 50)

    """
        * this method gets the location(i.e. index*50) of the node, and return it as a tuple.
        * parameter(s): none.
    """
    def getLocation(self):
        return self.__location
    
    """
        * this method sets the location of the node.
        * parameter(s): 
            - location: the new location you want to set.
    """
    def setLocation(self, location):
        x = location[0]
        y = location[1]
        self.__location = (x, y)
        self.__index = (x/50, y/50)

    """
        * this method sets the node to Wall type.
        * parameter(s): 
            - index: a tuple that contains a pair of points i.e. (x,y), x and y less than the number of max blocks.
    """
    def setToWall(self):
        self.isWall = True
        self.isExit = False
        self.containsFood = False

    def setToExit(self):
        self.isWall = False
        self.isExit = True
        self.containsFood = False

    def setToNone(self):
        self.isWall = False
        self.isExit = False
        self.containsFood = False

    def addFood(self):
        self.containsFood = True

    def removeFood(self):
        self.containsFood = False

    """
        * this method prints the information of the node.
        * parameter(s): none.
    """
    def __str__(self):
        if self.isWall == True:
            response = "index: " + str(self.__index) + "\ttype=wall" + "\n"
        elif self.isExit == True:
            response = "index: " + str(self.__index) + "\ttype=exit" + "\n"
        elif self.contains == True:
            response = "index: " + str(self.__index) + "\ttype=food" + "\n"
        return response