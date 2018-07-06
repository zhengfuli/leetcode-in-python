class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [False] * len(nums)
        dp[0] = dp[-1] = True

        for i in range(len(nums)):
            if i == len(nums) - 1:
                return i if nums[i] >= nums[i - 1] else None

            if dp[i]:
                if nums[i] >= nums[i + 1]:
                    return i
                else:
                    dp[i + 1] = True