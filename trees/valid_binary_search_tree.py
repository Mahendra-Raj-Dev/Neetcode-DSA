# Problem: Validate Binary Search Tree
# Pattern: tree (DFS / BST)
# Approach:
# - Use DFS with lower and upper bounds
# - Ensure each node value lies within valid BST range
# Time complexity: O(N), where N is the number of nodes
# Space complexity: O(H), where H is the height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node: return True

            if not (left < node.val < right):
                return False
            
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))

        return valid(root, float("-infinity"), float("infinity"))