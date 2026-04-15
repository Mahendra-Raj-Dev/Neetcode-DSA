# ----------------------- Solution 1 ---------------------
# Problem: Min Cost Climbing Stairs
# Pattern: dynamic programming (1D DP / memoization)
# Approach:
# - Use DFS with memoization to store minimum cost from each step
# - At each step, choose the cheaper path between 1-step and 2-step jump
# - Final answer is the minimum cost starting from step 0 or 1
# Time complexity: O(N), where N is number of steps
# Space complexity: O(N)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {n: 0}

        def dfs(i):
            if i > n:
                return float("inf")
            
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]

        return min(dfs(0), dfs(1))

# ------------------------ Solution 2 -----------------------
# Problem: Min Cost Climbing Stairs
# Pattern: dynamic programming (1D DP)
# Approach:
# - Append 0 as the top floor cost
# - Traverse from the end towards the start
# - Update each step with its own cost plus the cheaper of next 1 or 2 steps
# - Answer is the minimum cost starting from step 0 or 1
# Time complexity: O(N), where N is number of steps
# Space complexity: O(1)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        for i in range(n-3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        return min(cost[0], cost[1])