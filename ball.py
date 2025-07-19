from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create()
        self.x = 10
        self.y = 10
        self.move_speed = 0.01
        
    def create(self):
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(1,1)
        
    def refresh(self):
        self.home()
        self.move_speed = 0.01

    def move(self):
        self.goto(self.xcor() + self.x , self.ycor()+ self.y)


    def bounce(self):
        self.y = - self.y
        self.move_speed *= 0.9

    def rebounce(self):
        self.x = - self.x

    

        

