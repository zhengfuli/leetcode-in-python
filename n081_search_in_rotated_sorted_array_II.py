class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums: return False

        left, right = 0, len(nums)-1

        while left <= right:

            mid = int((left + right) / 2)

            if nums[mid] == target or nums[left] == target or nums[right] == target:
                return True

            if nums[left] < nums[mid]:
                if nums[left] < target < nums[mid]:
                    right = mid
                else:
                    left = mid
            elif nums[left] > nums[mid]:
                if nums[mid] < target < nums[right]:
                    left = mid
                else:
                    right = mid
            else:
                if nums[left] != target: left += 1
                if nums[right] != target: right -= 1

        return False
