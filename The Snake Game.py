import random
import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the snake game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
food.pos_of_food()
points = Score()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right_turn, "Right")
screen.onkey(snake.left_turn, "Left")

end_game = False

while not end_game:
    screen.update()
    time.sleep(0.09)
    snake.move()
    if snake.head.distance(food) < 13:
        food.pos_of_food()
        points.update()
        snake.extend()
        end_game = False
    if snake.head.xcor() > 280 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -280:
        points.game_over()
        end_game = True
    if len(snake.squares) > 3:
     for parts in snake.squares[1:]:
        if snake.head.distance(parts) < 10:
            points.game_over()
            end_game = True

screen.exitonclick()
