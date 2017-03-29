from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

def squaredraw_center(int):
    canvas.create_rectangle(150-int/2, 150-int/2, 150+int/2, 150+int/2)

squaredraw_center(50)
squaredraw_center(100)
squaredraw_center(250)

root.mainloop()
