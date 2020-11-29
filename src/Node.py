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
        self.__x = index[0]
        self.__y = index[1]
        self.__index = (index[0], index[1])
        self.__location = (index[0] * 50, index[1] * 50)
        self.isWall = isWall
        self.isExit = isExit
        self.containsFood = containsFood

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self,y):
        self.__y = y

    """
        * this method gets the index of the node, and return it as a tuple.
        * parameter(s): none.
    """
    def getIndex(self):
        return self.__index
    
    def setIndex(self, index):
        self.__index = index

    """
        * this method gets the location(i.e. index*50) of the node, and return it as a tuple.
        * parameter(s): none.
    """
    def getLocation(self):
        return self.__location
    
    def setLocation(self, location):
        self.__location = location


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