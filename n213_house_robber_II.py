class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        dp = [0]
        max_rob = 0

        for num in nums[1:]:
            if len(dp) < 2:
                dp.append(num)
            else:
                dp[0], dp[1] = max(dp), dp[0] + num

            max_rob = max(dp + [max_rob])

        dp = [0]
        for num in nums[:-1]:
            if len(dp) < 2:
                dp.append(num)
            else:
                dp[0], dp[1] = max(dp), dp[0] + num

            max_rob = max(dp + [max_rob])

        return max_rob