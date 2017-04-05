import random

class Cab():

    def __init__(self):
        self.cab_to_guess = random.randint(1000, 10000)
        self.status = 'playing'
        self.guess_counter = 0
        list_cab = list(self.cab_to_guess)

    def guess(self):
        print('Guess a 4-digit number: ' + input())
