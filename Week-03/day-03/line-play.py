from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/line-play/r1.png]

width = 300
height = 300

for i in range (0, width+1, 20):
    canvas.create_line(i, 0, width, i, fill='green')
    canvas.create_line(0, i, i, height, fill='purple')

root.mainloop()
