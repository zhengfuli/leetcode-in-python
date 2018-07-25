class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False

        dict = {}
        for num in nums:
            dict[num] = 1 if num not in dict else dict[num] + 1

        return True if max(list(dict.values())) > 1 else False