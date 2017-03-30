# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def weaponx(string1):
    if len(string1) ==1:
        if string1[0] == 'x':
            return 'y'
        else:
            return string1[0]
    else:
        if string1[0] == 'x':
            return 'y' + weaponx(string1[1:])
        else:
            return string1[0] + weaponx(string1[1:])

print(weaponx('axdgrfx'))
