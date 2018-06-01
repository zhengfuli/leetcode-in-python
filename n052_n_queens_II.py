class Solution:
    def __init__(self):
        self.count = 0

    # @return an integer
    def totalNQueens(self, n):

        def isvalid(k, j):
            for i in range(k):
                if board[i] == j or abs(board[i]-j) == abs(k-i):
                    return False
            return True

        def dfs(depth):

            if depth == n:
                self.count += 1
                return

            for i in range(n):
                if isvalid(depth, i):
                    board[depth] = i
                    dfs(depth+1)

        board = [-1] * n
        dfs(0)
        return self.count

if __name__ == '__main__':
    tb = Solution()
    print tb.totalNQueens(4)