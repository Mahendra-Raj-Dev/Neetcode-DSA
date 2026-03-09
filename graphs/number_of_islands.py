# Problem: Number of Islands
# Pattern: graph traversal (DFS on grid)
# Approach:
# - Traverse every cell in the grid
# - When a land cell ("1") is found, start a DFS
# - Mark all connected land cells as visited
# - Each DFS call represents one island
# Time complexity: O(R * C), where R is rows and C is columns
# Space complexity: O(R * C)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        iland = 0
        seen = set()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in seen or grid[r][c] == "0":
                return 
            
            seen.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    dfs(r, c)
                    iland += 1
        
        return iland