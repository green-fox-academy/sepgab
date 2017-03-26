students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

# create a function that takes a list of students and prints:
# - how many candies are owned by students

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies

def candies(list):
    for i in range(0, len(list)):
        for key, value in list[i].items():
            if key == 'candies':
                print(value)

candies(students)

def age_sum(list):
    list_min_candies =[]
    total_age = 0
    for i in range(0, len(list)):
        for key, value in list[i].items():
            if key == 'candies':
                if value < 5:
                    list_min_candies.append(list[i])
    for i in range(0, len(list_min_candies)):
        for key, value in list_min_candies[i].items():
            if key == 'age':
                total_age += value
    print(total_age)

age_sum(students)
