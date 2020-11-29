from Object import Object, Wall, Food

types = {"player":1, "wall":2, "exit":3, "food":4, "enemy":5}

class Node: 
    """
        * this method initializes the Node class.
        * parameter(s): 
            - index: a tuple that contains a pair of points i.e. (x,y).
            - isWall: a boolean flag that idicates whether this node is a wall object. i.e. true/False
            - contentList: a list that contains unique objects i.e. each object has a unique type (among Wall, Food, Enemy, Player)
    """
    def __init__(self, index, isWall=False, contentList=None):
        self.x = index[0]
        self.y = index[1]
        self.index = (self.x, self.y)
        self.location = (self.x*50, self.y*50)
        if isWall != False: #iswall - a Wall object
            self.isWall = True
        else:
            self.isWall = False
            if contentList == None:
                contentList = [] # i.e contentList = ["food", "food", "enemy", "player"]
                self.contentList = contentList 
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
        self.isWall == True
        self.contentList = []

    """
        * this method gets the content(s) of the node, and return it as a list.
        * parameter(s): none.
    """
    def getcontentList(self):
        return self.contentList

    """
        * this method adds a new content to the node.
        * parameter(s): 
            - obj: a new Object that has to be a valid type (i.e. Wall, Food, Exit, Enemy, Player)
    """
    def addContent(self,obj):
        self.contentList.append(obj)

    """
        * this method removes one item in the content(s) list of the node.
        * parameter(s): 
            - obj: the Object to be removed.
    """
    def remove(self,obj):
        for item in self.contentList:
            if item.isEqual(obj):
                self.contentList.remove(item)
    
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