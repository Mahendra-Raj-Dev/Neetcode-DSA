# Problem: Find Minimum in Rotated Sorted Array
# Pattern: binary search
# Approach:
# - Use binary search to locate the unsorted half
# - Update minimum while narrowing the search space
# - Stop early if subarray is already sorted
# Time complexity: O(log N), where N is the number of elements
# Space complexity: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l+r)//2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
        return res
        