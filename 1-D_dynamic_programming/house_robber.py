# Problem: House Robber
# Pattern: dynamic programming (1D DP)
# Approach:
# - Use two variables to track the best loot up to previous houses
# - For each house, choose between robbing it or skipping it
# - Update current maximum profit using max(previous + current, skip)
# Time complexity: O(N), where N is number of houses
# Space complexity: O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2