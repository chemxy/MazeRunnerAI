from Object import Object,Wall,Food

types = {"player":1, "wall":2, "exit":3, "food":4, "enemy":5}

class Block:
    def __init__(self, up=None, down=None, left=None, right=None, contents=None):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        if contents == None:
            contents = []
        self.contents = contents #this list only contains unique items. i.e. each item has a unique type.

    def getContents(self):
        return list(self.contents)

    def getUp(self):
        return self.up

    def getDown(self):
        return self.down

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def addContent(self,obj):
        self.contents.append(obj)

    def remove(self,obj):
        for item in self.contents:
            if item.isEqual(obj):
                self.contents.remove(item)
    
    def addUp(self,up):
        self.up = up

    def adddown(self,down):
        self.down = down

    def addLeft(self,left):
        self.left = left

    def addRight(self,right):
        self.right = right
