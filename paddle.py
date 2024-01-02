from turtle import Turtle,Screen



class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.setposition(position)

    def go_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)

    def go_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def l_paddle_move(self):
        screen = Screen()
        screen.listen()
        screen.onkey(self.go_up, "w")
        screen.onkey(self.go_down, 's')

    def r_paddle_move(self):
        screen = Screen()
        screen.listen()
        screen.onkey(self.go_up, "Up")
        screen.onkey(self.go_down, 'Down')
