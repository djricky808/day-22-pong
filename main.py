from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

RIGHT_PADDLE_POS = (350,0)
LEFT_PADDLE_POS = (-350,0)

right_paddle = Paddle(RIGHT_PADDLE_POS)
left_paddle = Paddle(LEFT_PADDLE_POS)

ball = Ball()
scoreboard = Scoreboard()

root = screen.getcanvas().winfo_toplevel()
root.call('wm','attributes','.','-topmost','1')

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() >= 280 or ball.ycor() <= -280 :
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor()<-380:
        ball.reset_ball()
        scoreboard.add_point_right()

    if ball.xcor()> 380:
        ball.reset_ball()
        scoreboard.add_point_left()

screen.exitonclick()