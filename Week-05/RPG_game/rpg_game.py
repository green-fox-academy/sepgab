from tkinter import *
from time import time, sleep
import random

root = Tk()
canvas = Canvas(root, width='930', height='720')
canvas.pack()




class Character():

    def strike(self, defender):
        self.sv = self.sp + 2 * random.randint(1, 6)
        if self.sv > defender.dp:
            defender.hp -= self.sv - defender.dp
            screen.strike_1()
        else:
            screen.strike_0()


class Player(Character):

    def __init__(self, x=0, y=0):
        self.pos_x = 0
        self.pos_y = 0
        self.char_down = PhotoImage(file="hero-down.png")
        self.char_left = PhotoImage(file="hero-left.png")
        self.char_right = PhotoImage(file="hero-right.png")
        self.char_up = PhotoImage(file="hero-up.png")
        self.hero = canvas.create_image(72 * self.pos_x, 72 * self.pos_y, anchor=NW, image=self.char_down)
        self.hp = 20 + 3 * random.randint(1, 6)
        self.hp_max = self.hp
        self.dp = 2 * random.randint(1, 6)
        self.sp = 5 + random.randint(1, 6)
        self.hero_level = 1

    def move(self, x, y, direction):
        canvas.delete(self.hero)
        self.hero = canvas.create_image(72 * self.pos_x, 72 * self.pos_y, anchor=NW, image=direction)
        if 0 <= x <= 9 and 0 <= y <= 9:
            if map_level_1[y][x] == 1:
                canvas.delete(self.hero)
                self.pos_x = x
                self.pos_y = y
                self.hero = canvas.create_image(72 * self.pos_x, 72 * self.pos_y, anchor=NW, image=direction)
            elif map_level[y][x] == 0:
                pass
            else:
                canvas.delete(self.hero)
                self.pos_x = x
                self.pos_y = y
                self.hero = canvas.create_image(72 * self.pos_x, 72 * self.pos_y, anchor=NW, image=direction)
                game.battle()

    def level_up(self):
        screen.leveling_up()
        self.hp_max += random.randint(1, 6)
        self.dp += random.randint(1, 6)
        self.sp += random.randint(1, 6)
        self.hero_level += 1
        screen.hero_stats()

    def new_area(self):
        screen.leveling_up()
        self.random_factor = random.randint(1, 10)
        if self.random_factor == 1:
            self.hp = self.hp_max
        elif 1 < self.random_factor < 6:
            self.hp += (self.hp_max-self.hp)/3
        else:
            self.hp += (self.hp_max-self.hp)/10
        screen.hero_stats()


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
            elif map_level[self.pos_y][self.pos_x] == 1:
                canvas.create_image(72*self.pos_x, 72*self.pos_y, anchor=NW, image=self.boss)
                self.boss_exist = True
                map_level[self.pos_y][self.pos_x] = 'boss'

    def place_skeletons(self):
        while self.skeleton_counter < self.number_of_skeletons:
            self.pos_x = random.randint(0, 9)
            self.pos_y = random.randint(0, 9)
            if self.pos_x == 0 and self.pos_y == 0:
                pass
            elif map_level[self.pos_y][self.pos_x] == 1:
                canvas.create_image(72*self.pos_x, 72*self.pos_y, anchor=NW, image=self.skeleton)
                self.skeleton_counter += 1
                map_level[self.pos_y][self.pos_x] = 'skeleton'

    def init_enemy(self):
        self.enemy_level = game.level
        self.random_factor = random.randint(1, 10)
        if self.random_factor == 1:
            self.enemy_level += 2
        elif 1 < self.random_factor < 6:
            self.enemy_level += 1

        if map_level[player.pos_y][player.pos_x] == 'skeleton':
            self.hp = 2 * self.enemy_level * random.randint(1, 6)
            self.dp = 0.5 * self.enemy_level * random.randint(1, 6)
            self.sp = self.enemy_level * random.randint(1, 6)
        elif map_level[player.pos_y][player.pos_x] == 'boss':
            self.hp = 2 * self.enemy_level * random.randint(1, 6) + random.randint(1, 6)
            self.dp = 0.5 * self.enemy_level * random.randint(1, 6) + 0.5 * random.randint(1, 6)
            self.sp = self.enemy_level * random.randint(1, 6) + self.enemy_level
        self.hp_max = self.hp
        screen.enemy_stats()

class GameLogic():

    def __init__(self):
        self.level = 1
        self.boss_killed = False
        self.got_key = False

    def on_key_press(self, e):
        if e.keycode == 38:
            player.move(player.pos_x, player.pos_y-1, player.char_up)
        elif e.keycode == 40:
            player.move(player.pos_x, player.pos_y+1, player.char_down)
        elif e.keycode == 37:
            player.move(player.pos_x-1, player.pos_y, player.char_left)
        elif e.keycode == 39:
            player.move(player.pos_x+1, player.pos_y, player.char_right)

    def battle(self):
        if map_level[player.pos_y][player.pos_x] != 1:
            enemy.init_enemy()
            screen.battle_started()
            while enemy.hp > 0 and player.hp > 0:
                player.strike(enemy)
                if enemy.hp < 0:
                    enemy.hp = 0
                screen.enemy_stats()
                if enemy.hp > 0:
                    enemy.strike(player)
                    if player.hp < 0:
                        player.hp = 0
                    screen.hero_stats()
        if player.hp == 0:
            screen.game_over()
        else:
            if map_level[player.pos_y][player.pos_x] == 'skeleton':
                if random.randint(1, enemy.skeleton_counter) == 1:
                    self.got_key = True
                    screen.got_key()
                enemy.skeleton_counter -= 1
            if map_level[player.pos_y][player.pos_x] == 'boss':
                self.boss_killed = True
                screen.boss_ko()
            map_level[player.pos_y][player.pos_x] = 1
            screen.battle_won()
            player.level_up()
        if self.got_key == True and self.boss_killed == True:
            player.new_area()
            screen.level_completed()
            self.new_area()

    def new_area(self):
        pass







class Render():

    def __init__(self):
        self.floor_tile = PhotoImage(file="floor.png")
        self.wall_tile = PhotoImage(file="wall.png")
        self.logo = PhotoImage(file="wanderer_logo.png")
        self.render_map(map_level)
        canvas.create_image(720, 0, anchor=NW, image=self.logo)
        self.render_quest()


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

    def render_quest(self):
        try:
            self.label_quest.destroy()
        except AttributeError:
            pass
        self.info_quest = 'Your Quests:\nFind key: ' + str(game.got_key) + '\nKill Boss: ' + str(game.boss_killed) + '\nLevel ' + str(game.level)
        self.label_quest = Label(root, text=self.info_quest, fg="grey", font=("Trajan Pro", 16))
        self.label_quest.place(x=737, y=250)

    def hero_stats(self):
        try:
            self.label_hero.destroy()
        except AttributeError:
            pass
        self.info_hero = 'Hero stats:\nHero level: ' + str(player.hero_level) + '\nHealth: ' + str(player.hp) + '/' +  str(player.hp_max) + '\nSP: ' + str(player.sp) + '\nDP: ' + str(player.dp)
        self.label_hero = Label(root, text=self.info_hero, fg="red", font=("Trajan Pro", 16))
        self.label_hero.place(x=743, y=360)

    def enemy_stats(self):
        try:
            self.label_enemy.destroy()
        except AttributeError:
            pass
        self.info_enemy = 'Enemy stats:\nHealth: ' + str(enemy.hp) + '/' +  str(enemy.hp_max) + '\nSP: ' + str(enemy.sp) + '\nDP: ' + str(enemy.dp)
        self.label_enemy = Label(root, text=self.info_enemy, fg="blue", font=("Trajan Pro", 16))
        self.label_enemy.place(x=745, y=500)

    def game_over(self):
        self.label_end = Label(root, text='GAME OVER', bg="black", fg="white", font=("Trajan Pro", 60))
        self.label_end.place(x=180, y=300)

    def battle_started(self):
        canvas.update()
        sleep(2)
        self.label_battle_start = Label(root, text='Battle started', bg="white", fg="grey", font=("Trajan Pro", 54))
        self.label_battle_start.place(x=60, y=300)
        canvas.update()
        sleep(2)
        self.label_battle_start.destroy()

    def strike_1(self):
        self.label_strike_1 = Label(root, text='Strike hit!', bg="white", fg="grey", font=("Trajan Pro", 42))
        self.label_strike_1.place(x=185, y=300)
        canvas.update()
        sleep(2)
        self.label_strike_1.destroy()

    def strike_0(self):
        self.label_strike_0 = Label(root, text='Strike defended', bg="white", fg="grey", font=("Trajan Pro", 42))
        self.label_strike_0.place(x=100, y=300)
        canvas.update()
        sleep(2)
        self.label_strike_0.destroy()

    def boss_ko(self):
        self.label_boss_ko = Label(root, text='You killed the boss!', bg="white", fg="red", font=("Trajan Pro", 42))
        self.label_boss_ko.place(x=50, y=300)
        canvas.update()
        sleep(1)
        self.label_boss_ko.destroy()

    def got_key(self):
        self.label_got_key = Label(root, text='You found the key!', bg="white", fg="red", font=("Trajan Pro", 42))
        self.label_got_key.place(x=60, y=300)
        canvas.update()
        sleep(1)
        self.label_got_key.destroy()

    def leveling_up(self):
        self.label_leveling_up = Label(root, text='Leveling up...', bg="white", fg="grey", font=("Trajan Pro", 24))
        self.label_leveling_up.place(x=240, y=300)
        canvas.update()
        sleep(2)
        self.label_leveling_up.destroy()

    def battle_won(self):
        self.label_battle_won = Label(root, text='Battle won!', bg="white", fg="red", font=("Trajan Pro", 54))
        self.label_battle_won.place(x=110, y=300)
        canvas.update()
        sleep(2)
        self.label_battle_won.destroy()
        self.label_enemy.destroy()
        canvas.create_image(72 * player.pos_x, 72 * player.pos_y, anchor=NW, image=screen.floor_tile)
        player.hero = canvas.create_image(72 * player.pos_x, 72 * player.pos_y, anchor=NW, image=player.char_down)
        self.render_quest()

    def level_completed(self):
        self.label_completed = Label(root, text='Level completed!', bg="white", fg="red", font=("Trajan Pro", 54))
        self.label_completed.place(x=30, y=300)
        canvas.update()
        sleep(2)
        self.label_completed.destroy()




map_level = [
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


game = GameLogic()
screen = Render()
player = Player()
enemy = Enemy()
screen.hero_stats()

canvas.bind("<KeyPress>", game.on_key_press)
canvas.pack()

canvas.focus_set()

root.mainloop()
