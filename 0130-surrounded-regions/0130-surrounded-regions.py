class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r=len(board)
        c=len(board[0])

        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or board[i][j]!='O':
                return
            
            board[i][j]='-1'
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
            


        for i in range(r):
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][c-1]=='O':
                dfs(i,c-1)
        
        for j in range(c):
            if board[0][j]=='O':
                dfs(0,j)
            if board[r-1][j]=='O':
                dfs(r-1,j)
        for i in range(r):
            for j in range(c):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='-1':
                    board[i][j]='O'

        
        