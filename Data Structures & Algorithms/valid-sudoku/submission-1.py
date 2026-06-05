class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".": continue
                # Three composite keys — one per constraint
                row_key = (val, r, "R")
                col_key = (val, c, "C")
                box_key = (val, r//3, c//3, "B")
                for key in (row_key, col_key, box_key):
                    if key in seen:
                        return False
                    seen.add(key)
        return True