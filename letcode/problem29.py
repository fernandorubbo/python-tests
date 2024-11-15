class Problem29:

    def divide(self, dividend: int, divisor: int) -> int:
        signal = 1 if (dividend < 0) == (divisor < 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        # Grow fast
        quotient = 0
        total = 0
        while total < dividend:
            exp = 0
            subTotal = 0
            while (total + subTotal) < dividend:
                exp += 1                           # dividend=10 & divisor=3
                #total = divisor * (2**exp)        # 3 * 2**1 = 6 | 3 * 2**2 = 2
                subTotal = divisor << exp          # same as above.. problem disalow multiplication
            if (total + subTotal) > dividend:
                exp -= 1
            quotient += 2**exp
            total += divisor << exp

        while total < dividend:
            quotient += 1
            total += divisor
        if total > dividend:
            quotient -= 1

        quotient = quotient * signal
        return min(max(quotient, -(2**31)), (2**31 - 1))


    def divide_medium(self, dividend: int, divisor: int) -> int:
        signal = 1 if (dividend < 0) == (divisor < 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        # Grow fast
        exp = 0
        total = 0
        while total <= dividend:
            exp += 1                           # dividend=10 & divisor=3
            #total = divisor * (2**exp)        # 3 * 2**1 = 6 | 3 * 2**2 = 2
            total = divisor << exp             # same thing as above.. problem disalow
        if total > dividend:
            exp -= 1

        # Grow slow
        quotient = 2**exp
        total = divisor * (2**exp)
        while total <= dividend:
            quotient += 1
            total += divisor
        if total > dividend:
            quotient -= 1

        quotient = min(max(quotient, -(2**31)), (2**31 - 1))
        return quotient * signal

    def divide_slow(self, dividend: int, divisor: int) -> int:
        exp = 0
        summ = 0
        while summ <= abs(dividend):
            exp += 1
            summ += abs(divisor)
        if summ > abs(dividend):
            exp -= 1
        if (dividend > 0 and divisor < 0)  or \
            (dividend < 0 and divisor > 0):
            exp = exp * -1
        minus_limit = -(2**31)
        plus_limit = (2**31 - 1)
        exp = min(max(exp, minus_limit), plus_limit)
        return exp
