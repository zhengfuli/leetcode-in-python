class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s: return 0

        left, right = 0, 1
        sub_sum = nums[left]
        min_length = len(nums)

        while right < len(nums):

            while sub_sum < s and right < len(nums):
                sub_sum += nums[right]
                right += 1

            while sub_sum >= s and left < right:
                sub_sum -= nums[left]
                min_length = min(min_length, right - left)
                left += 1

        return min_length