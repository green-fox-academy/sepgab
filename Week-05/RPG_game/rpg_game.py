from tkinter import *
import random

root = Tk()
canvas = Canvas(root, width='930', height='720')
canvas.pack()




class Character():
    pass


class Player(Character):

    def __init__(self, x=0, y=0):
        self.pos_x = 0
        self.pos_y = 0
        self.char_down = PhotoImage(file="hero-down.png")
        self.char_left = PhotoImage(file="hero-left.png")
        self.char_right = PhotoImage(file="hero-right.png")
        self.char_up = PhotoImage(file="hero-up.png")
        self.hero = canvas.create_image(72 * self.pos_x, 72 * self.pos_y, anchor=NW, image=self.char_down)
        self.hero_hp = 20 + 3 * random.randint(1, 6)
        self.hero_hp_max = self.hero_hp
        self.hero_dp = 2 * random.randint(1, 6)
        self.hero_sp = 5 + random.randint(1, 6)

    def move(self, x, y, direction):
        canvas.delete(self.hero)
        self.hero = canvas.create_image(72 * self.pos_x, 72 * self.pos_y, anchor=NW, image=direction)
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
                game.fight(player, skeleton)
            elif map_level_1[y][x] == 'boss':
                canvas.delete(self.hero)
                self.pos_x = x
                self.pos_y = y
                self.hero = canvas.create_image(72 * self.pos_x, 72 * self.pos_y, anchor=NW, image=direction)
                game.fight(player, boss)

class Enemy(Character):

    def __init__(self):
        self.skeleton = PhotoImage(file="skeleton.png")
        self.number_of_skeletons = random.randint(2, 5)
        self.skeleton_counter = 0
        self.boss = PhotoImage(file="boss.png")
        self.boss_exist = False
        self.place_boss()
        self.place_skeletons()

    def place_boss(self):
        while self.boss_exist == False:
            self.pos_x = random.randint(0, 9)
            self.pos_y = random.randint(0, 9)
            if self.pos_x == 0 and self.pos_y == 0:
                pass
            elif map_level_1[self.pos_y][self.pos_x] == 1:
                canvas.create_image(72*self.pos_x, 72*self.pos_y, anchor=NW, image=self.boss)
                self.boss_exist = True
                map_level_1[self.pos_y][self.pos_x] = 'boss'

    def place_skeletons(self):
        while self.skeleton_counter < self.number_of_skeletons:
            self.pos_x = random.randint(0, 9)
            self.pos_y = random.randint(0, 9)
            if self.pos_x == 0 and self.pos_y == 0:
                pass
            elif map_level_1[self.pos_y][self.pos_x] == 1:
                canvas.create_image(72*self.pos_x, 72*self.pos_y, anchor=NW, image=self.skeleton)
                self.skeleton_counter += 1
                map_level_1[self.pos_y][self.pos_x] = 'skeleton'





class Game_logic():

    def __init__(self):
        self.level = 1

    def on_key_press(self, e):
        if e.keycode == 38:
            player.move(player.pos_x, player.pos_y-1, player.char_up)
        elif e.keycode == 40:
            player.move(player.pos_x, player.pos_y+1, player.char_down)
        elif e.keycode == 37:
            player.move(player.pos_x-1, player.pos_y, player.char_left)
        elif e.keycode == 39:
            player.move(player.pos_x+1, player.pos_y, player.char_right)

    def fight(self, attacker, defender):
        self.enemy_hp = 2 * game.level * random.randint(1, 6)
        self.enemy_dp = 0.5 * game.level * random.randint(1, 6)
        self.enemy_sp = game.level * random.randint(1, 6)

        while self.enemy_hp > 0 and player.hero_hp > 0:
            pass

    def level_up(hero):
        pass

class Render():

    def __init__(self):
        self.floor_tile = PhotoImage(file="floor.png")
        self.wall_tile = PhotoImage(file="wall.png")
        self.logo = PhotoImage(file="wanderer_logo.png")
        self.render_map(map_level_1)
        canvas.create_image(720, 0, anchor=NW, image=self.logo)

    def draw_floor(self, x, y):
        canvas.create_image(x,y, anchor=NW, image=self.floor_tile)

    def draw_wall(self, x, y):
        canvas.create_image(x,y, anchor=NW, image=self.wall_tile)

    def render_map(self, level_map):
        for y in range(len(level_map)):
            for x in range(len(level_map[y])):
                if level_map[y][x] == 1:
                    self.draw_floor(72*x, 72*y)
                else:
                    self.draw_wall(72*x, 72*y)

    def game_infos(self):
        self.info_level = "Level " + str(game.level)
        self.info_hero = 'Health: ' + str(player.hero_hp) + '/' +  str(player.hero_hp_max)
        self.label_level = Label(root, text=self.info_level, fg="grey", font=("Verdana", 36))
        self.label_level.place(x=740, y=250)
        self.label_hero = Label(root, text=self.info_hero, fg="red", font=("Verdana", 18))
        self.label_hero.place(x=740, y=330)




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


game = Game_logic()
screen = Render()
player = Player()
skeleton = Enemy()
screen.game_infos()

canvas.bind("<KeyPress>", game.on_key_press)
canvas.pack()

canvas.focus_set()

root.mainloop()
