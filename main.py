#Listen to key strokes on the keyboard with eventlisteners
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.fd(10)

def move_backwards():
    tim.backward(10)

def turn_left():
   tim.setheading(tim.heading() + 10)
    #or you can use tim.left(10) it takes the 
    #degress of the turning angle.
    #Here in the first line the heading is set to 
    #zero.

def turn_right():
   tim.setheading(tim.heading() - 10)
#or alternatively you can use tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(key='w', fun=move_forward)    
screen.onkey(key='s', fun=move_backwards)    
screen.onkey(key='a', fun=turn_left)    
screen.onkey(key='d', fun=turn_right)    
screen.onkey(key='c', fun=clear_screen)


screen.exitonclick()