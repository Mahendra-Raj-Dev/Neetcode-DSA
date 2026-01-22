# Problem: Subtree of Another Tree
# Pattern: tree (DFS)
# Approach:
# - Traverse the main tree using DFS
# - At each node, check if the subtree matches using a same-tree comparison
# - Recursively search left and right subtrees
# Time complexity: O(N * M), where N is nodes in root and M is nodes in subRoot
# Space complexity: O(H), where H is the height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if not root or not subRoot or root.val != subRoot.val:
            return False
        
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        