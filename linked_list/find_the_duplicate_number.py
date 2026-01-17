# Problem: Find the Duplicate Number
# Pattern: Linked List (Cycle Detection)
# Approach:
# - Treat the array as a linked list
# - Use Floyd’s fast and slow pointers to find cycle
# - The meeting point of slow and slow2 gives the duplicate
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast,slow = 0,0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow