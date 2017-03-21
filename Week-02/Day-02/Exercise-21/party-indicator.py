a = int(input('The number of girls that comes to the party: '))
b = int(input('The number of boys that comes to the party: '))

if a == 0:
    print('Sausage party')
elif (a == b) and ((a + b) > 20):
    print('The party is excellent!!!')
elif a + b > 20 and a != 0:
    print('Quite cool party!')
else:
    print('Average party...')
