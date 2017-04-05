class Counter():
    def __init__(self, start=0):
        self.current = start
        self.start = start

    def get(self):
        return self.current

    def add(self, amount=1):
        self.current += amount

    def reset(self):
        self.current = self.start
