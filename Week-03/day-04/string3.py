# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def weaponstar(string1):
    if len(string1) ==1:
        return string1 + '*'
    else:
        return string1[0] + '*' + weaponstar(string1[1:])

print(weaponstar('axdgrfx'))
