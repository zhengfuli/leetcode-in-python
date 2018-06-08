class Solution:
    def largest_rectangle_in_histogram(self, heights_list):
        maxArea = 0
        for heights in heights_list:
            stack = []
            i = 0

            while i < len(heights):

                if not stack or heights[i] > heights[stack[-1]]:
                    stack.append(i)
                else:
                    temp = stack.pop()
                    width = i if not stack else i - stack[-1] - 1
                    maxArea = max(maxArea, width * heights[temp])
                    i -= 1
                i += 1

            while stack:
                temp = stack.pop()
                width = i if not stack else len(heights) - stack[-1] - 1
                maxArea = max(maxArea, width * heights[temp])

        return maxArea


    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        for i in range(len(matrix)):

            for j in range(len(matrix[i])):
                longest_ones = 0
                k = j

                while k < len(matrix[i]) and matrix[i][k] == "1":
                    longest_ones += 1
                    k += 1

                matrix[i][j] = longest_ones

        columns = []
        for i in range(len(matrix[0])):
            columns.append([row[i] for row in matrix])

        print(matrix, "\n", columns)

        return self.largest_rectangle_in_histogram(columns)



if __name__ == "__main__":

    tb = Solution()
    print(tb.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))