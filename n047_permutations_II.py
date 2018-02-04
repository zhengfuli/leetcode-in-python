class PermutationsII(object):
    def permutationsII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums):
            if nums == []:
                return []
            if len(nums) == 1:
                return [nums]
            res = set()
            for i in xrange(len(nums)):
                for j in dfs(nums[:i] + nums[i + 1:]):
                    res.add(tuple([nums[i]] + list(j)))
            return res

        res = dfs(tuple(nums))
        return [list(p) for p in res]
