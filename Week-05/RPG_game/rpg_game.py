from tkinter import *
import random

root = Tk()
canvas = Canvas(root, width='720', height='720')
canvas.pack()




class Character():

    def move(self, char_event):
        pass

    def fight(self, enemy):
        enemy_hp


class Hero(Character):

    def __init__(self, x=0, y=0):
        self.pos_x = 0
        self.pos_y = 0
        self.char_down = PhotoImage(file="hero-down.png")
        self.char_left = PhotoImage(file="hero-left.png")
        self.char_right = PhotoImage(file="hero-right.png")
        self.char_up = PhotoImage(file="hero-up.png")
        self.hero = canvas.create_image(72 * self.pos_x, 72 * self.pos_y, anchor=NW, image=self.char_down)

        self.hero_hp = 20 + 3 * random.randint(1, 6)
        self.hero_dp = 2 * random.randint(1, 6)
        self.hero_sp = 5 + random.randint(1, 6)

    def move(self, x, y, direction):
        if 0 <= x <= 9 and 0 <= y <= 9:
            if map_level_1[y][x] == 1:
                canvas.delete(self.hero)
                self.pos_x = x
                self.pos_y = y
                self.hero = canvas.create_image(72 * self.pos_x, 72 * self.pos_y, anchor=NW, image=direction)
            elif map_level_1[y][x] == 'skeleton':
                canvas.delete(self.hero)
                self.pos_x = x
                self.pos_y = y
                self.hero = canvas.create_image(72 * self.pos_x, 72 * self.pos_y, anchor=NW, image=direction)
                self.fight('skeleton')

class Enemy(Character):

    def __init__(self):
        self.skeleton = PhotoImage(file="skeleton.png")

    def place(self):
        self.number_of_skeletons = random.randint(3, 6)
        self.skeleton_counter = 0
        while self.skeleton_counter < self.number_of_skeletons:
            self.pos_x = random.randint(0, 9)
            self.pos_y = random.randint(0, 9)
            if self.pos_x == 0 and self.pos_y == 0:
                pass
            elif map_level_1[self.pos_y][self.pos_x] == 1:
                canvas.create_image(72*self.pos_x, 72*self.pos_y, anchor=NW, image=self.skeleton)
                self.skeleton_counter += 1
                map_level_1[self.pos_y][self.pos_x] = 'skeleton'

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
[1, 1, 1, 0, 1, 0, 0, 1, 1, 1]]

area = Area()
for y in range(len(map_level_1)):
    for x in range(len(map_level_1[y])):
        if map_level_1[y][x] == 1:
            area.draw_floor(72*x, 72*y)
        else:
            area.draw_wall(72*x, 72*y)

hero = Hero()
skeleton = Enemy()
skeleton.place()

def on_key_press(e):
    if e.keycode == 38:
        hero.move(hero.pos_x, hero.pos_y-1, hero.char_up)
    elif e.keycode == 40:
        hero.move(hero.pos_x, hero.pos_y+1, hero.char_down)
    elif e.keycode == 37:
        hero.move(hero.pos_x-1, hero.pos_y, hero.char_left)
    elif e.keycode == 39:
        hero.move(hero.pos_x+1, hero.pos_y, hero.char_right)

class Game():

    def __init__(self):
        self.level = 1

class Area():

    def __init__(self):
        self.floor_tile = PhotoImage(file="floor.png")
        self.wall_tile = PhotoImage(file="wall.png")

    def draw_floor(self, x, y):
        canvas.create_image(x,y, anchor=NW, image=self.floor_tile)

    def draw_wall(self, x, y):
        canvas.create_image(x,y, anchor=NW, image=self.wall_tile)

canvas.bind("<KeyPress>", on_key_press)
canvas.pack()

canvas.focus_set()

root.mainloop()
