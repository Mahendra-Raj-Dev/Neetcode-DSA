# Problem: Binary Tree Level Order Traversal
# Pattern: tree (BFS / level-order)
# Approach:
# - Use a queue to traverse the tree level by level
# - Collect node values for each level before moving to the next
# Time complexity: O(N), where N is the number of nodes
# Space complexity: O(W), where W is the maximum width of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            curr = []
            for i in range(len(q)):
                node = q.popleft()
                curr.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(curr)
        return res
