class Problem45:

    def jump(self, nums: list[int]) -> int:
        """
        Breadth First Search solution..
        BFS is commonly used for shortest path. And "minimum number of jumps" is the shortest path
        Complexity is O(n + jumps), best complexity is < O(n)
        Space is O(3n) -> O(n)

        Note that I kept track of the level along with the index in the queue
        """
        visited = {0}
        queue = [{'i':0,
                  'depth':0}]
        while queue:
            element = queue.pop(0)
            i = element['i']
            depth = element['depth']
            if i == len(nums)-1:
                return depth

            max_jumps = nums[i]
            for j in range(1, max_jumps+1):
                k = i + j
                if k not in visited:
                    visited.add(k)
                    if k < len(nums):
                        queue.append({'i':k,
                                      'depth':depth+1})

        return -1 #if not found



    def jump_time_exceeded(self, nums: list[int]) -> int:
        """
        Depth First Search.. What is not suitable for shortest path
        Even with some optimizations, it is not quick enough once it can go very depth in some cases
        """
        dead_end = set()

        def minJumps(i, count, min_jumps) -> tuple[int, bool]:
            if i >= len(nums) or i in dead_end:
                return min_jumps, False

            if count >= min_jumps:
                return min_jumps, None # I don't need to keep going, because I already have a better solution

            if i == len(nums) - 1:
                return count, True

            # Make big jumps first once they have biggest chances of being the shortest path
            # Possible Improvement/optimizations:
            #  - Check all i+1 before enter again in the recursion. We may already have the solution
            #  - Parallelize/Distribute - in this case it is not needed because it is light waight, but in real world that may havier
            found = False
            max_allowed_jumps = nums[i]
            if max_allowed_jumps > 0:
                for j in range(max_allowed_jumps, 0, -1):
                    r_jumps, r_found = minJumps(i + j, count + 1, min_jumps)
                    min_jumps = min(r_jumps, min_jumps)
                    if r_found == True or r_found is None:
                        found = r_found

            if found == False:
                dead_end.add(i)
            return min_jumps, found


        min_jumps, found = minJumps(0, 0, 100000)
        return min_jumps