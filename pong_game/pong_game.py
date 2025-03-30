#Break down the project into steps
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

#Step 1: Create the screen 600x800
sc = Screen()
sc.bgcolor('black')
sc.setup(width=800, height=600)
sc.title('Pong')
sc.tracer(0)#turn off animation 

sc.listen()

#Step 2: Create and move a paddle
right_paddle = Paddle((350, 0))

#Step 3: Create another paddle
left_paddle = Paddle((-350, 0))

ball = Ball()

#Move it up and down
sc.onkey(right_paddle.go_up, "Up")
sc.onkey(right_paddle.go_down, "Down")

sc.onkey(left_paddle.go_up, 'w')
sc.onkey(left_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    sc.update()

    #Step 4: Create the ball and make it move
    ball.move()

    #Step 5: Detect collision with the wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Step 6: Detect collision with paddle
    if ball.distance(right_paddle) < 60 and ball.xcor() > 320 or ball.distance(left_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    #Step 7: Detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_position()

    if ball.xcor() < -380:
        ball.reset_position()
#Step 8: Keep score
sc.exitonclick()