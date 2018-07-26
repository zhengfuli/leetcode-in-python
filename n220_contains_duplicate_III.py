import collections
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0:
            return False
        numDict = collections.OrderedDict()
        for x in range(len(nums)):
            key = nums[x] / max(1, t)
            for m in (key, key - 1, key + 1):
                if m in numDict and abs(nums[x] - numDict[m]) <= t:
                    return True
            numDict[key] = nums[x]
            if x >=  k:
                numDict.popitem(last=False)
        return False
