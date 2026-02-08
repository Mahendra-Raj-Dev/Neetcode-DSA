# Problem: Combination Sum
# Pattern: backtracking (DFS)
# Approach:
# - Use DFS to explore combinations by choosing or skipping each number
# - Allow reuse of the same number by not moving index after choosing
# - Add combination to result when total equals target
# Time complexity: O(2^N), where N is the number of candidates
# Space complexity: O(N), for recursion stack and current combination

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            
            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            dfs(i, curr, total+nums[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res