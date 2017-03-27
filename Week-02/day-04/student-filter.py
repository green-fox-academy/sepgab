students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints:
#  - how many candies they have on average

def candies_filter(list):
    list_max_candies = []
    for i in range(0, len(list)):
        for key, value in list[i].items():
            if key == 'candies':
                if value > 4:
                    list_max_candies.append(list[i])
    for i in range(0, len(list_max_candies)):
        for key, value in list_max_candies[i].items():
            if key == 'name':
                print(value)

candies_filter(students)

def candies_average(list):
    sum_candies = 0
    for i in range(0, len(list)):
        for key, value in list[i].items():
            if key == 'candies':
                sum_candies += value
    print(sum_candies / len(list))

candies_average(students)
