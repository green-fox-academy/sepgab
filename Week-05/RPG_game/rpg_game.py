from tkinter import *

root = Tk()
canvas = Canvas(root, width='600', height='660')
canvas.pack()

class Area():

    def __init__(self):
        self.floor_tile = PhotoImage(file="floor.png")
        self.floor_tile.zoom(6, 6)
        self.floor_tile.subsample(5, 5)
        self.wall_tile = PhotoImage(file="wall.png")
        self.wall_tile.zoom(6, 6)
        self.wall_tile.subsample(5, 5)

    def draw_floor(self, x, y):
        canvas.create_image(x,y, anchor=NW, image=self.floor_tile)

    def draw_wall(self, x, y):
        canvas.create_image(x,y, anchor=NW, image=self.wall_tile)

map_level_1 = [
[1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
[1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
[1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
[1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
[1, 1, 1, 1, 1, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 1, 1, 1]]

area = Area()
for y in range(len(map_level_1)):
    for x in range(len(map_level_1[y])):
        if map_level_1[y][x] == 1:
            area.draw_floor(60*x, 60*y)
        else:
            area.draw_wall(60*x, 60*y)






root.mainloop()
