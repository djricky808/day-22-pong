from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")


right_paddle_x_pos = 350
left_paddle_x_pos = -350

right_paddle = Paddle(right_paddle_x_pos)

root = screen.getcanvas().winfo_toplevel()
root.call('wm','attributes','.','-topmost','1')

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.exitonclick()