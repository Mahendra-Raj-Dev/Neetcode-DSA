# Problem: Invert Binary Tree
# Pattern: tree (DFS)
# Approach:
# - Swap left and right children of each node
# - Recursively apply the same operation to subtrees
# Time complexity: O(N), where N is the number of nodes
# Space complexity: O(H), where H is the height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root