import random
from Agent import Agent

class Character(Agent):
    def __init__(self, coordinates):
       super().__init__(coordinates)
       self.__pathHistory = {}   # record path history - dictionary {cordinates: number of times visited}
    
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
