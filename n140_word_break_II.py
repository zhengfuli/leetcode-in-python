class Solution(object):
    def dfs(self, s, comb, wordDict):
        if self.check(s, wordDict):
            if len(s) == 0: self.res.append(comb[1:])
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], comb + " " + s[:i], wordDict)

    def check(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[-1]

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.res = []
        self.dfs(s, "", wordDict)
        return self.res
