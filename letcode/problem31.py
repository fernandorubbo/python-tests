class Problem31:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        solved = False
        i = len(nums)-1
        while i>=0:
            j = i-1
            while j>=0 or (i==0 and j==-1): # when i==0, j=-1 (corner case)
                if nums[i]>nums[j]:
                    swap(i, j)
                    if j+1<len(nums)-1 or i==0: # when i==0, j=-1 (corner case)
                        start = i+1 if i == 0 else j+1
                        sorted_nums = sorted(nums[start:])
                        for k, v in enumerate(sorted_nums): # TODO: Perf improvements if I implement the in-place sort algorithm
                            nums[start+k] = v
                    solved = True
                    break
                j -= 1
            if solved:
                break
            i -= 1