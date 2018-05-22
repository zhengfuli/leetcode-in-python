class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        for m in matrix:
            if not m:
                return False

        left, right = 0, len(matrix) - 1

        if left == right:
            return target in matrix[left]

        while left < right:

            mid = (left + right) / 2
            if target > matrix[mid][0]:
                left = mid
            elif target < matrix[mid][0]:
                right = mid
            elif target == matrix[mid][0]:
                return True

            if left + 1 == right or left == right:
                if target in matrix[left] or target in matrix[right]:
                    return True
                else:
                    return False