inp = ("dog goat dad duck doodle never")

#Create a function named search palindrome following your current language's style guide. It should take a string, search for palindromes that at least 3 characters long and return a list with the found palindromes.

#3 characters:
palindromes = []

def search_palindrome(valami):
    for i in range(0, len(valami)-1):
        if valami[i-1] == valami[i+1]:
            palindromes.append(valami[i-1:i+2])
    return(palindromes)

search_palindrome(inp)

print(palindromes)
