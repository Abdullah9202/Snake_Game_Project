from turtle import Turtle
import random


# Creating the child class of turtle named food
class Food(Turtle):
    def __init__(self):
        super().__init__()
        # Defining the functions for food
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)  # 11 by 11 px
        self.speed("fastest")
        # Calling the function to refresh the food location
        self.refresh_food()

    # Creating a function to change the location of food when it is eaten
    def refresh_food(self):
        # Generating a random location for food
        rand_x_cor = random.randint(-330, 330)
        rand_y_cor = random.randint(-330, 330)
        # Assigning location
        self.goto(x=rand_x_cor, y=rand_y_cor)
