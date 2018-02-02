class Solution:
    # @return an integer
    def totalNQueens(self, n):
        def check(k, j):  # check if the kth queen can be put in column j!
            for i in range(k):
                if board[i]==j or abs(k-i)==abs(board[i]-j):
                    return False
            return True
        board=[-1 for i in range(n)]
        row=0; col=0; sum=0
        while row<n:
            while col<n:
                if check(row, col):
                    board[row]=col
                    col=0
                    break
                else:
                    col+=1
            if board[row]==-1:
                if row==0:
                    break
                else:
                    row-=1
                    col=board[row]+1
                    board[row]=-1
                    continue
            if row==n-1:
                sum+=1
                col=board[row]+1
                board[row]=-1
                continue
            row+=1
        return sum