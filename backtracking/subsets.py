# Problem: Subsets
# Pattern: backtracking (DFS)
# Approach:
# - Use DFS to explore both choices: include or exclude each element
# - Add the current subset to result when all elements are processed
# Time complexity: O(2^N), where N is the number of elements
# Space complexity: O(N), for recursion stack and current subset

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def dfs(i):
            if i == n:
                res.append(sol[:])
                return
            
            #don't pick nums[i]
            dfs(i + 1)

            #pick nums[i]
            sol.append(nums[i])
            dfs(i + 1)
            sol.pop()
        
        dfs(0)
        return res