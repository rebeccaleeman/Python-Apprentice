""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()
t.pendown()
t.pencolor ("blue")

def set_turtle_image(turtle, image_name):

 
    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)


set_turtle_image(t,"leaguebot_bolt.gif")
t.shapesize(10,10,10)
#t.turtlesize(stretch_wid=10, stretch_len=10, outline=10)

t.penup()

t.pendown()
for i in range (6):
    t.forward(150)                       # Move tina forward by the forward distance
    t.left(60)

turtle.exitonclick()



 
