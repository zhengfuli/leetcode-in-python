class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev = s[::-1]

        for i in range(len(s), 0, -1):
            if s[:i] == rev[len(s)-i:]:
                pos = i
                break

        return s[i:][::-1] + s

tb = Solution()
print(tb.shortestPalindrome("abcd"))