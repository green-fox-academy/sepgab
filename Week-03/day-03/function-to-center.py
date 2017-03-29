from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

width = 300
height = 300

def drawline(x, y):
    canvas.create_line(x, y, width/2, height/2)

for i in range (0, width+1, 20):
    drawline(i, 0)
    drawline(i, width)
    drawline(0, i)
    drawline(height, i)

root.mainloop()
