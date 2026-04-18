# Problem: Word Break
# Pattern: dynamic programming (1D DP)
# Approach:
# - Use a DP array where dp[i] means the substring s[i:] can be segmented
# - Start from the end since an empty string is always valid
# - For each index, try matching every word in the dictionary
# - If a word matches and the remaining substring is valid, mark dp[i] as True
# Time complexity: O(N * M * L), where N is length of string, M is number of words, and L is average word length
# Space complexity: O(N)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s)) and s[i: i+ len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]