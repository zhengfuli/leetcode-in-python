class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return

        res = 0

        for num in nums:
            res ^= num

        return res
