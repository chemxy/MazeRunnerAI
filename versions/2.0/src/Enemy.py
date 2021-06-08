from Agent import Agent

class Enemy(Agent):
   
    def __init__(self, coordinates):  
        super().__init__(coordinates)

    def move(self, direction):
        if direction == "UP":
            self.setY(self.__index[1] - 1)
        elif direction == "DOWN":
            self.setY(self.__index[1] + 1)
        elif direction == "LEFT":
            self.setX(self.__index[0] - 1)
        elif direction == "RIGHT":
            self.setX(self.__index[0] + 1)
