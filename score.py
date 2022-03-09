from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("Black")
        self.goto(-20,240)
        self.current_score = 0
        self.write(f"Score:{self.current_score}",font=("Verdana", 25, "normal"))

    def update_score(self):
        self.clear()
        self.current_score += 1
        self.write(f"Score:{self.current_score}",font=("Verdana", 25, "normal"))

    def game_over(self):
        pen = Turtle()
        pen.hideturtle()
        pen.write("Game Over",font=("Verdana", 25, "normal"))