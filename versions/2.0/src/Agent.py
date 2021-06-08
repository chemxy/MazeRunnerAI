class Agent():
    def __init__(self, coordinates):
        self.__coordinates = coordinates  # (x,y)
        self.animationCount = 0  # character's idle animation count

    def get_coordinates(self):
        return self.__coordinates
