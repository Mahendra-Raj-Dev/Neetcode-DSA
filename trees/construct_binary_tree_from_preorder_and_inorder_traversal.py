# Problem: Construct Binary Tree from Preorder and Inorder Traversal
# Pattern: tree (DFS / divide and conquer)
# Approach:
# - Use preorder to pick the root node
# - Use inorder indices to split left and right subtrees
# - Recursively build the tree
# Time complexity: O(N), where N is the number of nodes
# Space complexity: O(N), for recursion stack and hashmap

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val:idx for idx,val in enumerate(inorder) }
        self.pre_idx = 0

        def dfs(l, r):
            if l > r:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            m = indices[root_val]
            root.left = dfs(l, m-1)
            root.right = dfs(m+1, r)

            return root
        return dfs(0, len(inorder)-1)