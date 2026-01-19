# Problem: Largest Rectangle in Histogram
# Pattern: stack (monotonic increasing)
# Approach:
# - Use a monotonic increasing stack to store (start_index, height)
# - When a smaller height appears, pop from stack and calculate area
# - Track the maximum area while popping and after processing all bars
# Time complexity: O(N), where N is the number of bars
# Space complexity: O(N)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, (i-idx)*height)
                start = idx
            stack.append((start, h))
        
        for i,h in stack:
            maxArea = max(maxArea, (len(heights)-i)*h)
        return maxArea