from tkinter import *
import math

root = Tk()

canvas = Canvas(root, width='600', height='450')
canvas.pack()

canvas.create_rectangle(0,0,600,400, fill='lightskyblue')
canvas.create_rectangle(0,400,600,450, fill='sienna')

def drawtree(x1, y1, x2, y2, rot_degree, num):
    if num == 1:
        canvas.create_line(x1, y1, x2, y2, fill='green')

        angle = math.atan2(y2-y1, x2-x1)
        rot_angle_in_radians = rot_degree * math.pi / 180
        line_length = ((x2-x1)**2 + (y2-y1)**2)**0.5*0.5
        center_x = x1+(x2-x1)/2
        center_y = y1+(y2-y1)/2

        x3 = center_x + line_length * math.cos(angle + rot_angle_in_radians)
        y3 = center_y + line_length * math.sin(angle + rot_angle_in_radians)
        x4 = center_x + line_length * math.cos(angle - rot_angle_in_radians)
        y4 = center_y + line_length * math.sin(angle - rot_angle_in_radians)

        canvas.create_line(center_x, center_y, x3, y3, fill='green')
        canvas.create_line(center_x, center_y, x4, y4, fill='green')
    else:
        canvas.create_line(x1, y1, x2, y2, fill='saddlebrown')

        angle = math.atan2(y2-y1, x2-x1)
        rot_angle_in_radians = rot_degree * math.pi / 180
        line_length = ((x2-x1)**2 + (y2-y1)**2)**0.5*0.5
        center_x = x1+(x2-x1)/2
        center_y = y1+(y2-y1)/2

        x3 = center_x + line_length * math.cos(angle + rot_angle_in_radians)
        y3 = center_y + line_length * math.sin(angle + rot_angle_in_radians)
        x4 = center_x + line_length * math.cos(angle - rot_angle_in_radians)
        y4 = center_y + line_length * math.sin(angle - rot_angle_in_radians)

        canvas.create_line(center_x, center_y, x3, y3, fill='saddlebrown')
        canvas.create_line(center_x, center_y, x4, y4, fill='saddlebrown')

        drawtree(center_x, center_y, center_x+(x2-center_x)*2, center_y+(y2-center_y)*2, rot_degree, num-1)
        drawtree(center_x, center_y, center_x+(x3-center_x)*2, center_y+(y3-center_y)*2, rot_degree, num-1)
        drawtree(center_x, center_y, center_x+(x4-center_x)*2, center_y+(y4-center_y)*2, rot_degree, num-1)

drawtree(300, 400, 300, 320, 20, 8)

root.mainloop()
