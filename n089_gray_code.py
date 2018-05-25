class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []

        for i in range(1 << n):
            # xor by bit
            res.append((i >> 1)^i)

        return res