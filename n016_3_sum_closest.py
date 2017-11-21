import sys
class ThreeSumClosest(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = sys.maxint

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            p1, p2 = i + 1, len(nums) - 1
            while p1 < p2:
                sum = nums[i] + nums[p1] + nums[p2]
                if diff > abs(sum - target):
                    diff, res = abs(sum - target), sum
                if sum < target:
                    p1 += 1
                elif sum > target:
                    p2 -= 1
                else:
                    return target

        return res