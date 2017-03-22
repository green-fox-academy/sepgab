def create_palindrome(valami):
    palindrome = str(valami)
    for i in range(len(valami), 0, -1):
        palindrome += valami[i-1]
    return palindrome

print(create_palindrome("pear"))
