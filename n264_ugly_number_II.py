import sys

class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        if n == 1: return 1

        ugly_nums = [1]
        i2, i3, i5 = 0, 0, 0

        for k in range(n-1):
            n2, n3, n5 = 2 * ugly_nums[i2], 3 * ugly_nums[i3], 5 * ugly_nums[i5]
            m = min(n2, n3, n5)
            ugly_nums.append(m)

            i2 += (m == n2)
            i3 += (m == n3)
            i5 += (m == n5)

        return m

