import unittest
from sepgab_work import Apples, Operations, anagram_checker, letter_counter, fibonacci

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

class TestLetterCounter(unittest.TestCase):

    def test_letter_counting_for_empty_string(self):
        self.assertEqual(letter_counter(''), {})

    def test_letter_counting_for_one_character(self):
        self.assertEqual(letter_counter('d'), {'d': 1})

    def test_letter_counting_for_more_characters(self):
        self.assertEqual(letter_counter('Alma Ata'), {'A': 2, 'l': 1, 'm': 1, 'a': 2, 't': 1, ' ': 1})

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), 0)

    def test_fibonacci_two(self):
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_three(self):
        self.assertEqual(fibonacci(3), 1)

    def test_fibonacci_four(self):
        self.assertEqual(fibonacci(4), 2)

    def test_fibonacci_ten(self):
        self.assertEqual(fibonacci(10), 34)




if __name__ == '__main__':
    unittest.main()
