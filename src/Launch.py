from Game import Game
import pygame
import time
from Map import Map
from Node import Node
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
    print("game level: " + str(theGame.level))
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

            
    b1 = Node((0,0),True)
    b2 = Node((0,1),True)
    b3 = Node((1,0),True)
    b4 = Node((1,1))
    nodelist = [b1,b2,b3,b4]

    gameMap = Map(nodelist)
    print("map: ") 
    print(gameMap)
   
    
    print("adding vertex b5")
    b5 = Node((1,2),True)
    gameMap.addNode(b5)
    print("adding vertex b6")
    b6 = Node((2,1))
    gameMap.addNode(b6)
    print("adding vertex b7")
    b7 = Node((2,2), True)
    gameMap.addNode(b7)
    print("vertices added")
    print("map: ") 
    print(gameMap)

    # initializing pygame
    pygame.init()
    
    win.blit(background, (0,0))
    for node in gameMap.nodes():
        if node.isWall == True:
            #print(node.wall.location)
            win.blit(wall, node.location)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()


# main
if __name__ == "__main__":
    main2()
