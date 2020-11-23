"""
@Author: Xingyun Chen
@Github: github.com/chemxy
@All Copyright Reserved.

"""
import pygame
import random
import time
from math import floor,log10, log
from Object import Object, Food, Wall, ExitPoint
from Player import Player
from Enemy import Enemy
from Map import Map
from Block import Block


# setting up some global variables...

# set up game clock
clock = pygame.time.Clock()

# set game tittle
pygame.display.set_caption("Survival!")

# set pictures and animations' sources and canvas dimensions
map_size = 500  
win = pygame.display.set_mode((map_size, map_size))


MAX_BLOCKS = int(map_size/50)
print("max blocks: "+ str(MAX_BLOCKS) + "x" + str(MAX_BLOCKS))

playerAnimation = [pygame.image.load('../images/PlayerIdle1.png'), pygame.image.load('../images/PlayerIdle2.png'), pygame.image.load('../images/PlayerIdle3.png'), pygame.image.load('../images/PlayerIdle4.png'), pygame.image.load('../images/PlayerIdle5.png'), pygame.image.load('../images/PlayerIdle6.png')]
enemy1Animation = [pygame.image.load('../images/Enemy1_1.png'), pygame.image.load('../images/Enemy1_2.png'), pygame.image.load('../images/Enemy1_3.png')]
#enemy2 = [pygame.image.load('../images/Enemy2_1.png'), pygame.image.load('../images/Enemy2_2.png'), pygame.image.load('../images/Enemy2_3.png')]
wall = pygame.image.load('../images/Outerwall1.png')
food = pygame.image.load('../images/Food.png')
exit = pygame.image.load('../images/Exit.png')
background = pygame.image.load('../images/Background.png')

BLACK = pygame.Color(0, 0, 0)

# end setting-up

def randomBlockGenerator():
    # the number of total blocks (each block is 50x50 pixels)
    x = random.randint(1,MAX_BLOCKS-2)
    #print(x)
    return x

class Game:
    def __init__(self):
        # set difficulty
        self.difficulty = 1
        self.stepsCount = 0
        self.level = 1

        # load environment
        self.wallList = self.wallGenerator() #only contains walls
        print("wall list: " + str(self.wallList))

        self.exitPt = self.exitGenerator() # exit point location
        print("exit point: " + str(self.exitPt))
        
        self.foodDict = self.foodGenerator()
        print("food list: " + str(self.foodDict))
        
        # generate enemies
        self.enemyDict = self.enemyGenerator()
        print("enemy count: " + str(len(self.enemyDict.keys())))
        print("keys: " + str(self.enemyDict.keys()))
        print("vals: " + str(self.enemyDict.values()))

        # load character
        self.player = self.playerGenerator()
        print("player initial location: " + str(self.player.index))


        
    def isFood(self, x, y):
        for key in self.foodDict.keys():
            #print(key)
            if self.foodDict[key] == (x,y):
                self.foodDict.pop(key)
                return True
        #print(" not in list")
        return False

    def isExit(self,x, y):
        if (x,y) == self.exitPt:
            return True
        return False

    def isEnemy(self, x, y):
        if (x,y) in self.enemyDict.values():
            return True
        return False

    """" this generates the walls as well as the exit """
    def wallGenerator(self):
        #tempwalls = []
        wallList = []
        for i in range(0, MAX_BLOCKS):
            for j in range(0, MAX_BLOCKS):
                if (i == 0) or (j == 0) or (i == MAX_BLOCKS-1) or (j == MAX_BLOCKS-1):
                    wallList.append((i,j))
        
        wallCount = random.randint(5,20)
        print("wallcount: " + str(wallCount))
        for i in range(wallCount):
            x = randomBlockGenerator() 
            y = randomBlockGenerator() 
            while (x,y) in wallList:
                x = randomBlockGenerator() 
                y = randomBlockGenerator() 
            wallList.append((x,y))
        return wallList        
    
    def exitGenerator(self):
        x = randomBlockGenerator() 
        y = randomBlockGenerator() 
        while (x,y) in self.wallList:
            x = randomBlockGenerator() 
            y = randomBlockGenerator() 
        return (x,y)

    def foodGenerator(self):
        foodDict = {}
        foodCount = random.randint(0,3) 
        print("foodcount: " + str(foodCount))
        for i in range(foodCount):
            x =  randomBlockGenerator()
            y =  randomBlockGenerator()
            while ((x,y) in self.wallList) or ((x,y) == self.exitPt) or ((x,y) in foodDict.values()):
                x = randomBlockGenerator()
                y = randomBlockGenerator()         
            temp = Food(x,y)
            foodDict[temp] = (x,y)
        return foodDict

    def enemyGenerator(self):
        #enemyList = []
        enemyDict = {}
        for i in range(floor(log(self.difficulty))):
            x =  randomBlockGenerator()
            y =  randomBlockGenerator()
        #typeOfenemy = ""
        #result = random.randint(1,100) #1-100
        #if(result > 33):
        #    typeOfenemy = "A"
        #else:
        #    typeOfenemy = "B"
            while ((x,y) in self.wallList) or ((x,y) == self.exitPt) or ((x,y) in self.foodDict.values() or (x,y) in enemyDict.values()):
                x = randomBlockGenerator()
                y = randomBlockGenerator()    
            temp = Enemy(x,y)     
            #enemyList.append((x,y))
            enemyDict[temp] = (x,y)
        return enemyDict

    def playerGenerator(self):
        x =  randomBlockGenerator()
        y =  randomBlockGenerator()
        while ((x,y) in self.wallList) or ((x,y) == self.exitPt) or ((x,y) in self.foodDict.values() or (x,y) in self.enemyDict.values()):
            x = randomBlockGenerator()
            y = randomBlockGenerator()         
        
        return Player(x,y)

    def updateSteps(self, val):
        self.stepsCount += val
        if self.stepsCount < 0:
            self.stepsCount = 0

    def updateFrame(self):
        #win.fill(BLACK)
        win.blit(background, (0,0))
        
        win.blit(exit, (self.exitPt[0]*50, self.exitPt[1]*50))
        
        for (x,y) in self.wallList:
            #print(item)
            win.blit(wall, (x*50, y*50))

        for (x,y) in self.foodDict.values():
            win.blit(food, (x*50, y*50))
        
        for (x,y) in self.enemyDict.values():
            #if enemy.type == "A":
            enemyA = Enemy(x,y)
            #print(enemyA.animationCount)
            win.blit(enemy1Animation[int(enemyA.animationCount%3)], enemyA.location)
            enemyA.animationCount += 1
            # check all the count vraiables to loop properly
            if enemyA.animationCount >= 3:  # if animationCount + 1 >= 6 --> each frame is faster
                enemyA.animationCount = 0
            #else:
            #    win.blit(enemy2[int(enemy.animationCount%6)], (int(enemy.x), int(enemy.y)))
            #    enemy.animationCount += 1
                # check all the count vraiables to loop properly
            #    if enemy.animationCount + 1 > 3:  # if animationCount + 1 >= 6 --> each nod is faster
            #        enemy.animationCount = 0
        # updateFrame character
        win.blit(playerAnimation[int(self.player.animationCount%3)], self.player.location)
        self.player.animationCount += 1
        # check all the count vraiables to loop properly
        if self.player.animationCount >= 3:  # if animationCount + 1 >= 6 --> each frame is faster
            self.player.animationCount = 0
        # update display
        pygame.display.update()
    
    def run(self):
        # main loop
        isRun = True
        while isRun:
            # set game frame rate
            clock.tick(30) # the bigger the number, the faster the frame refreshes
            # detect QUIT input
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    isRun = False
                    break
                #detect user input
                elif event.type == pygame.KEYDOWN:
                    #prev = str(self.player.x) + "," + str(self.player.y)
                    if (event.key == pygame.K_ESCAPE):
                        isRun = False
                        break
                    elif (event.key == pygame.K_LEFT ) and ((self.player.x - 1,self.player.y) not in self.wallList): #not(self.isOuterwall(self.player.x -50, self.player.y)):    
                        self.player.move("LEFT")
                    elif (event.key == pygame.K_RIGHT )  and ((self.player.x + 1,self.player.y) not in self.wallList): #not(self.isOuterwall(self.player.x+50, self.player.y)):   
                        self.player.move("RIGHT")
                    elif (event.key == pygame.K_UP ) and ((self.player.x,self.player.y-1) not in self.wallList): #not(self.isOuterwall(self.player.x , self.player.y-50)):      
                        self.player.move("UP")
                    elif (event.key == pygame.K_DOWN ) and ((self.player.x,self.player.y+1) not in self.wallList): #not(self.isOuterwall(self.player.x, self.player.y+50)):   
                        self.player.move("DOWN")
                    self.updateSteps(1)
                    # check if there is food or exit in the location         
                    if(self.isFood(self.player.x, self.player.y)):
                        #self.player.life += 10
                        print("food + 1")
                        self.updateSteps(-10)

                    # check if there is the exit point
                    if(self.isExit(self.player.x, self.player.y)):
                        print("this is exit!")
                        isRun = False
                        break

                    """ when encountered an enemy: steps + 50 or end of game ? """
                    if(self.isEnemy(self.player.x, self.player.y)):  
                        print("encounter enemy!")
                        isRun = False
                        break       
                    #after = str(self.player.x) + "," + str(self.player.y)
                    #print("player move from " + prev + " to " + after)
            #update game frames
            self.updateFrame()
            time.sleep(0.1)
