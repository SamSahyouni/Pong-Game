from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_l_score()
        self.write_r_score()

    def write_l_score(self):
        self.goto((-100, 200))
        self.write(self.l_score,align="center",font= ("Courier",60,"normal") )

    def write_r_score(self):
        self.goto(100, 200)
        self.write(self.r_score,align="center",font= ("Courier",60,"normal") )

    def l_player_score(self):
        self.l_score += 1
        self.clear()
        self.write_l_score()
        self.write_r_score()
    def r_player_score(self):
        self.r_score += 1
        self.clear()
        self.write_r_score()
        self.write_l_score()