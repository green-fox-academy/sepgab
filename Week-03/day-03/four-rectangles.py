from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

rec1 = canvas.create_rectangle(50,50, 100,150, fill='red')
rec2 = canvas.create_rectangle(150,50, 200,250, fill='lime green')
rec3 = canvas.create_rectangle(20,150, 50,180, fill='green')
rec4 = canvas.create_rectangle(230,180, 250,300, fill='blue')

# draw four different size and color rectangles.

root.mainloop()
