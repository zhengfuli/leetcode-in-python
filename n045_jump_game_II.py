class JumpGameII(object):
    def jumpGameII(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        lastJump = 0
        currReach = 0
        for i in xrange(len(nums)):
            if i > lastJump:
                lastJump = currReach
                step += 1
            currReach = max(currReach, i+nums[i])
        return step