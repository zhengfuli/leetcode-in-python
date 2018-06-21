class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[False] * len(s) for i in range(len(s))]
        min_cut = [len(s) - i for i in range(len(s)+1)]

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (((j - i) < 2) or dp[i+1][j-1]):
                    dp[i][j] = True
                    min_cut[i] = min(min_cut[i], 1 + min_cut[j+1])
        return min_cut[0] - 1
