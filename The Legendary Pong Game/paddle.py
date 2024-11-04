from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, new_x, new_y):
        super().__init__()
        self.x = new_x
        self.y = new_y
        self.penup()
        self.fillcolor("White")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.x, self.y)

    def go_up(self):
        new_y = self.ycor() + 30
        new_x = self.x
        self.goto(new_x, new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        new_x = self.x
        self.goto(new_x, new_y)
