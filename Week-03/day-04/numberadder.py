# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

def adder(num):
    if num == 1:
        return 1
    if num != 1:
        return num + adder(num-1)

print(adder(5))
