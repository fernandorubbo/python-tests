class Problem32:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def f(s, e):
            res = [-1, -1]
            if e < s:
                return res

            h = s + (e-s)//2
            if target == nums[h]:
                res = [h,h]

                l = f(s, h-1)
                if l[0] > -1:
                    res[0] = l[0]
                elif l[1] > -1:
                    res[0] = l[1]

                r = f(h+1, e)
                if r[1] > -1:
                    res[1] = r[1]
                elif r[0] > -1:
                    res[1] = r[0]
            elif target < nums[h]:
                res = f(s, h-1)
            else:
                res = f(h+1, e)

            return res

        return f(0, len(nums)-1)
