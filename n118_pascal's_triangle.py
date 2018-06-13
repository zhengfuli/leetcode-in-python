class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []

        for i in range(numRows):
            if i < 2:
                res.append([1]*(i+1))
            else:
                temp = []
                for j in range(1, i):
                    temp.append(res[i-1][j-1] + res[i-1][j])
                res.append([1] + temp + [1])

        return res