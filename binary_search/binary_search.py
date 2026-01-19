# Problem: Binary Search
# Pattern: binary search
# Approach:
# - Maintain left and right pointers
# - Calculate mid index and compare with target
# - Narrow the search space based on comparison
# Time complexity: O(log N), where N is the number of elements
# Space complexity: O(1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m      
        return -1