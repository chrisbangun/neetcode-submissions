from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(0, 9):
            for col in range(0, 9):
                value = board[row][col]
                if value == '.':
                    continue
                
                box = (row // 3, col // 3)

                if (
                    value in rows[row] or
                    value in cols[col] or
                    value in boxes[box]):
                    return False
                
                rows[row].add(value)
                cols[col].add(value)
                boxes[box].add(value)
        return True

        