class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count, i = 0, 0

        while i < len(nums):
            if not nums[i]:
                nums.remove(nums[i])
                count += 1
                i -= 1
            i += 1

        nums += [0] * count


tb = Solution()

tb.moveZeroes([0,0,1])