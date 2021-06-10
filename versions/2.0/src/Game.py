import pygame
from Agent import Agent
from CellType import CellType
from Map import Map
from Direction import Direction

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
        self.__isRun = False
        self.__render_scale = 50    # set render scale
        self.__animation_count = 0

    def init_map(self, map_path):
        self.__map = Map(map_path) # init map canvas

    def get_map(self):
        return self.__map    

    def init_agent(self):
        self.__agent = Agent()   # init an agent

    """scale the coordinates by a factor
    """
    def __scale(self, coordinates): 
        return tuple([coordinate * self.__render_scale for coordinate in coordinates])

    def move(self, direction):
        x = self.get_map().get_agent_coordinates()[0]
        y = self.get_map().get_agent_coordinates()[1]
        if direction == Direction.UP:
            new_coordinates = (x, y-1)
        elif direction == Direction.DOWN:
              new_coordinates = (x, y+1)
        elif  direction == Direction.LEFT:
            new_coordinates = (x-1, y)
        elif  direction == Direction.RIGHT:
           new_coordinates = (x+1, y)

        if self.get_map().get_cell_at(new_coordinates).get_cell_type() is not CellType.WALL:
            self.get_map().set_agent_coordinates(new_coordinates)
    
    def render(self):
        # win.fill(BLACK)
        window.blit(background, (0, 0))
        
        # render walls, exit, traps and enemies on the map
        for k,v in self.get_map().get_cells().items():  
            if v.get_cell_type() == CellType.WALL:    # wall
                window.blit(wall_pic, self.__scale(k))
            elif v.get_cell_type() == CellType.EXIT:   # exit
                 window.blit(exit_pic, self.__scale(k))
            elif v.get_cell_type() == CellType.GOLD:   # gold
                window.blit(food_pic, self.__scale(k))
            elif v.get_cell_type() == CellType.TRAP:  # trap
                window.blit(trap_pic, self.__scale(k))
            elif v.get_cell_type() == CellType.ENEMY: # enemy
                window.blit(enemy1Animation[int(v.get_cell_type_value().animationCount % 3)], self.__scale(k))
                if self.__animation_count % 15  == 0:
                    v.get_cell_type_value().animationCount += 1

        # render the character on the map
       
        window.blit(playerAnimation[int(self.__agent.animationCount % 3)], self.__scale(self.__map.get_agent_coordinates()))
        if self.__animation_count % 15  == 0:
            self.__agent.animationCount += 1
        
        self.__animation_count += 1

        # update display
        pygame.display.update()

    def run(self):
        # main loop
        self.__isRun = True
        while self.__isRun:
           
            clock.tick(60)    # set game frame rate. the bigger the number, the faster the frame refreshes
            self.render()    # render the game

            # detect QUIT command from user inputs
            for event in pygame.event.get():
                # print(event.type)
                if event.type == pygame.QUIT:   # if user directly close the game window
                    self.__isRun = False
                    break   
                elif event.type == pygame.KEYDOWN:  # if the user press Escape key
                    if (event.key == pygame.K_ESCAPE):
                        self.__isRun = False
                        break
                    elif (event.key == pygame.K_LEFT):
                        self.move(Direction.LEFT)
                    # not(self.isOuterwall(self.player.getX()+SCALE, self.player.getY())):
                    elif (event.key == pygame.K_RIGHT):
                        self.move(Direction.RIGHT)
                    # not(self.isOuterwall(self.player.getX() , self.player.getY()-SCALE)):
                    elif (event.key == pygame.K_UP):
                        self.move(Direction.UP)
                    # not(self.isOuterwall(self.player.getX(), self.player.getY()+SCALE)):
                    elif (event.key == pygame.K_DOWN):
                        self.move(Direction.DOWN)



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
