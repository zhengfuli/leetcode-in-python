class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                # check only partial neighbors
                for nei_x, nei_y in [(i, j+1), (i+1, j+1), (i+1, j), (i+1, j-1)]:
                    # validate neighbors within boundaries
                    if 0 <= nei_x < len(board) and  0 <= nei_y < len(board[nei_x]):
                        # print(nei_x, nei_y)
                        # if this cell is dead
                        if board[i][j] <= 0:
                            if board[nei_x][nei_y] > 0:
                                board[i][j] -= 1
                        else:
                            if board[nei_x][nei_y] > 0:
                                board[i][j] += 1
                                # this cell is live, thus to its neighbor, this is a live neighbor
                                board[nei_x][nei_y] += 1
                            else:
                                board[nei_x][nei_y] -= 1
                print(board)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if 0 < board[i][j] < 3: board[i][j] = 0
                elif 3 <= board[i][j] <= 4: board[i][j] = 1
                elif board[i][j] > 4: board[i][j] = 0
                elif board[i][j] == -3: board[i][j] = 1
                else: board[i][j] = 0