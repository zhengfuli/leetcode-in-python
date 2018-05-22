class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ""
        k -= 1

        factor = 1
        for i in xrange(1, n):
            factor *= i

        num = [str(i) for i in xrange(1, 10)]

        for i in xrange(n - 1, -1, -1):
            cur = num[k / factor]
            res += cur
            num.remove(cur)

            if i != 0:
                k %= factor
                factor /= i

        return res