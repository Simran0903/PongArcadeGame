from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.goto(x,y)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed("fastest")
        self.color("white")
        self.go_up()
        self.go_down()

    def go_up(self):
        if self.ycor()<250:
            self.goto(self.xcor(), self.ycor() + 20)
        else:
            self.goto(self.xcor(),250)

    def go_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)
        else:
            self.goto(self.xcor(), -250)

