"""
@Author: Xingyun Chen
@Github: github.com/chemxy
"""
import pygame
import random
import time
from math import floor, log10, log
from Player import Player
from Enemy import Enemy
from Map import Map
from Node import Node


# setting up some global variables...

# set up salce
SCALE = 50

# set up game clock
clock = pygame.time.Clock()

# set game tittle
pygame.display.set_caption("Survival!")

# set pictures and animations' sources and canvas dimensions
map_size = 500
win = pygame.display.set_mode((map_size, map_size))


MAX_BLOCKS = int(map_size/SCALE)
print("max blocks: " + str(MAX_BLOCKS) + "x" + str(MAX_BLOCKS))

playerAnimation = [pygame.image.load('../images/PlayerIdle1.png'), pygame.image.load('../images/PlayerIdle2.png'), pygame.image.load('../images/PlayerIdle3.png'),
                   pygame.image.load('../images/PlayerIdle4.png'), pygame.image.load('../images/PlayerIdle5.png'), pygame.image.load('../images/PlayerIdle6.png')]
enemy1Animation = [pygame.image.load('../images/Enemy1_1.png'), pygame.image.load(
    '../images/Enemy1_2.png'), pygame.image.load('../images/Enemy1_3.png')]
# enemy2 = [pygame.image.load('../images/Enemy2_1.png'), pygame.image.load('../images/Enemy2_2.png'), pygame.image.load('../images/Enemy2_3.png')]
wall = pygame.image.load('../images/OuterWall1.png')
ground = pygame.image.load('../images/InnerWall1.png')
food = pygame.image.load('../images/Food.png')
exit = pygame.image.load('../images/Exit.png')
background = pygame.image.load('../images/Background.png')

BLACK = pygame.Color(0, 0, 0)

# end setting-up


def rand_block_generator():
    # the number of total blocks (each block is 50x50 pixels)
    x = random.randint(1, MAX_BLOCKS-2)
    # print(x)
    return x


class Game:
    def __init__(self):
        # set level
        self.level = 10
        self.steps = 0

        # genreate player
        self.Player = None

        # initialize map
        self.map = None

        # record path history
        self.pathHistory = []

        self.isRun = True

    """
        generate food count based on level
    """

    def food_count_generator(self):
        food_count = 0
        food_count = random.randint(0, 3)
        return food_count

    """
        generate enemy count based on level
    """

    def enemy_count_generator(self):
        enemy_count = 0
        enemy_count = floor(log(self.level))
        return enemy_count

    def map_generator(self, MAX_BLOCKS):
        node_list = []
        # generate wall_list
        wall_list = []
        for i in range(0, MAX_BLOCKS):
            for j in range(0, MAX_BLOCKS):
                if (i == 0) or (j == 0) or (i == MAX_BLOCKS-1) or (j == MAX_BLOCKS-1):
                    wall_list.append((i, j))

        wall_count = random.randint(5, 25)
        print("wall_count: " + str(wall_count))
        for i in range(wall_count):
            x = rand_block_generator()
            y = rand_block_generator()
            while (x, y) in wall_list:
                x = rand_block_generator()
                y = rand_block_generator()
            wall_list.append((x, y))
        print("wall list: " + str(wall_list))

        # generate exit point
        x = rand_block_generator()
        y = rand_block_generator()
        while (x, y) in wall_list:
            x = rand_block_generator()
            y = rand_block_generator()
        exit_location = (x, y)

        # generate food_list
        food_list = []
        food_count = self.food_count_generator()
        print("food_count: " + str(food_count))
        for i in range(food_count):
            x = rand_block_generator()
            y = rand_block_generator()
            while ((x, y) in wall_list) or ((x, y) in food_list):
                x = rand_block_generator()
                y = rand_block_generator()
            food_list.append((x, y))
        print("food list: " + str(food_list))

        # generate enemies
        enemy_dict = {}
        enemy_count = self.enemy_count_generator()
        for i in range(enemy_count):
            x = rand_block_generator()
            y = rand_block_generator()
            while ((x, y) in wall_list) or ((x, y) in enemy_dict.values()):
                x = rand_block_generator()
                y = rand_block_generator()
            enemy_dict[Enemy(x, y)] = (x, y)
        print("enemy dict: " + str(enemy_dict))
        print("enemy list: " + str(enemy_dict.keys()))

        # load character
        x = rand_block_generator()
        y = rand_block_generator()
        while ((x, y) in wall_list) or ((x, y) == exit_location) or ((x, y) in food_list) or ((x, y) in enemy_dict.values()):
            x = rand_block_generator()
            y = rand_block_generator()
        self.player = Player(x, y)

        # gnerate map and get_nodes
        for i in range(0, MAX_BLOCKS):
            for j in range(0, MAX_BLOCKS):
                if (i, j) in wall_list:
                    node_list.append(Node((i, j), "wall"))
                else:
                    node_list.append(Node((i, j), "ground"))

        map = Map(node_list, food_list, exit_location, enemy_dict.keys())
        return map

    def create_map(self):
        self.map = self.map_generator(MAX_BLOCKS)

    def has_enemy(self, index):
        for enemy in self.map.get_enemy_list():
            if enemy.get_index() == index:
                return True
        return False

    def is_wall(self, index):
        node = self.map.get_node(index)
        if node.get_type() == "wall":
            return True
        return False

    def is_food(self, index):
        if index in self.map.get_food_list():
            self.map.remove_food_from_list(index)
            return True
        return False

    def update_steps(self, val):
        self.steps += val
        if self.steps < 0:
            self.steps = 0

    def update_frame(self):
        # win.fill(BLACK)
        win.blit(background, (0, 0))

        for node in self.map.get_nodes():
            if node.get_type() == "wall":
                win.blit(wall, node.get_location())
            else:
                win.blit(ground, node.get_location())

        if self.map.get_show_exit() == True:
            win.blit(exit, self.map.get_exit_location())

        for (x, y) in self.map.get_food_list():
            win.blit(food, (x*SCALE, y*SCALE))

        for enemy in self.map.get_enemy_list():
            # if enemy.type == "A":
            # print(enemyA.animationCount)
            win.blit(
                enemy1Animation[int(enemy.animationCount % 3)], enemy.get_location())
            enemy.animationCount += 1
            # check all the count vraiables to loop properly
            if enemy.animationCount >= 3:  # if animationCount + 1 >= 6 --> each frame is faster
                enemy.animationCount = 0

        # update_frame character
        win.blit(playerAnimation[int(
            self.player.animationCount % 3)], self.player.get_location())
        self.player.animationCount += 1
        # check all the count vraiables to loop properly
        if self.player.animationCount >= 3:  # if animationCount + 1 >= 6 --> each frame is faster
            self.player.animationCount = 0
        # update display
        pygame.display.update()

    def run(self):
        # main loop
        self.isRun = True
        while self.isRun:
            # set game frame rate
            # the bigger the number, the faster the frame refreshes
            clock.tick(6)

            if self.map.get_food_count() == 0:
                self.map.set_show_exit(True)
                self.map.enable_exit()
            self.is_food(self.player.get_index())

            if self.map.get_exit_enabled() == True:
                if self.player.get_index() == self.map.get_exit_index():
                    self.isRun = False
                    break

            # detect QUIT input
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    self.isRun = False
                    break
                # detect user input
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_ESCAPE):
                        self.isRun = False
                        break
                    elif (event.key == pygame.K_LEFT) and (self.is_wall((self.player.get_x() - 1, self.player.get_y())) != True):
                        self.player.move("LEFT")
                    # not(self.isOuterwall(self.player.getX()+SCALE, self.player.getY())):
                    elif (event.key == pygame.K_RIGHT) and (self.is_wall((self.player.get_x() + 1, self.player.get_y())) != True):
                        self.player.move("RIGHT")
                    # not(self.isOuterwall(self.player.getX() , self.player.getY()-SCALE)):
                    elif (event.key == pygame.K_UP) and (self.is_wall((self.player.get_x(), self.player.get_y()-1)) != True):
                        self.player.move("UP")
                    # not(self.isOuterwall(self.player.getX(), self.player.getY()+SCALE)):
                    elif (event.key == pygame.K_DOWN) and (self.is_wall((self.player.get_x(), self.player.get_y()+1)) != True):
                        self.player.move("DOWN")
                    self.pathHistory.append(self.player.get_index())
                    self.update_steps(1)

            # update game frames
            self.update_frame()
            # time.sleep(0.1)
