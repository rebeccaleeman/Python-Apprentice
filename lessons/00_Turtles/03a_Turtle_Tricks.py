"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle() 
def drawolive(x,y):
    tina.penup()
    tina.goto(x,y)
    tina.begin_fill()
    tina.color("#1c1f1d")
    tina.circle(14)
    tina.end_fill()
   

tina.penup()
# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()
tina.speed(7)


tina.goto(-150,150)
tina.begin_fill()
tina.color("#a63c16")
tina.pendown()

tina.goto (150,150)
tina.goto(0,-160)
tina.goto(-150,150)
tina.end_fill()

tina.penup()
tina.goto(143,141)
tina.begin_fill()
tina.color("#e02d19")
tina.pendown()
tina.goto(0,-160)
tina.goto(-143,141)
tina.goto(-143,141)
tina.end_fill()

tina.penup()
tina.goto(143,135)
tina.begin_fill()
tina.color("#e8e097")
tina.pendown()
tina.goto (0,-160)
tina.goto(-143,135)
tina.end_fill()



drawolive(0,0)
drawolive(40,45)


turtle.exitonclick()                    # Close the window when we click on it
