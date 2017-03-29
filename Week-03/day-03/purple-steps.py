from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/purple-steps/r3.png]

for i in range(19):
    canvas.create_rectangle(10+i*10, 10+i*10, 20+i*10, 20+i*10, fill='purple')



root.mainloop()
