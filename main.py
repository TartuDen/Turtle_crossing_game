from turtle import Turtle, Screen
from turtleWalker import Walker
from turtleCars import Cars
import time
from score import Score

# Create an instance of the Score class
score = Score()

# Set up the screen
screen = Screen()
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.title("TURTLE CROSSING GAME")
screen.tracer(0)

# Create an instance of the Walker class
turtler = Walker()
speed = 0.05

# Create a list to store cars
list_of_cars = []
for i in range(10):
    car = Cars()
    list_of_cars.append(car)

# Listen for keypress and start the game loop
screen.listen()
screen.onkeypress(turtler.go_up, "Up")

game_over = False

# Display initial message with high score
print(f"Let's start! Can you beat the highest score so far -{score.high_score}?")
score.write_on_screen()

# Main game loop
while not game_over:
    time.sleep(speed)
    x_walker, y_walker = turtler.turtle_walker.position()
    
    # Logic for successful crossing
    if y_walker >= 265:
        turtler.turtle_walker.goto(0, -280)
        speed = speed - 0.5 * speed
        score.score += 1
        score.write_on_screen()
        print(f"my score - {score.score}, highest score - {score.high_score}")
        
        # Check if the current score is higher than the high score
        if int(score.score) > int(score.high_score):
            score.update_file()
            print(f"Congratulations, your score - {score.score} is the new HIGHEST SCORE!")
    
    # Check for collision with cars
    for c in list_of_cars:
        c.move_car()
        x_car, y_car = c.t_car.position()
        if abs(y_car - y_walker) < 25 and abs(x_car - x_walker) < 5:
            print(x_walker, y_walker, " - ", x_car, y_car)
            print("GAME OVER")
            exit()
    
    screen.update()

screen.exitonclick()
