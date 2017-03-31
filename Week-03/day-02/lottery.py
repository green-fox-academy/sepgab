# Create a method that returns the five most frequent lottery number in a pretty table format
my_file = open('otos.csv', "r")

#list_games = []


#list_games = my_file.readlines()
str_games = ''.join(my_file.readlines())
list_games = str_games.split('\n')
sep_list_games = []
list_number = []
numbers = []

for i in list_games:
    sep_list_games.append(i.split(';'))

for i in range(len(sep_list_games)):
    list_number.append(sep_list_games[i][11:16])

for i in range(len(list_number)):
    for j in range(0, 5):
        numbers.append(list_number[i][j])

print(numbers)

#print(sep_list_games[0][11:16])
#print(sep_list_games[1][11:16])





#print(list_games)

#print(sep_list_games)

#for line in range(len(list_games)):
#    print(list_games[line][0:5])

#str_games = ''.join(my_file.readlines())

#print(str_games)







#def five_most_frequent():
