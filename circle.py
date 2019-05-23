
class Cell:
    def __init__(self,x,y,r,color,id):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.id = id
        self.position = (x,y)

class CellPosition:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.position = (x,y)

