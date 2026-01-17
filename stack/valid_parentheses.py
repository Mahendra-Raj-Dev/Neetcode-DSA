# Problem: Valid Parentheses
# Pattern: Stack
# Approach:
# - Use a hashmap to map closing brackets to opening ones
# - Use a stack to validate matching parentheses
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def isValid(self, s):
        stack = []
        brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for x in s:
            if x in brackets:
                if stack and brackets[x] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return True if not stack else False