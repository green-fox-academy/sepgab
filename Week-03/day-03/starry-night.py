from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

width = 300
height = 300

canvas.create_rectangle(0,0,width,height, fill='black')
n = 50


for i in range(n):
    list_color = []
    x = random.randint(0,width)
    y = random.randint(0,height)
    a = random.randint(0,100)
    list_color = 'gray' + str(a)

    canvas.create_rectangle(x, y, x+5, y+5, fill=list_color)

root.mainloop()
