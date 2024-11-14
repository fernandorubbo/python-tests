class Problem07:
    def reverse(self, x: int) -> int:
        s = str(x)
        signal = ''
        if s[0] == '-':
            signal = '-'
            s = s[:0:-1]
        else:
            s = s[::-1]
        y = int(signal + s)
        return 0 if (y<-(2**31) or y>((2**31)-1)) else y