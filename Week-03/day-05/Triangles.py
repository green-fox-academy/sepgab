from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def triangles(size, num, pos_x, pos_y):
    if num == 0:
        canvas.create_polygon(pos_x, pos_y+size*3**0.5/2, pos_x-size, pos_y-size*3**0.5/2, pos_x+size, pos_y-size*3**0.5/2, fill='', outline='black')
    else:
        canvas.create_polygon(pos_x, pos_y+size*3**0.5/2, pos_x-size, pos_y-size*3**0.5/2, pos_x+size, pos_y-size*3**0.5/2, fill='', outline='black')
        triangles(size/2, num-1, pos_x, pos_y+size*3**0.5/4)
        triangles(size/2, num-1, pos_x-size/2, pos_y-size*3**0.5/4)
        triangles(size/2, num-1, pos_x+size/2, pos_y-size*3**0.5/4)


triangles(150, 8, 150, 150)


root.mainloop()
