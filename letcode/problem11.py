class Problem11:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height)-1
        max_area = 0
        while i<j:
            area = min(height[i], height[j]) * (j-i)
            max_area = max(area, max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area