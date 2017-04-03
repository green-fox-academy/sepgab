from fleet import Fleet
from thing import Thing

fleet = Fleet()
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

a = Thing('Get milk')
a.__str__()
fleet.add(a)

b = Thing('Remove the obstacles')
b.__str__()
fleet.add(b)

c = Thing('Stand up')
c.complete()
c.__str__()
fleet.add(c)

d = Thing('Eat lunch')
d.complete()
d.__str__()
fleet.add(d)

print(fleet)
