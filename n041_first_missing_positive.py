class FirstMissingPositive(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            while nums[i] != i + 1 and nums[i] > 0 and nums[i] < len(nums) + 1:
                print nums[i]
                if nums[nums[i] - 1] == nums[i]:
                    break
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in xrange(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1