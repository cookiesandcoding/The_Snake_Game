from turtle import Turtle
import random

class Food(Turtle):
    #inherited prop from turtle class and thus no need of creating a turtle object
    def __init__(self):
        super().__init__()
        #now we can use the functions directly without creating an object
        self.shape("circle")
        self.color("green")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.pos_of_food()


    def pos_of_food(self):
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)


