class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(nums, target, comb):
            # print(comb, nums)
            if len(comb) >= k: return

            for i in range(len(nums)):
                if nums[i] == target and len(comb) == k - 1:
                    res.append(comb+[nums[i]])
                elif nums[i] < target:
                    dfs(nums[i+1:], target-nums[i], comb+[nums[i]])
                else:
                    return

        dfs([i for i in range(1,10)], n, [])
        return res
