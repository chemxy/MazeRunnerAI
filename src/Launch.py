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

# main
if __name__ == "__main__":
    main1()
