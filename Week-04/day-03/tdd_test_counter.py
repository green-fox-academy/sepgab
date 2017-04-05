import unittest
from tdd_counter import Counter

class TestCounter(unittest.TestCase):
    def test_get_initial(self):
        counter = Counter()
        self.assertEqual(counter.get(), 0)

    def test_get_specified_initial(self):
        counter = Counter(7)
        self.assertEqual(counter.get(), 7)

    def test_add_one(self):
        counter = Counter()
        counter.add()
        self.assertEqual(counter.get(), 1)

    def test_add_more(self):
        counter = Counter()
        counter.add(7)
        self.assertEqual(counter.get(), 7)

    def test_reset_to_zero(self):
        counter = Counter()
        counter.add(3)
        counter.reset
        self.assertEqual(counter.get(), 0)

    def test_reset_to_zero(self):
        counter = Counter(7)
        counter.add(3)
        counter.reset()
        self.assertEqual(counter.get(), 7)


if __name__== '__main__':
    unittest.main()
