class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows=len(matrix)
        cols=len(matrix[0])
        self.prefix=[[0]*cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                top=self.prefix[r-1][c] if r>0 else 0
                left=self.prefix[r][c-1] if c>0 else 0
                dig=self.prefix[r-1][c-1] if r>0 and c>0 else 0

                self.prefix[r][c]=matrix[r][c]+top+left-dig

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top=self.prefix[row1-1][col2] if row1>0 else 0
        left=self.prefix[row2][col1-1] if col1>0 else 0
        dig=self.prefix[row1-1][col1-1] if row1>0 and col1>0 else 0

        return self.prefix[row2][col2]-top-left+dig
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)