class Problem05:

    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i, _ in enumerate(s):
            odd = self._expand(s, i, i)
            if len(odd) > len(longest):
                longest = odd
            if (i+1) < len(s):
                even = self._expand(s, i, i+1)
                if len(even) > len(longest):
                    longest = even
        return longest

    def _expand(self, s:str, left:int, right:int) -> str:
        while left>=0 and right<len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    def longestPalindrome_slow(self, s: str) -> str:
        longest_palindrome =  ""
        for i, _ in enumerate(s):
            j = len(s)-1
            while i <= j and (j-i+1)>len(longest_palindrome):
                if s[i] == s[j]:
                    word = s[i:j+1]
                    if self._is_palindrome(word) and \
                        len(word)>len(longest_palindrome):
                        longest_palindrome = word
                        continue
                    else:
                        j -= 1
                else:
                    j -= 1
        return longest_palindrome


    def _is_palindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<=j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
