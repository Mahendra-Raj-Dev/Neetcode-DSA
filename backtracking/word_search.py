# Problem: Word Search
# Pattern: backtracking (DFS on grid)
# Idea:
# - Try to match the word starting from each cell
# - Move in 4 directions and mark cells as visited
# - Backtrack after each path
# Time: O(R * C * 4^L)
# Space: O(L)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path:
                return False
            
            path.add((r, c))
            res = backtrack(r-1, c, i+1) or backtrack(r+1, c, i+1) or backtrack(r, c+1, i+1) or backtrack(r, c-1, i+1)
            path.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0): return True
        
        return False