from tkinter import *
from tkinter.ttk import *

root = Tk()

canvas = Canvas(root, width='410', height='0')
canvas.pack()


def imagefractal(x, y, size, num):
    if num == 1:
        filename = PhotoImage(file = "greenfox_sit.png")
        image0 = canvas.create_image(x, y, anchor=NW, image=filename)
        label = Label(image=filename)
        label.image = filename # keep a reference!
        label.pack()

imagefractal(5, 5, 1, 1)


root.mainloop()
