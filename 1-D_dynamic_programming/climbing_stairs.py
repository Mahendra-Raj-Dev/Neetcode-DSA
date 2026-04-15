# ---------------------- Solution 1 ------------------
# Problem: Climbing Stairs
# Pattern: dynamic programming (1D DP / memoization)
# Approach:
# - Use DFS with memoization to store ways from each step
# - At each step, choose to climb 1 or 2 stairs
# - Total ways = ways(step + 1) + ways(step + 2)
# Time complexity: O(N), where N is the number of stairs
# Space complexity: O(N)

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {n:1}

        def dfs(x):
            if x > n:
                return 0
            if x in memo:
                return memo[x]
            else:
                memo[x] = dfs(x + 1) + dfs(x + 2)
                return memo[x]
        return dfs(0)

# --------------------- Solution 2 ------------------------
# Problem: Climbing Stairs
# Pattern: dynamic programming (1D DP)
# Approach:
# - Use two variables to track the previous two step counts
# - Update them iteratively using Fibonacci relation
# - Current ways = previous + current
# Time complexity: O(N), where N is the number of stairs
# Space complexity: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        prev, cur = 1, 1

        for i in range(n - 1):
            prev, cur = cur, prev + cur
        
        return cur