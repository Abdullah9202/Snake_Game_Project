from turtle import Turtle
import time

# Setting the positions
INIT_POS = [(0, 0), (-20, 0), (-40, 0)]  # Initial position for snake segments
MOVE_DISTANCE = 20  # Moving paces of snake

# Reset labels
RESET_LABEL = "Resetting..."
RESET_TIME = 2
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

# Setting up the movement constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.snake_head = None
        self.snake_Segments = []  # To store the segments after positioning

    def add_segment(self, position):  # This function will add the segments into the snake's body
        new_segments = Turtle("square")  # Objects
        new_segments.color("white")  # Giving the white color
        new_segments.penup()  # Pulling up the pen
        new_segments.goto(position)  # Setting the position
        self.snake_Segments.append(new_segments)  # Appending the modified segments into the list

    def create_snake(self):  # This function will create the body of a snake
        # Using for loop to set positions
        for pos in INIT_POS:
            # Calling the add_segment function
            self.add_segment(position=pos)
            self.snake_head = self.snake_Segments[0]  # To store the head of the snake
            self.snake_head.shape("circle")

    def reset_Snake(self):
        # Sending the remaining of previous snakes out of the screen using for loop
        for segments in self.snake_Segments:
            segments.goto(1000, 1000)
        self.snake_Segments.clear()  # Resetting the snake segments
        self.create_snake()  # Recreating the snake

    def extend_snake(self):
        # Calling the add_segment function
        self.add_segment(self.snake_Segments[-1].position())  # Add the segment to the list of the list

    def move(self):  # This function is to move the snake segments
        # Using for loop to move the segments
        for seg_num in range(len(self.snake_Segments) - 1, 0, -1):
            new_x = self.snake_Segments[seg_num - 1].xcor()
            new_y = self.snake_Segments[seg_num - 1].ycor()
            self.snake_Segments[seg_num].goto(x=new_x, y=new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    # Movements functions
    def Up(self):
        if self.snake_head.heading() != DOWN:  # Executes when the head of snakes is not in the 270 degrees.
            self.snake_head.setheading(90)

    def Right(self):
        if self.snake_head.heading() != LEFT:  # Executes when the head of snakes is not in the 180 degrees.
            self.snake_head.setheading(0)

    def Left(self):
        if self.snake_head.heading() != RIGHT:  # Executes when the head of snakes is not in the 0 degrees.
            self.snake_head.setheading(180)

    def Down(self):
        if self.snake_head.heading() != UP:  # Executes when the head of snakes is not in the 90 degrees.
            self.snake_head.setheading(270)
