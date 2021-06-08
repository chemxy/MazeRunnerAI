from Cell import Cell

class Map:

    def __init__(self, map_path):
        self.__map = self.load_map(map_path)
        self.__exit_enabled = False

    def get_map_size(self):
        return self.__map_size

    def get_map(self):
        return self.__map

    def get_start_coordinates(self):
        return self.__start_coordinates

    def get_cell_at(self, x, y):
        return self.__map[(x,y)]
    
    # def show_exit(self):
    #     self.__exit_enabled = True

    def load_map(self, map_path):
        f = open(map_path, "r") # open map file
        lines = f.read().split("\n") # read each line into a list
        f.close()   # close map file

        self.__map_size = int(lines[0]) # init map size
        self.__start_coordinates = (int(lines[1].split(",")[0]), int(lines[1].split(",")[1])) # init start location
        
        #create a map based on the map file
        map = {}
        x = 0
        y = 0
        for line in lines[2:]:  
            for cell in line:
                map[(x,y)] = Cell(x, y, cell)
                x += 1
            y += 1
            x = 0
        return map

   

    
# test and debug
if __name__ == "__main__":   

    map = Map("../maps/map_1.txt")
    print(map.get_map_size())
    print(map.get_start_coordinates())
    
    print(map.get_map())
    print(map.get_map().keys())
    print(map.get_cell_at(0,0))
    print(map.get_cell_at(0,0).is_wall())

