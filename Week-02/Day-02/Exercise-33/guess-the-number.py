import random
a = int(random.randrange(1, 100))
print(a)
b = int(input("I picked a number from 1 to 100. Take a guess! "))

while a != b:
    if a > b:
        print("Nope, the number is higher. Guess again!")
        b = int(input("Guess again: "))
    else:
        print("Nope, the number is lower. Guess again!")
        b = int(input("Guess again: "))

print("Yes, that's it!")
