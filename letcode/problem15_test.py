import unittest
from problem15 import Problem15

class TestProblem15(unittest.TestCase):

    def test_all_zero(self):
        actual = Problem15().threeSum([0,0,0])
        expected = [[0,0,0]]
        self.assertEqual(actual, expected)

    def test_empty_result(self):
        actual = Problem15().threeSum([0,1,1])
        expected = []
        self.assertEqual(actual, expected)

    def test_many_numbers(self):
        actual = Problem15().threeSum([-1,0,1,2,-1,-4])
        expected = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(actual, expected)

    def test_many_numbers2(self):
        actual = Problem15().threeSum([-1,0,1,2,0,-1,-4,0])
        expected = [[-1,-1,2],[-1,0,1],[0,0,0]]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
