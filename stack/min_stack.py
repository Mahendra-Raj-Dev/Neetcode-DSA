# Problem: Min Stack
# Pattern: Stack
# Approach:
# - Use one stack to store values
# - Use another stack to store the minimum value at each level
# Time Complexity: O(1) for all operations
# Space Complexity: O(n) 

class MinStack:

    def __init__(self):
        self.stack = []
        self.Minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.Minstack[-1] if self.Minstack else val)
        self.Minstack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.Minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.Minstack[-1]
