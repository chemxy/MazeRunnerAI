class Cell:

    def __init__(self, x, y, cell_type):
        self.__x = x
        self.__y = y

        self.__Wall = True if cell_type is "1" else False
        self.__Exit = True if cell_type is "2" else False
        self.__Trap = True if cell_type is "x" else False
        self.__Gold = True if cell_type is "3" else False
        self.__Enemy = True if cell_type is "e" else False

    # getters
    def get_coordinates(self):
        return (self.__x, self.__y)

    def is_Wall(self):
        return self.__Wall

    def is_Exit(self):
        return self.__Exit

    def has_Trap(self):
        return self.__Trap

    def has_Gold(self):
        return self.__Gold

    def get_Enemy(self):
        return self.__Enemy

    # setters
    def remove_Gold(self):
        self.__Gold = False

    def remove_Enemy(self, enemy): #enemy: an Enemy object
        self.Enemy = enemy



    #def __str__(self): #TODO
        