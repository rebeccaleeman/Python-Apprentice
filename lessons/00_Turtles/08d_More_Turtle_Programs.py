"""
Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section " Click on the Turtle"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and when you click on it, it moves to a random location on the screen.

Use this code to get a random x and y location


    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

"""
import turtle as turtle

turtle.setup(width=600, height=600)

t = turtle.Turtle()

t.shape("turtle")
t.turtlesize(stretch_wid=10, stretch_len=10, outline=4) # Make the turtle really big
t.penup()
def turtle_clicked(t, x, y):

    print('turtle clicked!')

    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    print(x, y)

    t.goto (x,y)

# Connect the turtle to the turtle_clicked function
t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))




turtle.done()





turtle.exitonclick()