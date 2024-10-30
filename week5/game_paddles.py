# This code sets up a basic paddle game structure using the turtle module. 
# It creates two paddles (left and right) and a ball, defining functions to move the paddles up and down. 
# The paddles can be controlled through additional key bindings for a complete gameplay experience.



# Import the turtle graphics library
import turtle

# Set up the main game screen
t = turtle.Screen()
t.setup(width=1000, height=500)  # Set the screen width to 1000 and height to 500

# Initialize the right paddle
right_paddle = turtle.Turtle()  # Create a new turtle object for the right paddle
right_paddle.shape("square")    # Set the shape of the paddle to square
right_paddle.shapesize(stretch_wid=7, stretch_len=2)  # Stretch the square to create a paddle shape
right_paddle.penup()            # Lift the pen to avoid drawing lines
right_paddle.goto(450, 0)       # Position the right paddle on the right side of the screen

# Initialize the left paddle
left_paddle = turtle.Turtle()   # Create a new turtle object for the left paddle
left_paddle.shape("square")     # Set the shape of the paddle to square
left_paddle.shapesize(stretch_wid=7, stretch_len=2)  # Stretch the square to create a paddle shape
left_paddle.penup()             # Lift the pen to avoid drawing lines
left_paddle.goto(-450, 0)       # Position the left paddle on the left side of the screen

# Initialize the ball
b = turtle.Turtle()             # Create a new turtle object for the ball
b.shape("circle")               # Set the shape of the ball to circle

# Define the function to move the right paddle up
def right_paddle_up():
    x = right_paddle.ycor()     # Get the current y-coordinate of the right paddle
    x += 20                     # Increase the y-coordinate to move the paddle up
    right_paddle.sety(x)        # Set the new y-coordinate for the right paddle

# Define the function to move the right paddle down
def right_paddle_down():
    x = right_paddle.ycor()     # Get the current y-coordinate of the right paddle
    x -= 20                     # Decrease the y-coordinate to move the paddle down
    right_paddle.sety(x)        # Set the new y-coordinate for the right paddle

# Define the function to move the left paddle up
def left_paddle_up():
    x = left_paddle.ycor()      # Get the current y-coordinate of the left paddle
    x += 20                     # Increase the y-coordinate to move the paddle up
    left_paddle.sety(x)         # Set the new y-coordinate for the left paddle

# Define the function to move the left paddle down
def left_paddle_down():
    x = left_paddle.ycor()      # Get the current y-coordinate of the left paddle
    x -= 20                     # Decrease the y-coordinate to move the paddle down
    left_paddle.sety(x)         # Set the new y-coordinate for the left paddle

# Keeps the turtle graphics window open until manually closed
turtle.done()
