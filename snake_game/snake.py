from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(position)# takes a tuple
            self.segments.append(segment)
    
    def move(self):
        for sg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[sg_num - 1].xcor()
            new_y = self.segments[sg_num - 1].ycor()
            self.segments[sg_num].goto(new_x, new_y)

        self.segments[0].fd(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        