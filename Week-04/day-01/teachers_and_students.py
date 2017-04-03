# Create Student and Teacher classes
# Student
# learn()
# question(teacher) -> calls the teachers answer method
# Teacher
# teach(student) -> calls the students learn method
# answer()

class Student():

    def __init__(self):
        self.knowledge = 0

    def learn(self, time=1):
        print('Student is learning')
        self.knowledge += time

    def question(self, teacher):
        print('Student is questioning')
        teacher.answer()

class Teacher():

    def teach(self, student, time=0):
        print('Teacher is teaching')
        student.learn()

    def answer(self):
        print('Teacher is answering')


student1 = Student()
teacher1 = Teacher()

student1.learn(2)
print("Student's actual knowledge: " + str(student1.knowledge))

student1.question(teacher1)
print("Student's actual knowledge: " + str(student1.knowledge))

teacher1.teach(student1)
print("Student's actual knowledge: " + str(student1.knowledge))
