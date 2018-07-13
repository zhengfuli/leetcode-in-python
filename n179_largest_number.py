class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(a, b):
            return int(a+b) - int(b+a)

        nums = sorted(nums, key = lambda a,b: compare(a,b))
        res = ''.join(nums).lstrip('0')

        return res or '0'
