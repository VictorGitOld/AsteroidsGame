from polygon import Polygon
from point import Point
import random

class Rocks(Polygon):
    #Each time rock is called it creates a rock object of random n=2 sizes
    #we should maybe randomize rock points() even more and rock pulls depending on level
    def __init__(self):
    #send all rocks to polygon class.
        super().__init__(
            self.getRock(),
            x=random.randint(0, 640),
            y=random.randint(0, 480),
            rotation=random.randrange(0, 50, 5),
            pull=Point(round(random.uniform(0, 0.5), 1), round(random.uniform(0, 0.5), 1)),
            angular_velocity=round(random.uniform(-0.5, 0.5), 1))

    def getRock(self):
        rockType= random.randint(1,2)
        if rockType ==1:
            return [Point(0,10), Point(10,15), Point(18,9), Point(13,3), Point(17,-5), Point(5,-12), Point(-10,-12), Point(-16,-7), Point(-16,8), Point(-9,14)]
        else:
            return [Point(10, 30), Point(25, 25), Point(33, 11), Point(35, -7), Point(21, -13), Point(13, -29),
             Point(-13, -31), Point(-21, -28), Point(-28, -22), Point(-34, -6), Point(-32, 14), Point(-29, 21),
             Point(-23, 24), Point(-10, 30)]