class Garden():
    def __init__(self):
        self.flowers_and_trees = []

    def add_plant(self, plant):
        self.flowers_and_trees.append(plant)

    def watering(self, watering):
        print('Watering with ' + str(watering))
        self.plants_to_water = []
        for i in self.flowers_and_trees:
            if i.needs_watering == 'needs water':
                self.plants_to_water.append(i)
        self.water_amount = watering / len(self.plants_to_water)
        for i in self.plants_to_water:
            i.watering(self.water_amount)

    def __str__(self):
        result = ""
        for i in range(0, len(self.flowers_and_trees)):
            result += "The " + self.flowers_and_trees[i].color + " " +  self.flowers_and_trees[i].type + " " + self.flowers_and_trees[i].needs_watering + "\n"
        return result

class Flower():
    def __init__(self, color):
        self.color = color
        self.type = 'Flower'
        self.water_level = 0
        self.needs_watering = 'needs water'
        self.needs_watering_level = 5.0

    def watering(self, water_amount):
        self.water_level += water_amount*0.75
        if self.water_level >= self.needs_watering_level:
            self.needs_watering = 'doesn\'t need water'

class Tree():
    def __init__(self, color):
        self.color = color
        self.type = 'Tree'
        self.water_level = 0
        self.needs_watering = 'needs water'
        self.needs_watering_level = 10.0

    def watering(self, water_amount):
        self.water_level += water_amount*0.40
        if self.water_level >= self.needs_watering_level:
            self.needs_watering = 'doesn\'t need water'

garden = Garden()

flower1 = Flower('yellow')
flower2 = Flower('blue')
tree1 = Tree('purple')
tree2 = Tree('orange')

garden.add_plant(flower1)
garden.add_plant(flower2)
garden.add_plant(tree1)
garden.add_plant(tree2)

print(garden)

garden.watering(40)
print(garden)

garden.watering(70)
print(garden)
