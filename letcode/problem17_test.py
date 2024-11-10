import unittest
from problem17 import Problem17

class TestProblem17(unittest.TestCase):

    def test_empty(self):
        actual = Problem17().letterCombinations("")
        expected = []
        self.assertEqual(actual, expected)

    def test_2(self):
        actual = Problem17().letterCombinations("2")
        expected = ["a","b","c"]
        self.assertEqual(actual, expected)

    def test_23(self):
        actual = Problem17().letterCombinations("23")
        expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertEqual(actual, expected)

    def test_2859(self):
        actual = Problem17().letterCombinations("2859")
        expected = ["atjw","atjx","atjy","atjz","atkw","atkx","atky","atkz","atlw","atlx","atly","atlz","aujw","aujx","aujy","aujz","aukw","aukx","auky","aukz","aulw","aulx","auly","aulz","avjw","avjx","avjy","avjz","avkw","avkx","avky","avkz","avlw","avlx","avly","avlz","btjw","btjx","btjy","btjz","btkw","btkx","btky","btkz","btlw","btlx","btly","btlz","bujw","bujx","bujy","bujz","bukw","bukx","buky","bukz","bulw","bulx","buly","bulz","bvjw","bvjx","bvjy","bvjz","bvkw","bvkx","bvky","bvkz","bvlw","bvlx","bvly","bvlz","ctjw","ctjx","ctjy","ctjz","ctkw","ctkx","ctky","ctkz","ctlw","ctlx","ctly","ctlz","cujw","cujx","cujy","cujz","cukw","cukx","cuky","cukz","culw","culx","culy","culz","cvjw","cvjx","cvjy","cvjz","cvkw","cvkx","cvky","cvkz","cvlw","cvlx","cvly","cvlz"]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
