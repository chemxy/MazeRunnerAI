from Enemy import Enemy

class Cell:

    def __init__(self, x, y, cell_type):
        self.__coordinates = (x, y)
        self.__Wall = True if cell_type == "1" else False
        self.__Exit = True if cell_type == "2" else False
        self.__Trap = True if cell_type == "x" else False
        self.__Gold = True if cell_type == "3" else False
        self.__Enemy = Enemy(self.__coordinates) if cell_type == "e" else None

    # getters
    def get_coordinates(self):
        return self.__coordinates

    def is_wall(self):
        return self.__Wall

    def is_exit(self):
        return self.__Exit

    def has_trap(self):
        return self.__Trap

    def has_gold(self):
        return self.__Gold

    def get_enemy(self):
        return self.__Enemy

    # setters
    def remove_Gold(self):
        self.__Gold = False

    def remove_Enemy(self, enemy): #enemy: an Enemy object
        self.Enemy = enemy


    #def __str__(self): #TODO
        

# test and debug
if __name__ == "__main__":   

    cell1 = Cell(1,2, "0")
    cell2 = Cell(1,2, "1")
    cell3 = Cell(1,2, "2")
    cell4 = Cell(1,2, "x")
    cell5 = Cell(1,2, "3")
    cell6 = Cell(1,2, "e")
    