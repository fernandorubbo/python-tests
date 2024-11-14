class Problem08:
    def myAtoi(self, s: str) -> int:
        res = 0
        i = 0
        while i < len(s) and s[i]==' ':
            i += 1

        signal = '+'
        if i < len(s) and s[i] in ['-', '+']:
            signal = s[i]
            i += 1

        while i < len(s) and s[i]=='0':
            i += 1

        num = ''
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1

        if num != '':
            res = int(signal + num)

        if res < -2**31:
            return -2**31
        elif res > 2**31 - 1:
            return 2**31 - 1
        else:
            return res
