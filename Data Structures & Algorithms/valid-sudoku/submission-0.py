from collections import defaultdict

class Solution:
    def is_valid_square(self, s: int, board: List[List[str]]) -> bool:
        seen = set()
        # first square
        for r in range(s, s + 3):
            for c in range(0, 3):
                if board[r][c] in seen and board[r][c] != '.':
                    return False
                seen.add(board[r][c])
        
        seen = set()
        # second square
        for r in range(s, s + 3):
            for c in range(3, 6):
                if board[r][c] in seen and board[r][c] != '.':
                    return False
                seen.add(board[r][c])
        
        seen = set()
        # third square
        for r in range(s, s + 3):
            for c in range(6, 9):
                if board[r][c] in seen and board[r][c] != '.':
                    return False
                seen.add(board[r][c])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        location_map = defaultdict(lambda: defaultdict(set))
        for r in range(len(board)):
            for c in range(len(board)):
                value = board[r][c]
                if value == '.':
                    continue
                if value in location_map[f'{r}r'] or value in location_map[f'{c}c']:
                    return False
                location_map[f'{r}r'][value].add(c)
                location_map[f'{c}c'][value].add(r)

        for s in range(0, 9, 3):
            if not self.is_valid_square(s, board):
                return False
        
        return True
        