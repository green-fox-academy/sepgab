#Create a function named is anagram following your current language's style guide. It should take two strings and return a boolean value depending on whether its an anagram or not.


condition = 0

def anagram(string1, string2):
    string = string2[::-1]
    switch = 1
    if len(string1) != len(string2):
        switch = 0
    else:
        for i in range(len(string1)):
            if string1[i] == string[i]:
                switch *= 1
            else:
                switch *= 0
    if switch == 1:
        condition = True
    else:
        condition = False
    return condition

print(anagram('dog', 'god'))
print(anagram('greern', 'fox'))
