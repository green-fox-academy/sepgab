from tkinter import *

root = Tk()

canvas = Canvas(root, width='500', height='500')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/triangles/r5.png]

width = 300
height = 300
size = 15
hgt = size * 3 ** 0.5 / 2
n = int(height / hgt)

for i in range(n+1):
    canvas.create_line(100+width/2-i*size/2, 100+hgt*i, 100+width/2+i*size/2, 100+hgt*i)
    canvas.create_line(100+width/2-(n-i)*size/2, 100+hgt*(n-i), 100+width/2-(n-i)*size/2+i*size/2, 100+hgt*n )
    canvas.create_line(100+width/2+(n-i)*size/2, 100+hgt*(n-i), 100+width/2+(n-i)*size/2-i*size/2, 100+hgt*n)

root.mainloop()
