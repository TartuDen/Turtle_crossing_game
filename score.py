class Score():
    def __init__(self) -> None:
        self.score=0
        self.high_score=(self.read_file())
    def read_file(self):
        with open("highest_score.txt", "r") as file:
            high_score=file.read()
            return(high_score)
    def update_file(self):
        with open("highest_score.txt", "w") as file:
            file.write(str(self.score))
