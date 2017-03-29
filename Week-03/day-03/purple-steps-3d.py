from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/purple-steps-3d/r4.png]

a = 1.5
b = 20

for i in range(6):
    canvas.create_rectangle(a**(i-1)*b, a**(i-1)*b, a**(i)*b, a**(i)*b, fill='purple')


root.mainloop()
