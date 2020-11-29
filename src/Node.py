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
        self.x = index[0]
        self.y = index[1]
        self.index = (self.x, self.y)
        self.location = (self.x*50, self.y*50)
        self.isWall = isWall
        self.isExit = isExit
        self.containsFood = containsFood

    """
        * this method gets the index of the node, and return it as a tuple.
        * parameter(s): none.
    """
    def getIndex(self):
        return self.index

    """
        * this method gets the location(i.e. index*50) of the node, and return it as a tuple.
        * parameter(s): none.
    """
    def getLocation(self):
        return self.location

    """
        * this method sets the node to Wall type.
        * parameter(s): 
            - index: a tuple that contains a pair of points i.e. (x,y), x and y less than the number of max blocks.
    """
    def setToWall(self, index):
        self.isWall = True
        self.isExit = False
        self.containsFood = False

    
    """
        * this method prints the information of the node.
        * parameter(s): none.
    """
    def __str__(self):
        if self.isWall == False:
            response = "index: " + str(self.index) + "\tcontentList: " + str(self.contentList) + "\n"
        else:
            response = "index: " + str(self.index) + "\ttype=wall" + "\n"
        return response