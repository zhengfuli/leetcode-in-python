class Solution:
    def binary_search(self, left, right, nums, target):
        if left +1 == right:
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

        dp = {}
        max_len = 1

        for i in range(len(nums)):
            if not dp:
                dp[nums[i]] = [nums[i]]
            else:
                if nums[i] > nums[i-1]:
                    dp[nums[i]] = [dp[nums[i-1]].append(nums[i])]
                    max_len = max(max_len, dp[nums[i]][0])
                elif len(dp[nums[i-1]]) != 1 or len(dp[nums[i-1]][0]) != 1:
                    for sub in dp[nums[i-1]]:
                        new_sub = sub[:self.binary_search(0, len(sub)-1, sub, nums[i])+1].append(nums[i])
                        dp[nums[i]] = dp[nums[i-1]].append(new_sub)
                else:
                    dp[nums[i]] = [nums[i]]

        lengths = [len(sub) for sub in list(dp.values())]
        return max(lengths)

tb = Solution()
print(tb.binary_search(0, 4, [1,3,5,7], 6))