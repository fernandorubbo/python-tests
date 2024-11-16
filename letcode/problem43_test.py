import unittest

from problem43 import Problem43

class TestCaseProblem43(unittest.TestCase):

    def test_1(self):
        actual = Problem43().multiply("2", "3")
        expected = "6"
        self.assertEqual(actual, expected)

    def test_2(self):
        actual = Problem43().multiply("35", "7")
        expected = "245"
        self.assertEqual(actual, expected)

    def test_3(self):
        actual = Problem43().multiply("7", "35")
        expected = "245"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()