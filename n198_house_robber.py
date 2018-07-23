class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]
        rob_amount = 0

        for num in nums:
            if len(dp) < 2:
                dp.append(num)
            else:
                dp[0], dp[1] = max(dp), num + dp[0]

        return max(dp)

