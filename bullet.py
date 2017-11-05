from circle import Circle
from point import Point

class Bullet (Circle):
    def __init__(self,position, rotation, born):

        self.position = position
        self.rotation = rotation
        self.pull = Point(0,0)
        self.angular_velocity = 0
        self.radius = 3
        self.linewidth = 2
        self.accelerate(5)
        self.born = born
        self.frames_until_self_destruct=100+born

