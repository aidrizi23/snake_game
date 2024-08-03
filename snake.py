from turtle import Turtle, Screen

class Snake:
    
    def __init__(self):
        self.screen = Screen()
        self.turtles = []
        self.create_snake()
    def create_snake(self):
        
        for i in range(3):
            t = Turtle()
            t.penup()
            t.shape('square')
            t.color('white')
            t.setposition(x=-(i*20), y=0)
            self.turtles.append(t)
            self.screen.update()
    def move(self):
        for i in range(len(self.turtles)-1, 0, -1):
            self.turtles[i].goto(x=self.turtles[i-1].xcor(), y=self.turtles[i-1].ycor())

        self.turtles[0].forward(20)
    
    def up(self):
        if self.turtles[0].heading() != 270: 
            self.turtles[0].setheading(90)
    
    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)
    
    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)
        
    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)
            
    def grow_snake(self):
        t = Turtle()
        t.penup()
        t.shape('square')
        t.color('white')
        t.setposition(x=self.turtles[len(self.turtles)-1].xcor()-20, y=self.turtles[len(self.turtles)-1].ycor()-20)
        self.turtles.append(t)
        self.screen.update()