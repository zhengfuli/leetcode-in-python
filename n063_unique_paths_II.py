class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid: return 0

        if len(obstacleGrid) == 1: return 1 if 1 not in obstacleGrid[0] else 0

        if len(obstacleGrid[0]) == 1:
            for row in obstacleGrid:
                if row[0] == 1: return 0
            return 1

        dp = [[0] * len(obstacleGrid[0]) for i in range(len(obstacleGrid))]

        for i in range(len(obstacleGrid)):

            if not obstacleGrid[i]: return 0

            for j in range(len(obstacleGrid[0])):

                if i == 0 and j == 0:
                    dp[i][j] = 0 if obstacleGrid[i][j] == 1 else 1
                elif i == 0:
                    dp[i][j] = 0 if dp[i][j-1] == 0 or obstacleGrid[i][j] == 1 else dp[i][j-1]
                elif j == 0:
                    dp[i][j] = 0 if dp[i-1][j] == 0 or obstacleGrid[i][j] == 1 else dp[i-1][j]
                elif obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if not obstacleGrid[i-1][j]:
                        if not obstacleGrid[i][j-1]:
                            dp[i][j] = dp[i-1][j] + dp[i][j-1]
                        else:
                            dp[i][j] = dp[i-1][j]
                    else:
                        if not obstacleGrid[i][j-1]:
                            dp[i][j] = dp[i][j-1]
                        else:
                            dp[i][j] = 0

        return dp[-1][-1]
