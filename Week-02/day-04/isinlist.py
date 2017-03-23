# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts listOfNumbers as an input
# it should return "true" if it contains all, otherwise print "false"

listOfNumbers = [2, 4, 6, 8, 10, 12, 14, 16]

def finder(list):
    n = len(list)
    condition = [False, False, False, False]
    for x in range(5):
        for nr in range(n):
            if list[nr] == 4 * x:
                condition[x-1] = True
    if condition == [True, True, True, True]:
        print(True)
    else:
        print(False)

finder(listOfNumbers)
