class Person:
    def __init__(self, name, age, gender):
        self.name = str(name)
        self.age = int(age)
        self.gender = str('')

    def introduce(self):
        print('Hi, I\'m ' + self.name + ', a ' + str(self.age) + ' year old ' + self.gender + '.')

    def get_goal(self):
        print('My goal is: Live for the moment!')

class Student:
    def __init__(self, name, age, gender, prev_org):
        self.name = str(name)
        self.age = int(age)
        self.gender = str('')
        self.prev_org = str('')
        self.skipped_days = int(0)

    def introduce(self):
        print('Hi, I\'m ' + self.name + ', a ' + str(self.age) + ' year old ' + self.gender + ' from ' + self.prev_org + ' who skipped ' + str(self.skipped_days) + ' days from the course already.')

    def get_goal(self):
        print('My goal is: Be a junior software developer.')

    def skip_days(self, number_of_days=1):
        self.skipped_days += number_of_days

class Mentor:
    def __init__(self, name, age, gender, level):
        self.name = str(name)
        self.age = int(age)
        self.gender = str('')
        self.level= str('')

    def introduce(self):
        print('Hi, I\'m ' + self.name + ', a ' + str(self.age) + ' year old ' + self.gender + self.level + ' mentor.')

    def get_goal(self):
        print('My goal is: Educate brilliant junior software developers.')

class Sponsor:
    def __init__(self, name, age, gender, company):
        self.name = str(name)
        self.age = int(age)
        self.gender = str('')
        self.company = str(company)
        self.hired_students = 0

    def introduce(self):
        print('Hi, I\'m ' + self.name + ', a ' + str(self.age) + ' year old ' + self.gender + ' who represents ' + self.company + ' and hired ' + str(self.hired_students) + ' students so far.')

    def get_goal(self):
        print('My goal is: Hire brilliant junior software developers.')

    def hire(self):
        self.hired_students += 1
        return self.hired_students



people = []

mark = Person('Mark', 46, 'male')
people.append(mark)
jane = Person('Jane Doe', 30, 'female')
people.append(jane)
john = Student('John Doe', 20, 'male', 'BME')
people.append(john)
student = Student('Jane Doe', 30, 'female', 'The School of Life')
people.append(student)
gandhi = Mentor('Gandhi', 148, 'male', 'senior')
people.append(gandhi)
mentor = Mentor('Jane Doe', 30, 'female', 'intermediate')
people.append(mentor)
sponsor = Sponsor('Jane Doe', 30, 'female', 'Google')
people.append(sponsor)
elon = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
people.append(elon)
student.skip_days(3)


for i in range(5):
    elon.hire()

for i in range(3):
    sponsor.hire()

for member in people:
    member.introduce()
    member.get_goal()
