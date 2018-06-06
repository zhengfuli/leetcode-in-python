class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums):
            if not nums: return [[]]

            res = [[]]

            for i in range(len(nums)):
                subsets = dfs(nums[i+1:])

                for subset in subsets:
                    if sorted(([nums[i]] + subset)) not in res:
                        res.append(sorted([nums[i]] + subset))

            return res

        return dfs(nums)

if __name__ == '__main__':
    tb = Solution()
    print(tb.subsetsWithDup([4,4,4,1,4]))