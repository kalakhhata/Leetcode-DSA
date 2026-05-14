class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        
        
        
        
        def backtrack(r,col,diag1,diag2):
            if r==n:
                res.append([''.join(row) for row in board])
                return
            
            for c in range(n):
                if c in col or (r-c) in diag1 or (r+c) in diag2 or board[r][c]!='.':
                    continue
                
                col.add(c)
                diag1.add(r-c)
                diag2.add(r+c)
                board[r][c]='Q'
                backtrack(r+1,col,diag1,diag2)
                col.remove(c)
                diag1.remove(r-c)
                diag2.remove(r+c)
                board[r][c]='.'
        
        board=[['.']*n for _ in range(n)]
        res=[]
        backtrack(0,set(),set(),set())
        return res


        