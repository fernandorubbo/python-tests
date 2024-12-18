class Problem40:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        # only to get equal numers one after another
        candidates.sort()

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return

            # include candidates[i]
            cur.append(candidates[i])
            backtrack(i + 1, cur, total + candidates[i])
            cur.pop()

            # skip candidates[i] completely to avoid duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)
        return res
