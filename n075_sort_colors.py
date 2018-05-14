class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p0, p2 = 0, len(nums)-1
        index = 0
        while index <= p2:
            if nums[index] == 2:
                nums[index], nums[p2] = nums[p2], nums[index]
                p2 -= 1
            elif nums[index] == 0:
                nums[index], nums[p0] = nums[p0], nums[index]
                p0 += 1
                # judgement on p2 is prior to p0, thus there are only
                # two cases: 0 or 1 for nums[index] to be. Switching will
                # happen only when nums[index] = 0, thus it must increase
                # by one after switching
                index += 1
            else:
                index += 1
        print nums

if __name__ == '__main__':
    tb = Solution()
    tb.sortColors([2, 0, 2, 1, 1, 0])


