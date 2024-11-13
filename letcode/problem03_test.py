import unittest
from problem03 import Problem03

class TestProblem03(unittest.TestCase):

    def test_simple(self):
        actual = Problem03().lengthOfLongestSubstring("pwwkew")
        expected = 3
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()