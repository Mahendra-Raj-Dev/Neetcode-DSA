# Problem: Kth Smallest Element in a BST
# Pattern: tree (BST / inorder traversal)
# Approach:
# - Perform inorder traversal using a stack
# - Count nodes in ascending order
# - Return the value when count equals k
# Time complexity: O(N), where N is the number of nodes
# Space complexity: O(H), where H is the height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        count = 0
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            
            curr = curr.right
        
        return