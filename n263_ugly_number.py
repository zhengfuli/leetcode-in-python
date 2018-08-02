class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        while num and num % 2 == 0: num /= 2
        while num and num % 3 == 0: num /= 3
        while num and num % 5 == 0: num /= 5

        return num == 1