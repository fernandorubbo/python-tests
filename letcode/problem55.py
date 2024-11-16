class Problem55:
    def canJump(self, nums: list[int]) -> bool:
        """
        Greedy solution. Always choose the best option at the moment
        --
        Instead of moving forward and searching the end
        We start at the end and see which elements can get to it
        If we find the element that can get to it, we mark it as the end
        This reduces the problem each step
        """
        if len(nums) == 1:
            return True

        end = len(nums)-1
        for k in range(len(nums)-2, -1, -1):
            max_jumps = nums[k]
            if max_jumps > 0:
                for j in range(1, max_jumps+1):
                    if k + j == end:
                        end = k
                        break

        return end == 0



    def canJump_time_exceeded(self, nums: list[int]) -> bool:
        """
        Back tracking solution with dynamic programing, by
        saving dead ends and avoiding visiting it multiple times
        Complexity:
            - O(n2 + m) ~ O(n^3)
            - Space: O(n)
        """
        dead_end_indexes = set()

        def visitLast(i):
            if i > len(nums)-1 or i in dead_end_indexes:
                return False

            if i == len(nums)-1:
                return True

            max_jumps = nums[i]
            if max_jumps > 0:
                for j in range(1, max_jumps+1):
                    if visitLast(i + j):
                        return True
            dead_end_indexes.add(i)
            return False

        return visitLast(0)
