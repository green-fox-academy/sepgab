from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/envelope-star/r2.png]

width = 150
height = 150

for i in range (0, width+1, 10):
    canvas.create_line(i, height, width, height-i, fill='green')
for i in range (0, width+1, 10):
    canvas.create_line(width, i, width+i, height, fill='green')
for i in range (0, width+1, 10):
    canvas.create_line(i, height, width, height+i, fill='green')
for i in range (0, width+1, 10):
    canvas.create_line(width, height+i, 2*width-i, height, fill='green')

root.mainloop()
