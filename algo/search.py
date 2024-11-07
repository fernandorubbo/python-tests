import unittest
import math

def bsearch(arr, search):
    resutl = -1 #not found
    start = 0
    end = len(arr) - 1
    while True:
        if start > end:
            break

        i = int((end-start)/2) + start
        value = arr[i]
        if value == search:
            resutl = i # found
            break
        elif value < search:
            start = i + 1
        else:
            end = i - 1
    return resutl


class TestBsearch(unittest.TestCase):
    def test_is_empty(self):
        arr = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(bsearch(arr, 6), 5)
        self.assertEqual(bsearch(arr, 1), 0)
        self.assertEqual(bsearch(arr, -1), -1)
        self.assertEqual(bsearch(arr, 10), 9)
        self.assertEqual(bsearch(arr, 11), -1)


if __name__ == '__main__':
    unittest.main()


