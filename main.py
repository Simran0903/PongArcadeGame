from paddle import Paddle
from ball import Ball
from score_board import Score_Board
import time
from turtle import Turtle,Screen
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)


r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
ball=Ball()
score_board=Score_Board()
screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")

screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")
screen.update()

gameon=True

while gameon:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>270 or ball.ycor()<-270:
        ball.bounce_y()

    if ball.xcor() >320 and r_paddle.distance(ball)<50 or ball.xcor() <-320 and l_paddle.distance(ball)<50:
        ball.bounce_x()


    if ball.xcor()>390:
        score_board.update_scoreboard()
        ball.reset_position()
        score_board.l_point()

    if ball.xcor()<-390:
        score_board.update_scoreboard()
        ball.reset_position()
        score_board.r_point()



screen.exitonclick()