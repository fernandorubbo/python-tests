class Problem18:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        nums.sort()
        for a in range(len(nums)-3):
            if a>0 and nums[a] == nums[a-1]:
                continue

            for b in range(a+1, len(nums)-2):
                if b>a+1 and nums[b] == nums[b-1]:
                    continue

                c = b+1
                d = len(nums)-1
                while c<d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while c<d and nums[c]==nums[c-1]:
                            c +=1
                        d -=1
                        while c<d and nums[d]==nums[d+1]:
                            d -=1
                    elif total < target:
                        c += 1
                    else:
                        d -= 1

        return res