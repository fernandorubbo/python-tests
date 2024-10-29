import unittest

# Import the function you want to test
from main import sum 

class TestSum(unittest.TestCase):

    def test_sum_positive_numbers(self):
        self.assertEqual(sum(2, 3), 5)

    def test_sum_zero(self):
        self.assertEqual(sum(5, 0), 5)

    def test_sum_negative_numbers(self):
        self.assertEqual(sum(-2, -3), -5)

    def test_sum_mixed_numbers(self):
        self.assertEqual(sum(-5, 3), -2)

if __name__ == '__main__':
    unittest.main()