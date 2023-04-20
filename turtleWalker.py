from turtle import Turtle

class Walker():
    def __init__(self) -> None:
        self.turtle_walker=Turtle()
        self.turtle_walker.shape("turtle")
        self.turtle_walker.setheading(90)
        self.turtle_walker.color("green")
        self.turtle_walker.penup()
        self.turtle_walker.goto(0,-280)
    
    def go_up(self):
        x,y=self.turtle_walker.position()
        if y<265:
            self.turtle_walker.goto(x,y+20)
