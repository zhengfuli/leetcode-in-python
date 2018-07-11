class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1: return

        res = ""

        while n:
            res = chr((n - 1) % 26 + 65) + res
            n = (n - 1) / 26

        return res