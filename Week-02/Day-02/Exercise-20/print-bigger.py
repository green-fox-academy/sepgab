a = int(input('Give me a number: '))
b = int(input('Give me another number'))
if a >> b:
    print(str(a) + ' is the bigger number.')
elif a << b:
    print(str(b) + ' is the bigger number.')
else:
    print('The numbers are equal!')
