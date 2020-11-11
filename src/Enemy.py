
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
    
