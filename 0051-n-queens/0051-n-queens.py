class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def backtrack(r,cols,diag1,diag2,board):
            if r==n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r+c) in diag1 or (r-c) in diag2:
                    continue
                cols.add(c)
                diag1.add(r+c)
                diag2.add(r-c)
                board[r][c]='Q'
                backtrack(r+1,cols,diag1,diag2,board)
                board[r][c]='.'
                cols.remove(c)
                diag1.remove(r+c)
                diag2.remove(r-c)
        res=[]
        board=[['.']*n for _ in range(n)]
        backtrack(0,set(),set(),set(),board)
        return res
        

        