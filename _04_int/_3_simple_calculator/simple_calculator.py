"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""


from tkinter import Tk, simpledialog, messagebox

if __name__ == "__main__":
    window = Tk()
    window.withdraw()
    afkghkgfsadgkfsadjhfdsahgkdafsdsfasdfdfssgkfdgkdfsgkjdfashgkfdkfdaskghdfskgjhdfsagkhdfsajgkdsfagkhfads = simpledialog.askstring(title='FG', prompt='would you like +, X, /, or -???')
    if afkghkgfsadgkfsadjhfdsahgkdafsdsfasdfdfssgkfdgkdfsgkjdfashgkfdkfdaskghdfskgjhdfsagkhdfsajgkdsfagkhfads == '+':
        simpledialog.askinteger(title='FG', prompt='what is the answer for 1 + 1???' )
        messagebox.showinfo(title='aafsdgadfskgadkg', message='answer is 2')

    elif afkghkgfsadgkfsadjhfdsahgkdafsdsfasdfdfssgkfdgkdfsgkjdfashgkfdkfdaskghdfskgjhdfsagkhdfsajgkdsfagkhfads == 'X':
        simpledialog.askinteger(title='FG', prompt='what is the answer for 1 X 1???')
        messagebox.showinfo(title='aafsdgadfskgadkg', message='answer is 1')

    elif afkghkgfsadgkfsadjhfdsahgkdafsdsfasdfdfssgkfdgkdfsgkjdfashgkfdkfdaskghdfskgjhdfsagkhdfsajgkdsfagkhfads:
        simpledialog.askinteger(title='FG', prompt='what is the answer for 1/1???')
        messagebox.showinfo(title='aafsdgadfskgadkg', message='answer is 1')

    elif afkghkgfsadgkfsadjhfdsahgkdafsdsfasdfdfssgkfdgkdfsgkjdfashgkfdkfdaskghdfskgjhdfsagkhdfsajgkdsfagkhfads:
        simpledialog.askinteger(title='FG', prompt='what is the answer for 1 - 1???')
        messagebox.showinfo(title='aafsdgadfskgadkg', message='answer is 0')

