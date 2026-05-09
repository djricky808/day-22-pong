from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)

    def rotate_ball(self):
        self.setheading(35)

    def move_ball(self):
        if self.xcor()<380 and self.ycor()<280:
            self.forward(1)