# Create Counter class
# which has an integer field value
# when creating it should have a default value 0 or we can specify it when creating
# we can add(number) to this counter another whole number
# or we can add() without parameters just increasing the counter's value by one
# and we can get() the current value
# also we can reset() the value to the initial value
# Check if everything is working fine with the proper test
# Download test_counter.py and place it next to your solution
# Run the test file as a usual python program

class Counter:

    def __init__(self, field=0):
        self.field_0 = field
        self.field = field

    def add(self, num=1):
        self.field += num
        return self.field

    def get(self):
        print(self.field)
        return self.field

    def reset(self):
        self.field = self.field_0
        return self.field
#
# counterstrike = Counter()
# counterstrike.add(1)
# counterstrike.get()
# counterstrike.reset()
# counterstrike.get()
#
# counter1 = Counter(10)
# counter1.get()
# counter1.add(3)
# counter1.add(10)
# counter1.get()
# counter1.reset()
# counter1.get()
