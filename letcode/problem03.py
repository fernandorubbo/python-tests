class Problem03:

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_letters = 0
        letters = set()
        left = 0
        for right, _  in enumerate(s):
            if s[right] not in letters:
                letters.add(s[right])
                max_letters = max(max_letters, right-left+1)
            else:
                while s[right] in letters:
                    letters.remove(s[left])
                    left += 1
                letters.add(s[right])
        return max_letters


    def lengthOfLongestSubstring2(self, s: str) -> int:
        max_letters = 0 if s == "" else 1
        i,j = 0, 1
        letters = set()
        while i<len(s) and j<len(s):
            letters.add(s[i])
            while j<len(s) and s[j] not in letters:
                letters.add(s[j])
                max_letters = max(max_letters, j-i+1)
                j += 1
            while j<len(s) and s[i] != s[j]:
                letters.remove(s[i])
                i += 1
            letters.remove(s[i])
            i += 1
            j = (j+1) if j==i else j
        return max_letters

    def lengthOfLongestSubstring_slow(self, s: str) -> int:
        letters = dict()
        max_letters = 0 if s == "" else 1
        for i, l in enumerate(s):
            letters = {l}
            j = i+1
            while j<len(s) and s[j] not in letters:
                letters.add(s[j])
                max_letters = max(max_letters, j-i+1)
                j += 1
        return max_letters
