from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color('green')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280)) 
