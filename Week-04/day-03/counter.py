class Counter():

    def __init__(self, start=0):
        self.start = start
        self.current = start

    def add(self, amount=1):
        self.current += amount

    def get(self):
        return self.current

    def reset(self):
        self.current = self.start

# counter = Counter(7)
# counter.add(6)
# print(counter.get())
