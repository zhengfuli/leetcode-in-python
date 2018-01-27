class IsValidSudoku(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def isValid(sub):
            rule = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            for char in sub:
                if char == '.':
                    pass
                else:
                    if char in rule:
                        rule.remove(char)
                    else:
                        return False
            return True

        for i in xrange(len(board)):
            if not (isValid(board[i]) and isValid([c[i] for c in board])):
                return False

        for i in xrange(0, 9, 3):
            for j in xrange(0, 9, 3):
                if not isValid([board[s][t] for s in range(i, i + 3) for t in range(j, j + 3)]):
                    return False

        return True

