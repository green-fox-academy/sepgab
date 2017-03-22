a = int(input("How many numbers do you have? "))
summa = 0

for i in range(1, a + 1):
    nr = int(input("Give me number " + str(i) + ": "))
    summa += nr

print("The sum is: " + str(summa))
print("The average is: " + str(summa / a))
