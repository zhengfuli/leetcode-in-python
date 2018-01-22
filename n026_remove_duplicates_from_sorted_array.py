class RemoveDuplicates(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        j = 0
        length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[j] = nums[i]
                j += 1
                length += 1
        return length