class Problem46:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums.copy()]

        result = []
        for i in range(len(nums)):
            n = nums.pop(i)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
                result.append(perm)
            # for j in range(len(perms)):
            #     result.append([n] + perms[j]) # looks like make no performance difference of creating a new array and joining
            nums.insert(i, n)

        return result

# [1,2,3]
#     1, [2,3]
#         2,[3]
#             3
#         3,[2]
#             2
#     2, [1,3]
#     3, [1,2]