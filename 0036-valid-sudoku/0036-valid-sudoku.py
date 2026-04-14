class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N=9

        #hashset to record status
        rows=[set() for _ in range(N)]
        cols=[set() for _ in range(N)]
        boxes=[set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val=board[r][c]
                if val=='.':
                    continue
                idx=r//3 * 3 + c//3
                if val in rows[r] or val in cols[c] or val in boxes[idx]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[idx].add(val)
        return True
        