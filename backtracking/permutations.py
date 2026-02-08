# Problem: Permutations
# Pattern: backtracking (recursion)
# Approach:
# - Generate permutations of the remaining elements recursively
# - Insert the current element at every possible position
# - Collect all generated permutations
# Time complexity: O(N!), where N is the number of elements
# Space complexity: O(N), for recursion stack (excluding result storage)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])

        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p[:]
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        
        return res