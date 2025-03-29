from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
#bring out a pop-up
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
#print(user_bet)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    #set up a specific position for every turtle
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

#check if the user has placed a bet to start the race
if user_bet:
    is_race_on = True

while is_race_on:
   for turtle in all_turtles: 
        
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("you've won")
            else:
                print("you've lost")

        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)

#The turtle object is a 40x40 object



screen.exitonclick()