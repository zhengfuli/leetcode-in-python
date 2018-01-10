class SearchInRotatedSortedArray(object):
    def searchInRotatedSortedArray(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def dfs(nums, target):
            start, end = 0, len(nums)-1
            while start <= end:
                mid = (start + end) / 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] >= nums[start]:
                    if target >= nums[start] and target <= nums[mid]:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    if target >= nums[mid] and target <= nums[end]:
                        start = mid + 1
                    else:
                        end = mid - 1
            return -1

        return dfs(nums, target)