class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix: return
        self.height, self.width = len(matrix), len(matrix[0])

        self.left_up_to_right_down_sub_sum = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[i])):
                if not self.left_up_to_right_down_sub_sum:
                    row.append(sum(matrix[i][:j + 1]))
                else:
                    row.append(sum(matrix[i][:j + 1]) + self.left_up_to_right_down_sub_sum[-1][j])
            self.left_up_to_right_down_sub_sum.append(row)

        self.left_down_to_right_up_sub_sum = []
        for i in range(len(matrix)-1, -1, -1):
            row = []
            for j in range(len(matrix[i])):
                if not self.left_down_to_right_up_sub_sum:
                    row.append(sum(matrix[i][:j + 1]))
                else:
                    row.append(sum(matrix[i][:j + 1]) + self.left_down_to_right_up_sub_sum[-1][j])
            self.left_down_to_right_up_sub_sum.append(row)
        self.left_down_to_right_up_sub_sum = self.left_down_to_right_up_sub_sum[::-1]

        self.right_up_to_left_down_sub_sum = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[i])):
                if not self.right_up_to_left_down_sub_sum:
                    row.append(sum(matrix[i][j:]))
                else:
                    row.append(sum(matrix[i][j:]) + self.right_up_to_left_down_sub_sum[-1][j])
            self.right_up_to_left_down_sub_sum.append(row)

        self.right_down_to_left_up_sub_sum = []
        for i in range(len(matrix)-1, -1, -1):
            row = []
            for j in range(len(matrix[i])):
                if not self.right_down_to_left_up_sub_sum:
                    row.append(sum(matrix[i][j:]))
                else:
                    row.append(sum(matrix[i][j:]) + self.right_down_to_left_up_sub_sum[-1][j])
            self.right_down_to_left_up_sub_sum.append(row)
        self.right_down_to_left_up_sub_sum = self.right_down_to_left_up_sub_sum[::-1]

        # print(self.left_up_to_right_down_sub_sum, self.left_down_to_right_up_sub_sum, self.right_down_to_left_up_sub_sum, self.right_up_to_left_down_sub_sum)
        self.total_sum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.total_sum += matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        res += self.left_up_to_right_down_sub_sum[row2][col2] + self.left_down_to_right_up_sub_sum[row1][col2] + self.right_up_to_left_down_sub_sum[row2][col1] + self.right_down_to_left_up_sub_sum[row1][col1]
        # print(res)
        if row1 - 1 < 0 or col1 - 1 < 0:
            pass
        else:
            res += self.left_up_to_right_down_sub_sum[max(row1-1,0)][max(col1-1,0)]
        # print(res)
        if row2 + 1 >= self.height or col1 - 1 < 0:
            pass
        else:
            res += self.left_down_to_right_up_sub_sum[min(self.height-1, row2+1)][max(0, col1-1)]
        # print(res)
        if row1 - 1 < 0 or col2 + 1 >= self.width:
            pass
        else:
            res += self.right_up_to_left_down_sub_sum[max(0, row1-1)][min(self.width-1, col2+1)]
        # print(res)
        if row2 + 1 >= self.height or col2 + 1 >= self.width:
            pass
        else:
            res += self.right_down_to_left_up_sub_sum[min(self.height-1, row2+1)][min(self.width-1, col2+1)]
        # print(res)
        res -= 2 * self.total_sum
        res = int(res / 2)
        return res
