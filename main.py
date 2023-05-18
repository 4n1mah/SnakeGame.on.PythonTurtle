from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


# Screen size and colors
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("SnakeGame")
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = ScoreBoard()

# Moves the snake
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


# Starts the game
def start_game():
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move_snake()

        # detect when Snake hits food
        if snake.head.distance(food) < 20:
            food.refresh()
            snake.extend_snake()
            scoreboard.increase_score()

        # detect when the snake hits the wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.game_over()
            time.sleep(2)
            scoreboard.reset()
            snake.reset_snake()

        # detect if snake hits his tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                time.sleep(2)
                scoreboard.reset()
                snake.reset_snake()


start_game()


screen.exitonclick()
