from turtle import Turtle

INCREMENT = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)

    def move_ball(self):
        if self.xcor() < 380 and self.ycor() < 280:
            new_x = self.xcor() + INCREMENT
            new_y = self.ycor() + INCREMENT
            self.goto(new_x,new_y)