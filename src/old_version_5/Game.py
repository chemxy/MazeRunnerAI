from GameEngine import Game
import pygame
import time
from Map import Map
from Node import Node


def main():
    # initializing pygame
    pygame.init()

    # create a game instance
    theGame = Game()
    theGame.create_map()
    print("game begin!")

    # run game
    theGame.run()
    print("game end.")
    print("game level: " + str(theGame.level))
    print("steps: " + str(theGame.steps))

    # stop pygame
    pygame.quit()


# main
if __name__ == "__main__":
    main()
