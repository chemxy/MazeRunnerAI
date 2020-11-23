from Game import Game
import pygame
import time
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
    print("game difficulty: " + str(theGame.difficulty))
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

            
    b1 = Block(0,0,wallLocation=Wall(0,0))
    b2 = Block(0,1)
    b3 = Block(1,0,wallLocation=Wall(1,0))
    b4 = Block(1,1,wallLocation=Wall(1,1))
    themap = {b1:[b2,b3],
                b2:[b1,b4],
                b3:[b1,b4],
                b4:[]
    }
    gameMap = Map(map_dict=themap)
    print("map: ") 
    print(gameMap)
   
    
    print("adding vertex b5")
    b5 = Block(2,2, wallLocation=(2,2))
    gameMap.addVertex(b5)
    print("adding vertex b6")
    b6 = Block(0,2, wallLocation=(0,2))
    gameMap.addVertex(b6)
    print("adding vertex b7")
    b7 = Block(1,2)
    gameMap.addVertex(b7)
    print("vertices added")
    print("map: ") 
    print(gameMap)

    print("adding edge b5-b6")
    gameMap.addEdge((b5,b6))
    print("adding edge b6-b7")
    gameMap.addEdge((b6,b7))
    print("map: ") 
    print(gameMap)
    # initializing pygame
    pygame.init()
    
    win.blit(background, (0,0))
    for node in gameMap.vertices():
        if node.isWall == True:
            #print(node.wall.location)
            win.blit(wall, node.location)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()


# main
if __name__ == "__main__":
    main1()
