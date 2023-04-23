from turtle import Turtle, Screen
from turtleWalker import Walker
from turtleCars import Cars
import time
from score import Score


score=Score()

screen=Screen()
screen.bgcolor("white")
screen.setup(width=800,height=600)
screen.title("TURTLE CROSSING GAME")
screen.tracer(0)

turtler=Walker()
speed=0.05
list_of_cars=[]
for i in range(10):
    car=Cars()

    list_of_cars.append(car)


screen.listen()
screen.onkeypress(turtler.go_up,"Up")

game_over=False
print(f"my score - {score.score}, highest score - {score.high_score}")
while not game_over:
    time.sleep(speed)
    x_walker, y_walker = turtler.turtle_walker.position()
    if y_walker>=265:
        print(f"my score - {score.score}, highest score - {score.high_score}")
        turtler.turtle_walker.goto(0,-280)
        speed=speed-0.5*speed
        score.score+=1
        if int(score.score) > int(score.high_score):
            score.update_file()
            # print(f"my score - {score.score}, highest score - {score.high_score}")
    
    for c in list_of_cars:
        c.move_car()
        x_car,y_car = c.t_car.position()
        if abs(y_car - y_walker)<25 and abs(x_car-x_walker)<5:
            print(x_walker,y_walker, " - ", x_car, y_car)
            print("GAME OVER")
            exit()
    
    screen.update()

screen.exitonclick()
