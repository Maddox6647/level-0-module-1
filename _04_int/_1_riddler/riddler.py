"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk

if __name__ == "__main__":
    window = Tk()
    window.withdraw()
    shrek = simpledialog.askstring(title='yay', prompt='what three riddles do you want: ogre, muppit, or sus?')

    if shrek == 'ogre':
        donkey = simpledialog.askstring(title='mommy', prompt='what do you call an ogre that is the size of a tree but is from a movie?')
        if donkey == 'SHREK':
            messagebox.showinfo(title='er', message='U WIN!!!!!!')
        else:
            messagebox.showinfo(title='ballz', message='U FAILURE')

    elif shrek == 'muppit':
        MATTHEW = simpledialog.askstring(title='boo', prompt=' what is a muppit that is as dumb as a frog but as big as an arm')
        if MATTHEW == 'KERMIT THE FROG':
            messagebox.showinfo(title='shrek', message='lol that just luck')



