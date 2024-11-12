
class Problem16:



    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if abs(target - summ) < abs(target - closest):
                    closest = summ
                if summ < target:
                    j += 1
                elif summ > target:
                    k -= 1
                else:
                    return summ # equal to target
        return closest

# BKP

    def threeSumClosest_n3_timeouterror(self, nums: list[int], target: int) -> int:
        closest = None
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    summ = nums[i] + nums[j] + nums[k]
                    if self._is_sum_closer(target, summ, closest):
                        closest = summ
                        if closest == target:
                            return closest
        return closest

    def _is_sum_closer(self, target, summ, closest):
        return closest is None or \
            abs(target - summ) < abs(target - closest)