import unittest
from problem18 import Problem18


class TestProblem18(unittest.TestCase):

    def test_simple(self):
        actual = Problem18().fourSum([-3,-1,0,2,4,5], 2)
        expected = [[-3,-1,2,4]]
        self.assertEqual(actual, expected)

    def test_8(self):
        actual = Problem18().fourSum([2,2,2,2,2], 8)
        expected = [[2,2,2,2]]
        self.assertEqual(actual, expected)

    def test_0(self):
        actual = Problem18().fourSum([1,0,-1,0,-2,2], 0)
        expected = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()