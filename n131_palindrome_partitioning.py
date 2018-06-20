class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        dp = [[False if i != j else True for i in range(len(s))] for j in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s) - 1, i - 1, -1):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1:
                    dp[i][j] = (s[i] == s[j])
                elif j > i + 1:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])

        res = []

        def dfs(start, partition):
            # print(start, partition)
            if start == len(s): res.append(partition)

            for i in range(start, len(s)):
                if dp[start][i]:
                    dfs(i + 1, partition + [s[start:i + 1]])

        # print(dp)
        dfs(0, [])
        return res