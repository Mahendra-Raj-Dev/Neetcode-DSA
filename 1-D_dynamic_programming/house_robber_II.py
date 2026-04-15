# Problem: House Robber II
# Pattern: dynamic programming (1D DP)
# Approach:
# - Since houses are in a circle, first and last cannot both be robbed
# - Split into two linear cases: exclude first house or exclude last house
# - Reuse House Robber I logic on both cases
# - Return the maximum of the two results
# Time complexity: O(N), where N is number of houses
# Space complexity: O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, arr):
        rob1, rob2 = 0, 0
        for i in arr:
            rob1, rob2 = rob2, max(rob1 + i, rob2)
        return rob2
