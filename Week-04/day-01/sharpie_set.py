# Sharpie Set
#
# Reuse your Sharpie class
# Create SharpieSet class
# it contains a list of Sharpie
# count_usable() -> sharpie is usable if it has ink in it
# remove_trash() -> removes all unusable sharpies

class Sharpie:
    def __init__(self, color, width):
        self.color = str(color)
        self.width = float(width)
        self.ink_amount = float(100)

    def use(self, num):
        self.ink_amount -= num
        return self.ink_amount

class SharpieSet:
    def __init__(self):
        self.set = []

    def add(self, sharpie):
        self.set.append(sharpie)

    def count_usable(self):
        usable_pen = 0
        for pen in self.set:
            if pen.ink_amount > 0:
                usable_pen += 1
        return usable_pen

    def remove_trash(self):
        for pen in self.set:
            if pen.ink_amount == 0:
                self.set.remove(pen)
        return self.set

    def __str__(self):
        result = ""
        for i in range(0, len(self.set)):
            result += str(i+1) + ". " + self.set[i].color + ", " + str(self.set[i].width) + ", " + str(self.set[i].ink_amount) + "\n"
        return result

pen1 = Sharpie('black', 0.5)
pen2 = Sharpie('blue', 1)
pen3 = Sharpie('green', 2)
pen4 = Sharpie('red', 0.25)
pen5 = Sharpie('black', 0.5)

penset = SharpieSet()
penset.add(pen1)
penset.add(pen2)
penset.add(pen3)
penset.add(pen4)
penset.add(pen5)

print(penset)

print(penset.count_usable())

pen1.use(100)
pen3.use(50)
pen5.use(100)

print(penset.count_usable())

penset.remove_trash()

print(penset)
