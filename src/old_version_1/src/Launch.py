from Game import Game
import pygame

def main():
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

# main
if __name__ == "__main__":
    main()
