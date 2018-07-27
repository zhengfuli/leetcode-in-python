import collections

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0: return False

        dict = collections.OrderedDict()

        for num in nums:
            key = int(num / max(1, t))

            for i in (key - 1, key, key + 1):
                if i in dict and abs(dict[i] - num) <= t:
                    print(num, dict)
                    return True

            dict[key] = num

            if len(dict) > k:
                dict.popitem(last=False)

        return False