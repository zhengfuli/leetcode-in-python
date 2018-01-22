class RemoveDuplicates(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i+1])
            else:
                i += 1
        return len(nums)

