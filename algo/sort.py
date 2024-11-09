import unittest

#
# Merge Sort
#

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    i = int(len(arr)/2)
    l_arr = merge_sort(arr[:i])
    r_arr = merge_sort(arr[i:])
    return _merge(l_arr, r_arr)

def _merge(l, r):
    i = 0
    j = 0
    result = []
    while i < len(l) or j < len(r):
        if (j == len(r)) or (i<len(l) and l[i] < r[j]):
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j = j+1
    return result

class TestMergeSort(unittest.TestCase):
    def test(self):
        arr = [1,4,3,7,9,6,2,3,20,10]
        self.assertEqual(merge_sort(arr), [1,2,3,3,4,6,7,9,10,20])


#
# Quick Sort
#

def _swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def _quick_sort_recursive(arr, start, end):
    if start >= end:
        return
    i_pivot = start + int((end-start)/2) # getting the middle is naive -- improve
    pivot = arr[i_pivot]
    # swap pivot to the end
    _swap(arr, i_pivot, end)
    i = start
    j = end -1
    while i <= j:
        while arr[i] < pivot:
            i += 1
        # found i, where arr[i] > pivot
        while arr[j] > pivot:
            j -= 1
        # found j, where arr[j] < pivot        
        if i < j:
            _swap(arr, i, j)
            i += 1
            j -= 1
    # swap pivot to its correct place
    _swap(arr, i, end)
    _quick_sort_recursive(arr, start, i-1)
    _quick_sort_recursive(arr, i+1, end)

def quick_sort(arr):
    _quick_sort_recursive(arr, 0, len(arr)-1)

class TestQuickSort(unittest.TestCase):
    def test(self):
        arr = [1,4,3,7,9,6,2,3,20,10]
        quick_sort(arr)
        self.assertEqual(arr, [1,2,3,3,4,6,7,9,10,20])


if __name__ == '__main__':
    unittest.main()