# Problem: Daily Temperatures
# Pattern: Stack (Monotonic Stack)
# Approach:
# - Use a stack to store indices of temperatures waiting for a warmer day
# - When a warmer temperature is found, update the result for previous indices
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for idx, i in enumerate(temperatures):
            while stack and i > temperatures[stack[-1]]:
                res[stack[-1]] = idx-stack[-1]
                stack.pop()
            stack.append(idx)
        
        return res