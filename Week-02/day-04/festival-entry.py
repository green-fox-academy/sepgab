queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

# Queue of festivalgoers at entry
# no. of alcohol units
# no. of guns

# Create a security_check function that returns a list of festivalgoers who can enter the festival

# If guns are found, remove them and put them on the watchlist (only the names)
# If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival

def security_check(dict_1):
    watchlist = []
    security_alcohol_loot = 0
    enter_names = []
    for i in range(len(dict_1)):
        enter_names.append(dict_1[i]['name'])
    for i in range(len(dict_1)):
        for key in dict_1[i]:
            if dict_1[i]['guns'] != 0:
                dict_1[i]['guns'] = 0
                watchlist.append(dict_1[i]['name'])
                enter_names.remove(dict_1[i]['name'])
            if dict_1[i]['alcohol'] != 0:
                security_alcohol_loot += dict_1[i]['alcohol']
                dict_1[i]['alcohol'] = 0
    print(watchlist)
    print(security_alcohol_loot)
    print(enter_names)

security_check(queue)
