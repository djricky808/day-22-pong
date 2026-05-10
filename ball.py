from turtle import Turtle

INCREMENT = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.wall_direction = "up"
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)

    def move_ball(self):
        if self.ycor() >= 280:
            self.wall_direction = "down"
        elif self.ycor() <= -280:
            self.wall_direction = "up"
        if self.wall_direction == "up" :
            new_x = self.xcor() + INCREMENT
            new_y = self.ycor() + INCREMENT
        else:
            new_x = self.xcor() + INCREMENT
            new_y = self.ycor() - INCREMENT
        self.goto(new_x,new_y)