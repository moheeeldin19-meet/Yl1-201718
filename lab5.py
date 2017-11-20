import random
from turtle import Turtle,colormode
class Square(Turtle):
    def __init__(self,size):
        Turtle.__init__(self)
        self.shapesize(size)
        self.shape("square")
    def Random_color(self):
       r=random.randint(0,100)
       g=random.randint(0,100)
       b=random.randint(0,100)
       self.color(r,g,b)
jan=Square(9)
