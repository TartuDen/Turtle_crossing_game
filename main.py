from turtle import Turtle, Screen
from turtleWalker import Walker
from turtleCars import Cars
import time
import random



screen=Screen()
screen.bgcolor("white")
screen.setup(width=800,height=600)
screen.title("TURTLE CROSSING GAME")
screen.tracer(0)

turtler=Walker()
for i in range(10):
    car=Cars()
    car.move_car()
# turtler=new_game.turtle_walker

screen.listen()
screen.onkeypress(turtler.go_up,"Up")

game_over=False

while not game_over:
    time.sleep(0.05)
    car.move_car()
    screen.update()

screen.exitonclick()
