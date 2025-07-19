from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.shapesize( 5 , 1)
        
    def move_up(self):
        self.goto(self.xcor() , self.ycor() + 30)


    def move_down(self):
        self.goto(self.xcor() , self.ycor() - 30)

class Paddle1(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(350 , 0)
        

class Paddle2(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(-350 , 0)



    
    
        


        
        

