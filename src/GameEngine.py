"""
@Author: Xingyun Chen
@Github: github.com/chemxy
"""
import pygame
from Agent import Agent
from Enemy import Enemy
from Canvas import Canvas


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


class Game:
    def __init__(self):
        # set level
        self.level = 1

        self.isRun = True

        self.__canvas = Canvas("../maps/map_1.txt") # init map canvas

        (x, y) = self.__canvas.get_start_coordinates()
        self.__agent = Agent(x,y)   # init an agent



    def render(self):
        # win.fill(BLACK)
        win.blit(background, (0, 0))

        # for node in self.map.get_nodes():
        #     if node.get_type() == "wall":
        #         win.blit(wall, node.get_location())
        #     else:
        #         win.blit(ground, node.get_location())

        # if self.map.get_show_exit() == True:
        #     win.blit(exit, self.map.get_exit_location())

        # for (x, y) in self.map.get_food_list():
        #     win.blit(food, (x*SCALE, y*SCALE))

        # for enemy in self.map.get_enemy_list():
        #     # if enemy.type == "A":
        #     # print(enemyA.animationCount)
        #     win.blit(enemy1Animation[int(enemy.animationCount % 3)], enemy.get_location())
        #     enemy.animationCount += 1
        #     # check all the count vraiables to loop properly
        #     if enemy.animationCount >= 3:  # if animationCount + 1 >= 6 --> each frame is faster
        #         enemy.animationCount = 0

        # # render agent
        win.blit(playerAnimation[int(
            self.__agent.animationCount % 3)], self.__agent.get_location())
        self.__agent.animationCount += 1
        # check all the count vraiables to loop properly
        if self.__agent.animationCount >= 3:  # if animationCount + 1 >= 6 --> each frame is faster
            self.__agent.animationCount = 0

        # update display
        pygame.display.update()

    def run(self):
        # main loop
        self.isRun = True
        while self.isRun:
            # set game frame rate
            # the bigger the number, the faster the frame refreshes
            clock.tick(6)

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
                   

            # update game frames
            self.render()
            # time.sleep(0.1)


# test and debug
if __name__ == "__main__":   
    pygame.init()
    game = Game()
    
    print("game starts running.")
    game.run()
    print("game ends.")

    pygame.quit()
