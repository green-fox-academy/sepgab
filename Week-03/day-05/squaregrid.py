from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def squaregrid(size, num, pos_x, pos_y):
    if num == 1:
        canvas.create_rectangle(pos_x-size/2, pos_y-size/2, pos_x+size/2, pos_y+size/2, fill='', outline='green', width=size/10)
    else:
        canvas.create_rectangle(pos_x-size/2, pos_y-size/2, pos_x+size/2, pos_y+size/2, fill='', outline='green', width=size/10)
        squaregrid(size/2, num-1, pos_x-size/2, pos_y-size/2)
        squaregrid(size/2, num-1, pos_x-size/2, pos_y+size/2)
        squaregrid(size/2, num-1, pos_x+size/2, pos_y+size/2)
        squaregrid(size/2, num-1, pos_x+size/2, pos_y-size/2)

squaregrid(150, 5, 150, 150)

root.mainloop()
