"""
@Author: Xingyun Chen
@Github: github.com/chemxy
"""
import pygame
import random
import time
from math import floor,log10, log
from Object import Object, Food, Wall, ExitPoint
from Player import Player
from Enemy import Enemy
from Map import Map
from Node import Node


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
        # set level
        self.level = 10
        self.stepsCount = 0
               
        #generate enemy dictionary
        self.enemyList = []

        #genreate player
        self.Player=None

        #initialize map
        self.gameMap = self.mapGenerator(MAX_BLOCKS)

    def mapGenerator(self, MAX_BLOCKS):
        nodelist = []
        # generate wallList
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
        print("wall list: " + str(wallList))
        
        #generate exit point
        x = randomBlockGenerator() 
        y = randomBlockGenerator() 
        while (x,y) in wallList:
            x = randomBlockGenerator() 
            y = randomBlockGenerator() 
        exitPt = (x,y)

        #generate foodList
        foodList = []
        foodCount = random.randint(0,3) 
        print("foodcount: " + str(foodCount))
        for i in range(foodCount):
            x =  randomBlockGenerator()
            y =  randomBlockGenerator()
            while ((x,y) in wallList) or ((x,y) == exitPt) or ((x,y) in foodList):
                x = randomBlockGenerator()
                y = randomBlockGenerator()         
            foodList.append((x,y))

        #gnerate map and nodes
        for i in range(0, MAX_BLOCKS):
            for j in range(0, MAX_BLOCKS):
                if (i,j) in wallList:
                    nodelist.append(Node((i,j), isWall=True))
                else:
                    if (i,j) == exitPt:
                        nodelist.append(Node((i,j), isExit=True))
                    elif (i,j) in foodList:
                        nodelist.append(Node((i,j), containsFood=True))
                    else:
                        nodelist.append(Node((i,j)))
        gameMap = Map(nodelist)

        # generate enemies
        enemyList = []
        for i in range(floor(log(self.level))):
            x =  randomBlockGenerator()
            y =  randomBlockGenerator()
        #typeOfenemy = ""
        #result = random.randint(1,100) #1-100
        #if(result > 33):
        #    typeOfenemy = "A"
        #else:
        #    typeOfenemy = "B"
            while ((x,y) in wallList) or ((x,y) == exitPt) or ((x,y) in foodList) or ((x,y) in enemyList):
                x = randomBlockGenerator()
                y = randomBlockGenerator()    
                
            enemyList.append(Enemy(x,y))
            
        self.enemyList = enemyList
        print("enemy list: " + str(enemyList))
        print("enemy count: " + str(len(enemyList)))
       
        # load character
        x =  randomBlockGenerator()
        y =  randomBlockGenerator()
        while ((x,y) in wallList) or ((x,y) == exitPt) or ((x,y) in foodList) or ((x,y) in enemyList):
            x = randomBlockGenerator()
            y = randomBlockGenerator()         
        self.player =  Player(x,y)

        return gameMap
    
    def isEnemy(self, index):
        for enemy in self.enemyList:
            if enemy.index == index:
                return True
        return False
    

    def checkNode(self, index):
        node = self.gameMap.getNode(index)
        if node != None:
            if node.isWall == True:
                return "wall"
            elif node.isExit == True:
                return "exit"
            elif node.containsFood == True:
                return "food"
            else:
                return "none"
        

    def updateSteps(self, val):
        self.stepsCount += val
        if self.stepsCount < 0:
            self.stepsCount = 0

    def updateFrame(self):
        #win.fill(BLACK)
        win.blit(background, (0,0))
        
        for node in self.gameMap.nodes():
            if node.isWall == True:
                win.blit(wall, node.location)
            else:
                if node.isExit == True:
                    win.blit(exit, node.location)
                elif node.containsFood == True:
                    win.blit(food, node.location)

        """
        win.blit(exit, (self.exitPt[0]*50, self.exitPt[1]*50))
        
        for (x,y) in self.wallList:
            #print(item)
            win.blit(wall, (x*50, y*50))

        for (x,y) in self.foodDict.values():
            win.blit(food, (x*50, y*50))
        """
        for enemy in self.enemyList:
            #if enemy.type == "A":
            #print(enemyA.animationCount)
            win.blit(enemy1Animation[int(enemy.animationCount%3)], enemy.location)
            enemy.animationCount += 1
            # check all the count vraiables to loop properly
            if enemy.animationCount >= 3:  # if animationCount + 1 >= 6 --> each frame is faster
                enemy.animationCount = 0
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
                    if (event.key == pygame.K_ESCAPE):
                        isRun = False
                        break
                    elif (event.key == pygame.K_LEFT ) and (self.checkNode((self.player.x - 1,self.player.y)) != "wall"): #not(self.isOuterwall(self.player.x -50, self.player.y)):    
                        self.player.move("LEFT")
                    elif (event.key == pygame.K_RIGHT )  and (self.checkNode((self.player.x + 1,self.player.y)) != "wall"): #not(self.isOuterwall(self.player.x+50, self.player.y)):   
                        self.player.move("RIGHT")
                    elif (event.key == pygame.K_UP ) and (self.checkNode((self.player.x,self.player.y-1)) != "wall"): #not(self.isOuterwall(self.player.x , self.player.y-50)):      
                        self.player.move("UP")
                    elif (event.key == pygame.K_DOWN ) and (self.checkNode((self.player.x,self.player.y+1)) != "wall"): #not(self.isOuterwall(self.player.x, self.player.y+50)):   
                        self.player.move("DOWN")
                    self.updateSteps(1)
                    
                    # check if there is the exit point
                    if(self.checkNode(self.player.index) == "exit"):
                        print("this is exit!")
                        isRun = False
                        break

                    #when encountered an enemy: steps + 50 or end of game ? 
                    if(self.isEnemy(self.player.index)):  
                        print("encounter enemy!")
                        isRun = False
                        break       
                    
                    # check if there is food or exit in the location         
                    if(self.checkNode(self.player.index) == "food"):
                        #self.player.life += 10
                        print("food + 1")
                        self.updateSteps(-10)
                        self.gameMap.changeFood(self.player.index, flag=False)

                   
                   
            #update game frames
            self.updateFrame()
            time.sleep(0.1)
