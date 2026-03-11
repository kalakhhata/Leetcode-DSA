class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r=len(board)
        c=len(board[0])

        #run the dfs to see if there exists a diagonal place where there is still a 0
        def dfs(i,j):
            if i<0 or i>=r or j<0 or j>=c or board[i][j]!='O':
                return
            
            board[i][j]='T'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        #check the boarders if there exists a 'O'
        for i in range(r):
            #left border
            if board[i][0]=='O':
                dfs(i,0)

            #right border
            if board[i][c-1]=='O':
                dfs(i,c-1)
        
        for j in range(c):
            #top border
            if board[0][j]=='O':
                dfs(0,j)
            
            #bottom border
            if board[r-1][j]=='O':
                dfs(r-1,j)
        
        for i in range(r):
            for j in range(c):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='T':
                    board[i][j]='O'
        


        