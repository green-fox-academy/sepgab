import time
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

def squaredraw(size, color):
    canvas.create_rectangle(150-size/2, 150-size/2, 150+size/2, 150+size/2, fill=color)

squaredraw(50, 'red')

colorlist = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#8F00FF']
sizes = [300, 250, 200, 150, 100, 50]


for i in range(len(colorlist)):
    squaredraw(sizes[i], colorlist[i])

root.mainloop()
