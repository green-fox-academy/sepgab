# Petrol Station
#
# Create Station and Car classes
# Station
# gas_amount
# refill(car) -> decreases the gasAmount by the capacity of the car and increases the cars gas_amount
# Car
# gas_amount
# capacity
# create constructor for Car where:
# initialize gas_amount -> 0
# initialize capacity -> 100

class Station():

    def __init__(self):
        self.gas_amount = 1000

    def refill(self, car, amount):
        self.gas_amount -= amount
        car.gas_amount += amount

class Car():

    def __init__(self):
        self.gas_amount = 0
        self.capacity = 100

    def drive(self, km):
        self.gas_amount -= 0.1*km

mol = Station()
vehicle = Car()

print(mol.gas_amount)
print(vehicle.gas_amount)
mol.refill(vehicle, 100)

vehicle.drive(500)

print(mol.gas_amount)
print(vehicle.gas_amount)

mol.refill(vehicle, 20)

print(mol.gas_amount)
print(vehicle.gas_amount) 
