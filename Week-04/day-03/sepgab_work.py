class Apples():

    def get_apple(self):
        return 'Apple'

class Operations():

    def sum(self, list_of_int):
        self.total = 0
        for num in list_of_int:
            self.total += num
        return self.total

def anagram_checker(string1, string2):
    list_string1 = list(string1)
    list_string1.sort()
    list_string2 = list(string2)
    list_string2.sort()
    return  list_string1 == list_string2

def letter_counter(string):
    dict_letters = {}
    string_list = list(string)
    for letter in string_list:
        if letter not in dict_letters:
            dict_letters[letter] = 1
        else:
            dict_letters[letter] += 1
    return dict_letters

def fibonacci(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
