from Block import Block

class Map:
    def __init__(self, map_dict=None):
        if map_dict == None:
            map_dict = {}
        self.map_dict = map_dict

    """ return a list of nodes in a map """
    def vertices(self):
        return list(self.map_dict.keys())

    """ return a list of edges in a map """
    def edges(self):
        return self.generate_edges()
    
    def generate_edges(self):
        edges = []
        for vertex in self.map_dict:
            for neighbour in self.map_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def add_vertex(self, block):
        """ If the vertex "vertex" is not in 
            self.map_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if block not in self.map_dict:
            self.map_dict[block] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.map_dict:
            self.map_dict[vertex1].append(vertex2)
        else:
            self.map_dict[vertex1] = [vertex2]

    def __str__(self):
        res = "vertices: "
        for k in self.map_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.generate_edges():
            res += str(edge) + " "
        return res

# some test cases
def main():
    A = Block(contents=["wall"])
    B = Block(contents=["wall"])
    C = Block()
    D = Block()
    E = Block()
    map_dict = {
                A:[B], 
                C:[D, E]
            }
    GameMap = Map(map_dict)
    print(GameMap)
# main
if __name__ == "__main__":
    main()
