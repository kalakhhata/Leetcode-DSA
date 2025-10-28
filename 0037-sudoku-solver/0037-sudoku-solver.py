class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """


        ch=['1','2','3','4','5','6','7','8','9']
        def isValid(r,c,char):
            for i in range(9):
                if board[r][i]==char or board[i][c]==char:
                    return False
            startRow=(r//3)*3
            startCol=(c//3)*3
            for i in range(3):
                for j in range(3):
                    if board[startRow+i][startCol+j]==char:
                        return False
            
            return True

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c]=='.':
                        for char in ch:
                            if isValid(r,c,char):
                                board[r][c]=char
                                if solve():
                                    return True
                                board[r][c]='.'
                        return False
            return True

        solve()