import sys, math
class Solution:
    # TLE for 464
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [sys.maxsize] * n

        for i in range(1, n):

            if int(math.sqrt(i)) ** 2 == i:
                dp[i-1] = 1
            else:
                for j in range(int(i/2)+1):
                    dp[i] = min(dp[i-j] + dp[j], dp[i])

        return dp[-1]

    def numSquares(self, n):
        def isSquare(n):
            if int(math.sqrt(n)) ** 2 == n: return 1

        if isSquare(n): return 1

        # 4**k(8i+7)
        while n & 3 == 0:
            n >>= 2

        if n & 7 == 7:
            return 4

        for i in range(1, int(math.sqrt(n)) + 1):
            if isSquare(n - i ** 2):
                return 2

        return 3