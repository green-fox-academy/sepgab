a = int(input("Give me a number for the diamond: "))
nr = '*'
space = ' '
for i in range(0, a + 1):
    print(space * (a - i), nr * (2 * i + 1))
    i += 1
for j in range(0, a + 1):
    print(space * (j + 1), nr * (2 * (a - j ) - 1))
    j += 1
