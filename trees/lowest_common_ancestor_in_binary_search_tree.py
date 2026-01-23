# Problem: Lowest Common Ancestor of a Binary Search Tree
# Pattern: tree (BST traversal)
# Approach:
# - Traverse the BST starting from root
# - Move left or right based on values of p and q
# - The split point is the lowest common ancestor
# Time complexity: O(H), where H is the height of the tree
# Space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr