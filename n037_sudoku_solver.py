class SolveSudoku(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def isValid(num, board, x, y):
            if num in board[x]:
                return False

            for i in range(9):
                if num == board[i][y]:
                    return False

            for i in range((x/3)*3, (x/3)*3+3):
                for j in range((y/3)*3, (y/3)*3+3):
                    if num == board[i][j]:
                        return False
            board[x][y] = num
            return True

        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in ['1','2','3','4','5','6','7','8','9']:
                            if isValid(num, board, i, j) and dfs(board):
                                return True
                            else:
                                board[i][j] = '.'
                        return False
            return True

        dfs(board)


# if __name__ == '__main__':
#     tb = SolveSudoku()
#     tb.solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]])
