from Node import Node


class Map:
    """
        exit_index : (x,y)
        node_list : list
        food_count : int
    """

    def __init__(self, node_list, food_list, exit_index, enemy_list=None):
        self.__node_list = node_list
        self.__exit_index = exit_index
        self.__food_list = food_list
        self.__show_exit = False
        if enemy_list == None:
            enemy_list = []
        self.__enemy_list = enemy_list

    def get_exit_location(self):

        return (self.__exit_index[0] * 50, self.__exit_index[1] * 50)

    def get_food_count(self):
        return len(self.__food_list)

    def get_food_list(self):
        return self.__food_list

    def remove_food_from_list(self, index):
        for item in self.__food_list:
            if item == index:
                self.__food_list.remove(item)

    def get_enemy_count(self):
        return len(self.__enemy_list)

    def get_enemy_list(self):
        return self.__enemy_list
    """ 
        * this method returns a list of nodes in a map.
        * parameter(s): none.
    """

    def get_nodes(self):
        return self.__node_list

    """ 
        * this method returns the node with a particular index in a map.
        * parameter(s): 
            - index: a set of paired points.
    """

    def get_node(self, index):
        for node in self.__node_list:
            if index == node.get_index():
                return node
        return None

    def get_show_exit(self):
        return self.__show_exit

    def set_show_exit(self, val):
        self.__show_exit = val

    """ 
        * this method adds a new node to the map.
        * parameter(s):
            - newNode: a new node.
    """

    def add_node(self, newNode):
        if newNode not in self.__node_list:
            self.__node_list.append(newNode)

    """
        * this method prints the information of the map (i.e. print each node in the node list).
        * parameter(s): none.
    """

    def __str__(self):
        response = ""
        for node in self.__node_list:
            response += "node: " + str(node)
        return response

    def check_neighbors(self, index):
        x = index[0]
        y = index[1]
        neighbors = {}
        for node in self.__node_list:
            if node.get_index() == (x + 1, y):
                neighbors[node] = "RIGHT"
            elif node.get_index() == (x, y + 1):
                neighbors[node] = "DOWN"
            elif node.get_index() == (x - 1, y):
                neighbors[node] = "LEFT"
            elif node.get_index() == (x, y - 1):
                neighbors[node] = "UP"
        return neighbors


"""
graph and find path
https://www.python-course.eu/graphs_python.php
https://www.python-course.eu/networkx.php
https://www.python.org/doc/essays/graphs/

"""
