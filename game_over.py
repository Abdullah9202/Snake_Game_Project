from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
LABEL = "Game Over"


# Creating a child class of Turtle named Game_Over
class Game_Over(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=0, y=0)
        self.color("white")
        self.write(arg=LABEL, align=ALIGNMENT, font=FONT)