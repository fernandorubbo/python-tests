class Problem33:
    def search(self, nums: list[int], target: int) -> int:
        def f(start, end):
            if end < start:
                return -1
            if start==end:
                if nums[start] == target:
                    return start
                else:
                    return -1

            half = start + ((end-start)//2)
            if nums[half] == target:
                return half

            res = -1
            if target < nums[half]:
                res = f(start, half-1)
                if res == -1:
                    res = f(half+1, end)
            else:
                res = f(half+1, end)
                if res == -1:
                    res = f(start, half-1)

            return res

        return f(0, len(nums)-1)
