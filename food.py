import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
         super().__init__()
         self.penup()
         self.speed('fastest')
         self.shape('circle')
         self.refresh()
         self.shapesize(stretch_len=0.5, stretch_wid=0.5)
         self.color('blue')

    def refresh(self):
        self.setx(random.randint(-270, 270))
        self.sety(random.randint(-270, 270))
