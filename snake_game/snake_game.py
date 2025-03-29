#Step 1: Create a snake body
from turtle import Screen, Turtle
import time
from snake import Snake

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor('black')
sc.title('Snake game')
sc.tracer(0)#turn off the animation

""" segment_1 = Turtle('square')
segment_1.color('white')

segment_2 = Turtle('square')
segment_2.color('white')
segment_2.goto(-20, 0)

segment_3 = Turtle('square')
segment_3.color('white')
segment_3.goto(-40, 0)
 """
snake = Snake()

sc.listen()
sc.onkey(snake.up, 'Up')
sc.onkey(snake.down, 'Down')
sc.onkey(snake.left, 'Left')
sc.onkey(snake.right, 'Right')


#Step 2: Move the snake
sc.update()

game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(0.1)# 0.1 second delay after seg moves
    
    snake.move()


#Step 3: Control the snake
#Step 4: Detect collision with food
#Step 5: Create a scoreboard
#Step 6: Detect collision with wall
#Step 7: Detect collision with self
sc.exitonclick()