import unittest
from sepgab_work import Apples, Operations, anagram_checker

class TestApples(unittest.TestCase):

    def test_apple(self):
        object1 = Apples()
        self.assertEqual(object1.get_apple(), 'Apple')

class TestOperations(unittest.TestCase):

    def test_sum_method(self):
        list = [1, 2, 3, 5]
        object1 = Operations()
        self.assertEqual(object1.sum(list), 11)

    def test_sum_with_empty_list(self):
        list = []
        object1 = Operations()
        self.assertEqual(object1.sum(list), 0)

    def test_sum_with_one_element(self):
        list = [5]
        object1 = Operations()
        self.assertEqual(object1.sum(list), 5)

    def test_sum_with_more_elements(self):
        list = [5, 15, 485, 2]
        object1 = Operations()
        self.assertEqual(object1.sum(list), 507)

    def test_sum_with_null(self):
        list = [0]
        object1 = Operations()
        self.assertEqual(object1.sum(list), 0)

class TestAnagrams(unittest.TestCase):

    def test_anagrams_function_one_letter(self):
        self.assertEqual(anagram_checker('a', 'b'), False)

    def test_anagrams_function_more_letters(self):
        self.assertEqual(anagram_checker('abba', 'baba'), True)

    def test_anagrams_function_more_letters_tricky(self):
        self.assertEqual(anagram_checker('abba ', 'babab'), False)






if __name__ == '__main__':
    unittest.main()
