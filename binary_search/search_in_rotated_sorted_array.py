# Problem: Search in Rotated Sorted Array
# Pattern: binary search
# Approach:
# - Use binary search while identifying the sorted half
# - Check if target lies in the sorted portion
# - Discard the irrelevant half and continue searching
# Time complexity: O(log N), where N is the number of elements
# Space complexity: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)//2

            if target == nums[m]:
                return m
            
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            
            else:
                if target < nums[m] or target > nums[r]:
                    r = r - 1
                else:
                    l = m + 1
        return -1