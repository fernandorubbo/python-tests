class Problem43:
    def multiply(self, num1: str, num2: str) -> str:
        """
        TODO: possible improvements
         - use array of len(num1) + len(num2) to avoid string to int and int to string conversions
         - above also avoid the hack at the end
         - while multiplying, we could already sum
         - reverse the string at the begining to simplify logic
        """
        total = ""
#      7 n2
#     35 n1
# --------
#      35
#     210
# --------
#     245
        for i in range(len(num1)-1, -1, -1):
            # multiply
            n1 = int(num1[i])
            incr = 0
            line = "" if (i == len(num1)-1) else "0" * (len(num1)-1-i)
            for j in range(len(num2)-1, -1, -1):
                n2 = int(num2[j])
                v = n1 * n2 + incr
                incr = v // 10
                mod = v % 10
                line = str(mod) + line
            if incr > 0:
                line = str(incr) + line

            # sum lines
            sub_total = ""
            incr = 0
            t, l = len(total)-1, len(line)-1
            while t>=0 or l>=0:
                n1, n2 = 0, 0
                if t>=0:
                    n1 = int(total[t])
                if l>=0:
                    n2 = int(line[l])
                v = n1 + n2 + incr
                incr = v // 10
                mod = v % 10
                sub_total = str(mod) + sub_total
                t -= 1
                l -= 1
            if incr>0:
                sub_total = str(incr) + sub_total

            total = sub_total

        # workaround for when multiplication by 0 happes.
        # because I append 0, I get the following in this math
        # num1="9133", num2="0" --> "0000"
        return str(int(total))
