class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1: return

        d = n
        res = ""

        while d > 26:
            r = d % 26
            d = int(d / 26)
            res += chr(r + 66)

        res += chr(d + 64)
        return res[::-1]