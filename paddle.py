from turtle import Turtle

WIDTH = 1
HEIGHT = 5
INCREMENT = 20

class Paddle:
    def __init__(self, position):
        self.paddle = Turtle()
        self.paddle.shape('square')
        self.paddle.color('white')
        self.paddle.penup()
        self.paddle.shapesize(stretch_wid= HEIGHT, stretch_len= WIDTH)
        self.paddle.goto(position[0],position[1])

    def move_up(self):
        if self.paddle.ycor() < 250:
            new_y = self.paddle.ycor() + INCREMENT
            self.paddle.goto(self.paddle.xcor(), new_y)

    def move_down(self):
        if self.paddle.ycor() > -250:
            new_y = self.paddle.ycor() - INCREMENT
            self.paddle.goto(self.paddle.xcor(), new_y)