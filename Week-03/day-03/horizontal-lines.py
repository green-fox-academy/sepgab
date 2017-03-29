from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

def drawline (int1, int2):
    canvas.create_line(int1, int2, int1+50, int2)

drawline(50,100)
drawline(250,100)
drawline(100,250)

root.mainloop()
