class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])





        def isExist(r,c,idx):
            if idx==len(word):
                return True
            
            if r<0 or c<0 or r>=n or c>=m or word[idx]!=board[r][c]:
                return False
            
            temp=board[r][c]
            board[r][c]='@'
            ans=  (
                isExist(r,c+1,idx+1) or
                isExist(r,c-1,idx+1) or
                isExist(r+1,c,idx+1) or
                isExist(r-1,c,idx+1)
            )
            board[r][c]=temp
            return ans
        

        for i in range(n):
            for j in range(m):
                if word[0]==board[i][j] and isExist(i,j,0):
                    return True
        
        return False








        