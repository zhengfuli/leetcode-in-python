class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0

        while m != n:
            i += 1
            m >>= 1
            n >>= 1

        return m << i

