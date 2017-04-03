import random

class Dice():

    def __init__(self):
        self.dice = [0, 0, 0, 0, 0, 0]

    def roll(self):
        for i in range(len(self.dice)):
            self.dice[i] = random.randint(1,6)
        return self.dice

    def getCurrent(self, index=None):
        if index != None:
            return self.dice[index]
        else:
            return self.dice

    def reroll(self, index=None):
        if index != None:
            self.dice[index] = random.randint(1,6)
        else:
            self.roll()


dice = Dice()
dice.roll()
print(dice.getCurrent())
for i in range(0, 6):
    while dice.getCurrent(i) != 6:
        dice.reroll(i)
print(dice.getCurrent())
#dice.reroll(1)
#print(dice.getCurrent(3))
#print(dice.getCurrent())
