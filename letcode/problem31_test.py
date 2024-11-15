import unittest
from problem31 import Problem31

class TestCaseProblem31(unittest.TestCase):

    def test_0(self):
        nums = [1,3,2]
        Problem31().nextPermutation(nums)
        expected = [2,1,3]
        self.assertEqual(nums, expected)

    def test_1(self):
        nums = [1,2,3]
        Problem31().nextPermutation(nums)
        expected = [1,3,2]
        self.assertEqual(nums, expected)

    def test_2(self):
        nums = [3,2,1]
        Problem31().nextPermutation(nums)
        expected = [1,2,3]
        self.assertEqual(nums, expected)

    def test_3(self):
        nums = [1,1,5]
        Problem31().nextPermutation(nums)
        expected = [1,5,1]
        self.assertEqual(nums, expected)

    def test_4(self):
        nums = [1]
        Problem31().nextPermutation(nums)
        expected = [1]
        self.assertEqual(nums, expected)

    def test_5(self):
        nums = [4,2,0,2,3,2,0]
        Problem31().nextPermutation(nums)
        expected = [4,2,0,3,0,2,2]
        self.assertEqual(nums, expected)





if __name__ == '__main__':
    unittest.main()
