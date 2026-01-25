# Problem: Binary Tree Maximum Path Sum
# Pattern: tree (DFS / postorder)
# Approach:
# - Use DFS to compute maximum gain from left and right subtrees
# - Ignore negative paths by taking max with 0
# - Update global maximum using left + right + current node value
# Time complexity: O(N), where N is the number of nodes
# Space complexity: O(H), where H is the height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def dfs(root):
            if not root: return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            self.res = max(self.res, leftMax + rightMax + root.val)
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return self.res