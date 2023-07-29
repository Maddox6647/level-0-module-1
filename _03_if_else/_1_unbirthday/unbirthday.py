from tkinter import messagebox, Tk, simpledialog




if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    birthday = simpledialog.askstring(title='bob', prompt='when was ur birthday???')
    if birthday == 'July 28, 2023':
        messagebox.showinfo(title='nothing', message='hope you have an awesome birthday')
    else:
        messagebox.showinfo(title='bobby1545', message='hope you have a very merry unbirthday!')