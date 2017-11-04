from circle import Circle


class Bullet(Circle):
    def __init__(self, x=1, y=1, r = 3  , rotation=0):
        super().__init__(x,y,r,rotation)