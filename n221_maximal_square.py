class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) is 0:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        rm = [[0]*col for i in range(row)]
        for i in range(col):
            rm[0][i] = int(matrix[0][i])
        for i in range(row):
            rm[i][0] = int(matrix[i][0])
        for i in range(1,row):
            for j in range(1,col):
                rm[i][j] = int(matrix[i][j])
                if rm[i][j] is not 0:
                    rm[i][j] = int(min(rm[i-1][j-1],rm[i][j-1],rm[i-1][j]))+1
        r = 0
        for i in rm:
            for j in i:
                if r<j:
                    r = j
        return r**2