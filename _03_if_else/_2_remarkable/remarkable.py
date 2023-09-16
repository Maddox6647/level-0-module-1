from tkinter import messagebox, Tk, simpledialog
if __name__ == "__main__":

    window = Tk()

    window.withdraw()

    name = simpledialog.askstring(title='remarkable', prompt='what is ur name?')
    if name == name:
        messagebox.showinfo(title='remarkable', message='' + name + ', you are remarkable because you are fat')

