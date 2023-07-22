import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    bob = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    u = simpledialog.askstring(title='gdfhdh', prompt='what would you like the turtle to draw???circle, square, or rectangle')
    # Draw the shape requested by the user using if-elif-else statements
    if u == "circle":
        bob.goto(x=0,y=0)
        bob.circle(radius=100)

    elif u == "square":
        bob.goto(x=0, y=0)
        for i in range(4):
            bob.forward(100)
            bob.right(90)
    elif u == "rectangle":
        bob.goto(x=0, y=0)
        bob.forward(300)
        bob.right(90)
        bob.forward(100)
        bob.right(90)
        bob.forward(300)
        bob.right(90)
        bob.forward(100)
        bob.right(90)


    else:
        pass

    # Call the turtle .done() method
