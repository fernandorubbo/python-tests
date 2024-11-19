import unittest

from problem53 import Problem53

class TestCaseProblem53(unittest.TestCase):
    def test_1(self):
        actual = Problem53().maxSubArray([-2, -1])
        expected = -1
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()