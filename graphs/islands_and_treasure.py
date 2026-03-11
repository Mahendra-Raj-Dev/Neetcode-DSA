# Problem: Islands and Treasure (Walls and Gates)
# Pattern: multi-source BFS (grid traversal)
# Approach:
# - Add all treasure cells (0) into the queue as starting points
# - Perform BFS simultaneously from all treasures
# - Expand level by level and update distance to the nearest treasure
# - Skip walls (-1) and already visited cells
# Time complexity: O(R * C), where R is rows and C is columns
# Space complexity: O(R * C)

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        
        def fillLand(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or grid[r][c] == -1:
                return 
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        d = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = d
                fillLand(r + 1, c)
                fillLand(r - 1, c)
                fillLand(r, c + 1)
                fillLand(r, c - 1)
            d += 1
