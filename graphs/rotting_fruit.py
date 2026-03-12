# Problem: Rotting Oranges
# Pattern: multi-source BFS (grid traversal)
# Approach:
# - Add all initially rotten oranges (2) to the queue
# - Perform BFS to spread rot to adjacent fresh oranges (1)
# - Each BFS level represents one minute of time
# - Track remaining fresh oranges to determine if all can rot
# Time complexity: O(R * C), where R is rows and C is columns
# Space complexity: O(R * C)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1

