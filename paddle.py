from turtle import Turtle

WIDTH = 1
HEIGHT = 5
INCREMENT = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid= HEIGHT, stretch_len= WIDTH)
        self.goto(position[0],position[1])

    def move_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + INCREMENT
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - INCREMENT
            self.goto(self.xcor(), new_y)