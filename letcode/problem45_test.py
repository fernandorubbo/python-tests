import unittest

from problem45 import Problem45

class TestCaseProblem45(unittest.TestCase):

    def test_1(self):
        actual = Problem45().jump([2,3,1,1,4])
        expected = 2
        self.assertEqual(actual, expected)

    def test_2(self):
        actual = Problem45().jump([2,3,0,1,4])
        expected = 2
        self.assertEqual(actual, expected)

    def test_3(self):
        actual = Problem45().jump([9,8,2,2,0,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5])
        expected = 3
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
