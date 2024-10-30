# Enhanced Paddle Game using Turtle Graphics
# This game includes paddle and ball movement, collision detection, scoring, and screen boundaries.

import turtle

# Set up the main game screen
t = turtle.Screen()
t.title("Paddle Game")
t.setup(width=1000, height=500)
t.bgcolor("black")
t.tracer(0)  # Turn off automatic updates for smoother gameplay

# Variables for ball movement
ball_dx = 3  # Ball movement in x direction
ball_dy = 3  # Ball movement in y direction

# Variables for scoring
left_score = 0
right_score = 0

# Initialize the right paddle
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("blue")
right_paddle.shapesize(stretch_wid=7, stretch_len=2)
right_paddle.penup()
right_paddle.goto(450, 0)

# Initialize the left paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("red")
left_paddle.shapesize(stretch_wid=7, stretch_len=2)
left_paddle.penup()
left_paddle.goto(-450, 0)

# Initialize the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(0)  # Maximum speed for the ball
ball.goto(0, 0)

# Initialize the scoreboard
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 210)
score_display.write("Left Player: 0  Right Player: 0", align="center", font=("Courier", 24, "normal"))

# Update score display
def update_score():
    score_display.clear()
    score_display.write(f"Left Player: {left_score}  Right Player: {right_score}", align="center", font=("Courier", 24, "normal"))

# Define paddle movements
def right_paddle_up():
    y = right_paddle.ycor()
    if y < 200:  # Set upper boundary for paddle movement
        right_paddle.sety(y + 20)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -200:  # Set lower boundary for paddle movement
        right_paddle.sety(y - 20)

def left_paddle_up():
    y = left_paddle.ycor()
    if y < 200:  # Set upper boundary for paddle movement
        left_paddle.sety(y + 20)

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -200:  # Set lower boundary for paddle movement
        left_paddle.sety(y - 20)

# Keyboard bindings for paddle control
t.listen()
t.onkeypress(right_paddle_up, "Up")
t.onkeypress(right_paddle_down, "Down")
t.onkeypress(left_paddle_up, "w")
t.onkeypress(left_paddle_down, "s")

# Game loop
while True:
    t.update()  # Refresh screen to apply movements
    
    # Move the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # Ball collision with the top boundary
    if ball.ycor() > 240:
        ball.sety(240)
        ball_dy *= -1  # Reverse the y-direction

    # Ball collision with the bottom boundary
    if ball.ycor() < -240:
        ball.sety(-240)
        ball_dy *= -1  # Reverse the y-direction

    # Ball collision with right paddle
    if (ball.xcor() > 430 and ball.xcor() < 450) and (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
        ball.setx(430)
        ball_dx *= -1  # Reverse the x-direction

    # Ball collision with left paddle
    if (ball.xcor() < -430 and ball.xcor() > -450) and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-430)
        ball_dx *= -1  # Reverse the x-direction

    # Ball goes out on the right side (left player scores)
    if ball.xcor() > 490:
        ball.goto(0, 0)  # Reset the ball to center
        ball_dx *= -1  # Reverse the ball's x-direction
        left_score += 1  # Increment left player's score
        update_score()  # Update the score display

    # Ball goes out on the left side (right player scores)
    if ball.xcor() < -490:
        ball.goto(0, 0)  # Reset the ball to center
        ball_dx *= -1  # Reverse the ball's x-direction
        right_score += 1  # Increment right player's score
        update_score()  # Update the score display
