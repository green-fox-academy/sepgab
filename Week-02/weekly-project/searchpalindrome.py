inp = ("dog goat dad duck doodle never")

#Create a function named search palindrome following your current language's style guide. It should take a string, search for palindromes that at least 3 characters long and return a list with the found palindromes.

#Working for 3 characters:
"""palindromes = []

def search_palindrome(valami):
    for i in range(len(valami)-1):
        if valami[i-1] == valami[i+1]:
            palindromes.append(valami[i-1:i+2])
    return(palindromes)

search_palindrome(inp)

print(palindromes)"""

#Working for 3-n characters:
palindromes = []

def search_palindrome(valami):
    for i in range(len(valami)-2):
        for j in range(2, len(valami)-i-1):
            switch = 1
            for k in range(0, j//2+1):
#                print(i, j, k)
                if valami[i+k] == valami[i+j-k]:
                    switch *= 1
                else:
                    switch *= 0
#            print(switch)
            if switch == 1:
                palindromes.append(valami[i:i+j+1])
    return(palindromes)

search_palindrome(inp)

print(palindromes)
