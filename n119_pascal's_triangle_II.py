class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        i = 0
        row = []
        if rowIndex < 2: return [1]*(rowIndex+1)
        while i <= rowIndex:
            row.append(1)
            for j in range(len(row)-2, 0, -1):
                row[j] += row[j-1]
            i += 1
        return row
