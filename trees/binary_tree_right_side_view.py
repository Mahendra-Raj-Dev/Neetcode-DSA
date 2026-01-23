# Problem: Binary Tree Right Side View
# Pattern: tree (BFS / level-order)
# Approach:
# - Perform level-order traversal using a queue
# - Track the last node value at each level
# Time complexity: O(N), where N is the number of nodes
# Space complexity: O(W), where W is the maximum width of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root])
        res = []

        while q:
            curr = None
            for i in range(len(q)):
                node = q.popleft()
                curr = node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(curr)
        return res