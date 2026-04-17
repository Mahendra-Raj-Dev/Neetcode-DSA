# Problem: Coin Change
# Pattern: dynamic programming (1D DP / memoization)
# Approach:
# - Use DFS with memoization to find minimum coins for each amount
# - Try every coin and recursively solve for remaining amount
# - Take the minimum coins among all choices
# - Use infinity to handle impossible cases
# Time complexity: O(A * C), where A is amount and C is number of coins
# Space complexity: O(A)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}

        def dfs(amt):
            if amt in memo:
                return memo[amt]
            
            if amt < 0:
                return float("inf")
            
            res = float("inf")
            for c in coins:
                res = min(res , 1 + dfs(amt - c))
            
            memo[amt] = res
            return res
        ans = dfs(amount)
        return ans if ans != float("inf") else -1
