from Object import Object

class Enemy(Object):
    def __init__(self, x, y): #enemytype = "A" or "B"
        # character's width and height in pixels
        #self.player_size = 50
        # iniitial character x-y coordinates in pixels
        self.x = x
        self.y = y
        self.index = (x,y)
        self.location = (x*50, y*50)
        # character's idle animation count
        self.idleCount = 0
        #self.life = 100
        #self.type = enemyType
    