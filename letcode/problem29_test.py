import unittest
from problem29 import Problem29


class TestCaseProblem29(unittest.TestCase):

    def test_simple(self):
        actual = Problem29().divide(10, 3)
        expected = 3
        self.assertEqual(actual, expected)

    def test_simple2(self):
        actual = Problem29().divide(-2147483648, 1)
        expected = -2147483648
        self.assertEqual(actual, expected)




if __name__ == '__main__':
    unittest.main()