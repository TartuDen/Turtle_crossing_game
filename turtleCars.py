from turtle import Turtle
import random
import time
class Cars(Turtle):
    def __init__(self):
        list_colors=["blue", "green", "black", "yellow", "red"]
        self.t_car=Turtle()
        self.t_car.shape("square")
        self.t_car.setheading(180)
        self.t_car.color(random.choice(list_colors))
        self.t_car.penup()
        self.t_car.goto(280, random.randint(-200,200))
        x,y=self.t_car.position()
        self.speed=random.randint(5,15)
    def move_car(self):
        x,y=self.t_car.position()
        if x>-280:
            self.t_car.goto(x-self.speed,y)

  
    