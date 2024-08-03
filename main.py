import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')

gameon = True
initial_speed = 0.1
speed = initial_speed

while gameon:
    screen.update()
    time.sleep(speed)
    snake.move()

    # Detect collision with food.
    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        snake.grow_snake()
        score.increase_score()

        speed *= 0.95  

    # Detect collision with walls.
    if snake.turtles[0].xcor() <= -300 or snake.turtles[0].xcor() >= 300 or snake.turtles[0].ycor() <= -300 or snake.turtles[0].ycor() >= 300:
        gameon = False
        score.reset()


    for turtle in snake.turtles[1:]:  # Skip the head
        if snake.turtles[0].distance(turtle) < 10:
            gameon = False
            score.reset()

screen.exitonclick()
