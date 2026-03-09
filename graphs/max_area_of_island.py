# Problem: Max Area of Island
# Pattern: graph traversal (DFS on grid)
# Approach:
# - Traverse the grid and start DFS when a land cell (1) is found
# - Explore all connected land cells and count their area
# - Track the maximum island area encountered
# Time complexity: O(R * C), where R is rows and C is columns
# Space complexity: O(R * C)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in seen or not grid[r][c]:
                return 0

            seen.add((r, c))
            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and (r, c) not in seen:
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea