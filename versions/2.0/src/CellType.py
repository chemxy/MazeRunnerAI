from enum import Enum, auto, unique
from Enemy import Enemy

@unique
class CellType(Enum):
    GROUND = 0
    WALL = 1
    EXIT = 2
    GOLD = 3
    TRAP = 4
    ENEMY = Enemy()
