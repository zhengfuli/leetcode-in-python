class SolveNQueens(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def check(k, j):  # check if the kth queen can be put in column j!
            for i in range(k):
                if board[i] == j or abs(k - i) == abs(board[i] - j):
                    return False
            return True

        def dfs(depth, valuelist):
            if depth == n: res.append(valuelist); return
            for i in range(n):
                if check(depth, i):
                    board[depth] = i
                    s = '.' * n
                    dfs(depth + 1, valuelist + [s[:i] + 'Q' + s[i + 1:]])

        board = [-1 for i in range(n)]
        res = []
        dfs(0, [])
        return res



