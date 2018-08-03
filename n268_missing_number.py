class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append('m')

        for i in range(len(nums)):
            if nums[i] == 'm':
                pass

            else:
                while nums[i] != 'm' and nums[i] != i:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        return nums.index('m')