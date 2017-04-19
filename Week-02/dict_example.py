pirate ={"name": "Jack", "gold": 7, "has wooden leg": True}

print(pirate["name"])
pirate["gold"] = 8

print(pirate["gold"])

for key in pirate:
    print(key)
    print(pirate[key])

for key, value in pirate.items():
    print(key)
    print(value)
    print(key + ": " + str(value))

print(len(pirate))

armylist = [
{},
{}
]

armylist[1]['red'] = 9

print(armylist)

print(len(armylist[1]))

for key in armylist[1]:
    print(key)

armylist[1] = {}

print(armylist)
