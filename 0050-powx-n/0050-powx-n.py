class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        def power(n):
            if n == 0:
                return 1

            half = power(n // 2)

            if n % 2 == 0:
                return half * half

            else:
                return x * half * half

        return power(n)            