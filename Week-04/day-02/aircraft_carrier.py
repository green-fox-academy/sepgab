class Aircrafts():
    def __init__(self):
        self.ammo_level = 0

    def fight(self):
        self.damage_caused = self.ammo_level*self.base_damage
        self.ammo_level = 0
        return self.damage_caused

    def refill(self, num):
        if num < self.max_ammo - self.ammo_level:
            self.ammo_level += num
        else:
            self.ammo_level = self.max_ammo
        return self.ammo_level

    def get_type(self):
        print(self.type)

    def get_status(self):
        print('Type ' + self.type + ', Ammo: ' + str(self.ammo_level) + ', Base Damage: ' + str(self.base_damage) + ', All Damage: ' + str(self.ammo_level*self.base_damage) + '\n')

class F16(Aircrafts):
    def __init__(self):
        super().__init__()
        self.max_ammo = 8
        self.base_damage = 30
        self.type = 'F16'

class F35(Aircrafts):
    def __init__(self):
        super().__init__()
        self.max_ammo = 12
        self.base_damage = 50
        self.type = 'F35'

class Carrier():
    def __init__(self, init_ammo):
        self.aircraft_list = []
        self.store_ammo = 1000
        self.ammo_level = 0
        if init_ammo < self.store_ammo:
            self.ammo_level = init_ammo
        else:
            self.ammo_level = self.store_ammo
        self.health = 1000

    def add_aircraft(self, aircraft):
        self.aircraft_list.append(aircraft)
        return self.aircraft_list

    def fill(self):
        if self.ammo_level == 0:
            print('No more ammo!')
            return
        else:
            self.ammo_needed = 0
            for aircraft in self.aircraft_list:
                self.ammo_needed += aircraft.max_ammo - aircraft.ammo_level
            if self.ammo_needed <= self.ammo_level:
                for aircraft in self.aircraft_list:
                    aircraft.refill(aircraft.max_ammo - aircraft.ammo_level)
                    self.ammo_level -= aircraft.max_ammo - aircraft.ammo_level
            else:
                while self.ammo_level < 0:
                    for aircraft in self.aircraft_list:
                        if aircraft.type == 'F35':
                            if self.ammo_level >= aircraft.max_ammo - aircraft.ammo_level:
                                aircraft.refill(aircraft.max_ammo - aircraft.ammo_level)
                                self.ammo_level -= aircraft.max_ammo - aircraft.ammo_level
                            else:
                                aircraft.refill(self.ammo_level)
                                self.ammo_level = 0
                    for aircraft in self.aircraft_list:
                        if aircraft.type == 'F16':
                            if self.ammo_level >= aircraft.max_ammo - aircraft.ammo_level:
                                aircraft.refill(aircraft.max_ammo - aircraft.ammo_level)
                                self.ammo_level -= aircraft.max_ammo - aircraft.ammo_level
                            else:
                                aircraft.refill(self.ammo_level)
                                self.ammo_level = 0
            return self.ammo_level

    def fight(self, carrier):
        pass



    def get_status(self):
        self.total_damage = 0
        for aircraft in self.aircraft_list:
            self.total_damage += aircraft.ammo_level*aircraft.base_damage

        print('Aircraft count: ' + str(len(self.aircraft_list)) + ', Ammo Storage: ' + str(self.ammo_level) + ', Total Damage: ' + str(self.total_damage))






aircraft1 = F16()
aircraft2 = F35()
aircraft3 = F16()
aircraft4 = F35()
aircraft5 = F16()
aircraft6 = F35()

# print(aircraft1.ammo_level)
# print(aircraft1.max_ammo)
# print(aircraft1.get_status())
# aircraft1.refill(5)
# print(aircraft1.get_status())
# aircraft1.fight()
# print(aircraft1.get_status())
# aircraft1.refill(62)
# print(aircraft1.get_status())

carrier1 = Carrier(100)
carrier2 = Carrier(1000)

carrier1.add_aircraft(aircraft1)
carrier1.add_aircraft(aircraft2)
carrier1.add_aircraft(aircraft3)
carrier1.add_aircraft(aircraft4)
carrier1.add_aircraft(aircraft5)
carrier1.add_aircraft(aircraft6)

carrier1.get_status()
carrier1.fill()
carrier1.get_status()
