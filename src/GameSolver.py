import pygame
import random
import time
from Object import Object, Food, Wall
from Player import Player
from Enemy import Enemy

class GameSolver:
    def __init__(self, game):
        self.game = game