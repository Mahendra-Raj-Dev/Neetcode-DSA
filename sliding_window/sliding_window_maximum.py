# Problem: Sliding Window Maximum
# Pattern: Sliding window
# Approach:
# - Use a deque to store indices of elements
# - Maintain decreasing order in the deque
# - Front of deque always holds the maximum for the window
# Time complexity: O(n)
# Space complexity: O(n) 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() # Indices

        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r+1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res