# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def weaponx(string1):
    if len(string1) ==1:
        if string1[0] == 'x':
            return ''
        else:
            return string1[0]
    else:
        if string1[0] == 'x':
            return '' + weaponx(string1[1:])
        else:
            return string1[0] + weaponx(string1[1:])

print(weaponx('axdgrfx'))
