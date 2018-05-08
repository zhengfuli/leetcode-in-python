class UniquePaths(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 and n == 1:
            paths = [[1]]
        elif m == 1 and n > 1:
            paths = [[1] * n]
        elif m > 1 and n == 1:
            paths = [[1] for i in xrange(m)]
        else:
            paths = [[0] * n for i in xrange(m)]
            for i in xrange(0, n):
                paths[0][i] = 1
            for i in xrange(0, m):
                paths[i][0] = 1
            for i in xrange(1, m):
                for j in xrange(1, n):
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[m-1][n-1]

