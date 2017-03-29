from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/line-play/r1.png]

width = 150
height = 150

for i in range (0, width+1, 10):
    canvas.create_line(i, 0, width, i, fill='green')
    canvas.create_line(0, i, i, height, fill='purple')

for i in range (0, width+1, 10):
    canvas.create_line(width+i, 0, 2*width, i, fill='green')
    canvas.create_line(width, i, width+i, height, fill='purple')

for i in range (0, width+1, 10):
    canvas.create_line(i, height, width, height+i, fill='green')
    canvas.create_line(0, height+i, i, 2*height, fill='purple')

for i in range (0, width+1, 10):
    canvas.create_line(width+i, height, 2*width, height+i, fill='green')
    canvas.create_line(width, height+i, width+i, 2*height, fill='purple')


root.mainloop()
