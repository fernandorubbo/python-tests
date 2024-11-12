mapping = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }

class Problem12:

    def intToRoman(self, num: int) -> str:
        if num == 0:
            return ""

        roman = ""
        rest = 0
        if num >= 1000:
            i = int(num/1000)
            rest = num%1000
            roman = "M" * i
        elif num >= 500:
            if num >= 900:
                roman = "CM"
                rest = num - 900
            else:
                roman = "D"
                rest = num - 500
        elif num >= 100:
            i = int(num/100)
            rest = num%100
            roman = "CD" if i == 4 else ("C" * i)
        elif num >= 50:
            if num >= 90:
                roman = "XC"
                rest = num - 90
            else:
                roman = "L"
                rest = num - 50
        elif num >= 10:
            i = int(num/10)
            rest = num%10
            roman = "XL" if i == 4 else ("X" * i)
        elif num >= 5:
            if num == 9:
                roman = "IX"
                rest = 0
            else:
                roman = "V"
                rest = num - 5
        elif num >= 1:
            roman = "IV" if num == 4 else ("I" * num)

        return roman + self.intToRoman(rest)
