a = int(input("Give me a number for the square: "))
sq = '%'
space = ' '
print(sq * (a + 1))
for i in range(1, a - 1):
    print(sq, space * (a - 3), sq)
    i += 1
print(sq * (a + 1))
