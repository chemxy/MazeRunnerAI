from Cell import Cell


class Map:

    def __init__(self, map_path):
        self.__cells = self.load_cells(map_path)    # init all cells in a dictionary
        self.__exit_enabled = False
        self.__agent_coordinates = (self.get_start_coordinates()) # init agent's location

    def get_map_size(self):
        return self.__map_size

    def get_cells(self):
        return self.__cells

    def get_start_coordinates(self):
        return self.__start_coordinates

    def get_cell_at(self, coordinates):
        return self.__cells[coordinates]

    def get_agent_coordinates(self):
        return self.__agent_coordinates

    def set_agent_coordinates(self, coordinates):
         self.__agent_coordinates = coordinates
         
    # def show_exit(self):
    #     self.__exit_enabled = True

    def load_cells(self, map_path):
        f = open(map_path, "r")  # open map file
        lines = f.read().split("\n")  # read each line into a list
        f.close()   # close map file

        self.__map_size = int(lines[0])  # init map size
        self.__start_coordinates = (int(lines[1].split(",")[0]), int(lines[1].split(",")[1]))  # init start location

        # create a map based on the map file
        map = {}  # init map
        x = 0   # row count
        y = 0   # column count
        for line in lines[2:]:  # access the map matrix from line 3
            for cell in line:   # read each char/digit in each line and convert the char/digit to Cell object
                # add the converted Cell object into map
                map[(x, y)] = Cell(x, y, cell)
                x += 1
            y += 1
            x = 0
        return map

    def get_neighbor_cells_at(self, coordinates):
        (x, y) = coordinates
        neighbors = {}
        if x+1 < self.__map_size:
            neighbors[(x + 1, y)] = self.get_cell_at((x + 1, y)) 
        if x-1 >= 0:
            neighbors[(x - 1, y)] = self.get_cell_at((x - 1, y))
        if y+1 < self.__map_size:
            neighbors[(x, y + 1)] = self.get_cell_at((x, y + 1))
        if y-1 >= 0:
            neighbors[(x, y - 1)] = self.get_cell_at((x, y - 1))
        return neighbors







# test and debug
if __name__ == "__main__":

    map = Map("../../../maps/map_1.txt")
    print(map.get_map_size())
    print(map.get_start_coordinates())

    # print(map.get_map())
    # print(map.get_map().keys())
    print(map.get_cell_at((4, 5)))
    print(map.get_cell_at((0, 0)).get_cell_type())

    print(map.get_neighbor_cells_at((4, 5)))
    print(map.get_neighbor_cells_at((0, 0)))
    print(map.get_neighbor_cells_at((9, 9)))
