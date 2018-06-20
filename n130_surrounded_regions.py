class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return

        queue = set()

        for i in range(len(board)):
            queue.add((i, 0))
            queue.add((i, len(board[0])-1))

        for i in range(len(board[0])):
            queue.add((0, i))
            queue.add((len(board)-1, i))

        while queue:
            x, y = queue.pop()

            if board[x][y] == "O":
                board[x][y] = "D"

                for surrounded in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                    if 0 <= surrounded[0] <= len(board)-1 and 0 <= surrounded[1] <= len(board[0])-1:
                        if board[surrounded[0]][surrounded[1]] == "O":
                            queue.add(surrounded)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O": board[i][j] = "X"

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "D": board[i][j] = "O"