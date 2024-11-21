class Problem52:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        results = []
        tmp_interval = None
        s_intervals = sorted(intervals)
        for curr_interval in s_intervals:
            if tmp_interval is None:
                tmp_interval = curr_interval
                continue
            if curr_interval[0] <= tmp_interval[1]:
                tmp_interval[1] = max(curr_interval[1], tmp_interval[1])
            else:
                results.append(tmp_interval)
                tmp_interval = curr_interval
        results.append(tmp_interval)
        return results