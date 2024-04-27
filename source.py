from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score_board

# Setting up screen
screen = Screen()
# Dimensions
screen.setup(width=700, height=700)
# Title
screen.title("Snake Game")
# Background color
screen.bgcolor("black")
# Turning off the tracer
screen.tracer(0)  # The Program is executed in the background, but it is shown to the user on the correct instants

# TODO : 1 Creating the snake's body
snake = Snake()  # Calling the function from snake class to create the snake's body
snake.create_snake()

# TODO : 4 Creating the snake's food
food = Food()

# TODO : 6 Creating a scoreboard
score_board = Score_board()

# TODO : 3 Controlling the snake
screen.listen()  # Listen to the keystrokes
screen.onkey(key="Up", fun=snake.Up)
screen.onkey(key="Down", fun=snake.Down)
screen.onkey(key="Left", fun=snake.Left)
screen.onkey(key="Right", fun=snake.Right)


# TODO : 2 Moving the snake
game_is_ON = True  # Boolean to control the game execution
while game_is_ON:
    screen.update()  # To show the segments after they move
    time.sleep(0.1)
    snake.move()  # Calling the move function from snake's class to move the segments of snake

    # TODO : 7 Detecting the collision with wall
    if snake.snake_head.xcor() > 340 or snake.snake_head.xcor() < -340 or snake.snake_head.ycor() > 340 or snake.snake_head.ycor() < -340:
        # Resetting the score board
        score_board.reset_Game()
        # Resetting the snake
        snake.reset_Snake()
        # # Terminating the game
        # game_is_ON = False
        # # Print the game over
        # Game_Over()

    # TODO : 8 Detecting the collision with body
    # Using for loop to detect collision with body
    for segments in snake.snake_Segments[1:]:
        if snake.snake_head.distance(segments) < 7:
            # Resetting the score board
            score_board.reset_Game()
            # Resetting the snake
            snake.reset_Snake()
            # game_is_ON = False
            # # Printing game over
            # Game_Over()

    # TODO : 5 Detecting collision with food
    if snake.snake_head.distance(food) <= 15:
        # Calling the function to refresh the food location
        food.refresh_food()
        # Calling the extend_snake() function to extend the body of the snake
        snake.extend_snake()
        # Calling the score_board function and increasing the score
        score_board.increase_score()


# Exit
screen.exitonclick()
