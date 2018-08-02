class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return 0

        res = num % 9

        if not res: return 9
        else: return res