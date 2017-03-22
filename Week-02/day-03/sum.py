# - Write a function called `sum` that sum all the numbers
#   until the given parameter

def sum(nr: int):
    summa = 0
    for i in range(0, nr):
        summa += i
    return(summa)

print(sum(5))
print(sum(10))    
