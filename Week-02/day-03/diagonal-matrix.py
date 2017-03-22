# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

a = int(input('Elements of the matrix: '))

print("\n")
Matrix = [[0 for x in range(a)] for y in range(a)]
for i in range(0, a):
    Matrix[i][i] = 1

for i in range(0, a):
    print(Matrix[i][:])

print("\n Same, but joined: \n")

for row in Matrix:
  print(' '.join(map(str,row)))
