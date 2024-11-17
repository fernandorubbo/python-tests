class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # ["eat","tea","tan","ate","nat","bat"]
        # key -> ['eat', 'tea', 'ate'], key2 -> ['bat'], key3 -> ['tan', 'nat']
        result = dict()

        for s in strs:
            # Problem constraint: strs[i] consists of lowercase English letters.
            #    That means a-z = 26 letters
            #    eg. eat = [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
            #
            # While other solutions were sorting each word and then comparing words multiple times O(n * m log m + n * m * n-1)
            # This solution is counting each letter and storing in an array O(n * m)
            count = [0] * 26
            for c in s:
                posi = ord(c) - ord('a')
                count[posi] = count[posi] + 1

            # list[int] can not be used as key in a dict
            # so we can use tuple (unmutable), or a string.. ex. key = "".join([str(c) for c in count])
            key = tuple(count)
            anagrams = result.get(key, [])
            anagrams.append(s)
            result[key] = anagrams

                # dict.values() is not a list, so need to convert to a list
        return list(result.values())



    def groupAnagrams_ainda_slow(self, strs: list[str]) -> list[list[str]]:
        strs_letters = []
        for s in strs:
            letters = dict()
            for l in s:
                letters[l] = letters.get(l, 0) + 1
            strs_letters.append(letters)

        result = []
        while strs:
            current = strs.pop(0)
            current_letters = strs_letters.pop(0)
            anagrams = [current]
            i = 0
            while i < len(strs):
                if current_letters == strs_letters[i]: # are anagrams?
                    anagrams.append(strs.pop(i))
                    strs_letters.pop(i)
                else:
                    i += 1
            result.append(anagrams)
        return result


    def groupAnagrams_still_slow(self, strs: list[str]) -> list[list[str]]:
        sorted_strs = []
        for s in strs:
            sorted_strs.append("".join(sorted(s)))

        result = []
        while strs:
            s = strs.pop(0)
            sorted_s = sorted_strs.pop(0)
            anagrams = [s]
            i = 0
            while i < len(sorted_strs):
                if sorted_s == sorted_strs[i]: # are anagrams?
                    anagrams.append(strs.pop(i))
                    sorted_strs.pop(i)
                else:
                    i += 1
            result.append(anagrams)
        return result

    def groupAnagrams_slow(self, strs: list[str]) -> list[list[str]]:
        result = []
        while strs:
            s = strs.pop(0)
            anagrams = [s]
            i = 0
            while i < len(strs):
                if self.areAnagrams(s, strs[i]):
                    anagrams.append(strs.pop(i))
                else:
                    i += 1
            result.append(anagrams)
        return result

    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        return ("".join(sorted(s1))) == ("".join(sorted(s2)))




# ["tan","ate","nat","bat"] O(n) + is anagram m * n
#     sort + bsearch O(2 m log m)
#         aat? pop if I find it

# while strs:
#     "eat" - pop(0)
#     anagrams = ["eat"]
#     for i in remaining
#         if same size? and is anagram?
#             anagrams.append( "tea" - pop(i) )