class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0

        dp = [[0] * len(grid[0]) for i in range(len(grid))]

        for i in range(len(grid)):

            if not grid[i]: return 0

            for j in range(len(grid[0])):

                if i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]

                elif j == 0 and i != 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]

                elif i == 0 and j == 0:
                    dp[i][j] = grid[i][j]

                else:
                    dp[i][j] = min(grid[i][j]+dp[i-1][j], grid[i][j]+dp[i][j-1])

        return dp[-1][-1]