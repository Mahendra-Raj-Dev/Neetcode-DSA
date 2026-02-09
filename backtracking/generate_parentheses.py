# Problem: Generate Parentheses
# Pattern: backtracking (DFS)
# Approach:
# - Build valid strings by adding '(' and ')' under constraints
# - Add '(' if open count < n, add ')' if close count < open count
# - Collect results when both counts reach n
# Time complexity: O(4^N / √N), where N is the number of pairs
# Space complexity: O(N), for recursion stack and current string

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        backtrack(0, 0)
        return res