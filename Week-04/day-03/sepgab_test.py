import unittest
from sepgab_work import Apples, Operations, anagram_checker, letter_counter, fibonacci, Sharpie, Animal

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
        self.assertEqual(fibonacci(5), 3)

class TestSharpie(unittest.TestCase):

    def test_sharpie_init_color(self):
        pen = Sharpie('black', 100)
        self.assertEqual(pen.color, 'black')

    def test_sharpie_init_width(self):
        pen = Sharpie('black', 100)
        self.assertEqual(pen.width, 100)

    def test_sharpie_use_some(self):
        pen = Sharpie('black', 100)
        pen.use(10)
        self.assertEqual(pen.ink_amount, 90)

    def test_sharpie_use_all(self):
        pen = Sharpie('black', 100)
        pen.use(100)
        self.assertEqual(pen.ink_amount, 0)

    def test_sharpie_use_more_than_all(self):
        pen = Sharpie('black', 100)
        pen.use(120)
        self.assertEqual(pen.ink_amount, 0)

class TestAnimal(unittest.TestCase):

    def test_animal_init_with_parameters(self):
        animal1 = Animal(80, 100)
        self.assertEqual(animal1.hunger, 80)
        self.assertEqual(animal1.thirst, 100)

    def test_animal_init_without_parameters(self):
        animal1 = Animal()
        self.assertEqual(animal1.hunger, 50)
        self.assertEqual(animal1.thirst, 50)

    def test_animal_eat(self):
        animal1 = Animal()
        animal1.eat()
        self.assertEqual(animal1.hunger, 49)

    def test_animal_drink(self):
        animal1 = Animal()
        animal1.drink()
        self.assertEqual(animal1.thirst, 49)

    def test_animal_play(self):
        animal1 = Animal()
        animal1.play()
        self.assertEqual(animal1.hunger, 51)
        self.assertEqual(animal1.thirst, 51)








if __name__ == '__main__':
    unittest.main()
