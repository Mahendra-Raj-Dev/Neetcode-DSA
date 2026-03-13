# Problem: Surrounded Regions
# Pattern: graph traversal (DFS on grid)
# Approach:
# - Run DFS from all border cells containing 'O'
# - Mark these connected 'O's as temporary '#' since they cannot be captured
# - Traverse the board and convert remaining 'O's to 'X' (they are surrounded)
# - Convert temporary '#' cells back to 'O'
# Time complexity: O(R * C), where R is rows and C is columns
# Space complexity: O(R * C)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return
            
            board[r][c] = "#"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS -1, c)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                
                if board[r][c] == "#":
                    board[r][c] = "O"