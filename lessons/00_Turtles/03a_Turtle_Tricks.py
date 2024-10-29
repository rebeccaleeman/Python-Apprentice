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
tina.speed (20)
tina.hideturtle()
def drawolive(x,y):
    tina.penup()
    tina.goto(x,y)
    tina.begin_fill()
    tina.color("#1c1f1d")
    tina.circle(14)
    tina.end_fill()
    tina.penup()
    tina.goto(x,y+6)
    tina.pendown()
    tina.begin_fill()
    tina.color ("#e8e097")
    tina.circle(7)
    tina.end_fill()

def drawsquare (color, x, y, size):
    tina.penup()
    tina.goto (x,y)
    tina.pendown()
    tina.begin_fill()
    tina.color (color)
    tina.seth(0)
    for i in range (4):
        tina.forward(size)
        tina.right (90)
    tina.end_fill()
    tina.penup()

redorwhite=0

for i in range(300,-240,-60):
    for j in range (-300, 240,60):
        if redorwhite==0:
            drawsquare("red",j, i, 60)
        else:
            drawsquare("white",j,i,60)
        redorwhite=redorwhite+1
        redorwhite%=2
def drawpepper(x,y):
    print(x,y)
    drawsquare("yellow",x,y,17)





tina.penup()
# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

tina.speed(10)
tina.pencolor("gray")
tina.goto(0,-170)
tina.begin_fill()
tina.fillcolor("white")
tina.pendown()
tina.circle(200)
tina.end_fill()

tina.penup()
tina.goto(-150,150)
tina.begin_fill()
tina.pendown()
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
drawolive(90,90)
drawolive (-90,90)
drawolive(0,-100)
drawolive(-6,100)
drawolive(48,14)
drawolive(-41,65)
drawolive(-63,19)
drawolive(26,-30)
drawolive(-31,-40)
drawolive(77,65)
drawolive(-5,67)




screen=turtle.Screen()
turtle.onscreenclick(drawpepper)

screen.mainloop()

turtle.done()                   # Close the window when we click on it
