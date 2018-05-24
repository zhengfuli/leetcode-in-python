class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row, col = [], []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] ==  0:
                    row.append(i)
                    col.append(j)

        for r in row:
            matrix[r] = [0] * len(matrix[0])

        for c in col:
            for i in range(len(matrix)):
                matrix[i][c] = 0