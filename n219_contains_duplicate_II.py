class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set([])
        for i in xrange(len(nums)):
            if i > k:
                window.discard(nums[i-k-1])
            if nums[i] in window:
                return True
            else:
                window.add(nums[i])
        return False