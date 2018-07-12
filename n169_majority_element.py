class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        compare, count = None, 0

        for i in range(len(nums)):
            if not count:
                compare, count = nums[i], 1
            else:
                if nums[i] == compare:
                    count += 1
                else:
                    count -= 1

        return compare