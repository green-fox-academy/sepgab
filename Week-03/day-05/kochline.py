from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def drawkoch(x1, y1, x2, y2, num):
    if num == 1:
        canvas.create_line(x1, y1, x1+(x2-x1)/3, y1+(y2-y1)/3)
        canvas.create_line(x1+(x2-x1)/3, y1+(y2-y1)/3, x1+(x2-x1)/3+0.5*(x2-x1)/3+3**0.5*0.5*(y2-y1)/3, y1+(y2-y1)/3-3**0.5*0.5*(x2-x1)/3+0.5*(y2-y1)/3)
        canvas.create_line(x1+(x2-x1)/3+0.5*(x2-x1)/3+3**0.5*0.5*(y2-y1)/3, y1+(y2-y1)/3-3**0.5*0.5*(x2-x1)/3+0.5*(y2-y1)/3, x1+2*(x2-x1)/3, y1+2*(y2-y1)/3)
        canvas.create_line(x1+2*(x2-x1)/3, y1+2*(y2-y1)/3, x2, y2)
    else:
        drawkoch(x1, y1, x1+(x2-x1)/3, y1+(y2-y1)/3, num-1)
        drawkoch(x1+(x2-x1)/3, y1+(y2-y1)/3, x1+(x2-x1)/3+0.5*(x2-x1)/3+3**0.5*0.5*(y2-y1)/3, y1+(y2-y1)/3-3**0.5*0.5*(x2-x1)/3+0.5*(y2-y1)/3, num-1)
        drawkoch(x1+(x2-x1)/3+0.5*(x2-x1)/3+3**0.5*0.5*(y2-y1)/3, y1+(y2-y1)/3-3**0.5*0.5*(x2-x1)/3+0.5*(y2-y1)/3, x1+2*(x2-x1)/3, y1+2*(y2-y1)/3, num-1)
        drawkoch(x1+2*(x2-x1)/3, y1+2*(y2-y1)/3, x2, y2, num-1)

drawkoch(10, 150, 290, 150, 4)

root.mainloop()
