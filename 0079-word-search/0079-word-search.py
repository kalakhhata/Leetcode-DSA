class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        l=len(word)

        def dfsBT(r,c,idx):
            if idx==l:
                return True
            
            if r<0 or c<0 or r>=m or c>=n or board[r][c]!=word[idx]:
                return False
            
            temp=board[r][c]
            board[r][c]='@'

            found=(
                dfsBT(r+1,c,idx+1) or
                dfsBT(r-1,c,idx+1) or
                dfsBT(r,c+1,idx+1) or
                dfsBT(r,c-1,idx+1)
            )
            board[r][c]=temp
            return found
        
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and dfsBT(i,j,0):
                    return True
        
        return False

        