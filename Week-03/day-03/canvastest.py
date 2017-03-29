from tkinter import *

root = Tk()
canvas = Canvas(root, width='800', height='600')
canvas.pack()

lime_box = canvas.create_rectangle(0, 0, 400, 300, fill='lime green')
line = canvas.create_line(0, 0, 800, 600, fill='#009900', width=1)

points = [ 0,0, 800,600, 0,600, 150,200]
polygon = canvas.create_polygon( points, fill='yellow')

#img = PhotoImage(file="whatever.png")
#canvas.create_image(50,0, anchor=NW, image=img)

canvas.create_oval(50,50, 300,300, fill='blue')

coord = [50, 50, 240, 210]
arc = canvas.create_arc(coord, start=0, extent=150, fill="red")

canvas.create_oval(200,100, 230,130, fill='black')


root.mainloop()
