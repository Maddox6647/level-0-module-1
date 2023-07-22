from tkinter import messagebox, simpledialog, Tk




if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    birthday = simpledialog.askstring(title='bob', prompt='when was ur birthday???')
    if birthday == 'July 21, 2023':
        messagebox.showinfo(title='nothing', message='hope you have an awesome birthday')
    if birthday