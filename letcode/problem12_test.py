import unittest
from problem12 import Problem12

class TestProblem12(unittest.TestCase):

    def test_3749(self):
        actual = Problem12().intToRoman(3749)
        expected = "MMMDCCXLIX"
        self.assertEqual(actual, expected)

    def test_1994(self):
        actual = Problem12().intToRoman(1994)
        expected = "MCMXCIV"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()