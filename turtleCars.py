from turtle import Turtle
import random
import time
class Cars(Turtle):
    def __init__(self):
        self.list_colors=[ "black", "gray", "red", "green", "blue", "cyan", "yellow", "magenta", "orange", "pink", "purple"]
        self.t_car=Turtle()
        self.t_car.shape("square")
        self.t_car.setheading(180)
        self.t_car.color(random.choice(self.list_colors))
        self.t_car.penup()
        step=20
        self.t_car.goto(370, random.randint(-200//step,200/step)*step)
        x,y=self.t_car.position()
        self.speed=random.randint(5,15)
    def move_car(self):
        x,y=self.t_car.position()
        if x>-370:
            self.t_car.goto(x-self.speed,y)
        else:
            self.speed=random.randint(2,7)
            self.t_car.color(random.choice(self.list_colors))
            self.t_car.goto(370, random.randint(-200,200))

  
    