from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

width_screen = 300

canvas.create_rectangle(0, 0, width_screen, width_screen, fill='yellow')


def drawlines(width, num, origo_x, origo_y):
    if num == 0:
        canvas.create_line(origo_x-width/6, origo_y-width/2, origo_x-width/6, origo_y+width/2)
        canvas.create_line(origo_x+width/6, origo_y-width/2, origo_x+width/6, origo_y+width/2)
        canvas.create_line(origo_x-width/2, origo_y-width/6, origo_x+width/2, origo_y-width/6)
        canvas.create_line(origo_x-width/2, origo_y+width/6, origo_x+width/2, origo_y+width/6)
    else:
        canvas.create_line(origo_x-width/6, origo_y-width/2, origo_x-width/6, origo_y+width/2)
        canvas.create_line(origo_x+width/6, origo_y-width/2, origo_x+width/6, origo_y+width/2)
        canvas.create_line(origo_x-width/2, origo_y-width/6, origo_x+width/2, origo_y-width/6)
        canvas.create_line(origo_x-width/2, origo_y+width/6, origo_x+width/2, origo_y+width/6)
        drawlines(width/3, num-1, origo_x, origo_y-width/3)
        drawlines(width/3, num-1, origo_x, origo_y+width/3)
        drawlines(width/3, num-1, origo_x-width/3, origo_y)
        drawlines(width/3, num-1, origo_x+width/3, origo_y)

drawlines(300, 3, 150, 150)






root.mainloop()
