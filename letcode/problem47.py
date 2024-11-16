class Problem47:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums.copy()]

        visited = set()
        result = []
        for i in range(len(nums)):
            if nums[i] not in visited:
                visited.add(nums[i])
                n = nums.pop(i)
                permutations = self.permuteUnique(nums)
                for perm in permutations:
                    perm.append(n)
                    result.append(perm)
                nums.insert(i,n)

        return result
