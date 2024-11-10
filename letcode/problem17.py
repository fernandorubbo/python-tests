# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 17. Letter Combinations of a Phone Number

class Problem17:
    def __init__(self):
        self.number_to_letters = {
            1: None,
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz',
            0: None,
        }

    def letterCombinations(self, digits: str) -> list[str]:
        output = []
        for d in digits:
            try:
                digit = int(d)
            except ValueError:
                continue

            if digit == 0 or digit == 1:
                continue

            letters = list(self.number_to_letters[digit])
            if len(output) == 0:
                output = letters
            else:
                previous_output = output.copy()
                output = []
                for word in previous_output:
                    for l in letters:
                        output.append(word + l)

        return output