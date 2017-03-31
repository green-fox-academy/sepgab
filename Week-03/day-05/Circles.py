from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def circles(size, num, pos_x, pos_y):
    if num == 0:
        canvas.create_oval(pos_x-size, pos_y-size, pos_x+size, pos_y+size)
    else:
        canvas.create_oval(pos_x-size, pos_y-size, pos_x+size, pos_y+size)
        circles(size/2, num-1, pos_x, pos_y-size/2)
        circles(size/2, num-1, pos_x+size/2, pos_y+size*3**0.5/4)
        circles(size/2, num-1, pos_x-size/2, pos_y+size*3**0.5/4)


circles(150, 5, 150, 150)


root.mainloop()
