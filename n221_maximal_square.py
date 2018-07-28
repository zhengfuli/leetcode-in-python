class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp = [[0] * len(matrix[0]) for i in range(len(matrix))]
        max_edge = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    if int(matrix[i][j]):
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    else:
                        dp[i][j] = 0

                max_edge = max(max_edge, dp[i][j])

        return max_edge ** 2