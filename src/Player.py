from Object import Object
import random

types = {"player": 1, "wall": 2, "exit": 3, "food": 4, "enemy": 5}


class Player(Object):
    def __init__(self, x, y):
        self.__index = (x, y)
        self.__location = (x * 50, y * 50)
        # character's idle animation count
        self.animationCount = 0
        #self.life = 100
        self.__type = "player"

    def getX(self):
        return self.__index[0]

    def getY(self):
        return self.__index[1]

    def setX(self, x):
        self.__index = (x, self.__index[1])
        self.__location = (x * 50, self.__index[1] * 50)

    def setY(self, y):
        self.__index = (self.__index[0], y)
        self.__location = (self.__index[0] * 50, y * 50)

    def getIndex(self):
        return self.__index

    def setIndex(self, index):
        x = index[0]
        y = index[1]
        self.__index = (x, y)
        self.__location = (x * 50, y * 50)

    def getLocation(self):
        return self.__location

    def setLocation(self, location):
        x = location[0]
        y = location[1]
        self.__location = (x, y)
        self.__index = (x / 50, y / 50)

    def getType(self):
        return self.__type

    def move(self, direction):
        if direction == "UP":
            self.setY(self.__index[1] - 1)
            return True
        elif direction == "DOWN":
            self.setY(self.__index[1] + 1)
            return True
        elif direction == "LEFT":
            self.setX(self.__index[0] - 1)
            return True
        elif direction == "RIGHT":
            self.setX(self.__index[0] + 1)
            return True
        else:
            print("stayed on the same location.")
            return False

    # def moveTo(self, index):
    #   self.setIndex(index)

    def perceive(self, percept):
        neighbors = percept
        accessibleNeighbors = []
        action = "NONE"
        for node in neighbors.keys():
            print("node: " + str(node.getLocation()) + " / isWall: " + str(node.isWall) + " / isExit: " +
                  str(node.isExit) + " / isEnemy: " + str(node.isEnemy) + " / isFood: " + str(node.isFood))
            if node.isExit == True:
                accessibleNeighbors.append(node)
            elif node.isWall == True:
                print("node: " + str(node.getIndex()) + " is wall.")
            else:
                if node.isEnemy == True:
                    print("node: " + str(node.getIndex()) + " is enemy.")
                elif node.isFood == True:
                    accessibleNeighbors.append(node)
                else:
                    accessibleNeighbors.append(node)
        if len(accessibleNeighbors) == 0:
            print("no action can be taken.")
        elif len(accessibleNeighbors) == 1:
            action = str(neighbors[accessibleNeighbors[0]])
        else:
            x = random.randint(0, len(accessibleNeighbors) - 1)
            action = str(neighbors[accessibleNeighbors[x]])
        return action
