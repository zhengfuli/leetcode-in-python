class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        left, right, up, down = 0, n-1, 0, n-1

        matrix = [[0] * n for i in range(n)]

        direction = 0

        count = 1

        while True:

            if direction == 0:
                for i in range(left, right+1):
                    matrix[up][i] = count
                    count += 1
                up += 1

            if direction == 1:
                for i in range(up, down+1):
                    matrix[i][right] = count
                    count += 1
                right -= 1

            if direction == 2:
                for i in range(right, left-1, -1):
                    matrix[down][i] = count
                    count += 1
                down -= 1

            if direction == 3:
                for i in range(down, up-1, -1):
                    matrix[i][left] = count
                    count += 1
                left += 1

            if left > right or down < up: return matrix

            direction = (direction + 1) % 4