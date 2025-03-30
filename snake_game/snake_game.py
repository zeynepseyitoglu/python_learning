#Step 1: Create a snake body
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor('black')
sc.title('Snake game')
sc.tracer(0)#turn off the animation

snake = Snake()
food = Food()
scoreboard = Scoreboard()

sc.listen()
sc.onkey(snake.up, 'Up')
sc.onkey(snake.down, 'Down')
sc.onkey(snake.left, 'Left')
sc.onkey(snake.right, 'Right')


sc.update()

game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(0.1)# 0.1 second delay after segment moves
    
    #Step 2: Move the snake
    snake.move()

    #Step 4: Detect collision with food
    #Checks the distance between two turtle objects
    if snake.head.distance(food) < 15:
        print('Nom Nom Nom') 
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Step 6: Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Step 7: Detect collision with self
    #if the head collides with any segment in the tail game over
    for segment in snake.segments: 
        if segment == snake.head():
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

sc.exitonclick()