from turtle import Turtle
FONT = ('Courier', 20, 'normal')

class Score (Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 267)
        self.hideturtle()
        self.write(f"Score:{self.score}", align="center", font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write("GAME OVER !!! ", align="center", font=FONT)
