import unittest
from cows_and_bulls import Cab

class TestCAB(unittest.TestCase):

    def test_CAB_init(self):
        cab = Cab()
        self.assertEqual(len(str(cab.cab_to_guess)), 4)
        self.assertEqual(cab.status, 'playing')
        self.assertEqual(cab.guess_counter, 0)






if __name__ == '__main__':
    unittest.main()
