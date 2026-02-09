# Problem: Subsets II
# Pattern: backtracking (DFS)
# Approach:
# - Sort the array to handle duplicates
# - Use DFS to explore include/exclude choices
# - Skip duplicate elements to avoid repeated subsets
# Time complexity: O(2^N), where N is the number of elements
# Space complexity: O(N), for recursion stack and current subset

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        def dfs(i, curr):
            if i == n:
                res.append(curr[:])
                return
            
            curr.append(nums[i])
            dfs(i + 1, curr)

            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1

            curr.pop()
            dfs(i + 1, curr)
        
        dfs(0, [])
        return res