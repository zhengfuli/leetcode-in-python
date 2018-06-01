class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        size = len(nums)
        first = 0
        last = size - 1
        while first <= last:
            mid = (last + first) / 2
            print(first,mid, last)
            if nums[mid] == target:
                return True
            if nums[mid] == nums[first] == nums[last]:
                first += 1; last -= 1
            elif nums[first] <= nums[mid]:
                if target < nums[mid] and target >= nums[first]:
                    last = mid - 1
                else:
                    first = mid + 1
            else:
                if target >= nums[mid] and target < nums[first]:
                    first = mid + 1
                else:
                    last = mid - 1



        return False