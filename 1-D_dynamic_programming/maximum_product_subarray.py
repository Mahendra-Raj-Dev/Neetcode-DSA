# Problem: Maximum Product Subarray
# Pattern: dynamic programming (1D DP)
# Approach:
# - Track both current maximum and minimum products
# - Negative numbers can flip min ↔ max, so both are needed
# - Reset when encountering zero
# - Update result with the maximum product at each step
# Time complexity: O(N), where N is length of array
# Space complexity: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curMax, curMin = 1, 1
        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue
            temp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(temp, curMin * n, n)
            res = max(res, curMax)
        return res