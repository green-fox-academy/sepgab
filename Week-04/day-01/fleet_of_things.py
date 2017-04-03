from fleet import Fleet
from thing import Thing

fleet = Fleet()
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

a = Thing('Get milk')
fleet.add(a)

b = Thing('Remove the obstacles')
fleet.add(b)

c = Thing('Stand up')
c.complete()
fleet.add(c)

d = Thing('Eat lunch')
d.complete()
fleet.add(d)

print(fleet)
