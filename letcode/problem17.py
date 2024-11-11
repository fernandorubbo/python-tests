# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 17. Letter Combinations of a Phone Number

class Problem17:
    def __init__(self):
        self.number_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

    def letterCombinations(self, digits: str) -> list[str]:
        output = []
        for digit in digits:
            try:
                int(digit)
            except ValueError:
                continue

            if digit == '0' or digit == '1':
                continue

            letters = self.number_to_letters[digit]
            if len(output) == 0:
                output = letters
            else:
                previous_output = output.copy()
                output = []
                for word in previous_output:
                    for l in letters:
                        output.append(word + l)

        return output

    def letterCombinations_rec(self, digits: str) -> list[str]:

        def rec(prefix:str, digits) -> list[str]:
            if len(digits)==0:
                return [] if prefix == '' else [prefix]

            output = []
            letters =  self.number_to_letters[digits[0]]
            for l in letters:
                output += rec(prefix+l, digits[1:])
            return output

        return rec('', digits)
