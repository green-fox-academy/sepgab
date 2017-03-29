from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

list_box = [[10, 10], [290,  10], [290, 290], [10, 290]]
list_dots = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]

def draw_polygon(list):
    n = len(list)
    for i in range(n):
        if i != n-1:
            canvas.create_line(list[i][0], list[i][1], list[i+1][0], list[i+1][1], fill='green')
        elif i == n-1:
            canvas.create_line(list[i][0], list[i][1], list[0][0], list[0][1], fill='green')

draw_polygon(list_box)

draw_polygon(list_dots)

root.mainloop()
