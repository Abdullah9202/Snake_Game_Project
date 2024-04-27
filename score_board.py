from turtle import Turtle

SCORE_BOARD_ALIGNMENT = "center"
SCORE_BOARD_FONT = ("Courier", 15, "normal")

# File name and path of the file to store the high_score
FILE_NAME = "data.txt"


# Creating a child class of turtle named score board
class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.high_score = 0  # To keep the record of highest score
        self.penup()
        self.goto(x=0, y=310)
        self.hideturtle()
        self.update_score()



    def update_score(self):
        # Clearing the previous score
        self.clear()

        # Reading high_score form the data file and assign to the high_score variable
        with open(file=FILE_NAME, mode='r') as file:
            (self.high_score) = int(file.read())  # Data from the file is converted to the int and assigned to high_score
        self.write(arg=f"Score : {self.score} High Score : {self.high_score}", align=SCORE_BOARD_ALIGNMENT, font=SCORE_BOARD_FONT)

    def reset_Game(self):  # Assign the score to the highest score if it is greater than the previous score
        if self.score > self.high_score:
            self.high_score = self.score

        # Sending the high score into the data file
        with open(file=FILE_NAME, mode='w') as file:
            file.write(f"{self.high_score}")

        # Setting the score to zero for the next game
        self.score = 0
        # Updating the score board
        self.update_score()

    # Creating a function to increase the score
    def increase_score(self):
        self.score += 1
        # Calling the update_score function
        self.update_score()