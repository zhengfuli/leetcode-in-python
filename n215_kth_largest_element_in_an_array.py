class FindKthLargest(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums:
            return sorted(nums, reverse=True)[k - 1]