a = int(input("Give me a number for the pyramid: "))
nr = '*'
space = ' '
for i in range(0, a + 1):
    print(space * (a - i), nr * (2 * i + 1))
    i += 1
