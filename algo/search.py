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
        ivalue = arr[i]
        if search == ivalue:
            resutl = i # found
            break
        elif search > ivalue:
            start = i + 1
        else:
            end = i - 1
    return resutl

def bsearch_recursive(arr, search, start, end):
    if start > end:
        return -1
    i = start + int((end-start)/2) 
    ivalue = arr[i]
    if search == ivalue :
        return i
    elif search < ivalue :
        return bsearch_recursive(arr, search, start, i-1)
    else:
        return bsearch_recursive(arr, search, i+1, end)

def bsearch_rec(arr, search):
    return bsearch_recursive(arr, search, 0, len(arr)-1)


class TestBsearch(unittest.TestCase):
    def test(self):
        arr = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(bsearch(arr, 6), 5)
        self.assertEqual(bsearch(arr, 1), 0)
        self.assertEqual(bsearch(arr, -1), -1)
        self.assertEqual(bsearch(arr, 10), 9)
        self.assertEqual(bsearch(arr, 11), -1)

    def test_recursion(self):
        arr = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(bsearch_rec(arr, 6), 5)
        self.assertEqual(bsearch_rec(arr, 1), 0)
        self.assertEqual(bsearch_rec(arr, -1), -1)
        self.assertEqual(bsearch_rec(arr, 10), 9)
        self.assertEqual(bsearch_rec(arr, 11), -1)

# --

if __name__ == '__main__':
    unittest.main()


