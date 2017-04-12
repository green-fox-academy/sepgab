from tkinter import *

root = Tk()

canvas = Canvas(root, width='900', height='900')
canvas.pack()

def drawsquares(size, num, pos_x, pos_y):
    if num == 1:
        canvas.create_rectangle(pos_x-size/2, pos_y-size/2, pos_x+size/2, pos_y+size/2, fill='green')
    else:
        canvas.create_rectangle(pos_x-size/2, pos_y-size/2, pos_x+size/2, pos_y+size/2, fill='green')
        drawsquares(size/3, num-1, pos_x+size, pos_y-size)
        drawsquares(size/3, num-1, pos_x+size, pos_y)
        drawsquares(size/3, num-1, pos_x+size, pos_y+size)
        drawsquares(size/3, num-1, pos_x-size, pos_y-size)
        drawsquares(size/3, num-1, pos_x-size, pos_y)
        drawsquares(size/3, num-1, pos_x-size, pos_y+size)
        drawsquares(size/3, num-1, pos_x, pos_y-size)
        drawsquares(size/3, num-1, pos_x, pos_y+size)

drawsquares(300, 6, 450, 450)

root.mainloop()
