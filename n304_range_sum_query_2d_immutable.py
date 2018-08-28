class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.left_up_to_right_down_sub_sum = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[i])):
                if not self.left_up_to_right_down_sub_sum:
                    row.append(sum(matrix[i][:j + 1]))
                else:
                    row.append(sum(matrix[i][:j + 1]) + self.left_up_to_right_down_sub_sum[i - 1][j])
            self.left_up_to_right_down_sub_sum.append(row)

        self.left_down_to_right_up_sub_sum = []
        for i in range(len(matrix)-1, -1, -1):
            row = []
            for j in range(len(matrix[i])):
                if not self.left_down_to_right_up_sub_sum:
                    row.append(sum(matrix[i][:j + 1]))
                else:
                    row.append(sum(matrix[i][:j + 1]) + self.left_down_to_right_up_sub_sum[i - 1][j])
            self.left_down_to_right_up_sub_sum.append(row)
        self.left_down_to_right_up_sub_sum = self.left_down_to_right_up_sub_sum[::-1]

        self.right_up_to_left_down_sub_sum = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[i])):
                if not self.right_up_to_left_down_sub_sum:
                    row.append(sum(matrix[i][j:]))
                else:
                    row.append(sum(matrix[i][j:]) + self.right_up_to_left_down_sub_sum[i - 1][j])
            self.right_up_to_left_down_sub_sum.append(row)

        self.right_down_to_left_up_sub_sum = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[i])):
                if not self.right_down_to_left_up_sub_sum:
                    row.append(sum(matrix[i][j:]))
                else:
                    row.append(sum(matrix[i][j:]) + self.right_down_to_left_up_sub_sum[i - 1][j])
            self.right_down_to_left_up_sub_sum.append(row)
        self.right_down_to_left_up_sub_sum = self.right_down_to_left_up_sub_sum[::-1]

        print(self.left_up_to_right_down_sub_sum, self.left_down_to_right_up_sub_sum, self.right_down_to_left_up_sub_sum, self.right_up_to_left_down_sub_sum)
        self.total_sum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.total_sum += matrix[i][j]

        self.height, self.width = len(matrix), len(matrix[0])
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return (self.left_up_to_right_down_sub_sum[row1-1][col1-1] + self.left_up_to_right_down_sub_sum[row2][col2]
        + self.left_down_to_right_up_sub_sum[self.height-row2][self.width-col1] + self.left_down_to_right_up_sub_sum[row1][col2]
        + self.right_up_to_left_down_sub_sum[self.height-row1][self.width-col2] + self.right_up_to_left_down_sub_sum[row2][col1]
        + self.right_down_to_left_up_sub_sum[self.height-row2][self.width-col2] + self.right_down_to_left_up_sub_sum[row1][col1]
        - 2 * self.total_sum) / 2


        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)

tb = NumMatrix([[1,2,3],[4,5,6],[7,8,9]])
print(tb.sumRegion(1,1,1,1))