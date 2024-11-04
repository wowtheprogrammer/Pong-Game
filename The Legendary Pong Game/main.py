from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)

r_paddle = Paddle(new_x=350, new_y=0)
l_paddle = Paddle(new_x=-350, new_y=0)
ball = Ball()
scoreboard = Scoreboard()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Ultimate Legendary Pong Game")
screen.update()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 :
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -325 :
        ball.bounce_x()

    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.write_score()

    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.write_score()




screen.exitonclick()
