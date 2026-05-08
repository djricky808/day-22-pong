from turtle import Turtle

WIDTH = 1
HEIGHT = 5
Y = 0
INCREMENT = 20

class Paddle:
    def __init__(self,x_pos):
        self.paddle = Turtle()
        self.paddle.shape('square')
        self.paddle.color('white')
        self.paddle.penup()
        self.paddle.shapesize(stretch_wid= HEIGHT, stretch_len= WIDTH)
        self.x = x_pos
        self.y = Y
        self.paddle.goto(self.x , self.y)

    def move_up(self):
        if self.y < 250:
            self.y += INCREMENT
            self.paddle.goto(self.x, self.y)

    def move_down(self):
        if self.y > -250:
            self.y -= INCREMENT
            self.paddle.goto(self.x, self.y)