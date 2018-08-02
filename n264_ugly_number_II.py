import sys


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        factor_and_index = {2: 0, 3: 0, 5: 0}
        ugly_nums = [1]
        min_ugly_num = sys.maxsize

        while len(ugly_nums) < n:
            min_ugly_num, factor_index = sys.maxsize, 0
            for index in factor_and_index:
                temp = index * ugly_nums[factor_and_index[index]]
                if temp < min_ugly_num:
                    min_ugly_num, factor_index = temp, index

            if min_ugly_num not in ugly_nums:
                ugly_nums.append(min_ugly_num)

            factor_and_index[factor_index] += 1

        # print(ugly_nums)
        return ugly_nums[-1]

