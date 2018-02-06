class WordSearch(object):
    def wordSearch(self, board, word):
        def search(board, word, index, stack):
            if index == len(word):
                return True

            x, y = stack[len(stack) - 1]

            if x - 1 >= 0 and [x - 1, y] not in stack and board[x - 1][y] == word[index]:
                if search(board, word, index + 1, stack + [[x - 1, y]]): return True

            if x + 1 <= len(board) - 1 and [x + 1, y] not in stack and board[x + 1][y] == word[index]:
                if search(board, word, index + 1, stack + [[x + 1, y]]): return True

            if y - 1 >= 0 and [x, y - 1] not in stack and board[x][y - 1] == word[index]:
                if search(board, word, index + 1, stack + [[x, y - 1]]): return True

            if y + 1 <= len(board[x]) - 1 and [x, y + 1] not in stack and board[x][y + 1] == word[index]:
                if search(board, word, index + 1, stack + [[x, y + 1]]): return True

            return False

        if not word:
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if search(board, word, 1, [[i, j]]):
                        return True
        return False