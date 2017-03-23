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
    print(key + ": " + value)
