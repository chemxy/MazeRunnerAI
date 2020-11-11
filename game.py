"""
@Author: Xingyun Chen
@Github: github.com/chemxy
@All Copyright Reserved.

"""
import pygame
import random
import time

# some global variables


# set up game clock
clock = pygame.time.Clock()

# set game tittle
pygame.display.set_caption("Survival!")

# set pictures and animations' sources and canvas dimensions
map_size = 600  
win = pygame.display.set_mode((map_size, map_size))


MAX_BLOCKS = int(map_size/50)
print("max blocks: "+ str(MAX_BLOCKS) + "x" + str(MAX_BLOCKS))

playerIdle = [pygame.image.load('PlayerIdle1.png'), pygame.image.load('PlayerIdle2.png'), pygame.image.load('PlayerIdle3.png'), pygame.image.load('PlayerIdle4.png'), pygame.image.load('PlayerIdle5.png'), pygame.image.load('PlayerIdle6.png')]
enemy1 = [pygame.image.load('Enemy1_1.png'), pygame.image.load('Enemy1_2.png'), pygame.image.load('Enemy1_3.png')]
enemy2 = [pygame.image.load('Enemy2_1.png'), pygame.image.load('Enemy2_2.png'), pygame.image.load('Enemy2_3.png')]
innerWall = pygame.image.load('InnerWall1.png')
outterWall1 = pygame.image.load('OutterWall1.png')
outterWall2 = pygame.image.load('OutterWall2.png')
food = pygame.image.load('Food.png')
exit = pygame.image.load('Exit.png')
background = pygame.image.load('Background.png')


BLACK = pygame.Color(0, 0, 0)

types = {"innerWall":1, "outterWall":2, "exit":3, "food":4, "enemy":5, "player": 6 }

mov_value = 50


def randomBlockGenerator():
    # the number of total blocks (each block is 50x50 pixels)
    return random.randint(1,MAX_BLOCKS-2) * 50

class Object:
    def __init__(self, x, y, type): #objType = "innerWall", "outterWall", "exit", "food"
        self.x = x
        self.y = y
        self.location = (self.x, self.y)
        if(type in types.keys()):
            self.type = type

    def isEqual(self, another):
        if int(self.x) == int(another.x) and int(self.y) == int(another.y) and str(self.type) == str(another.type):
            return True
        else:
            return False
    def isSameLocation(self, another):
        if int(self.x) == int(another.x) and int(self.y) == int(another.y):
            return True
        else:
            return False

    def getType(self):
        return self.type

    def getLocation(self):
        return self.location

    def changeTypeTo(self, newType):
        self.type = newType

    def toString(self):
        s = str(self.type) + " : " +str(self.location)
        print(s)

class Player(): 
    def __init__(self,x ,y):
        # character's width and height in pixels
        #self.player_size = 50
        # iniitial character x-y coordinates in pixels
        self.x = x
        self.y = y
        #print("player initial location: " + str(self.x) + " " +str(self.y))
        self.location = (self.x, self.y)
        # character's idle animation count
        self.idleCount = 0
        self.life = 100

class Enemy():
    def __init__(self, x, y, enemyType): #enemytype = "A" or "B"
        # character's width and height in pixels
        #self.player_size = 50
        # iniitial character x-y coordinates in pixels
        self.x = x
        self.y = y
        self.location = (self.x, self.y)
        # character's idle animation count
        self.idleCount = 0
        self.life = 100
        self.type = enemyType
    

class Game:
    def __init__(self):
        self.isRun = True
        # set difficulty
        self.difficulty = 1
        self.stepsCount = 0
        self.level = 1

        # load environment
        self.walls = [] #only contains outterwall1
        self.foods = []
        self.exit = self.wallGenerator()
        #print(self.exit)
      
        self.foodGenerator()
      
        # generate enemies
        self.enemies = [] 
        for i in range(random.randint(0, self.difficulty)):
            self.enemyGenerator()
 
        # load character
        self.player = self.playerGenerator()
        print("player initial location: " + str(self.player.x) + " " + str(self.player.y))


    def isOutterWall(self, x, y):
        #print(str(x) + " " + str(y))
        temp = Object(x,y,"outterWall")
        if self.isSameLocation(temp, self.walls):
            return True   
        #print("not outterwall")
        return False

    """ this checks if this nodeA's location is the same as any node's location in listA """
    def isSameLocation(self,nodeA,listA): 
        #print("nodeA: " + str(nodeA))
        for item in listA:
            if nodeA.isSameLocation(item):
                #print(" already in list")
                return True
        #print(" not in list")
        return False
        
    """" this generates the walls as well as the exit """
    def wallGenerator(self):
        for i in range(0, MAX_BLOCKS):
            for j in range(0, MAX_BLOCKS):
                if (i == 0) or (j == 0) or (i == MAX_BLOCKS-1) or (j == MAX_BLOCKS-1):
                    temp = Object(i*50,j*50, "outterWall")
                    #temp.toString()
                    self.walls.append(temp)
            
        #print(self.walls)            

        wallCount = random.randint(25,45)
        print("wallcount: " + str(wallCount))
        for i in range(wallCount):
            temp = Object(randomBlockGenerator(), randomBlockGenerator(), "outterWall")
            while self.isSameLocation(temp, self.walls):
                temp = Object(randomBlockGenerator(), randomBlockGenerator(), "outterWall")
            self.walls.append(temp)
        #print(self.walls)        

        tempExit = Object(randomBlockGenerator(), randomBlockGenerator(), "exit")
        while self.isSameLocation(tempExit, self.walls):
            tempExit = Object(randomBlockGenerator(), randomBlockGenerator(), "outterWall")
        return tempExit.getLocation()


    def foodGenerator(self):
        foodCount = random.randint(1,3) 
        print("foodcount: " + str(foodCount))
        for i in range(foodCount):
            temp = Object(randomBlockGenerator(), randomBlockGenerator(), "food")
            #print("food temp: " + str(temp))
            #temp.toString()
            while self.isSameLocation(temp, self.walls) or self.isSameLocation(temp, self.foods):
                temp = Object(randomBlockGenerator(), randomBlockGenerator(), "food")
                #print("food already in list")
            #print("food not in foods")
            self.foods.append(temp)

    def playerGenerator(self):
        x =  randomBlockGenerator()
        y =  randomBlockGenerator()
        while(x < 50 and x >= map_size-50 and y < 50 and y >= map_size-50):
            x = randomBlockGenerator()
            y = randomBlockGenerator()
        return Player(x,y)

    def enemyGenerator(self):
        x =  randomBlockGenerator()
        y =  randomBlockGenerator()
        while(x < 50 and x >= map_size-50 and y < 50 and y >= map_size-50):
            x = randomBlockGenerator()
            y = randomBlockGenerator()

        result = random.randint(1,100) #1-100
        if(result > 33):
            temp = Enemy(x,y,"A")
            self.enemies.append(temp)

        else:
            temp = Enemy(x,y,"B")
            self.enemies.append(temp)
      
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

    def updateFrame(self):
        #win.fill(BLACK)
        win.blit(background, (0,0))
        win.blit(exit, self.exit)
        
        for item in self.walls:
            #print(item)
            win.blit(outterWall1, item.location)

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
                        
                    elif (event.key == pygame.K_LEFT ) and not(self.isOutterWall(self.player.x -50, self.player.y)):    
                        self.player.x -= mov_value
                        self.stepsCount += 1
                    elif (event.key == pygame.K_RIGHT )  and not(self.isOutterWall(self.player.x+50, self.player.y)):   
                        self.player.x += mov_value
                        self.stepsCount += 1
                    elif (event.key == pygame.K_UP ) and not(self.isOutterWall(self.player.x , self.player.y-50)):      
                            self.player.y -= mov_value
                            self.stepsCount += 1
                    elif (event.key == pygame.K_DOWN ) and not(self.isOutterWall(self.player.x, self.player.y+50)):   
                            self.player.y += mov_value
                            self.stepsCount += 1
                    # check if there is food or exit in the location         
                    if(self.isFood(self.player.x, self.player.y)):
                        self.player.life += 10
                    if(self.isExit(self.player.x, self.player.y)):
                        print("exit!")
                        self.isRun = False
                        break
                    
                    #after = str(self.player.x) + "," + str(self.player.y)
                    #print("player move from " + prev + " to " + after)
            #update game frames
            self.updateFrame()
            time.sleep(0.1)
        

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
