# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

def divide(number:int):
    try:
        print(10 / number)
    except ZeroDivisionError:
        print('fail')

divide(100)
divide(0)
