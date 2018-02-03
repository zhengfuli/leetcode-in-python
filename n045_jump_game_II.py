class JumpGameII(object):
    def jumpGameII(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        last = 0
        curr = 0
        for i in range(len(A)):
            if i > last:
                last = curr
                ret += 1
            curr = max(curr, i+A[i])
        return ret