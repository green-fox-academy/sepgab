# Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# The frist columns should be automatically as wide as the longest key

ingredients = [
	{ 'vodka': 1, 'needs_cooling': True },
	{ 'coffee_liqueur': 0, 'needs_cooling': True },
	{ 'fresh_cream': 1, 'needs_cooling': True },
	{ 'captain_morgan_rum': 2, 'needs_cooling': True },
	{ 'mint_leaves': 0, 'needs_cooling': False },
	{ 'sugar': 100, 'needs_cooling': False },
	{ 'lime juice': 10, 'needs_cooling': True },
	{ 'soda': 100, 'needs_cooling': True }
]

lenmax = 0
for i in range(len(ingredients)):
	lendraft = 0
	for key in ingredients[i]:
		lendraft = len(key)
		if lendraft > lenmax:
			lenmax = lendraft

print('+' + '-'*(lenmax+2) + '+' + 15*'-' + '+' + '-'*10 + '+')
print('| ' + 'Ingredient' + (lenmax-9)*' ' + '| Needs cooling | In stock |')
print('+' + '-'*(lenmax+2) + '+' + 15*'-' + '+' + '-'*10 + '+')

for i in range(len(ingredients)):
	a = ''
	b = ''
	c = ''
	for key, value in ingredients[i].items():
		if key != 'needs_cooling':
			a = str(key)
			c = str(value)
		if key == 'needs_cooling':
			if value == True:
				b = 'Yes'
			elif value == False:
				b = 'No'
	print('| ' + a + (lenmax-len(a))*' ' + ' | ' + b + (13-len(b))*' ' + ' | ' + c + (9-len(c))*' '+'|')

print('+' + '-'*(lenmax+2) + '+' + 15*'-' + '+' + '-'*10 + '+')
