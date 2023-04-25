from turtle import Turtle
class Score():
    def __init__(self) -> None:
        self.score=0
        self.high_score=(self.read_file())
        self.score_trutle=Turtle()
        self.score_trutle.penup()
        self.score_trutle.hideturtle()
        self.score_trutle.goto(0,280)
        
    def read_file(self):
        with open("highest_score.txt", "r") as file:
            high_score=file.read()
            return(high_score)
    def update_file(self):
        with open("highest_score.txt", "w") as file:
            file.write(str(self.score))
        
    def write_on_screen(self):
        print("inside write on screen")
        self.score_trutle.clear()
        self.score_trutle.write(f"Your score - {self.score}, Record - {self.high_score}", align="center", font=24)

