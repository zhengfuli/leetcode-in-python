class TwoSum(object):
    def twoSum(self, nums, target):
        """
        :param nums:list[int]
        :param target: int
        :return: list[list[int]]
        """
        augend = {}
        for i in range(len(nums)):
            if nums[i] not in augend:
                augend[target-nums[i]] = i
            else:
                return [augend[nums[i]], i]
        return None