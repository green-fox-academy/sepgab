from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

line1 = canvas.create_line(50,50, 50,250, fill='red')
line2 = canvas.create_line(50,250, 250,250, fill='yellow')
line3 = canvas.create_line(250,250, 250,50, fill='blue')
line4 = canvas.create_line(250,50, 50,50, fill='black')


#draw a box that has different colored lines on each edge.

root.mainloop()
