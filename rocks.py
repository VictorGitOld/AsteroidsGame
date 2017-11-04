from polygon import Polygon
from point import Point
import random

class Rocks(Polygon):
    def __init__(self, i):
        #rocks
        rock1 = [Point(0,10), Point(10,15), Point(18,9), Point(13,3), Point(17,-5), Point(5,-12), Point(-10,-12), Point(-16,-7), Point(-16,8), Point(-9,14)]
        rock2 = [Point(10,30), Point(25,25), Point(33,11), Point(35,-7), Point(21,-13), Point(13,-29), Point(-13,-31), Point(-21,-28), Point(-28,-22), Point(-34,-6), Point(-32,14), Point(-29,21), Point(-23,24), Point(-10,30)]
        rock3 = [Point(-15 ,30), Point(30,15), Point(50, 20), Point(35, -35), Point(-5, -20)]
        rock4 = [Point(-15 ,30), Point(30,15), Point(50, 20), Point(35, -35), Point(-5, -20)]

        self.rocks = [rock1, rock2, rock3, rock4]
        #send all rocks to polygon class.
        super().__init__(self.rocks[i],
                         x=random.randint(0, 640),
                         y=random.randint(0, 480),
                         rotation=random.randrange(0, 50, 5),
                         pull=Point(round(random.uniform(0, 0.5), 1), round(random.uniform(0, 0.5), 1)),
                         angular_velocity=round(random.uniform(-0.5, 0.5), 1))



