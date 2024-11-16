import unittest
from problem47 import Problem47

class TestCaseProblem47(unittest.TestCase):

    def test_1(self):
        actual = Problem47().permuteUnique([1,1,2])
        expected = [[2,1,1],[1,2,1],[1,1,2]]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
