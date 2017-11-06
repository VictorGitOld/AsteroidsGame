from circle import Circle
from point import Point

class Bullet (Circle):
    def __init__(self,position, rotation, born):
        super().__init__(position.x, position.y, 3, rotation, l =2)
        #self.position = position
        #self.rotation = rotation
        #self.pull = Point(0,0)
        #self.angular_velocity = 0
        #self.radius = 3
        #self.linewidth = l
        self.accelerate(10)
        self.born = born
        self.lifetime=50+born

