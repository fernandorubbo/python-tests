import unittest
from problem05 import Problem05

class TestProblem05(unittest.TestCase):

    def test_simple(self):
        actual = Problem05().longestPalindrome("babad")
        expected =  "bab"
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()