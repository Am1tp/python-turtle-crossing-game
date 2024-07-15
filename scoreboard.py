from turtle import Turtle
FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x=-200, y=240)
        self.write(arg= f"Level: {self.level}", align='center', font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.goto(x=-200, y=240)
        self.write(arg= f"Level: {self.level}", align='center', font=FONT)

    def game_over(self):
        self.clear()
        self.goto(x=-200, y=240)
        self.write("GAME OVER", align='center', font=FONT)
        self.level = 1



