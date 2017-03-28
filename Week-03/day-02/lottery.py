# Create a method that returns the five most frequent lottery number in a pretty table format
my_file = open('otos.csv', "r")

#list_games = []


#list_games = my_file.readlines()
str_games = ''.join(my_file.readlines())
list_games = str_games.split('\n')

sep_list_games = []

#sep_list_games = list_games[0].split(';')

for i in list_games:
    sep_list_games.append(i.split(';'))

print(sep_list_games)


#print(list_games)

#print(sep_list_games)

#for line in range(len(list_games)):
#    print(list_games[line][0:5])

#str_games = ''.join(my_file.readlines())

#print(str_games)







#def five_most_frequent():
