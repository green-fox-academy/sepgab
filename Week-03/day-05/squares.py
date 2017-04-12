from tkinter import *

root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

def drawsquares(size, num):
    a = 5/(6*(3**0.5+1/3))
    b = 5*3**0.5/(6*(3**0.5+1/3))
    c = a+(b-a)*b/(a+b)
    multiplier = c*2/3
    if num == 1:
        canvas.create_polygon(300+size, 300-size/2, 300+size/2, 300+size, 300-size, 300+size/2, 300-size/2, 300-size, fill='red', outline='black')
        canvas.create_polygon(300+size*a, 300-size*b, 300+size*b, 300+size*a, 300-size*a, 300+size*b, 300-size*b, 300-size*a, fill='orange', outline='black')
        canvas.create_polygon(300+size*c, 300, 300, 300+size*c, 300-size*c, 300, 300, 300-size*c, fill='yellow', outline='black')
    else:
        canvas.create_polygon(300+size, 300-size/2, 300+size/2, 300+size, 300-size, 300+size/2, 300-size/2, 300-size, fill='red', outline='black')
        canvas.create_polygon(300+size*a, 300-size*b, 300+size*b, 300+size*a, 300-size*a, 300+size*b, 300-size*b, 300-size*a, fill='orange', outline='black')
        canvas.create_polygon(300+size*c, 300, 300, 300+size*c, 300-size*c, 300, 300, 300-size*c, fill='yellow', outline='black')
        drawsquares(size*multiplier, num-1)

drawsquares(300, 10)

root.mainloop()
