from turtle import Turtle,Screen
from paddle import Paddle1 , Paddle2
from ball import Ball
from scoreboard import ScoreBoard
import time

speed = 0.01

screen = Screen()
screen.title("Ping Pong")
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)

p1 = Paddle1()
p2 = Paddle2()
b = Ball()
s1 = ScoreBoard(-20)
s2 = ScoreBoard(20)

screen.update()
screen.tracer(1)

screen.onkey(p1.move_up , "Up")
screen.onkey(p1.move_down , "Down")

screen.onkey(p2.move_up , "w")
screen.onkey(p2.move_down , "s")

screen.listen()

def gameloop():
    global speed
    time.sleep(b.move_speed)

    b.move()

    if b.xcor() > 350:
        b.refresh()
        s1.update()

    elif b.xcor() < -350:
        b.refresh()
        s2.update()

    elif b.ycor() > 290 or b.ycor() < -290:
        b.bounce()

    elif b.distance(p1) < 50 and b.xcor() > 320:
        b.rebounce()

    elif b.distance(p2) < 50 and b.xcor() < -320:
        b.rebounce()

    if s1.point == 10:
        s1.gameover("Left")
        
    elif s2.point == 10:
        s2.gameover("Right")
        
    else:
        screen.ontimer(gameloop , 10)

gameloop()
screen.mainloop()

