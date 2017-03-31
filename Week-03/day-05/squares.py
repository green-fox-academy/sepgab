from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def drawsquares(size, num):
    a = 5/(6*(3**0.5+1/3))
    b = 5*3**0.5/(6*(3**0.5+1/3))
    c = a+(b-a)*b/(a+b)
    multiplier = c*2/3
    if num == 1:
        canvas.create_polygon(150+size, 150-size/2, 150+size/2, 150+size, 150-size, 150+size/2, 150-size/2, 150-size, fill='red', outline='black')
        canvas.create_polygon(150+size*a, 150-size*b, 150+size*b, 150+size*a, 150-size*a, 150+size*b, 150-size*b, 150-size*a, fill='orange', outline='black')
        canvas.create_polygon(150+size*c, 150, 150, 150+size*c, 150-size*c, 150, 150, 150-size*c, fill='yellow', outline='black')
    else:
        canvas.create_polygon(150+size, 150-size/2, 150+size/2, 150+size, 150-size, 150+size/2, 150-size/2, 150-size, fill='red', outline='black')
        canvas.create_polygon(150+size*a, 150-size*b, 150+size*b, 150+size*a, 150-size*a, 150+size*b, 150-size*b, 150-size*a, fill='orange', outline='black')
        canvas.create_polygon(150+size*c, 150, 150, 150+size*c, 150-size*c, 150, 150, 150-size*c, fill='yellow', outline='black')
        drawsquares(size*multiplier, num-1)

drawsquares(150, 10)

root.mainloop()
