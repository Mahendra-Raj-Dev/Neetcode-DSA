# Problem: Combination Sum II
# Pattern: backtracking (DFS)
# Approach:
# - Sort the array to handle duplicates
# - Use DFS to explore combinations by picking or skipping elements
# - Skip duplicate values to avoid repeated combinations
# Time complexity: O(2^N), where N is the number of candidates
# Space complexity: O(N), for recursion stack and current combination

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if i >= len(candidates) or total > target:
                return 
            
            #pick candidates[i]
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i + 1, curr, total)
        dfs(0, [], 0)
        return res