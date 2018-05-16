class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3): return False

        dp = [[False] * (len(s1) + 1) for i in xrange(len(s2) + 1)]

        for i in xrange(len(s2) + 1):
            for j in xrange(len(s1) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i > 0 and dp[i - 1][j] and s2[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True
                elif j > 0 and dp[i][j - 1] and s1[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False

        return dp[len(s2)][len(s1)]
