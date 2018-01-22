class FourSum(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dict = {}
        res = set()

        if len(nums) < 4:
            return []

        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                key = nums[i] + nums[j]
                if key in dict:
                    dict[key].append([i, j])
                else:
                    dict[key] = [[i, j]]

        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                key = target - nums[i] - nums[j]
                if key in dict:
                    for cords in dict[key]:
                        if i not in cords and j not in cords:
                            res.add(tuple(sorted([nums[cords[0]], nums[cords[1]], nums[i], nums[j]])))

        return [list(i) for i in res]