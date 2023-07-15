import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    circle_variable = simpledialog.askinteger(title='circle', prompt='what is the radius')
    # Make a new turtle
    turtle_circle = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    turtle_circle.circle(radius=circle_variable)
    # Call the turtle .penup() method
    turtle_circle.penup()
    # Move your turtle to a new x,y position using .goto()
    turtle_circle.goto(x=0, y=0,)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area = math.pi * circle_variable
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    turtle_circle.write(arg="area = " + str(area), move=True, align='left', font=('Arial', 30, 'normal'))

    # Hide your turtle
    turtle_circle.hideturtle()
    # Call turtle.done()
    turtle.done()