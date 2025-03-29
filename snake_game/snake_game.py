#Step 1: Create a snake body
from turtle import Screen, Turtle
import time

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
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    segment = Turtle('square')
    segment.color('white')
    segment.penup()
    segment.goto(position)# takes a tuple
    segments.append(segment)

#Step 2: Move the snake
sc.update()

game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(0.1)# 1 second delay after seg moves

    for sg_num in range(len(segments)-1, 0, -1):
        new_x = segments[sg_num - 1].xcor()
        new_y = segments[sg_num - 1].ycor()
        segments[sg_num].goto(new_x, new_y)

    segments[0].fd(20)

#Step 3: Control the snake
#Step 4: Detect collision with food
#Step 5: Create a scoreboard
#Step 6: Detect collision with wall
#Step 7: Detect collision with self
sc.exitonclick()