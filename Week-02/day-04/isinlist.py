# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts listOfNumbers as an input
# it should return "true" if it contains all, otherwise print "false"

listOfNumbers = [2, 4, 6, 8, 10, 12, 14, 16]

def finder(list):
    condition = [False, False, False, False]

    for a in range(4):
        for nr in range(0, len(list)-1):
            if list[nr] == 4 * a:
                condition[a] = True
            else:
                pass

    if condition == True:
        print(True)
    else:
        print(False)

finder(listOfNumbers)
