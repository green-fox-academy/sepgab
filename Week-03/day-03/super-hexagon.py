from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/super-hexagon/r6.gif]

def hexagon(pos_x, pos_y, size):
    canvas.create_polygon(pos_x+size, pos_y, pos_x+size/2, pos_y+size*3**0.5/2, pos_x-size/2, pos_y+size*3**0.5/2, pos_x-size, pos_y, pos_x-size/2, pos_y-size*3**0.5/2, pos_x+size/2, pos_y-size*3**0.5/2, fill='', outline='black')

size = 20
width = 300
height = 300
hgt = int(size*3**0.5)


for i in range(2*size, height-2*size, hgt):
    hexagon(width/2, i, size)
for i in range(2*size, height-4*size, hgt):
    hexagon(width/2-1.5*size, size+i, size)
    hexagon(width/2+1.5*size, size+i, size)
for i in range(2*size, height-6*size, hgt):
    hexagon(width/2-3*size, 2*size+i, size)
    hexagon(width/2+3*size, 2*size+i, size)
for i in range(2*size, height-7*size, hgt):
    hexagon(width/2-4.5*size, 3*size+i, size)
    hexagon(width/2+4.5*size, 3*size+i, size)

root.mainloop()
