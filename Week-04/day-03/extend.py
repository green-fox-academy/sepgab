# Adds a and b, returns as result
def add(a, b):
    return a+b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b > a and b >= c:
        return b
    else:
        return c

# Returns the median value of a list given as param
def median(pool):
    sorted_pool = sorted(pool)
    pool_len = len(pool)
    index = (pool_len - 1) // 2
    if (pool_len % 2):
        return sorted_pool[index]
    else:
        return (sorted_pool[index] + sorted_pool[index + 1])/2.0

# Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aeiouéáőűöüóúí'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    word = list(str(hungarian))
    teve = []
    for char in word:
        if is_vovel(char):
            teve.append(char+'v'+char)
        else:
            teve.append(char)
    return ''.join(teve)
