from turtle import Turtle, Screen
import time
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("Blue")

        self.penup()
        self.goto(random.randint(-280, 280), random.randint(-280, 280))


    def move(self):
        self.hideturtle()
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.showturtle()