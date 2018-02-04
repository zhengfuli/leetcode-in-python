class JumpGame(object):
    def jumpGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxReach = nums[0]
        for i in xrange(1, len(nums)):
            if maxReach > 0:
                maxReach -= 1
                maxReach = max(maxReach, nums[i])
            else:
                return False
        return True
