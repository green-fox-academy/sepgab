a = int(input("Give me a number for the diagonal: "))
sq = '%'
space = ' '
print(sq * (a + 1))
for i in range(1, a - 1):
    print(sq, space * ((a - i - 3) / 2), sq, space * ((a - 3) / 2), sq)
    i += 1
print(sq * (a + 1))
