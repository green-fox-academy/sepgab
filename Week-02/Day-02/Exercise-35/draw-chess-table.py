a = int(input("The number of columns: "))
b = int(input("The number of lines: "))

if a % 2 == 0 and b % 2 == 0:
    for i in range (0, b // 2):
        print((a // 2) * " %")
        print((a // 2) * "% ")
elif a % 2 == 0 and b % 2 == 1:
    for i in range (0, b // 2):
        print((a // 2) * " %")
        print((a // 2) * "% ")
    print((a // 2) * " %")
elif a % 2 == 1 and b % 2 == 0:
    for i in range (0, b // 2):
        print((a // 2) * " %" + " ")
        print((a // 2) * "% " + "%")
else:
    for i in range (0, b // 2):
        print((a // 2) * " %" + " ")
        print((a // 2) * "% " + "%")
    print((a // 2) * " %" + " ")
