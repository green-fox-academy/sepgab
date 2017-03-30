# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

def count_ears(num):
    if num == 1:
        return 2
    else:
        return 2 + count_ears(num-1)


print(count_ears(10))
