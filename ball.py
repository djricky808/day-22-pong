from turtle import Turtle

INCREMENT = 10
SPEED_INCREMENT = 1.2


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = INCREMENT
        self.y_move = INCREMENT

    def reset_ball(self):
        self.goto(0,0)
        self.x_move = INCREMENT
        self.y_move = INCREMENT
        self.bounce_x()

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.increase_ball_speed()

    def increase_ball_speed(self):
        self.x_move *= SPEED_INCREMENT
        self.y_move *= SPEED_INCREMENT