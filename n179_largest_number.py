from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort(key=cmp_to_key(lambda a, b: int(str(a)+str(b)) - int(str(b)+str(a))),reverse=True)
        nums = [str(num) for num in nums]
        res = ''.join(nums).lstrip('0')
        return res or '0'