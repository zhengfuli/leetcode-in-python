class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = "{0:b}".format(n)
        return binary.count("1")