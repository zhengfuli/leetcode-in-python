class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}

        for i in range(len(nums)):
            if nums[i] in dict:
                if abs(i - abs(dict[nums[i]])) <= k:
                    return True

            dict[nums[i]] = i

        return False