from Node import Node
from Object import Object, Food, Wall

class Map:
    def __init__(self, nodeList=None):
        if nodeList == None:
            nodeList = []
        self.nodeList = nodeList

    """ return a list of nodes in a map """
    def nodes(self):
        return self.nodeList

    def addNode(self, newNode):
        if newNode not in self.nodeList:
            self.nodeList.append(newNode)

    def __str__(self):
        response = ""
        for node in self.nodeList:
            response += "node: " + str(node) 
        return response

    def findPath(self, curNode, endNode):
        return None

"""
graph and find path
https://www.python-course.eu/graphs_python.php
https://www.python-course.eu/networkx.php
https://www.python.org/doc/essays/graphs/

"""