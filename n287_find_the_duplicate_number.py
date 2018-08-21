class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast, dup = 0, 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(slow, fast)
            if slow == fast: break

        while True:
            print(dup, slow)
            slow = nums[slow]
            dup = nums[dup]
            if slow == dup: break

        return dup

tb = Solution()
print(tb.findDuplicate([1,3,4,2,2]))