class MaxSubArray(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        maxSum = -2**31-1
        for num in nums:
            if sum < 0:
                sum = 0
            sum += num
            maxSum = max(sum, maxSum)
        return maxSum