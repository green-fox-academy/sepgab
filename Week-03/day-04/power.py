# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def power_n(base, num):
    if num == 1:
        return base
    else:
        return base * power_n(base, num-1)

print(power_n(4, 3))
