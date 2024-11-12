import unittest
from problem11 import Problem11

class TestProblem11(unittest.TestCase):

    def test_11(self):
        actual = Problem11().maxArea([1,1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_many(self):
        actual = Problem11().maxArea([1,8,6,2,5,4,8,3,7])
        expected = 49
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()