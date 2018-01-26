class SearchRange(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # if target not in nums:
        #     return [-1,-1]
        # start = nums.index(target)
        # return [start, start+nums.count(target)-1] 
        left, right = 0, len(nums) - 1
        res = [-1, -1]
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if nums[left] == target: res[0] = left
                if nums[right] == target: res[1] = right
                for i in xrange(mid - 1, left - 1, -1):
                    print i
                    if nums[i] != target:
                        res[0] = i + 1
                        break
                for j in xrange(mid, right + 1):
                    if nums[j] != target:
                        res[1] = j - 1
                        break
                return res
        return res