# Problem: Balanced Binary Tree
# Pattern: tree (DFS / postorder)
# Approach:
# - Use DFS to get balance status and height for each subtree
# - A tree is balanced if both subtrees are balanced and height difference ≤ 1
# Time complexity: O(N), where N is the number of nodes
# Space complexity: O(H), where H is the height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dsf(curr):
            if not curr:
                return [True, 0]
            
            left, right = dsf(curr.left), dsf(curr.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dsf(root)[0]