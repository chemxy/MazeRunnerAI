from Object import Object

class Player(Object): 
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