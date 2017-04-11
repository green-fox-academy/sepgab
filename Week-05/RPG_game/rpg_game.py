from tkinter import *

root = Tk()
canvas = Canvas(root, width='600', height='660')
canvas.pack()

class Area():

    def __init__(self):
        self.floor_tile = PhotoImage(file="floor.png")
        self.floor_tile.zoom(6, 6)
        self.floor_tile.subsample(5, 5)

    def draw_tile(self, x, y):
        canvas.create_image(x,y, anchor=NW, image=self.floor_tile)


area = Area()
for x in range(10):
    for y in range(11):
        area.draw_tile(60*x, 60*y)






root.mainloop()
