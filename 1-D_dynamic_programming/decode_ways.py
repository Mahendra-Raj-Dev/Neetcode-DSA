# Problem: Decode Ways
# Pattern: dynamic programming (1D DP / memoization)
# Approach:
# - Use DFS with memoization to store decoding ways from each index
# - If current digit is '0', no decoding is possible
# - Try decoding one digit and, when valid, two digits
# - Total ways = one-digit ways + two-digit ways
# Time complexity: O(N), where N is length of string
# Space complexity: O(N)

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res
        
        return dfs(0)