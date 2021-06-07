
import random

types = {"player": 1, "wall": 2, "exit": 3, "food": 4, "enemy": 5}


class Agent():
    def __init__(self, x, y):
        self.__index = (x, y)
        self.__location = (x * 50, y * 50)
        # character's idle animation count
        self.animationCount = 0
        #self.life = 100
        self.__type = "player"

        # record path history - dictionary {cordinates: number of times visited}
        self.pathHistory = {}

    def get_x(self):
        return self.__index[0]

    def get_y(self):
        return self.__index[1]

    def set_x(self, x):
        self.__index = (x, self.__index[1])
        self.__location = (x * 50, self.__index[1] * 50)

    def set_y(self, y):
        self.__index = (self.__index[0], y)
        self.__location = (self.__index[0] * 50, y * 50)

    def get_index(self):
        return self.__index

    def setIndex(self, index):
        x = index[0]
        y = index[1]
        self.__index = (x, y)
        self.__location = (x * 50, y * 50)

    def get_location(self):
        return self.__location

    def setLocation(self, location):
        x = location[0]
        y = location[1]
        self.__location = (x, y)
        self.__index = (x / 50, y / 50)

    def get_type(self):
        return self.__type

    def move(self, direction):
        if direction == "UP":
            self.set_y(self.__index[1] - 1)
            return True
        elif direction == "DOWN":
            self.set_y(self.__index[1] + 1)
            return True
        elif direction == "LEFT":
            self.set_x(self.__index[0] - 1)
            return True
        elif direction == "RIGHT":
            self.set_x(self.__index[0] + 1)
            return True
        else:
            print("stayed on the same location.")
            return False

    def perceive(self, percept):
        neighbors = percept
        accessibleNeighbors = []
        action = "NONE"
        for node in neighbors.keys():
            # print("node: " + str(node.get_location()) + " / isWall: " + str(node.isWall) + " / isExit: " +
            # str(node.isExit) + " / isEnemy: " + str(node.isEnemy) + " / isFood: " + str(node.isFood))
            if node.isExit == True:
                accessibleNeighbors.append(node)
                break
            elif node.isWall == True:
                print("node: " + str(node.get_index()) + " is wall.")
            else:
                if node.isEnemy == True:
                    print("node: " + str(node.get_index()) + " is enemy.")
                elif node.isFood == True:
                    accessibleNeighbors.append(node)
                else:
                    accessibleNeighbors.append(node)
        # print(self.pathHistory.keys())
        if len(accessibleNeighbors) == 0:
            print("no action can be taken.")
        elif len(accessibleNeighbors) == 1:
            action = str(neighbors[accessibleNeighbors[0]])
            # print(accessibleNeighbors[0])

            if accessibleNeighbors[0] not in self.pathHistory.keys():
                self.pathHistory[accessibleNeighbors[0].get_index()] = 1
            else:
                # print(self.pathHistory[accessibleNeighbors[0].get_index()])
                self.pathHistory[accessibleNeighbors[0].get_index()] += 1
        elif len(accessibleNeighbors) > 1:
            x = random.randint(0, len(accessibleNeighbors) - 1)
            action = str(neighbors[accessibleNeighbors[x]])

            if accessibleNeighbors[x].get_index() not in self.pathHistory.keys():
                self.pathHistory[accessibleNeighbors[x].get_index()] = 1
            else:
                # print(self.pathHistory[accessibleNeighbors[x].get_index()])
                self.pathHistory[accessibleNeighbors[x].get_index()] += 1
        return action
