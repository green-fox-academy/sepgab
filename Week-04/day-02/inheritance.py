class Person():
    def __init__(self, name, age, gender):
        self.name = str(name)
        self.age = int(age)
        self.gender = str('')

    def introduce(self):
        print('Hi, I\'m ' + self.name + ', a ' + str(self.age) + ' year old ' + self.gender + '.')

    def get_goal(self):
        print('My goal is: Live for the moment!')

class Student(Person):
    def __init__(self, name, age, gender, prev_org):
        super().__init__(name, age, gender)
        self.prev_org = str('')
        self.skipped_days = int(0)

    def introduce(self):
        print('Hi, I\'m ' + self.name + ', a ' + str(self.age) + ' year old ' + self.gender + ' from ' + self.prev_org + ' who skipped ' + str(self.skipped_days) + ' days from the course already.')

    def get_goal(self):
        print('My goal is: Be a junior software developer.')

    def skip_days(self, number_of_days=1):
        self.skipped_days += number_of_days

class Mentor(Person):
    def __init__(self, name, age, gender, level):
        super().__init__(name, age, gender)
        self.level= str('')

    def introduce(self):
        print('Hi, I\'m ' + self.name + ', a ' + str(self.age) + ' year old ' + self.gender + self.level + ' mentor.')

    def get_goal(self):
        print('My goal is: Educate brilliant junior software developers.')

class Sponsor(Person):
    def __init__(self, name, age, gender, company):
        super().__init__(name, age, gender)
        self.company = str(company)
        self.hired_students = 0

    def introduce(self):
        print('Hi, I\'m ' + self.name + ', a ' + str(self.age) + ' year old ' + self.gender + ' who represents ' + self.company + ' and hired ' + str(self.hired_students) + ' students so far.')

    def get_goal(self):
        print('My goal is: Hire brilliant junior software developers.')

    def hire(self):
        self.hired_students += 1
        return self.hired_students

class LagopusClass():
    def __init__(self, class_name):
        self.name = class_name
        self.students = []
        self.mentors = []

    def add_student(self, Student):
        self.students.append(Student)

    def add_mentor(self, Mentor):
        self.mentors.append(Mentor)

    def info(self):
        self.students_size = str(len(self.students))
        self.mentors_size = str(len(self.mentors))
        print('Lagopus ' + self.name + ' class has ' + self.students_size + ' students and ' + self.mentors_size + ' mentors.')



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

badass = LagopusClass('BADA55')
badass.add_student(student)
badass.add_student(john)
badass.add_mentor(mentor)
badass.add_mentor(gandhi)
badass.info()
