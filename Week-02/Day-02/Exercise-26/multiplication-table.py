a = int(input("Give me a number for the multiplication table: "))
for i in range(1, 11):
    print(str(i) + ' * ' + str(a) + ' = ' + str(a * i))
    i += 1
