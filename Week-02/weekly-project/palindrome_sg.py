#Create a function named create palindrome following your current language's style guide. It should take a string, create a palindrome from it and then return it.

def create_palindrome(valami):
    palindrome = str(valami)
    for i in range(len(valami), 0, -1):
        palindrome += valami[i-1]
    return palindrome

print(create_palindrome("pear"))
