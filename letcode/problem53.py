class Problem53:
    def maxSubArray(self, nums: list[int]) -> int:
        first = 0
        max_sub_sum = nums[first]
        while first < len(nums):
            tmp_sum = nums[first]
            current = first + 1
            while current < len(nums):
                if nums[current] > tmp_sum and tmp_sum <= 0:
                    max_sub_sum = max(max_sub_sum, nums[current])
                    break
                tmp_sum += nums[current]
                max_sub_sum = max(max_sub_sum, tmp_sum)
                current += 1
            first = current
        return max_sub_sum