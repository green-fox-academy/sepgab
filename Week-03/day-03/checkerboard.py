from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.
width = 300
height = 300
n = 8

for i in range(0, n, 2):
    for j in range(0, n, 2):
        canvas.create_rectangle(i*width/n, j*height/n, (i+1)*width/n, (j+1)*height/n, fill='black')
        canvas.create_rectangle((i+1)*width/n, (j+1)*height/n, (i+2)*width/n, (j+2)*height/n, fill='black')

root.mainloop()
