import random

class Cab():

    def __init__(self):
        self.list_cab = [random.randint(1, 9)]
        for i in range(3):
            digit_checker = True
            while digit_checker == True:
                num = random.randint(0, 9)
                digit_checker = False
                for j in range(len(self.list_cab)):
                    if self.list_cab[j] == num:
                        digit_checker = True
            self.list_cab.append(num)
        self.status = 'playing'
        self.guess_counter = 0
        print(self.list_cab)


    def guess(self):
        while self.status == 'playing':
            self.guess = input('Guess a 4-digit number: ')
            list_guess = list(self.guess)
            for i in range(len(list_guess)):
                list_guess[i] = int(list_guess[i])
            print(list_guess)
            result = []
            self.guess_counter += 1
            print('Guess counter: ' + str(self.guess_counter))
            for i in range(len(list_guess)):
                if list_guess[i] == self.list_cab[i]:
                    result.append('cow')
                else:
                    for j in range(len(self.list_cab)):
                        if list_guess[i] == self.list_cab[j]:
                            result.append('bull')
                            pass
            print('You have: ' + ', '.join(result))
            if result == ['cow', 'cow', 'cow', 'cow']:
                print('Congratulations!')
                self.status = 'finished'

number = Cab()
number.guess()
