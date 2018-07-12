class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for char in s:
            index = ord(char) - 64
            num = num * 26 + index

        return num
