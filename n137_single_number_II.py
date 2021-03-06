class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two, three = 0, 0, 0
        for num in nums:
            two |= one & num
            one ^= num
            three = one & two

            one &= ~three
            two &= ~three

        return one