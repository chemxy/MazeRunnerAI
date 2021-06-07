from Cell import Cell
import pygame

class Canvas:

    def __init__(self, map_path):
        # set up salce
        self.__scale = 50
        self.__map = {}
        self.__exit_enabled = False

        self.load_map(map_path)

        
    def get_map_scale(self):
        return self.__scale

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
        # print(lines[2:])
        f.close()   # close map file

        self.__map_size = int(lines[0]) # init map size
        self.__start_coordinates = (int(lines[1].split(",")[0]), int(lines[1].split(",")[1])) # init start location
        
        #create a map based on the map file
        x = 0
        y = 0
        for line in lines[1:]:  
            for cell in line:
                # print(cell)
               self.__map[(x,y)] = Cell(x, y, cell)
            x += 1
            y += 1

   

    
# test and debug
if __name__ == "__main__":   

    canvas = Canvas("../maps/map_1.txt")
    print(canvas.get_map_size())
    print(canvas.get_start_coordinates())
    
    print(canvas.get_map())
    print(canvas.get_cell_at(0,0))
    print(canvas.get_cell_at(0,0).is_Wall())

