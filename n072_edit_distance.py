class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1: return len(word2)

        if not word2: return len(word1)

        dp = [[-1] * (len(word1) + 1) for i in range(len(word2) + 1)]

        for i in range(len(word1), -1, -1): dp[-1][i] = len(word1) - i

        for i in range(len(word2), -1, -1): dp[i][-1] = len(word2) - i

        for i in range(len(word2) - 1, -1, -1):
            for j in range(len(word1) - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] if word1[j] == word2[i] else min(dp[i + 1][j], dp[i][j + 1],
                                                                             dp[i + 1][j + 1]) + 1

        return dp[0][0]