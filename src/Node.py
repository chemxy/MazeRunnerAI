
types = {"player": 1, "wall": 2, "exit": 3, "food": 4, "enemy": 5}


class Node:
    """
        * this method initializes the Node class.
        * parameter(s): 
            - index: (x,y)
            - node_type: String
    """

    def __init__(self, index, node_type):
        x = index[0]
        y = index[1]
        self.__index = (x, y)
        self.__location = (x * 50, y * 50)

        self.__neighbors = []
        if node_type in ["wall", "ground"]:
            self.__node_type = node_type
        else:
            raise Exception("wrong input: node_type")
        self.__node_type = node_type

    def is_equal(self, another):
        if self.get_index() == another.get_index() and self.get_type() == another.get_type():
            return True
        else:
            return False

    def is_same_location(self, another):
        if self.__index == another.get_index():
            return True
        else:
            return False

    def get_x(self):
        return self.__index[0]

    def get_y(self):
        return self.__index[1]

    def get_type(self):
        return self.__node_type

    """
        * this method gets the index of the node, and return it as a tuple.
        * parameter(s): none.
    """

    def get_index(self):
        return self.__index

    """
        * this method gets the location(i.e. index*50) of the node, and return it as a tuple.
        * parameter(s): none.
    """

    def get_location(self):
        return self.__location

    """
        * this method prints the information of the node.
        * parameter(s): none.
    """

    def __str__(self):
        # TODO
        response = ""
        return response
