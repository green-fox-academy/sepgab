import unittest
from sepgab_work import Apples

class TestCounter(unittest.TestCase):

    def test_apple(self):
        object1 = Apples()
        self.assertEqual(object1.get_apple(), 'Apple')




if __name__ == '__main__':
    unittest.main()
