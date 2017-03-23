# Check if the list contains "7" if it contains print "Hoorray" otherwise print "Noooooo"

numbers = [1,2,3,4,5,6,8];
condition = False

for nr in range(0, len(numbers)-1):
    if numbers[nr] == 7:
        condition = True
    else:
        pass

if condition == True:
    print('Hoorray')
else:
    print('Nooooo')
