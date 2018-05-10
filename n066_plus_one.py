import string
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(char) for char in str(int("".join([str(digit) for digit in digits])) + 1)]


