from turtle import Screen

from ball import Ball
from paddle import Paddle
import time

from scoreboard import Scoreboard

screen= Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#Initialize Paddles
right_paddle=Paddle((350,0))
left_paddle=Paddle((-350,0))

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

#Initialize ball
ball=Ball()

#Initialize Scoreboard
scoreboard=Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with ceiling or floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with Right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect when right paddle missed ball
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.left_point()

    # detect when left paddle missed ball
    elif ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()

