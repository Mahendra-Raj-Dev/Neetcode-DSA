# Problem: Copy List with Random Pointer
# Approach:
# 1. First pass: create a copy of each node and store mapping from old -> new.
# 2. Second pass: assign next and random pointers using the mapping.
# Time Complexity: O(n)
# Space Complexity: O(n)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        OldToNew = {None: None}

        curr = head
        while curr:
            new = Node(curr.val)
            OldToNew[curr] = new
            curr = curr.next
        
        curr = head
        while curr:
            new = OldToNew[curr]
            new.next = OldToNew[curr.next]
            new.random = OldToNew[curr.random]
            curr = curr.next

        return OldToNew[head]