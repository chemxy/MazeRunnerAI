from Enemy import Enemy
from CellType import CellType

class Cell:

    def __init__(self, x, y, cell_type):
        self.__coordinates = (x, y)
        # self.__Wall = True if cell_type == "1" else False
        # self.__Exit = True if cell_type == "2" else False
        # self.__Trap = True if cell_type == "4" else False
        # self.__Gold = True if cell_type == "3" else False
        # self.__Enemy = Enemy(self.__coordinates) if cell_type == "5" else None

        if cell_type == "0":
            self.__cell_type = CellType.GROUND
        elif cell_type == "1":
            self.__cell_type = CellType.WALL
        elif cell_type == "2":
             self.__cell_type = CellType.EXIT
        elif cell_type == "3":
             self.__cell_type = CellType.GOLD
        elif cell_type == "4":
             self.__cell_type = CellType.TRAP
        elif cell_type == "5":
             self.__cell_type = CellType.ENEMY


    # getters
    def get_coordinates(self):
        return self.__coordinates

    def get_cell_type(self):
        return self.__cell_type

    def get_cell_type_value(self):
        return self.__cell_type.value


    # def get_cell_type_as_string(self):
    #     if self.is_exit is True:
    #         return "exit"
    #     elif self.is_wall is True:
    #         return "wall"
    #     elif self.has_gold is True:
    #         return "gold"
    #     elif self.has_trap is True:
    #         return "trap"
    #     elif self.get_enemy is not None:
    #         return "enemy"

    # setters
    def remove_cell_value(self):
        if self.__cell_type == CellType.GOLD or self.__cell_type == CellType.TRAP or self.__cell_type == CellType.ENEMY:
            self.__cell_type = CellType.GROUND 

    #def __str__(self): #TODO
        

# test and debug
if __name__ == "__main__":   

    cell0 = Cell(1,2, "0")
    cell1 = Cell(1,2, "1")
    cell2 = Cell(1,2, "2")
    cell3 = Cell(1,2, "3")
    cell4 = Cell(1,2, "4")
    cell5 = Cell(1,2, "5")
    print(cell0.get_cell_type_value())
    print(cell1.get_cell_type())
    print(cell2.get_cell_type())
    print(cell3.get_cell_type())
    print(cell4.get_cell_type())
    print(cell5.get_cell_type())
    print(cell5.get_cell_type_value())
    cell5.remove_cell_value()
    print(cell5.get_cell_type())
    print(cell5.get_cell_type_value())
    