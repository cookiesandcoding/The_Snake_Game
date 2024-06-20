from turtle import Turtle
starting_position = [(0, 0), (20, 0), (40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in starting_position:
            self.add_snake_body(position)


    def add_snake_body (self,position):
        sq = Turtle("square")
        sq.color("white")
        sq.penup()
        sq.goto(position)
        self.squares.append(sq)

    def extend(self):
        self.add_snake_body((self.squares[-1]).position())

    def move(self):
        for seg_num in range((len(self.squares))-1, 0, -1):
            new_x = self.squares[seg_num - 1].xcor()
            new_y = self.squares[seg_num - 1].ycor()
            self.squares[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left_turn(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right_turn(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
