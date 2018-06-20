class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[False] * len(s) for i in range(len(s))]

        for i in range(len(s)-1, -1, -1):
            for j in range(len(s)-1, i-1, -1):
                if i == j: dp[i][j] = True
                elif j - i == 1: dp[i][j] = s[i] == s[j]
                elif j > i + 1: dp[i][j] = dp[i+1][j-1] and s[i] == s[j]

        self.min_cut = 0

        def dfs(min_cut, start):
            if start == len(s):
                self.min_cut = min(self.min_cut, min_cut)
                return

            for i in range(start, len(s)):
                if dp[start][i]:
                    dfs(min_cut+1, start+1)

        dfs(self.min_cut, 0)
        return self.min_cut