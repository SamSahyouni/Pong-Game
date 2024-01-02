from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
L_PADDLE_POS = (-350,0)
R_PADDLE_POS = (350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(L_PADDLE_POS)
r_paddle = Paddle(R_PADDLE_POS)
l_paddle.l_paddle_move()
r_paddle.r_paddle_move()
ball = Ball()

scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    if ball.ycor() < 280 or ball.ycor() > -280:
        ball.move()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # print("yes")
        ball.bounce_x()
    # detect miss
    if ball.xcor() > 380:
        # print("out")
        scoreboard.l_player_score()
        ball.reset_position()


    if ball.xcor() < -380:
        scoreboard.r_player_score()
        ball.reset_position()

screen.exitonclick()