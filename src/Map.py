from Node import Node
from Object import Object, Food, Wall

class Map:
    def __init__(self, nodeList=None):
        if nodeList == None:
            nodeList = []
        self.nodeList = nodeList

    """ 
        * this method returns a list of nodes in a map.
        * parameter(s): none.
    """
    def nodes(self):
        return self.nodeList

    """ 
        * this method returns the node with a particular index in a map.
        * parameter(s): 
            - index: a set of paired points.
    """
    def getNode(self, index):
        for node in self.nodeList:
            if index == node.getIndex():
                return node
        return None

    """ 
        * this method changes __containsFood property.
        * parameter(s): 
            - index: the index of the node you wanted to change.
            - flag: the change you want to make i.e. change to True/False.
    """
    def changeFood(self, index, flag=True):
        if flag:
            self.getNode(index).addFood()
        else:
            self.getNode(index).removeFood()

    """ 
        * this method adds a new node to the map.
        * parameter(s):
            - newNode: a new node.
    """
    def addNode(self, newNode):
        if newNode not in self.nodeList:
            self.nodeList.append(newNode)

    """
        * this method prints the information of the map (i.e. print each node in the node list).
        * parameter(s): none.
    """
    def __str__(self):
        response = ""
        for node in self.nodeList:
            response += "node: " + str(node) 
        return response

    """
        * this method 
    """
    def findPath(self, start, end):
        
        return None

"""
graph and find path
https://www.python-course.eu/graphs_python.php
https://www.python-course.eu/networkx.php
https://www.python.org/doc/essays/graphs/

"""