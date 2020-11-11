"""
@Author: Xingyun Chen
@Github: github.com/chemxy
@All Copyright Reserved.

"""
import pygame
import random
import time
from Object import Object
from Player import Player
from Enemy import Enemy

# setting up some global variables...

# set up game clock
clock = pygame.time.Clock()

# set game tittle
pygame.display.set_caption("Survival!")

# set pictures and animations' sources and canvas dimensions
map_size = 600  
win = pygame.display.set_mode((map_size, map_size))


MAX_BLOCKS = int(map_size/50)
print("max blocks: "+ str(MAX_BLOCKS) + "x" + str(MAX_BLOCKS))

playerIdle = [pygame.image.load('../images/PlayerIdle1.png'), pygame.image.load('../images/PlayerIdle2.png'), pygame.image.load('../images/PlayerIdle3.png'), pygame.image.load('../images/PlayerIdle4.png'), pygame.image.load('../images/PlayerIdle5.png'), pygame.image.load('../images/PlayerIdle6.png')]
enemy1 = [pygame.image.load('../images/Enemy1_1.png'), pygame.image.load('../images/Enemy1_2.png'), pygame.image.load('../images/Enemy1_3.png')]
enemy2 = [pygame.image.load('../images/Enemy2_1.png'), pygame.image.load('../images/Enemy2_2.png'), pygame.image.load('../images/Enemy2_3.png')]
innerWall = pygame.image.load('../images/InnerWall1.png')
outerwall1 = pygame.image.load('../images/Outerwall1.png')
outerwall2 = pygame.image.load('../images/Outerwall2.png')
food = pygame.image.load('../images/Food.png')
exit = pygame.image.load('../images/Exit.png')
background = pygame.image.load('../images/Background.png')

BLACK = pygame.Color(0, 0, 0)

types = {"innerWall":1, "outerwall":2, "exit":3, "food":4, "enemy":5, "player": 6 }

mov_value = 50

# end setting-up

def randomBlockGenerator():
    # the number of total blocks (each block is 50x50 pixels)
    return random.randint(1,MAX_BLOCKS-2) * 50


class Game:
    def __init__(self):
        self.isRun = True
        # set difficulty
        self.difficulty = 1
        self.stepsCount = 0
        self.level = 1

        # load environment
        self.walls = [] #only contains outerwall1
        self.foods = []
        self.exit = self.wallGenerator()
        #print(self.exit)
      
        self.foodGenerator()
      
        # generate enemies
        self.enemies = [] 
        for i in range(random.randint(1, self.difficulty)):
            self.enemyGenerator()
 
        # load character
        self.player = self.playerGenerator()
        print("player initial location: " + str(self.player.x) + " " + str(self.player.y))


    def isOuterwall(self, x, y):
        #print(str(x) + " " + str(y))
        temp = Object(x,y,"outerwall")
        if self.isSameLocation(temp, self.walls):
            return True   
        #print("not outerwall")
        return False

    """ this checks if this nodeA's location is the same as any node's location in listA """
    def isSameLocation(self,objcA,listA): 
        #print("nodeA: " + str(nodeA))
        for item in listA:
            if objcA.isSameLocation(item):
                #print(" already in list")
                return True
        #print(" not in list")
        return False
        
    def isFood(self, x, y):
        temp = Object(x, y, "food")
        #print(str(item.x) + " " + str(item.y))
        for item in self.foods:
            if item.isEqual(temp):
                #print(" already in list")
                self.foods.remove(item)
                return True
        #print(" not in list")
        return False

    def isExit(self,x, y):
        if self.exit == (x,y):
            return True
        return False

    def isEnemy(self, x, y):
        for enemy in self.enemies:
            if enemy.x == x and enemy.y == y:
                return True
        return False

    def isOutOfBound(self,x ,y):
        if(x < 50 or x >= map_size-50 or y < 50 or y >= map_size-50):
            return True
        else:
            return False

    """" this generates the walls as well as the exit """
    def wallGenerator(self):
        for i in range(0, MAX_BLOCKS):
            for j in range(0, MAX_BLOCKS):
                if (i == 0) or (j == 0) or (i == MAX_BLOCKS-1) or (j == MAX_BLOCKS-1):
                    temp = Object(i*50,j*50, "outerwall")
                    #temp.toString()
                    self.walls.append(temp)
            
        #print(self.walls)            

        wallCount = random.randint(25,45)
        print("wallcount: " + str(wallCount))
        for i in range(wallCount):
            temp = Object(randomBlockGenerator(), randomBlockGenerator(), "outerwall")
            while self.isSameLocation(temp, self.walls):
                temp = Object(randomBlockGenerator(), randomBlockGenerator(), "outerwall")
            self.walls.append(temp)
        #print(self.walls)        

        tempExit = Object(randomBlockGenerator(), randomBlockGenerator(), "exit")
        while self.isSameLocation(tempExit, self.walls):
            tempExit = Object(randomBlockGenerator(), randomBlockGenerator(), "outerwall")
        return tempExit.getLocation()


    def foodGenerator(self):
        foodCount = random.randint(1,3) 
        print("foodcount: " + str(foodCount))
        for i in range(foodCount):
            x =  randomBlockGenerator()
            y =  randomBlockGenerator()
            temp = Object(x, y, "food")
            #print("food temp: " + str(temp))
            #temp.toString()
            while(self.isOutOfBound(x,y) or self.isOuterwall(x,y) or self.isExit(x,y) or self.isSameLocation(temp, self.walls) or self.isSameLocation(temp, self.foods) ):
                x = randomBlockGenerator()
                y = randomBlockGenerator()         
                temp = Object(x,y,"food")
                #print("food already in list")
                #print("food not in foods")
            self.foods.append(temp)

    def playerGenerator(self):
        x =  randomBlockGenerator()
        y =  randomBlockGenerator()
        temp = Object(x,y,"player")
        while(self.isOutOfBound(x,y) or self.isOuterwall(x,y) or self.isExit(x,y) or self.isSameLocation(temp, self.walls) or self.isSameLocation(temp, self.foods) ):     
            x = randomBlockGenerator()
            y = randomBlockGenerator()         
            temp = Object(x,y,"player")

        return Player(x,y)

    def enemyGenerator(self):
        x =  randomBlockGenerator()
        y =  randomBlockGenerator()
        temp = Object(x,y,"enemy")
        while(self.isOutOfBound(x,y) or self.isOuterwall(x,y) or self.isExit(x,y) or self.isSameLocation(temp, self.walls) or self.isSameLocation(temp, self.foods) ):            
            x = randomBlockGenerator()
            y = randomBlockGenerator()         
            temp = Object(x,y,"enemy")

        result = random.randint(1,100) #1-100
        if(result > 33):
            temp = Enemy(x,y,"A")
            self.enemies.append(temp)

        else:
            temp = Enemy(x,y,"B")
            self.enemies.append(temp)

    def updateFrame(self):
        #win.fill(BLACK)
        win.blit(background, (0,0))
        win.blit(exit, self.exit)
        
        for item in self.walls:
            #print(item)
            win.blit(outerwall1, item.location)

        for item in self.foods:
            win.blit(food, item.location)
        
        for enemy in self.enemies:
            if enemy.type == "A":
                    win.blit(enemy1[int(enemy.idleCount%6)], (int(enemy.x), int(enemy.y)))
                    enemy.idleCount += 1
                    # check all the count vraiables to loop properly
                    if enemy.idleCount + 1 > 3:  # if idleCount + 1 >= 6 --> each frame is faster
                        enemy.idleCount = 0
            else:
                win.blit(enemy2[int(enemy.idleCount%6)], (int(enemy.x), int(enemy.y)))
                enemy.idleCount += 1
                # check all the count vraiables to loop properly
                if enemy.idleCount + 1 > 3:  # if idleCount + 1 >= 6 --> each nod is faster
                    enemy.idleCount = 0
        # updateFrame character
        win.blit(playerIdle[int(self.player.idleCount%6)], (int(self.player.x), int(self.player.y)))
        self.player.idleCount += 1
        # check all the count vraiables to loop properly
        if self.player.idleCount + 1 > 3:  # if idleCount + 1 >= 6 --> each frame is faster
            self.player.idleCount = 0
        # update display
        pygame.display.update()
    

    def run(self):
        # main loop
        while self.isRun:
            #time.sleep(0.05)
            # set game frame rate
            clock.tick(9) # the bigger the number, the faster the frame refreshes
            # detect QUIT input
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    self.isRun = False
                    break
                    
                #detect user input
                elif event.type == pygame.KEYDOWN:
                    
                    #prev = str(self.player.x) + "," + str(self.player.y)
                    
                    if (event.key == pygame.K_ESCAPE):
                        self.isRun = False
                        break
                        
                    elif (event.key == pygame.K_LEFT ) and not(self.isOuterwall(self.player.x -50, self.player.y)):    
                        self.player.x -= mov_value
                        self.stepsCount += 1
                    elif (event.key == pygame.K_RIGHT )  and not(self.isOuterwall(self.player.x+50, self.player.y)):   
                        self.player.x += mov_value
                        self.stepsCount += 1
                    elif (event.key == pygame.K_UP ) and not(self.isOuterwall(self.player.x , self.player.y-50)):      
                            self.player.y -= mov_value
                            self.stepsCount += 1
                    elif (event.key == pygame.K_DOWN ) and not(self.isOuterwall(self.player.x, self.player.y+50)):   
                            self.player.y += mov_value
                            self.stepsCount += 1
                    # check if there is food or exit in the location         
                    if(self.isFood(self.player.x, self.player.y)):
                        self.player.life += 10
                    if(self.isExit(self.player.x, self.player.y)):
                        print("this is exit!")
                        self.isRun = False
                        break
                    if(self.isEnemy(self.player.x, self.player.y)):        
                        print("encounter enemy!")
                        self.isRun = False
                        break       
                    #after = str(self.player.x) + "," + str(self.player.y)
                    #print("player move from " + prev + " to " + after)
            #update game frames
            self.updateFrame()
            time.sleep(0.1)
    