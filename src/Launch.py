from Game import Game
import pygame
from Map import Map
from Block import Block
from Object import Wall, Object, Food

def main1():
    # initializing pygame
    pygame.init()
    
    # create a game instance
    theGame = Game()
    print("game begin!")
    
    # run game 
    theGame.run()
    print("game end.")
    print("steps: " + str(theGame.stepsCount))
    
    #stop pygame 
    pygame.quit()

def main2():
        
    # set pictures and animations' sources and canvas dimensions
    map_size = 500  
    win = pygame.display.set_mode((map_size, map_size))


    wall = pygame.image.load('../images/Outerwall1.png')
    food = pygame.image.load('../images/Food.png')
    background = pygame.image.load('../images/Background.png')

    BLACK = pygame.Color(0, 0, 0)

    b1 = Block(isWall=Wall(0,0))
    b2 = Block(isWall=Wall(0,1))
    b3 = Block(isWall=Wall(1,0))
    b4 = Block(isWall=Wall(1,1))
    themap = {b1:[b2,b3],
                b2:[b1,b4],
                b3:[b1,b4],
                b4:[b2,b3]
    }
    gameMap = Map(map_dict=themap)
    print("map: ") 
    print(gameMap)
    print("nodes: ")
    print(gameMap.vertices())
    print("edges: ")  
    print(gameMap.edges())

    # initializing pygame
    pygame.init()
    while True:      
        win.blit(background, (0,0))
        for node in gameMap.vertices():
            #print(node.wall.location)
            win.blit(wall, node.wall.location)
        pygame.display.update()
    pygame.quit()


# main
if __name__ == "__main__":
    main1()
