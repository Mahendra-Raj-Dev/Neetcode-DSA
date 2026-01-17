# Problem: Evaluate Reverse Polish Notation
# Pattern: Stack
# Approach:
# - Use a stack to store operands
# - Pop top two values when an operator is encountered
# - Apply the operation and push the result back
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            
            else: 
                stack.append(int(c))
        
        return stack[0]