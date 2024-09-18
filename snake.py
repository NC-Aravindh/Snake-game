from turtle import Turtle
import time

class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        #3 Turtles are set in a sequence to create a snake.
        for position in self.starting_positions:
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.penup()
            new_turtle.goto(position)
            self.segments.append(new_turtle)
        self.size = len(self.segments)
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    #New turtle will be created and added the current tail's position and to the snake.
    def extend(self):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.penup()
        new_segment.goto(self.tail.position())
        self.segments.append(new_segment)


    def move_forward(self):
        #Here the all the segments except the head , will move to its previous segments position.
        #Head which is the 0th segment will move forward by 20 pixels.
        for segment_no in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_no - 1].xcor()
            new_y = self.segments[segment_no - 1].ycor()
            self.segments[segment_no].goto(new_x, new_y)

        self.segments[0].forward(20)

    #For the below controls , the head of the snake will be turned and rest will follow.
    def move_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def move_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def move_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def move_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

