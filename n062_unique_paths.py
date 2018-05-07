class UniquePaths(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 and n == 1:
            path = [[1]]
        if m > 1 and n == 1:
            path = [[1] for i in range(m)]
        if m == 1 and n > 1:
            path = [[]]