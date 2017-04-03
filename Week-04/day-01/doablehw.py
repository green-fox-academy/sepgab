# 5 trees with dict:

tree1 = {"type": "oak", "leafcolor": "green", "age": 50, "sex": "male"}
tree2 = {"type": "oak", "leafcolor": "green", "age": 50, "sex": "male"}
tree3 = {"type": "oak", "leafcolor": "green", "age": 50, "sex": "male"}
tree4 = {"type": "oak", "leafcolor": "green", "age": 50, "sex": "male"}
tree5 = {"type": "oak", "leafcolor": "green", "age": 50, "sex": "male"}

tree1_list = ["oak", "green", 50, "male"]
tree2_list = ["oak", "green", 50, "male"]
tree3_list = ["oak", "green", 50, "male"]
tree4_list = ["oak", "green", 50, "male"]
tree5_list = ["oak", "green", 50, "male"]

class Car:
    brand = ''
    model = ''
    color = ''

car1 = Car()
car2 = Car()

car1.brand = 'Nissan'
car1.model = 'Sunny'
car1.color = 'green'
car2.brand = 'Mercedes'
car2.model = '190'
car2.color = 'red'

print ('Brand of car1: ' + car1.brand + ', Model: ' + car1.model + ', Color: ' + car1.color)
print ('Brand of car2: ' + car2.brand + ', Model: ' + car2.model + ', Color: ' + car2.color)

class Texts():

  def __init__(self):
    self.status = "empty"
    self.texts = []

  def add_new_text(self, new_text):
    self.texts.append(new_text)
    self.status = "length of list: " + str(len(self.texts))
    return self.texts

  def check_state(self):
    print(self.status)

  def check_text(self):
    print(self.texts)

  def check_hello(self, mit):
        print(mit)




my_texts = Texts()      # instantiate my own texts
my_texts.check_state()  # check its state
my_texts.check_hello("valami")
my_texts.add_new_text('alma')   # add some new text
my_texts.check_state()          # then check the class's state
my_texts.check_text()           # and its content

my_texts.add_new_text('korte')  # and another one
my_texts.check_state()
my_texts.check_text()
