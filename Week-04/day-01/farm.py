class Animal:

    def __init__(self, hunger=50, thirst=50):
        self.hunger = int(50)
        self.thirst = int(50)

    def eat(self):
        self.hunger -= 1
        return self.hunger

    def drink(self):
        self.thirst -= 1
        return self.thirst

    def play(self):
        self.hunger += 1
        self.thirst += 1
        return self.hunger, self.thirst

class Farm:
    def __init__(self, num=10):
        self.set = []
        self.freeslots = num
        self.slot0 = num

    def breed(self, animal):
        if self.freeslots > 0:
            self.freeslots -= 1
            self.set.append(animal)
        else:
            print("No more free slots!")

    def slaughter(self):
        least_hungry_animal = 100
        for animal in self.set:
            if animal.hunger < least_hungry_animal:
                least_hungry_animal = animal.hunger
        for animal in self.set:
            if animal.hunger == least_hungry_animal:
                self.set.remove(animal)
                self.freeslots += 1

    def __str__(self):
        result = ""
        for i in range(0, len(self.set)):
            result += str(i+1) + ". Hunger: " + str(self.set[i].hunger) + ", thirst: " + str(self.set[i].thirst) + "\n"
        return result

animal1 = Animal()
animal2 = Animal()
animal3 = Animal()
animal4 = Animal()
animal5 = Animal()

farm = Farm()
print(farm.freeslots)

farm.breed(animal1)
farm.breed(animal2)
farm.breed(animal3)
farm.breed(animal4)
farm.breed(animal5)

print(farm)
print(farm.freeslots)

animal1.play()
animal2.play()
animal3.play()
animal4.play()

print(farm)

farm.slaughter()

print(farm)
print(farm.freeslots)
