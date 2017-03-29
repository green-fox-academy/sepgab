from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

redline = canvas.create_line(0,150, 150,150, fill='red')
# draw a red horizontal line to the canvas' middle.
greenline = canvas.create_line(150,0, 150,150, fill='green')
# draw a green vertical line to the canvas' middle.

root.mainloop()
