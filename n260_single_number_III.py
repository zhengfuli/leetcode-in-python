class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num

        first_one_pos = len(bin(xor)) - bin(xor).rfind('1') - 1

        res1, res2 = 0, 0

        for num in nums:
            if (num >> first_one_pos) & 1:
                res1 ^= num
            else:
                res2 ^= num

        return [res1, res2]