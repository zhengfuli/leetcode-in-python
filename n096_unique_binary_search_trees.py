class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        catalan = [1, 1, 2]

        if n <= 2: return catalan[n]

        for i in range(len(catalan), n + 1):
            sum = 0
            for j in range(i):
                sum += catalan[j] * catalan[len(catalan) - 1 - j]

            catalan.append(sum)

        return catalan[-1]