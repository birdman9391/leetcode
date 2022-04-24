class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_plus = True
        if dividend < 0:
            is_plus = not is_plus
            dividend = -dividend

        if divisor < 0:
            is_plus = not is_plus
            divisor = -divisor
    
        n = 0
        quotient_total = 0
        quotient_n = 1
        divisor_n = divisor
        if dividend < divisor_n:
            return 0

        while True:
            divisor_n_plus_1 = divisor_n << 1

            if divisor_n_plus_1 > dividend:
                break

            divisor_n = divisor_n_plus_1
            n += 1 # divisor_n = divisor * 2^n
            quotient_n <<= 1 # 2^n
            # print("quotient_n", quotient_n)

        # print("##", n, quotient_n, dividend, divisor_n)
        while dividend > 0:
            # print(n, quotient_n, dividend, divisor_n)
            if dividend >= divisor_n:
                dividend -= divisor_n
                quotient_total += quotient_n
            n -= 1
            quotient_n >>= 1
            divisor_n >>= 1
            if n < 0:
                break
        if is_plus:
            return min(quotient_total, (1<<31) - 1)
        return max(-quotient_total, -(1<<31))
                
            