# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

def count_ears(num):
    if num == 1:
        return 2
    elif num == 0:
        return 3
    else:
        if num % 2 == 1:
            return 2 + count_ears(num-1)
        elif num % 2 == 0:
            return 3 + count_ears(num-1)

print(count_ears(5))
