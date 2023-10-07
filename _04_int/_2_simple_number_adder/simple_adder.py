"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""

from tkinter import Tk, simpledialog, messagebox

if __name__ == "__main__":
    window = Tk()
    window.withdraw()
    simpledialog.askinteger(title='FG', prompt='what is the answer for 1 + 1???' )
    messagebox.showinfo(title='aafsdgadfskgadkg', message='answer is 2')