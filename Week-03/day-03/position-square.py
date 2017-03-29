from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

def squaredraw(int1, int2):
    canvas.create_rectangle(int1, int2, int1+50, int2+50)

squaredraw(50,50)
squaredraw(150,250)
squaredraw(0,150)


root.mainloop()
