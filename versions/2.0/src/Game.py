import pygame
from Character import Character
from Map import Map

# setting up some global variables...

# set up game clock
clock = pygame.time.Clock()

# set game tittle
pygame.display.set_caption("Survival!")

# set pictures and animations' sources and canvas dimensions
map_size = 500
window = pygame.display.set_mode((map_size, map_size))

root_path = "../../../"
images_path = root_path + "/images"
maps_path = root_path + "/maps"

playerAnimation = [pygame.image.load(images_path + '/PlayerIdle1.png'), 
                    pygame.image.load(images_path + '/PlayerIdle2.png'), 
                    pygame.image.load(images_path + '/PlayerIdle3.png'),
                   pygame.image.load(images_path + '/PlayerIdle4.png'), 
                   pygame.image.load(images_path + '/PlayerIdle5.png'), 
                   pygame.image.load(images_path + '/PlayerIdle6.png')]
enemy1Animation = [pygame.image.load(images_path + '/Enemy1_1.png'), 
                pygame.image.load(images_path + '/Enemy1_2.png'), 
                pygame.image.load(images_path + '/Enemy1_3.png')]
# enemy2Animation = [pygame.image.load(images_path + '/Enemy2_1.png'), 
#           pygame.image.load(images_path + '/Enemy2_2.png'), 
#           pygame.image.load(images_path + '/Enemy2_3.png')]
wall_pic = pygame.image.load(images_path + '/OuterWall1.png')
trap_pic = pygame.image.load(images_path + '/Trap.png')
ground_pic = pygame.image.load(images_path + '/InnerWall1.png')
food_pic = pygame.image.load(images_path + '/Food.png')
exit_pic = pygame.image.load(images_path + '/Exit.png')
background = pygame.image.load(images_path + '/Background.png')

class Game:
    def __init__(self):
        
        self.level = 1  # init level
        self.isRun = True   # let game run
        self.__render_scale = 50    # set render scale

    def init_map(self, map_path):
        self.__map = Map(map_path) # init map canvas

    def get_map(self):
        return self.__map    

    def init_agent(self):
        self.__agent = Character(self.__map.get_start_coordinates())   # init an agent

    def __scale_coordinates(self, coordinates):
        return tuple([coordinate * self.__render_scale for coordinate in coordinates])

    def render(self):
        # win.fill(BLACK)
        window.blit(background, (0, 0))
        
        # render walls, exit, traps and enemies on the map
        for k,v in self.get_map().get_map().items():
            if v.is_wall() is True:
                window.blit(wall_pic, self.__scale_coordinates(k))
            elif v.is_exit() is True:
                 window.blit(exit_pic, self.__scale_coordinates(k))
            elif v.has_gold() is True:
                window.blit(food_pic, self.__scale_coordinates(k))
            elif v.has_trap() is True:
                window.blit(trap_pic, self.__scale_coordinates(k))
            elif v.get_enemy() is not None:
                window.blit(enemy1Animation[int(v.get_enemy().animationCount % 3)], self.__scale_coordinates(k))
                v.get_enemy().animationCount = (v.get_enemy().animationCount + 1)  % 3

        # render the character on the map
        window.blit(playerAnimation[int(self.__agent.animationCount % 3)], self.__scale_coordinates(self.__agent.get_coordinates()))
        self.__agent.animationCount =  (self.__agent.animationCount + 1) % 3
      
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
    game.init_map(maps_path + "/map_1.txt")
    game.init_agent()
    
    print("game starts running.")
    game.run()
    print("game ends.")

    pygame.quit()
