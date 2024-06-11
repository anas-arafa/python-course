import turtle
t=turtle.Screen()
right_paddle=turtle.Turtle()
t.setup(width=1000,height=500)
#right paddle
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=7,stretch_len=2)
right_paddle.penup()
right_paddle.goto(450,0)
#left paddle
left_paddle=turtle.Turtle()
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=7,stretch_len=2)
left_paddle.penup()
left_paddle.goto(-450,0)
#the ball
b=turtle.Turtle()
b.shape("circle")

def right_paddle_up():
    x=right_paddle.ycor()
    x+=20
    right_paddle.sety(x)
def right_paddle_down():
    x=right_paddle.ycor()
    x-=20
    right_paddle.sety(x)

def left_paddle_up():
    x=left_paddle.ycor()
    x+=20
    left_paddle.sety(x)
def left_paddle_down():
    x=left_paddle.ycor()
    x-=20
    left_paddle.sety(x)

turtle.done()