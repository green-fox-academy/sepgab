from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

def drawline(int1, int2):
    canvas.create_line(int1, int2, 150, 150)

drawline(0, 0)
drawline(250,100)
drawline(50, 650)


root.mainloop()
