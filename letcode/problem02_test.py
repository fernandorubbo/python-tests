import unittest
from problem02 import (
    Problem02,
    ListNode
)

def to_ListNone(arr):
    prev = None
    for n in reversed(arr):
        l  = ListNode(n)
        if prev is not None:
            l.next = prev
        prev = l
    return l

class TestProblem02(unittest.TestCase):

    def test_simple(self):
        l1 = to_ListNone([2,4,3])
        l2 = to_ListNone([5,6,4])
        actual = Problem02().addTwoNumbers(l1, l2)
        expected = to_ListNone([7,0,8])
        self.assertEqualListNode(actual, expected)

    def test_zero(self):
        l1 = to_ListNone([0])
        l2 = to_ListNone([0])
        actual = Problem02().addTwoNumbers(l1, l2)
        expected = to_ListNone([0])
        self.assertEqualListNode(actual, expected)

    def assertEqualListNode(self, actual, expected):
        while True:
            self.assertEqual(actual.val, expected.val)
            actual = actual.next
            expected = expected.next
            if actual is None and expected is None:
                break
            elif (actual is not None and expected is None) or \
                (actual is None and expected is not None):
                self.fail()

if __name__ == '__main__':
    unittest.main()