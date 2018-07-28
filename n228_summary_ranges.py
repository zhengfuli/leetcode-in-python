class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []

        start, end = 0, 0
        res = []

        for i in range(len(nums)):
            if not nums[i] - nums[start] == i - start:
                if start != end:
                    res.append(str(nums[start]) + "->" + str(nums[end]))
                else:
                    res.append(str(nums[start]))

                start = end = i
            else:
                end = i

            if end == len(nums) - 1:
                if start == end:
                    res.append(str(nums[start]))
                else:
                    res.append(str(nums[start]) + "->" + str(nums[end]))

        return res
