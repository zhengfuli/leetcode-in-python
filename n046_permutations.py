class Permutations(object):
    def permutations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in xrange(len(nums)):
            for j in self.permutations(nums[:i]+nums[i+1:]):
                res.append([nums[i]]+j)
        return res