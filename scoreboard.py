from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self , x):
        super().__init__()
        self.point = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x,250)
        self.create()

    def create(self):
        self.write(self.point , move=False, align = "center", font=("Arial", 20, "normal"))
    
    def update(self):
        self.clear()
        self.point += 1
        self.write(self.point , move=False, align = "center", font=("Arial", 20, "normal"))

    def gameover(self , winner):
        s = Turtle()
        s.penup()
        s.color("white")
        s.hideturtle()
        s.goto(0,100)
        s.write(f"{winner} has won!" , move=False, align = "center", font=("Arial", 20, "normal"))
