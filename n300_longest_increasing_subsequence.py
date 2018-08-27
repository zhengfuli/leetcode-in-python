class Solution:
    def binary_search(self, left, right, nums, target):
        # print(left, right, nums)
        if left == right: return left

        if left + 1 == right:
            if nums[left] <= target <= nums[right]:
                return left
            elif nums[left] > target:
                return 0

        mid = int((left + right) / 2)

        if nums[mid] > target:
            return self.binary_search(left, mid, nums, target)
        else:
            return self.binary_search(mid, right, nums, target)

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        dp = []

        for num in nums:
            if not dp:
                dp.append(num)
            else:
                if num > dp[-1]:
                    dp.append(num)
                else:
                    pos = self.binary_search(0, len(dp)-1, dp, num)
                    print(pos)
                    if dp[pos] == num:
                        pass
                    elif pos == 0 and num <= dp[pos]:
                        dp[0] = num
                    else:
                        dp = dp[:pos+1] + [num] + dp[pos+2:]
            print(dp)
        return len(dp)

tb = Solution()
# print(tb.binary_search(0, 7, [10,9,2,5,3,4], 6))
print(tb.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))