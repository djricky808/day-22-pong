from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 30, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(x=0, y=250)
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f"{self.left_score}|{self.right_score}", move=False, align=ALIGNMENT, font= FONT)

    def add_point_left(self):
        self.left_score += 1
        self.clear()
        self.update_score()

    def add_point_right(self):
        self.right_score += 1
        self.clear()
        self.update_score()