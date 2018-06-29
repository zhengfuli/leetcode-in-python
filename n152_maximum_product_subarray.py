class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        max_product, min_product, res = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            max_temp = max_product * num
            min_temp = min_product * num

            max_product = max(max(max_temp, min_temp), num)
            min_product = min(min(max_temp, min_temp), num)
            res = max(max_product, res)

        return res