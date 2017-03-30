from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def drawhexagons(size, num, pos_x, pos_y):
    if num == 1:
        canvas.create_polygon(pos_x+size, pos_y, pos_x+size/2, pos_y+size*3**0.5/2, pos_x-size/2, pos_y+size*3**0.5/2, pos_x-size, pos_y, pos_x-size/2, pos_y-size*3**0.5/2, pos_x+size/2, pos_y-size*3**0.5/2, fill='', outline='black')
    else:
        canvas.create_polygon(pos_x+size, pos_y, pos_x+size/2, pos_y+size*3**0.5/2, pos_x-size/2, pos_y+size*3**0.5/2, pos_x-size, pos_y, pos_x-size/2, pos_y-size*3**0.5/2, pos_x+size/2, pos_y-size*3**0.5/2, fill='', outline='black')
        drawhexagons(size/2, num-1, pos_x-size/4, pos_y-size*3**0.5/4)
        drawhexagons(size/2, num-1, pos_x-size/4, pos_y+size*3**0.5/4)
        drawhexagons(size/2, num-1, pos_x+size/2, pos_y)


drawhexagons(150, 6, 150, 150)

root.mainloop()
